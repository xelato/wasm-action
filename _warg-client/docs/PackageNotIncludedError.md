# PackageNotIncludedError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**reason** | **str** | The reason why the bundle could not be generated. | 
**log_id** | **str** | Represents a supported hash. | 

## Example

```python
from _warg_client.models.package_not_included_error import PackageNotIncludedError

# TODO update the JSON string below
json = "{}"
# create an instance of PackageNotIncludedError from a JSON string
package_not_included_error_instance = PackageNotIncludedError.from_json(json)
# print the JSON string representation of the object
print PackageNotIncludedError.to_json()

# convert the object into a dict
package_not_included_error_dict = package_not_included_error_instance.to_dict()
# create an instance of PackageNotIncludedError from a dict
package_not_included_error_from_dict = PackageNotIncludedError.from_dict(package_not_included_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


