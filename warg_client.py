
from urllib.parse import urlparse
import hashlib
import urllib3

import leb128
import warg_openapi as warg


class WargClient:

    def __init__(self, registry, warg_url, access_token=None):
        self.registry = registry

        configuration = warg.Configuration(
            host = "{}{}".format(warg_url, 'v1' if warg_url.endswith('/') else '/v1'),
            #access_token=access_token,
        )

        # Support for digest strings as path params: sha256:<digest>
        # or else they get quoted, resulting in "Invalid content digest" error.
        configuration.safe_chars_for_path_param = "/:"

        client = warg.ApiClient(configuration=configuration)

        # stealth mode
        # client.default_headers['User-Agent'] = urllib3.util.SKIP_HEADER

        self.fetch_api = warg.FetchApi(client)
        self.content_api = warg.ContentApi(client)

    def get_warg_registry(self, namespace):
        return "{}.{}".format(namespace, self.registry)

    def get_checkpoint(self, namespace):
        return self.fetch_api.get_checkpoint(warg_registry=self.get_warg_registry(namespace))

    def fetch_logs(self, namespace, name, log_length):
        log_id = generate_log_id(namespace, name)
        print("{}/{}: {}".format(namespace, name, log_id))
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


def generate_log_id(namespace, name):
    """Derive logId from package name"""
    package_name = "{}:{}".format(namespace, name)
    s = hashlib.sha256()
    s.update(b'WARG-PACKAGE-LOG-ID-V0:')
    s.update(b'WARG-PACKAGE-ID-V0')
    s.update(leb128.u.encode(len(package_name)))
    s.update(package_name.encode('utf8'))
    return 'sha256:{}'.format(s.hexdigest())
