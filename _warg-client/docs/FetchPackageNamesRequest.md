# FetchPackageNamesRequest

A request to fetch package names from the registry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packages** | **List[str]** | The log ID for each requested package. | 

## Example

```python
from _warg_client.models.fetch_package_names_request import FetchPackageNamesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchPackageNamesRequest from a JSON string
fetch_package_names_request_instance = FetchPackageNamesRequest.from_json(json)
# print the JSON string representation of the object
print FetchPackageNamesRequest.to_json()

# convert the object into a dict
fetch_package_names_request_dict = fetch_package_names_request_instance.to_dict()
# create an instance of FetchPackageNamesRequest from a dict
fetch_package_names_request_from_dict = FetchPackageNamesRequest.from_dict(fetch_package_names_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


