# SourcingRecord

The package record is sourcing content.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the package record. | 
**missing_content** | **object** | The map of content digest to missing content info. | 

## Example

```python
from _warg_client.models.sourcing_record import SourcingRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SourcingRecord from a JSON string
sourcing_record_instance = SourcingRecord.from_json(json)
# print the JSON string representation of the object
print SourcingRecord.to_json()

# convert the object into a dict
sourcing_record_dict = sourcing_record_instance.to_dict()
# create an instance of SourcingRecord from a dict
sourcing_record_from_dict = SourcingRecord.from_dict(sourcing_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


