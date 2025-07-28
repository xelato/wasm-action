# FetchWarning

A warning message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The warning message itself. | [optional] 

## Example

```python
from _warg_client.models.fetch_warning import FetchWarning

# TODO update the JSON string below
json = "{}"
# create an instance of FetchWarning from a JSON string
fetch_warning_instance = FetchWarning.from_json(json)
# print the JSON string representation of the object
print FetchWarning.to_json()

# convert the object into a dict
fetch_warning_dict = fetch_warning_instance.to_dict()
# create an instance of FetchWarning from a dict
fetch_warning_from_dict = FetchWarning.from_dict(fetch_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


