# GetPackageRecord404Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**type** | **str** | The type of entity that was not found. | 
**id** | **str** | Represents a supported hash. | 

## Example

```python
from _warg_client.models.get_package_record404_response import GetPackageRecord404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPackageRecord404Response from a JSON string
get_package_record404_response_instance = GetPackageRecord404Response.from_json(json)
# print the JSON string representation of the object
print GetPackageRecord404Response.to_json()

# convert the object into a dict
get_package_record404_response_dict = get_package_record404_response_instance.to_dict()
# create an instance of GetPackageRecord404Response from a dict
get_package_record404_response_from_dict = GetPackageRecord404Response.from_dict(get_package_record404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


