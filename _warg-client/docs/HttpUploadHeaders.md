# HttpUploadHeaders

The HTTP headers for upload request. Header name is required to be all lowercase.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | **str** | Authorization header. | [optional] 
**content_type** | **str** | Content type header. | [optional] 

## Example

```python
from _warg_client.models.http_upload_headers import HttpUploadHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of HttpUploadHeaders from a JSON string
http_upload_headers_instance = HttpUploadHeaders.from_json(json)
# print the JSON string representation of the object
print HttpUploadHeaders.to_json()

# convert the object into a dict
http_upload_headers_dict = http_upload_headers_instance.to_dict()
# create an instance of HttpUploadHeaders from a dict
http_upload_headers_from_dict = HttpUploadHeaders.from_dict(http_upload_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


