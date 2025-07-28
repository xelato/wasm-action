# TimestampedCheckpoint

A timestamped registry checkpoint.  Checkpoints are hashed by concatenating the following:   * A prefix of the byte string `WARG-TIMESTAMPED-CHECKPOINT-V0`   * The LEB128-encoded `logLength`   * The LEB128-length-prefixed `logRoot`   * The LEB128-length-prefixed `mapRoot`   * The LEB128-encoded `timestamp` 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_length** | **int** | The log length of the checkpoint. | 
**log_root** | **str** | Represents a supported hash. | 
**map_root** | **str** | Represents a supported hash. | 
**timestamp** | **int** | The time that the checkpoint was generated, in seconds since the Unix epoch.  | 

## Example

```python
from _warg_client.models.timestamped_checkpoint import TimestampedCheckpoint

# TODO update the JSON string below
json = "{}"
# create an instance of TimestampedCheckpoint from a JSON string
timestamped_checkpoint_instance = TimestampedCheckpoint.from_json(json)
# print the JSON string representation of the object
print TimestampedCheckpoint.to_json()

# convert the object into a dict
timestamped_checkpoint_dict = timestamped_checkpoint_instance.to_dict()
# create an instance of TimestampedCheckpoint from a dict
timestamped_checkpoint_from_dict = TimestampedCheckpoint.from_dict(timestamped_checkpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


