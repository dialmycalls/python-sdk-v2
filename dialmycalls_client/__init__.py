# coding: utf-8

"""
    DialMyCalls API

    The DialMyCalls API

    OpenAPI spec version: 2.0.1
    Contact: support@dialmycalls.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into sdk package
from .models.accessaccount import Accessaccount
from .models.account import Account
from .models.call_recipient import CallRecipient
from .models.callerid import Callerid
from .models.callservice import Callservice
from .models.contact import Contact
from .models.contact_attributes import ContactAttributes
from .models.create_access_account_parameters import CreateAccessAccountParameters
from .models.create_call_parameters import CreateCallParameters
from .models.create_caller_id_parameters import CreateCallerIdParameters
from .models.create_contact_parameters import CreateContactParameters
from .models.create_group_parameters import CreateGroupParameters
from .models.create_recording_by_phone_parameters import CreateRecordingByPhoneParameters
from .models.create_recording_by_url_parameters import CreateRecordingByUrlParameters
from .models.create_recording_parameters import CreateRecordingParameters
from .models.create_text_parameters import CreateTextParameters
from .models.create_unverified_caller_id_parameters import CreateUnverifiedCallerIdParameters
from .models.donotcontact import Donotcontact
from .models.group import Group
from .models.identifier import Identifier
from .models.incomingtext import Incomingtext
from .models.keyword import Keyword
from .models.polling import Polling
from .models.push_to_listen_again import PushToListenAgain
from .models.push_to_opt_out import PushToOptOut
from .models.push_to_record import PushToRecord
from .models.push_to_talk import PushToTalk
from .models.recording import Recording
from .models.service import Service
from .models.shortcode import Shortcode
from .models.text_recipient import TextRecipient
from .models.update_access_account_by_id_parameters import UpdateAccessAccountByIdParameters
from .models.update_caller_id_by_id_parameters import UpdateCallerIdByIdParameters
from .models.update_contact_by_id_parameters import UpdateContactByIdParameters
from .models.update_group_by_id_parameters import UpdateGroupByIdParameters
from .models.update_recording_by_id_parameters import UpdateRecordingByIdParameters
from .models.update_vanity_number_by_id_parameters import UpdateVanityNumberByIdParameters
from .models.vanitynumber import Vanitynumber
from .models.verify_caller_id_by_id_parameters import VerifyCallerIdByIdParameters

# import apis into sdk package
from .apis.accounts_api import AccountsApi
from .apis.caller_ids_api import CallerIdsApi
from .apis.calls_api import CallsApi
from .apis.contacts_api import ContactsApi
from .apis.do_not_contacts_api import DoNotContactsApi
from .apis.groups_api import GroupsApi
from .apis.keywords_api import KeywordsApi
from .apis.recordings_api import RecordingsApi
from .apis.texts_api import TextsApi
from .apis.vanity_numbers_api import VanityNumbersApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
