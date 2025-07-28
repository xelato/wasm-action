# PublishPackageRecordRequest

A request to publish a record to a package log.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_name** | **str** | The name of the package log being published to. | 
**record** | [**EnvelopeBody**](EnvelopeBody.md) | The package record being published to the log. | 
**content_sources** | **object** | The map of content digest to sources. | [optional] 

## Example

```python
from _warg_client.models.publish_package_record_request import PublishPackageRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPackageRecordRequest from a JSON string
publish_package_record_request_instance = PublishPackageRecordRequest.from_json(json)
# print the JSON string representation of the object
print PublishPackageRecordRequest.to_json()

# convert the object into a dict
publish_package_record_request_dict = publish_package_record_request_instance.to_dict()
# create an instance of PublishPackageRecordRequest from a dict
publish_package_record_request_from_dict = PublishPackageRecordRequest.from_dict(publish_package_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


