# dialmycalls_client.KeywordsApi

All URIs are relative to *https://api.dialmycalls.com/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_keyword_by_id**](KeywordsApi.md#delete_keyword_by_id) | **DELETE** /keyword/{KeywordId} | Delete Keyword
[**get_keyword_by_id**](KeywordsApi.md#get_keyword_by_id) | **GET** /keyword/{KeywordId} | Get Keyword
[**get_keywords**](KeywordsApi.md#get_keywords) | **GET** /keywords | List Keywords


# **delete_keyword_by_id**
> object delete_keyword_by_id(keyword_id)

Delete Keyword

Delete a keyword. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/keyword/$KEYWORD_ID ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.KeywordsApi()
keyword_id = 'keyword_id_example' # str | KeywordId

try: 
    # Delete Keyword
    api_response = api_instance.delete_keyword_by_id(keyword_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KeywordsApi->delete_keyword_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword_id** | **str**| KeywordId | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keyword_by_id**
> object get_keyword_by_id(keyword_id)

Get Keyword

Retrieve a keyword. <br><br> Returns a keyword object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H "Content-Type: application/json" -X GET https://$API_KEY@api.dialmycalls.com/2.0/keyword/$KEYWORD_ID ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.KeywordsApi()
keyword_id = 'keyword_id_example' # str | KeywordId

try: 
    # Get Keyword
    api_response = api_instance.get_keyword_by_id(keyword_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KeywordsApi->get_keyword_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword_id** | **str**| KeywordId | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keywords**
> object get_keywords(range=range)

List Keywords

Retrieve a list of keywords. <br><br> Returns a list of keyword objects. <br><br> ``` curl -i -H "Content-Type: application/json" -X GET https://$API_KEY@api.dialmycalls.com/2.0/keywords ```

### Example 
```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = dialmycalls_client.KeywordsApi()
range = 'range_example' # str | Range (ie \"records=201-300\") of keywords requested (optional)

try: 
    # List Keywords
    api_response = api_instance.get_keywords(range=range)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling KeywordsApi->get_keywords: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Range (ie \&quot;records&#x3D;201-300\&quot;) of keywords requested | [optional] 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

