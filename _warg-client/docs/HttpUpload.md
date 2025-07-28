# HttpUpload

A HTTP upload endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of upload endpoint. | 
**method** | **str** | The HTTP method for the upload request. Uppercase is required. | 
**url** | **str** | The URL of the upload endpoint, which may be relative to the API base URL. | 
**headers** | [**HttpUploadHeaders**](HttpUploadHeaders.md) |  | [optional] 

## Example

```python
from _warg_client.models.http_upload import HttpUpload

# TODO update the JSON string below
json = "{}"
# create an instance of HttpUpload from a JSON string
http_upload_instance = HttpUpload.from_json(json)
# print the JSON string representation of the object
print HttpUpload.to_json()

# convert the object into a dict
http_upload_dict = http_upload_instance.to_dict()
# create an instance of HttpUpload from a dict
http_upload_from_dict = HttpUpload.from_dict(http_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


