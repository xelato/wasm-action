# MissingContent

Information about missing content.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | [**List[HttpUpload]**](HttpUpload.md) | Upload endpoint(s) for the missing content. | [optional] 

## Example

```python
from warg_openapi.models.missing_content import MissingContent

# TODO update the JSON string below
json = "{}"
# create an instance of MissingContent from a JSON string
missing_content_instance = MissingContent.from_json(json)
# print the JSON string representation of the object
print MissingContent.to_json()

# convert the object into a dict
missing_content_dict = missing_content_instance.to_dict()
# create an instance of MissingContent from a dict
missing_content_from_dict = MissingContent.from_dict(missing_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


