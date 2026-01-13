
import hashlib
import urllib3
import base64
import leb128
import warg_openapi as warg
from dataclasses import dataclass
from .crypto import PrivateKey
from . import proto


class WargClient:

    def __init__(self, registry, warg_url, warg_token=None, warg_private_key=None, stealth=False):
        self.registry = registry

        configuration = warg.Configuration(
            host = "{}{}".format(warg_url, 'v1' if warg_url.endswith('/') else '/v1'),
        )

        # Support for digest strings as path params: sha256:<digest>
        # or else they get quoted, resulting in "Invalid content digest" error.
        configuration.safe_chars_for_path_param = "/:"

        client = warg.ApiClient(
            configuration=configuration,
        )

        # private packages
        if warg_token:
            client.default_headers['Authorization'] = 'Bearer {}'.format(warg_token)

        if stealth:
            client.default_headers['User-Agent'] = urllib3.util.SKIP_HEADER

        self.fetch_api = warg.FetchApi(client)
        self.content_api = warg.ContentApi(client)
        self.package_api = warg.PackageApi(client)

        self.private_key = PrivateKey.load(warg_private_key) if warg_private_key else None

    def get_warg_registry(self, namespace):
        return "{}.{}".format(namespace, self.registry)

    def get_checkpoint(self, namespace):
        return self.fetch_api.get_checkpoint(warg_registry=self.get_warg_registry(namespace))

    def fetch_logs(self, namespace, name, log_length):
        log_id = generate_log_id(namespace, name)
        return self.fetch_api.fetch_logs(
            fetch_logs_request=warg.FetchLogsRequest(
                log_length=log_length,
                packages={
                    log_id: None,
                },
            ),
            warg_registry=self.get_warg_registry(namespace),
        )

    def fetch_names(self, namespace, name):
        """Translate log_id to package name."""
        log_id = generate_log_id(namespace, name)
        request = warg.FetchPackageNamesRequest(packages=[log_id])
        return self.fetch_api.fetch_names(
            fetch_package_names_request=request,
            warg_registry=self.get_warg_registry(namespace))

    def get_content_sources(self, namespace, digest):
        return self.content_api.get_content_sources(
            digest=digest,
            warg_registry=self.get_warg_registry(namespace)
        )

    def get_package_record(self, namespace, name, record_id):
        kwargs = {
            'log_id': generate_log_id(namespace, name),
            'record_id': record_id,
            'warg_registry': self.get_warg_registry(namespace),
        }
        res = self.package_api.get_package_record(**kwargs)
        return res.to_dict()

    def publish_package_record(self, namespace, name, version, content_bytes, prev_id):
        digest = hashlib.sha256(content_bytes).hexdigest()
        record = self.create_version_record(
            version=version,
            digest=digest,
        )

        # link to previous record
        if prev_id:
            record.prev = prev_id

        record_bytes = record.SerializeToString()

        record_request = warg.PublishPackageRecordRequest(
            package_name="{}:{}".format(namespace, name),

            # signed record bytes
            record=warg.EnvelopeBody(
                key_id=self.private_key.public_key().fingerprint(),
                signature=self.sign(record_bytes),
                content_bytes=base64.b64encode(record_bytes).decode('ascii'),
            ),

        )

        kwargs = {
            'log_id': generate_log_id(namespace, name),
            'publish_package_record_request': record_request,
            'warg_registry': self.get_warg_registry(namespace),
        }

        res = self.package_api.publish_package_record(**kwargs)
        return res.to_dict()

    def create_version_record(self, version, digest) -> proto.PackageRecord:
        release = proto.PackageRelease()
        release.version = version
        release.content_hash = "sha256:{}".format(digest)

        entry = proto.PackageEntry()
        entry.release.CopyFrom(release)

        record = proto.PackageRecord()
        record.entries.MergeFrom([entry])
        # sets it to current time
        record.time.GetCurrentTime()
        return record

    def sign(self, record_bytes):
        prefix = b'WARG-PACKAGE-RECORD-SIGNATURE-V0'
        return self.private_key.sign_canonical(prefix + b':' + record_bytes)


@dataclass
class PackageRecord:
    id: str
    prev_id: str
    proto: object
    orig: object


class PackageLogs:

    def __init__(self, res: warg.FetchLogsResponse):
        self.log_id = None
        if res.packages:
            for key in res.packages:
                self.log_id = key

        self.packages = res.packages.get(self.log_id) if self.log_id else []
        self.res = res

    def records(self):
        records = []
        prev: PackageRecord = None
        for package in self.packages:

            record_bytes = base64.b64decode(package['contentBytes'])
            record = proto.PackageRecord()
            record.ParseFromString(record_bytes)

            if prev and prev.id != record.prev:
                raise Exception('Log inconsistency')

            # augment the original record with more attributes
            item = PackageRecord(
                id=generate_record_id(record_bytes),
                prev_id=prev.id if prev else None,
                proto=record,
                orig=package,
            )

            records.append(item)
            prev = item

        return records

    def last_record(self):
        records = self.records()
        return records[-1] if records else None


def generate_log_id(namespace, name):
    """Derive logId from package name"""
    package_name = "{}:{}".format(namespace, name)
    s = hashlib.sha256()
    s.update(b'WARG-PACKAGE-LOG-ID-V0:')
    s.update(b'WARG-PACKAGE-ID-V0')
    s.update(leb128.u.encode(len(package_name)))
    s.update(package_name.encode('utf8'))
    return 'sha256:{}'.format(s.hexdigest())


def generate_record_id(record_bytes):
    """Derive package record id from record content bytes."""
    s = hashlib.sha256()
    s.update(b'WARG-PACKAGE-LOG-RECORD-V0:')
    s.update(record_bytes)
    return 'sha256:{}'.format(s.hexdigest())
