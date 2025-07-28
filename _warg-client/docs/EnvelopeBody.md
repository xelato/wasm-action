# EnvelopeBody

A signed envelope body.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Represents a supported hash. | 
**signature** | **str** | The algorithm-prefixed bytes of the signature (base64 encoded). | 
**content_bytes** | **bytearray** | Base64-encoded bytes of the content.  The content of an envelope body is typically a serialized protocol buffer representing an operator or package record.  | 

## Example

```python
from _warg_client.models.envelope_body import EnvelopeBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeBody from a JSON string
envelope_body_instance = EnvelopeBody.from_json(json)
# print the JSON string representation of the object
print EnvelopeBody.to_json()

# convert the object into a dict
envelope_body_dict = envelope_body_instance.to_dict()
# create an instance of EnvelopeBody from a dict
envelope_body_from_dict = EnvelopeBody.from_dict(envelope_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


