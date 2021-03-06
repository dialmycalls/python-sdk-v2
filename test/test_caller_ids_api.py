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

import os
import sys
import unittest

import dialmycalls_client
from dialmycalls_client.rest import ApiException
from dialmycalls_client.apis.caller_ids_api import CallerIdsApi


class TestCallerIdsApi(unittest.TestCase):
    """ CallerIdsApi unit test stubs """

    def setUp(self):
        self.api = dialmycalls_client.apis.caller_ids_api.CallerIdsApi()

    def tearDown(self):
        pass

    def test_create_caller_id(self):
        """
        Test case for create_caller_id

        Add Caller ID
        """
        pass

    def test_create_unverified_caller_id(self):
        """
        Test case for create_unverified_caller_id

        Add Caller ID (Unverified)
        """
        pass

    def test_delete_caller_id_by_id(self):
        """
        Test case for delete_caller_id_by_id

        Delete Caller ID
        """
        pass

    def test_get_caller_id_by_id(self):
        """
        Test case for get_caller_id_by_id

        Get Caller ID
        """
        pass

    def test_get_caller_ids(self):
        """
        Test case for get_caller_ids

        List Caller IDs
        """
        pass

    def test_update_caller_id_by_id(self):
        """
        Test case for update_caller_id_by_id

        Update Caller ID
        """
        pass

    def test_verify_caller_id_by_id(self):
        """
        Test case for verify_caller_id_by_id

        Verify Caller ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
