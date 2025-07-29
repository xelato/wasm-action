# Checkpoint

A registry checkpoint.  Checkpoints are hashed by concatenating the following:   * A prefix of the byte string `WARG-CHECKPOINT-V0`   * The LEB128-encoded `logLength`   * The LEB128-length-prefixed `logRoot`   * The LEB128-length-prefixed `mapRoot` 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_length** | **int** | The log length of the checkpoint. | 
**log_root** | **str** | Represents a supported hash. | 
**map_root** | **str** | Represents a supported hash. | 

## Example

```python
from warg_openapi.models.checkpoint import Checkpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Checkpoint from a JSON string
checkpoint_instance = Checkpoint.from_json(json)
# print the JSON string representation of the object
print Checkpoint.to_json()

# convert the object into a dict
checkpoint_dict = checkpoint_instance.to_dict()
# create an instance of Checkpoint from a dict
checkpoint_from_dict = Checkpoint.from_dict(checkpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


