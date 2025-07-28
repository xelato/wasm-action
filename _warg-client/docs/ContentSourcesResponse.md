# ContentSourcesResponse

Content digest sources for download.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_sources** | **object** | The map of content digest to sources. | 

## Example

```python
from _warg_client.models.content_sources_response import ContentSourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSourcesResponse from a JSON string
content_sources_response_instance = ContentSourcesResponse.from_json(json)
# print the JSON string representation of the object
print ContentSourcesResponse.to_json()

# convert the object into a dict
content_sources_response_dict = content_sources_response_instance.to_dict()
# create an instance of ContentSourcesResponse from a dict
content_sources_response_from_dict = ContentSourcesResponse.from_dict(content_sources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


