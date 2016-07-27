# dialmycalls_client.VanityNumbersApi

All URIs are relative to *https://api.dialmycalls.com/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vanity_number_by_id**](VanityNumbersApi.md#delete_vanity_number_by_id) | **DELETE** /vanitynumber/{VanityNumberId} | Delete Vanity Number
[**get_vanity_number_by_id**](VanityNumbersApi.md#get_vanity_number_by_id) | **GET** /vanitynumber/{VanityNumberId} | Get Vanity Number
[**get_vanity_numbers**](VanityNumbersApi.md#get_vanity_numbers) | **GET** /vanitynumbers | List Vanity Numbers
[**update_vanity_number_by_id**](VanityNumbersApi.md#update_vanity_number_by_id) | **PUT** /vanitynumber/{VanityNumberId} | Update Vanity Number


# **delete_vanity_number_by_id**
> object delete_vanity_number_by_id(vanity_number_id)

Delete Vanity Number

Delete a vanity number. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/keyword/$VANITYNUMBER_ID ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.VanityNumbersApi()
vanity_number_id = 'vanity_number_id_example' # str | VanityNumberId

try: 
    # Delete Vanity Number
    api_response = api_instance.delete_vanity_number_by_id(vanity_number_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VanityNumbersApi->delete_vanity_number_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vanity_number_id** | **str**| VanityNumberId | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vanity_number_by_id**
> object get_vanity_number_by_id(vanity_number_id)

Get Vanity Number

Retrieve a vanity number. <br><br> Returns a vanitynumber object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X GET https://$API_KEY@api.dialmycalls.com/2.0/vanitynumber/$VANITYNUMBER_ID ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.VanityNumbersApi()
vanity_number_id = 'vanity_number_id_example' # str | VanityNumberId

try: 
    # Get Vanity Number
    api_response = api_instance.get_vanity_number_by_id(vanity_number_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VanityNumbersApi->get_vanity_number_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vanity_number_id** | **str**| VanityNumberId | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vanity_numbers**
> object get_vanity_numbers(range=range)

List Vanity Numbers

Retrieve a list of vanity numbers. <br><br> Returns a list of vanitynumber objects. <br><br> ``` curl -i -H "Content-Type: application/json" -X GET https://$API_KEY@api.dialmycalls.com/2.0/vanitynumbers ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.VanityNumbersApi()
range = 'range_example' # str | Range (ie \"records=201-300\") of vanitynumbers requested (optional)

try: 
    # List Vanity Numbers
    api_response = api_instance.get_vanity_numbers(range=range)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VanityNumbersApi->get_vanity_numbers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Range (ie \&quot;records&#x3D;201-300\&quot;) of vanitynumbers requested | [optional] 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vanity_number_by_id**
> object update_vanity_number_by_id(update_vanity_number_by_id_parameters, vanity_number_id)

Update Vanity Number

Update a vanity number. <br><br> Returns a vanitynumber object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X PUT -d "{\"ptt_number_id\":\"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee\",\"call_options\":{\"voicemail\":true}}" https://$API_KEY@api.dialmycalls.com/2.0/vanitynumber/$VANITYNUMBER_ID ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.VanityNumbersApi()
update_vanity_number_by_id_parameters = dialmycalls_client.UpdateVanityNumberByIdParameters() # UpdateVanityNumberByIdParameters | Request body
vanity_number_id = 'vanity_number_id_example' # str | VanityNumberId

try: 
    # Update Vanity Number
    api_response = api_instance.update_vanity_number_by_id(update_vanity_number_by_id_parameters, vanity_number_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VanityNumbersApi->update_vanity_number_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_vanity_number_by_id_parameters** | [**UpdateVanityNumberByIdParameters**](UpdateVanityNumberByIdParameters.md)| Request body | 
 **vanity_number_id** | **str**| VanityNumberId | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

