# PublishedRecord

A record that has been published to the log.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the package record. | 
**registry_index** | **int** | The index of the record in the registry log. | 

## Example

```python
from _warg_client.models.published_record import PublishedRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedRecord from a JSON string
published_record_instance = PublishedRecord.from_json(json)
# print the JSON string representation of the object
print PublishedRecord.to_json()

# convert the object into a dict
published_record_dict = published_record_instance.to_dict()
# create an instance of PublishedRecord from a dict
published_record_from_dict = PublishedRecord.from_dict(published_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


