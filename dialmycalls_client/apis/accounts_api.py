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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AccountsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_access_account(self, create_access_account_parameters, **kwargs):
        """
        Add Access Account
        Add a access account. <br><br> Returns a access account object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"email\\\": \\\"test@test.com\\\", \\\"password\\\": \\\"1234A5678\\\", \\\"name\\\": \\\"John Doe\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/accessaccount ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_access_account(create_access_account_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateAccessAccountParameters create_access_account_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_access_account_with_http_info(create_access_account_parameters, **kwargs)
        else:
            (data) = self.create_access_account_with_http_info(create_access_account_parameters, **kwargs)
            return data

    def create_access_account_with_http_info(self, create_access_account_parameters, **kwargs):
        """
        Add Access Account
        Add a access account. <br><br> Returns a access account object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"email\\\": \\\"test@test.com\\\", \\\"password\\\": \\\"1234A5678\\\", \\\"name\\\": \\\"John Doe\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/accessaccount ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_access_account_with_http_info(create_access_account_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateAccessAccountParameters create_access_account_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_access_account_parameters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_access_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_access_account_parameters' is set
        if ('create_access_account_parameters' not in params) or (params['create_access_account_parameters'] is None):
            raise ValueError("Missing the required parameter `create_access_account_parameters` when calling `create_access_account`")

        resource_path = '/accessaccount'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_access_account_parameters' in params:
            body_params = params['create_access_account_parameters']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete_access_account_by_id(self, access_account_id, **kwargs):
        """
        Delete Access Account
        Delete a access account. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/accessaccount/$ACCESSACCOUNT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_access_account_by_id(access_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_account_id: AccessAccountId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_access_account_by_id_with_http_info(access_account_id, **kwargs)
        else:
            (data) = self.delete_access_account_by_id_with_http_info(access_account_id, **kwargs)
            return data

    def delete_access_account_by_id_with_http_info(self, access_account_id, **kwargs):
        """
        Delete Access Account
        Delete a access account. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/accessaccount/$ACCESSACCOUNT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_access_account_by_id_with_http_info(access_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_account_id: AccessAccountId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_access_account_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_account_id' is set
        if ('access_account_id' not in params) or (params['access_account_id'] is None):
            raise ValueError("Missing the required parameter `access_account_id` when calling `delete_access_account_by_id`")

        resource_path = '/accessaccount/{AccessAccountId}'.replace('{format}', 'json')
        path_params = {}
        if 'access_account_id' in params:
            path_params['AccessAccountId'] = params['access_account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_access_account_by_id(self, access_account_id, **kwargs):
        """
        Get Access Account
        Retrieve an access account. <br><br> Returns a access account object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/accessaccount/$ACCESSACCOUNT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_access_account_by_id(access_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_account_id: AccessAccountId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_access_account_by_id_with_http_info(access_account_id, **kwargs)
        else:
            (data) = self.get_access_account_by_id_with_http_info(access_account_id, **kwargs)
            return data

    def get_access_account_by_id_with_http_info(self, access_account_id, **kwargs):
        """
        Get Access Account
        Retrieve an access account. <br><br> Returns a access account object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/accessaccount/$ACCESSACCOUNT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_access_account_by_id_with_http_info(access_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_account_id: AccessAccountId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_account_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_account_id' is set
        if ('access_account_id' not in params) or (params['access_account_id'] is None):
            raise ValueError("Missing the required parameter `access_account_id` when calling `get_access_account_by_id`")

        resource_path = '/accessaccount/{AccessAccountId}'.replace('{format}', 'json')
        path_params = {}
        if 'access_account_id' in params:
            path_params['AccessAccountId'] = params['access_account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_access_accounts(self, **kwargs):
        """
        List Access Accounts
        Retrieve a list of access accounts. <br><br> Returns a list of access account objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/accessaccounts ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_access_accounts(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str range: Range (ie \"records=201-300\") of accessaccounts requested
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_access_accounts_with_http_info(**kwargs)
        else:
            (data) = self.get_access_accounts_with_http_info(**kwargs)
            return data

    def get_access_accounts_with_http_info(self, **kwargs):
        """
        List Access Accounts
        Retrieve a list of access accounts. <br><br> Returns a list of access account objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/accessaccounts ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_access_accounts_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str range: Range (ie \"records=201-300\") of accessaccounts requested
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['range']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/accessaccounts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'range' in params:
            header_params['Range'] = params['range']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_account(self, **kwargs):
        """
        Get Account
        Retrieve account details. <br><br> Returns a account object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/account ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_with_http_info(**kwargs)
        else:
            (data) = self.get_account_with_http_info(**kwargs)
            return data

    def get_account_with_http_info(self, **kwargs):
        """
        Get Account
        Retrieve account details. <br><br> Returns a account object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/account ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/account'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_access_account_by_id(self, update_access_account_by_id_parameters, access_account_id, **kwargs):
        """
        Update Access Account
        Update an existing access account. <br><br> Returns a access account object if a valid identifier was provided and input validation passed, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X PUT -d \"{\\\"name\\\": \\\"New Name\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/accessaccount/$ACCESSACCOUNT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_access_account_by_id(update_access_account_by_id_parameters, access_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateAccessAccountByIdParameters update_access_account_by_id_parameters: Request body (required)
        :param str access_account_id: AccessAccountId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_access_account_by_id_with_http_info(update_access_account_by_id_parameters, access_account_id, **kwargs)
        else:
            (data) = self.update_access_account_by_id_with_http_info(update_access_account_by_id_parameters, access_account_id, **kwargs)
            return data

    def update_access_account_by_id_with_http_info(self, update_access_account_by_id_parameters, access_account_id, **kwargs):
        """
        Update Access Account
        Update an existing access account. <br><br> Returns a access account object if a valid identifier was provided and input validation passed, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X PUT -d \"{\\\"name\\\": \\\"New Name\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/accessaccount/$ACCESSACCOUNT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_access_account_by_id_with_http_info(update_access_account_by_id_parameters, access_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateAccessAccountByIdParameters update_access_account_by_id_parameters: Request body (required)
        :param str access_account_id: AccessAccountId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['update_access_account_by_id_parameters', 'access_account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_access_account_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'update_access_account_by_id_parameters' is set
        if ('update_access_account_by_id_parameters' not in params) or (params['update_access_account_by_id_parameters'] is None):
            raise ValueError("Missing the required parameter `update_access_account_by_id_parameters` when calling `update_access_account_by_id`")
        # verify the required parameter 'access_account_id' is set
        if ('access_account_id' not in params) or (params['access_account_id'] is None):
            raise ValueError("Missing the required parameter `access_account_id` when calling `update_access_account_by_id`")

        resource_path = '/accessaccount/{AccessAccountId}'.replace('{format}', 'json')
        path_params = {}
        if 'access_account_id' in params:
            path_params['AccessAccountId'] = params['access_account_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_access_account_by_id_parameters' in params:
            body_params = params['update_access_account_by_id_parameters']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='object',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
