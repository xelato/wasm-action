# PublishedRecordEnvelope

A signed envelope body with the published registry log index.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_bytes** | **bytearray** | Base64-encoded bytes of the content.  The content of an envelope body is typically a serialized protocol buffer representing an operator or package record.  | 
**key_id** | **str** | Represents a supported hash. | 
**signature** | **str** | The algorithm-prefixed bytes of the signature (base64 encoded). | 
**registry_index** | **int** | The index of the published record in the registry log. | 
**fetch_token** | **str** | The fetch token for the registry log. Used as a cursor for incrementally fetching log records. | 

## Example

```python
from warg_openapi.models.published_record_envelope import PublishedRecordEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedRecordEnvelope from a JSON string
published_record_envelope_instance = PublishedRecordEnvelope.from_json(json)
# print the JSON string representation of the object
print PublishedRecordEnvelope.to_json()

# convert the object into a dict
published_record_envelope_dict = published_record_envelope_instance.to_dict()
# create an instance of PublishedRecordEnvelope from a dict
published_record_envelope_from_dict = PublishedRecordEnvelope.from_dict(published_record_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


