# dialmycalls_client.GroupsApi

All URIs are relative to *https://api.dialmycalls.com/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupsApi.md#create_group) | **POST** /group | Add Group
[**delete_group_by_id**](GroupsApi.md#delete_group_by_id) | **DELETE** /group/{GroupId} | Delete Group
[**get_group_by_id**](GroupsApi.md#get_group_by_id) | **GET** /group/{GroupId} | Get Group
[**get_groups**](GroupsApi.md#get_groups) | **GET** /groups | List Groups
[**update_group_by_id**](GroupsApi.md#update_group_by_id) | **PUT** /group/{GroupId} | Update Group


# **create_group**
> object create_group(create_group_parameters)

Add Group

Add a contact group. <br><br> Returns a group object on success, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X POST -d "{\"name\": \"Test Group\"}" https://$API_KEY@api.dialmycalls.com/2.0/group ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.GroupsApi()
create_group_parameters = dialmycalls_client.CreateGroupParameters() # CreateGroupParameters | Request body

try: 
    # Add Group
    api_response = api_instance.create_group(create_group_parameters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->create_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_parameters** | [**CreateGroupParameters**](CreateGroupParameters.md)| Request body | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_by_id**
> object delete_group_by_id(group_id)

Delete Group

Delete a contact group. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/group/$GROUP_ID ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.GroupsApi()
group_id = 'group_id_example' # str | GroupId

try: 
    # Delete Group
    api_response = api_instance.delete_group_by_id(group_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->delete_group_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| GroupId | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_by_id**
> object get_group_by_id(group_id)

Get Group

Retrieve a contact group. <br><br> Returns a group object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X GET https://$API_KEY@api.dialmycalls.com/2.0/group/$GROUP_ID ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.GroupsApi()
group_id = 'group_id_example' # str | GroupId

try: 
    # Get Group
    api_response = api_instance.get_group_by_id(group_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->get_group_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| GroupId | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> object get_groups(range=range)

List Groups

Retrieve a list of contact groups. <br><br> Returns a list of group objects. <br><br> ``` curl -i -H "Content-Type: application/json" -X GET https://$API_KEY@api.dialmycalls.com/2.0/groups ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.GroupsApi()
range = 'range_example' # str | Range (ie \"records=201-300\") of groups requested (optional)

try: 
    # List Groups
    api_response = api_instance.get_groups(range=range)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->get_groups: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Range (ie \&quot;records&#x3D;201-300\&quot;) of groups requested | [optional] 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_by_id**
> object update_group_by_id(update_group_by_id_parameters, group_id)

Update Group

Update an existing contact group. <br><br> Returns a group object if a valid identifier was provided and input validation passed, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X PUT -d "{\"name\": \"Test Group Updated\"}" https://$API_KEY@api.dialmycalls.com/2.0/group/$GROUP_ID ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.GroupsApi()
update_group_by_id_parameters = dialmycalls_client.UpdateGroupByIdParameters() # UpdateGroupByIdParameters | Request body
group_id = 'group_id_example' # str | GroupId

try: 
    # Update Group
    api_response = api_instance.update_group_by_id(update_group_by_id_parameters, group_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->update_group_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_group_by_id_parameters** | [**UpdateGroupByIdParameters**](UpdateGroupByIdParameters.md)| Request body | 
 **group_id** | **str**| GroupId | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

