# SignedCheckpoint

A signed registry checkpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Represents a supported hash. | 
**signature** | **str** | The algorithm-prefixed bytes of the signature (base64 encoded). | 
**contents** | [**TimestampedCheckpoint**](TimestampedCheckpoint.md) |  | 

## Example

```python
from _warg_client.models.signed_checkpoint import SignedCheckpoint

# TODO update the JSON string below
json = "{}"
# create an instance of SignedCheckpoint from a JSON string
signed_checkpoint_instance = SignedCheckpoint.from_json(json)
# print the JSON string representation of the object
print SignedCheckpoint.to_json()

# convert the object into a dict
signed_checkpoint_dict = signed_checkpoint_instance.to_dict()
# create an instance of SignedCheckpoint from a dict
signed_checkpoint_from_dict = SignedCheckpoint.from_dict(signed_checkpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


