# dialmycalls_client.DoNotContactsApi

All URIs are relative to *https://api.dialmycalls.com/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_do_not_contacts**](DoNotContactsApi.md#get_do_not_contacts) | **GET** /donotcontacts | List DoNotContacts


# **get_do_not_contacts**
> object get_do_not_contacts(range=range)

List DoNotContacts

Retrieve a list of donotcontacts. <br><br> Returns a list of donotcontact objects. <br><br> ``` curl -i -H "Content-Type: application/json" -X GET https://$API_KEY@api.dialmycalls.com/2.0/donotcontacts ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.DoNotContactsApi()
range = 'range_example' # str | Range (ie \"records=201-300\") of donotcontacts requested (optional)

try: 
    # List DoNotContacts
    api_response = api_instance.get_do_not_contacts(range=range)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DoNotContactsApi->get_do_not_contacts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Range (ie \&quot;records&#x3D;201-300\&quot;) of donotcontacts requested | [optional] 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

