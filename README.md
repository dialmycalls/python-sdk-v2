# dialmycalls_client
The DialMyCalls API

For more information, please visit [https://www.dialmycalls.com](https://www.dialmycalls.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/dialmycalls/python-sdk-v2.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/dialmycalls/python-sdk-v2.git`)

Then import the package:
```python
import dialmycalls_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dialmycalls_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import dialmycalls_client
from dialmycalls_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
dialmycalls_client.configuration.api_key['X-Auth-ApiKey'] = 'YOUR_API_KEY'
# create an instance of the API class
api_instance = dialmycalls_client.AccountsApi
create_access_account_parameters = dialmycalls_client.CreateAccessAccountParameters() # CreateAccessAccountParameters | Request body

try:
    # Add Access Account
    api_response = api_instance.create_access_account(create_access_account_parameters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->create_access_account: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.dialmycalls.com/2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**create_access_account**](docs/AccountsApi.md#create_access_account) | **POST** /accessaccount | Add Access Account
*AccountsApi* | [**delete_access_account_by_id**](docs/AccountsApi.md#delete_access_account_by_id) | **DELETE** /accessaccount/{AccessAccountId} | Delete Access Account
*AccountsApi* | [**get_access_account_by_id**](docs/AccountsApi.md#get_access_account_by_id) | **GET** /accessaccount/{AccessAccountId} | Get Access Account
*AccountsApi* | [**get_access_accounts**](docs/AccountsApi.md#get_access_accounts) | **GET** /accessaccounts | List Access Accounts
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /account | Get Account
*AccountsApi* | [**update_access_account_by_id**](docs/AccountsApi.md#update_access_account_by_id) | **PUT** /accessaccount/{AccessAccountId} | Update Access Account
*CallerIdsApi* | [**create_caller_id**](docs/CallerIdsApi.md#create_caller_id) | **POST** /callerid | Add Caller ID
*CallerIdsApi* | [**create_unverified_caller_id**](docs/CallerIdsApi.md#create_unverified_caller_id) | **POST** /verify/callerid | Add Caller ID (Unverified)
*CallerIdsApi* | [**delete_caller_id_by_id**](docs/CallerIdsApi.md#delete_caller_id_by_id) | **DELETE** /callerid/{CalleridId} | Delete Caller ID
*CallerIdsApi* | [**get_caller_id_by_id**](docs/CallerIdsApi.md#get_caller_id_by_id) | **GET** /callerid/{CalleridId} | Get Caller ID
*CallerIdsApi* | [**get_caller_ids**](docs/CallerIdsApi.md#get_caller_ids) | **GET** /callerids | List Caller IDs
*CallerIdsApi* | [**update_caller_id_by_id**](docs/CallerIdsApi.md#update_caller_id_by_id) | **PUT** /callerid/{CalleridId} | Update Caller ID
*CallerIdsApi* | [**verify_caller_id_by_id**](docs/CallerIdsApi.md#verify_caller_id_by_id) | **PUT** /verify/callerid/{CalleridId} | Verify Caller ID
*CallsApi* | [**cancel_call_by_id**](docs/CallsApi.md#cancel_call_by_id) | **DELETE** /service/call/{CallId} | Cancel Call
*CallsApi* | [**create_call**](docs/CallsApi.md#create_call) | **POST** /service/call | Create Call
*CallsApi* | [**get_call_by_id**](docs/CallsApi.md#get_call_by_id) | **GET** /service/call/{CallId} | Get Call
*CallsApi* | [**get_call_recipients_by_call_id**](docs/CallsApi.md#get_call_recipients_by_call_id) | **GET** /service/call/{CallId}/recipients | Get Call Recipients
*CallsApi* | [**get_calls**](docs/CallsApi.md#get_calls) | **GET** /service/calls | List Calls
*ContactsApi* | [**create_contact**](docs/ContactsApi.md#create_contact) | **POST** /contact | Add Contact
*ContactsApi* | [**delete_contact_by_id**](docs/ContactsApi.md#delete_contact_by_id) | **DELETE** /contact/{ContactId} | Delete Contact
*ContactsApi* | [**get_contact_by_id**](docs/ContactsApi.md#get_contact_by_id) | **GET** /contact/{ContactId} | Get Contact
*ContactsApi* | [**get_contacts**](docs/ContactsApi.md#get_contacts) | **GET** /contacts | List Contacts
*ContactsApi* | [**get_contacts_by_group_id**](docs/ContactsApi.md#get_contacts_by_group_id) | **GET** /contacts/{GroupId} | List Contacts in Group
*ContactsApi* | [**update_contact_by_id**](docs/ContactsApi.md#update_contact_by_id) | **PUT** /contact/{ContactId} | Update Contact
*DoNotContactsApi* | [**get_do_not_contacts**](docs/DoNotContactsApi.md#get_do_not_contacts) | **GET** /donotcontacts | List DoNotContacts
*GroupsApi* | [**create_group**](docs/GroupsApi.md#create_group) | **POST** /group | Add Group
*GroupsApi* | [**delete_group_by_id**](docs/GroupsApi.md#delete_group_by_id) | **DELETE** /group/{GroupId} | Delete Group
*GroupsApi* | [**get_group_by_id**](docs/GroupsApi.md#get_group_by_id) | **GET** /group/{GroupId} | Get Group
*GroupsApi* | [**get_groups**](docs/GroupsApi.md#get_groups) | **GET** /groups | List Groups
*GroupsApi* | [**update_group_by_id**](docs/GroupsApi.md#update_group_by_id) | **PUT** /group/{GroupId} | Update Group
*KeywordsApi* | [**delete_keyword_by_id**](docs/KeywordsApi.md#delete_keyword_by_id) | **DELETE** /keyword/{KeywordId} | Delete Keyword
*KeywordsApi* | [**get_keyword_by_id**](docs/KeywordsApi.md#get_keyword_by_id) | **GET** /keyword/{KeywordId} | Get Keyword
*KeywordsApi* | [**get_keywords**](docs/KeywordsApi.md#get_keywords) | **GET** /keywords | List Keywords
*RecordingsApi* | [**create_recording**](docs/RecordingsApi.md#create_recording) | **POST** /recording/tts | Create Recording (Text-to-Speech)
*RecordingsApi* | [**create_recording_by_phone**](docs/RecordingsApi.md#create_recording_by_phone) | **POST** /recording/phone | Create Recording (Phone)
*RecordingsApi* | [**create_recording_by_url**](docs/RecordingsApi.md#create_recording_by_url) | **POST** /recording/url | Create Recording (URL)
*RecordingsApi* | [**delete_recording_by_id**](docs/RecordingsApi.md#delete_recording_by_id) | **DELETE** /recording/{RecordingId} | Delete Recording
*RecordingsApi* | [**get_recording_by_id**](docs/RecordingsApi.md#get_recording_by_id) | **GET** /recording/{RecordingId} | Get Recording
*RecordingsApi* | [**get_recordings**](docs/RecordingsApi.md#get_recordings) | **GET** /recordings | List Recordings
*RecordingsApi* | [**update_recording_by_id**](docs/RecordingsApi.md#update_recording_by_id) | **PUT** /recording/{RecordingId} | Update Recording
*TextsApi* | [**cancel_text_by_id**](docs/TextsApi.md#cancel_text_by_id) | **DELETE** /service/text/{TextId} | Cancel Text
*TextsApi* | [**create_text**](docs/TextsApi.md#create_text) | **POST** /service/text | Create Text
*TextsApi* | [**delete_incoming_text_by_id**](docs/TextsApi.md#delete_incoming_text_by_id) | **DELETE** /incoming/text/{TextId} | Delete Incoming Text
*TextsApi* | [**get_incoming_text_by_id**](docs/TextsApi.md#get_incoming_text_by_id) | **GET** /incoming/text/{TextId} | Get Incoming Text
*TextsApi* | [**get_incoming_texts**](docs/TextsApi.md#get_incoming_texts) | **GET** /incoming/texts | List Incoming Texts
*TextsApi* | [**get_short_codes**](docs/TextsApi.md#get_short_codes) | **GET** /shortcodes | List Shortcodes
*TextsApi* | [**get_text_by_id**](docs/TextsApi.md#get_text_by_id) | **GET** /service/text/{TextId} | Get Text
*TextsApi* | [**get_text_recipients_by_text_id**](docs/TextsApi.md#get_text_recipients_by_text_id) | **GET** /service/text/{TextId}/recipients | Get Text Recipients
*TextsApi* | [**get_texts**](docs/TextsApi.md#get_texts) | **GET** /service/texts | List Texts
*VanityNumbersApi* | [**delete_vanity_number_by_id**](docs/VanityNumbersApi.md#delete_vanity_number_by_id) | **DELETE** /vanitynumber/{VanityNumberId} | Delete Vanity Number
*VanityNumbersApi* | [**get_vanity_number_by_id**](docs/VanityNumbersApi.md#get_vanity_number_by_id) | **GET** /vanitynumber/{VanityNumberId} | Get Vanity Number
*VanityNumbersApi* | [**get_vanity_numbers**](docs/VanityNumbersApi.md#get_vanity_numbers) | **GET** /vanitynumbers | List Vanity Numbers
*VanityNumbersApi* | [**update_vanity_number_by_id**](docs/VanityNumbersApi.md#update_vanity_number_by_id) | **PUT** /vanitynumber/{VanityNumberId} | Update Vanity Number


## Documentation For Models

 - [Accessaccount](docs/Accessaccount.md)
 - [Account](docs/Account.md)
 - [CallRecipient](docs/CallRecipient.md)
 - [Callerid](docs/Callerid.md)
 - [Callservice](docs/Callservice.md)
 - [Contact](docs/Contact.md)
 - [ContactAttributes](docs/ContactAttributes.md)
 - [CreateAccessAccountParameters](docs/CreateAccessAccountParameters.md)
 - [CreateCallParameters](docs/CreateCallParameters.md)
 - [CreateCallerIdParameters](docs/CreateCallerIdParameters.md)
 - [CreateContactParameters](docs/CreateContactParameters.md)
 - [CreateGroupParameters](docs/CreateGroupParameters.md)
 - [CreateRecordingByPhoneParameters](docs/CreateRecordingByPhoneParameters.md)
 - [CreateRecordingByUrlParameters](docs/CreateRecordingByUrlParameters.md)
 - [CreateRecordingParameters](docs/CreateRecordingParameters.md)
 - [CreateTextParameters](docs/CreateTextParameters.md)
 - [CreateUnverifiedCallerIdParameters](docs/CreateUnverifiedCallerIdParameters.md)
 - [Donotcontact](docs/Donotcontact.md)
 - [Group](docs/Group.md)
 - [Identifier](docs/Identifier.md)
 - [Incomingtext](docs/Incomingtext.md)
 - [Keyword](docs/Keyword.md)
 - [Polling](docs/Polling.md)
 - [PushToListenAgain](docs/PushToListenAgain.md)
 - [PushToOptOut](docs/PushToOptOut.md)
 - [PushToRecord](docs/PushToRecord.md)
 - [PushToTalk](docs/PushToTalk.md)
 - [Recording](docs/Recording.md)
 - [Service](docs/Service.md)
 - [Shortcode](docs/Shortcode.md)
 - [TextRecipient](docs/TextRecipient.md)
 - [UpdateAccessAccountByIdParameters](docs/UpdateAccessAccountByIdParameters.md)
 - [UpdateCallerIdByIdParameters](docs/UpdateCallerIdByIdParameters.md)
 - [UpdateContactByIdParameters](docs/UpdateContactByIdParameters.md)
 - [UpdateGroupByIdParameters](docs/UpdateGroupByIdParameters.md)
 - [UpdateRecordingByIdParameters](docs/UpdateRecordingByIdParameters.md)
 - [UpdateVanityNumberByIdParameters](docs/UpdateVanityNumberByIdParameters.md)
 - [Vanitynumber](docs/Vanitynumber.md)
 - [VerifyCallerIdByIdParameters](docs/VerifyCallerIdByIdParameters.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-Auth-ApiKey
- **Location**: HTTP header


## Author

support@dialmycalls.com

