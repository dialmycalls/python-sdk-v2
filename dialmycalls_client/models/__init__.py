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

# import models into model package
from .accessaccount import Accessaccount
from .account import Account
from .call_recipient import CallRecipient
from .callerid import Callerid
from .callservice import Callservice
from .contact import Contact
from .contact_attributes import ContactAttributes
from .create_access_account_parameters import CreateAccessAccountParameters
from .create_call_parameters import CreateCallParameters
from .create_caller_id_parameters import CreateCallerIdParameters
from .create_contact_parameters import CreateContactParameters
from .create_group_parameters import CreateGroupParameters
from .create_recording_by_phone_parameters import CreateRecordingByPhoneParameters
from .create_recording_by_url_parameters import CreateRecordingByUrlParameters
from .create_recording_parameters import CreateRecordingParameters
from .create_text_parameters import CreateTextParameters
from .create_unverified_caller_id_parameters import CreateUnverifiedCallerIdParameters
from .donotcontact import Donotcontact
from .group import Group
from .identifier import Identifier
from .incomingtext import Incomingtext
from .keyword import Keyword
from .polling import Polling
from .push_to_listen_again import PushToListenAgain
from .push_to_opt_out import PushToOptOut
from .push_to_record import PushToRecord
from .push_to_talk import PushToTalk
from .recording import Recording
from .service import Service
from .shortcode import Shortcode
from .text_recipient import TextRecipient
from .update_access_account_by_id_parameters import UpdateAccessAccountByIdParameters
from .update_caller_id_by_id_parameters import UpdateCallerIdByIdParameters
from .update_contact_by_id_parameters import UpdateContactByIdParameters
from .update_group_by_id_parameters import UpdateGroupByIdParameters
from .update_recording_by_id_parameters import UpdateRecordingByIdParameters
from .update_vanity_number_by_id_parameters import UpdateVanityNumberByIdParameters
from .vanitynumber import Vanitynumber
from .verify_caller_id_by_id_parameters import VerifyCallerIdByIdParameters