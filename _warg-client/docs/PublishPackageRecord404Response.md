# PublishPackageRecord404Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**type** | **str** | The type of entity that was not found. | 
**id** | **str** | The identifier of the entity that was not found.  | 

## Example

```python
from _warg_client.models.publish_package_record404_response import PublishPackageRecord404Response

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPackageRecord404Response from a JSON string
publish_package_record404_response_instance = PublishPackageRecord404Response.from_json(json)
# print the JSON string representation of the object
print PublishPackageRecord404Response.to_json()

# convert the object into a dict
publish_package_record404_response_dict = publish_package_record404_response_instance.to_dict()
# create an instance of PublishPackageRecord404Response from a dict
publish_package_record404_response_from_dict = PublishPackageRecord404Response.from_dict(publish_package_record404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


