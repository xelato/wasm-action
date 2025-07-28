# ProcessingRecord

A record that is being processed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the package record. | 

## Example

```python
from _warg_client.models.processing_record import ProcessingRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingRecord from a JSON string
processing_record_instance = ProcessingRecord.from_json(json)
# print the JSON string representation of the object
print ProcessingRecord.to_json()

# convert the object into a dict
processing_record_dict = processing_record_instance.to_dict()
# create an instance of ProcessingRecord from a dict
processing_record_from_dict = ProcessingRecord.from_dict(processing_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


