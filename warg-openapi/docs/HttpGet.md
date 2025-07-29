# HttpGet

A known GET HTTP content source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of content source. | 
**url** | **str** | The URL of the content. | 
**accept_ranges** | **bool** | Flag indicating if the server accepts byte ranges with &#x60;Range&#x60; header. | [optional] 
**size** | **int** | Content size in bytes. | [optional] 

## Example

```python
from warg_openapi.models.http_get import HttpGet

# TODO update the JSON string below
json = "{}"
# create an instance of HttpGet from a JSON string
http_get_instance = HttpGet.from_json(json)
# print the JSON string representation of the object
print HttpGet.to_json()

# convert the object into a dict
http_get_dict = http_get_instance.to_dict()
# create an instance of HttpGet from a dict
http_get_from_dict = HttpGet.from_dict(http_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


