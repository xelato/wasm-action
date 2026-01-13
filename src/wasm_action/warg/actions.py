import os
import hashlib
import base64
import time

import requests
from dataclasses import dataclass

from . import proto
from .client import WargClient, PackageLogs

import warg_openapi


@dataclass
class PackageDownload:
    namespace: str
    name: str
    version: str
    content: bytes
    digest: str


def error(text):
    return ValueError(text)


def warg_push(registry, warg_url, namespace, name, version, content_bytes, warg_token:str, warg_private_key:str):

    client = WargClient(
        registry=registry,
        warg_url=warg_url,
        warg_token=warg_token,
        warg_private_key=warg_private_key,
    )

    # fetch logs
    res = client.get_checkpoint(namespace=namespace)

    res = client.fetch_logs(
        namespace=namespace, name=name, log_length=res.contents.log_length)

    package_logs = PackageLogs(res)

    # publish record
    last = package_logs.last_record()
    prev_id = last.id if last else ''
    res = client.publish_package_record(namespace, name, version, content_bytes, prev_id=prev_id)

    record_id = res['recordId']
    state = res['state']

    timeout_sec = 10
    start = time.time()
    while time.time() - start < timeout_sec:

        # state: processing -> wait
        if state == 'processing':
            time.sleep(1)

        # state: sourcing -> upload sources
        elif state == 'sourcing':
            if 'missingContent' in res:
                for _, data in res['missingContent'].items():
                    if 'upload' in data:
                        for upload in data['upload']:
                            requests.put(upload['url'], data=content_bytes)

        # state: rejected -> error
        elif state == 'rejected':
            break

        # state: published -> complete
        elif state == 'published':
            break

        # get updated published record
        res = client.get_package_record(namespace, name, record_id)

        state = res['state']

    return {
        'namespace': namespace,
        'name': name,
        'version': version,
        'record_id': record_id,
        'state': state,
    }


def warg_pull(registry, warg_url, namespace, name, version=None, warg_token=None) -> PackageDownload:

    client = WargClient(
        registry=registry,
        warg_url=warg_url,
        warg_token=warg_token,
    )

    res = client.get_checkpoint(namespace=namespace)

    res = client.fetch_logs(
        namespace=namespace, name=name, log_length=res.contents.log_length)

    if not res.packages:
        raise error('failed to fetch logs')

    log_id, packages = res.packages.popitem()

    if not packages:
        raise error('failed to fetch logs')

    found_version, digest = find_version(packages, requested_version=version)

    if not digest or not found_version:
        raise error(
            'no package version found' if not version
            else 'requested version {} not found'.format(version))

    # get content sources
    res = client.get_content_sources(
        namespace=namespace,
        digest=digest,
    )

    if not res.content_sources:
        raise error('failed to fetch sources')

    digest, sources = res.content_sources.popitem()
    if not sources:
        raise error('failed to fetch sources')
    source = sources[0]
    url = source['url']

    # Fetch content from url with digest expected
    res = requests.get(url)
    content_digest = 'sha256:{}'.format(hashlib.sha256(res.content).hexdigest())
    if digest != content_digest:
        raise error('unexpected content digest')

    return PackageDownload(
        namespace=namespace,
        name=name,
        version=found_version,
        content=res.content,
        digest=digest,
    )


def find_version(packages, requested_version=None):
    version, digest = None, None
    for package in packages:
        record = proto.PackageRecord()
        record.ParseFromString(base64.b64decode(package['contentBytes']))
        for entry in record.entries:

            obj = getattr(entry, entry.WhichOneof('contents'))

            if isinstance(obj, proto.PackageRelease):

                if requested_version:
                    if obj.version == requested_version:
                        version = obj.version
                        digest = obj.content_hash
                else:
                    # latest version, assuming already ordered
                    version = obj.version
                    digest = obj.content_hash

    return version, digest
