# PackageRecord

A package log record.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** | Represents a supported hash. | 
**state** | **str** | The state of the package record. | 
**missing_content** | **object** | The map of content digest to missing content info. | 
**reason** | **str** | The reason the package record was rejected. | 
**registry_index** | **int** | The index of the record in the registry log. | 

## Example

```python
from warg_openapi.models.package_record import PackageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PackageRecord from a JSON string
package_record_instance = PackageRecord.from_json(json)
# print the JSON string representation of the object
print PackageRecord.to_json()

# convert the object into a dict
package_record_dict = package_record_instance.to_dict()
# create an instance of PackageRecord from a dict
package_record_from_dict = PackageRecord.from_dict(package_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


