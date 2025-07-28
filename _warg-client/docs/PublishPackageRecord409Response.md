# PublishPackageRecord409Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**type** | **str** | The type of entity that was not found. | 
**id** | **str** | The identifier of the entity that was not found.  | 

## Example

```python
from _warg_client.models.publish_package_record409_response import PublishPackageRecord409Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPackageRecord409Response from a JSON string
publish_package_record409_response_instance = PublishPackageRecord409Response.from_json(json)
# print the JSON string representation of the object
print PublishPackageRecord409Response.to_json()

# convert the object into a dict
publish_package_record409_response_dict = publish_package_record409_response_instance.to_dict()
# create an instance of PublishPackageRecord409Response from a dict
publish_package_record409_response_from_dict = PublishPackageRecord409Response.from_dict(publish_package_record409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


