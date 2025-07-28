# RejectedRecord

A rejected package record.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the package record. | 
**reason** | **str** | The reason the package record was rejected. | 

## Example

```python
from warg_openapi.models.rejected_record import RejectedRecord

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedRecord from a JSON string
rejected_record_instance = RejectedRecord.from_json(json)
# print the JSON string representation of the object
print RejectedRecord.to_json()

# convert the object into a dict
rejected_record_dict = rejected_record_instance.to_dict()
# create an instance of RejectedRecord from a dict
rejected_record_from_dict = RejectedRecord.from_dict(rejected_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


