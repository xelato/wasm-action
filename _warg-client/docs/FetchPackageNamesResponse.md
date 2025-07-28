# FetchPackageNamesResponse

A response containing the requested package names.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packages** | **object** | The map of log ID to package name. | [optional] 

## Example

```python
from _warg_client.models.fetch_package_names_response import FetchPackageNamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchPackageNamesResponse from a JSON string
fetch_package_names_response_instance = FetchPackageNamesResponse.from_json(json)
# print the JSON string representation of the object
print FetchPackageNamesResponse.to_json()

# convert the object into a dict
fetch_package_names_response_dict = fetch_package_names_response_instance.to_dict()
# create an instance of FetchPackageNamesResponse from a dict
fetch_package_names_response_from_dict = FetchPackageNamesResponse.from_dict(fetch_package_names_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


