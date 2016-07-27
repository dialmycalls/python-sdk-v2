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
from dialmycalls_client.apis.keywords_api import KeywordsApi


class TestKeywordsApi(unittest.TestCase):
    """ KeywordsApi unit test stubs """

    def setUp(self):
        self.api = dialmycalls_client.apis.keywords_api.KeywordsApi()

    def tearDown(self):
        pass

    def test_delete_keyword_by_id(self):
        """
        Test case for delete_keyword_by_id

        Delete Keyword
        """
        pass

    def test_get_keyword_by_id(self):
        """
        Test case for get_keyword_by_id

        Get Keyword
        """
        pass

    def test_get_keywords(self):
        """
        Test case for get_keywords

        List Keywords
        """
        pass


if __name__ == '__main__':
    unittest.main()
