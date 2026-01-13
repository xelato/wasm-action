
import enum
import requests

class RegistryType(enum.Enum):
    OCI = 'oci'
    WARG = 'warg'

    def __str__(self):
        return self.value


def detect_registry_settings(registry):
    """Discovery based on .well-known domain config"""
    url = "https://{domain}/.well-known/wasm-pkg/registry.json".format(domain=registry)
    r = requests.get(url, timeout=10)
    if not r.ok:
        return {}

    data = r.json()

    result = {}
    if 'preferredProtocol' in data:
        if data['preferredProtocol'] == 'warg':
            result['registry-type'] = RegistryType.WARG
            if 'warg' in data:
                if 'url' in data['warg']:
                    result['warg-url'] = data['warg']['url']

        elif data['preferredProtocol'] == 'oci':
            result['registry-type'] = RegistryType.OCI
            if 'oci' in data:
                if 'registry' in data['oci']:
                    result['oci-registry'] = data['oci']['registry']
                if 'namespacePrefix' in data['oci']:
                    result['oci-namespace-prefix'] = data['oci']['namespacePrefix']

    elif 'wargUrl' in data:
        result['registry-type'] = RegistryType.WARG
        result['warg-url'] = data['wargUrl']

    elif 'ociRegistry' in data:
        result['registry-type'] = RegistryType.OCI
        result['oci-registry'] = data['ociRegistry']
        if 'ociNamespacePrefix' in data:
            result['oci-namespace-prefix'] = data['ociNamespacePrefix']

    return result
