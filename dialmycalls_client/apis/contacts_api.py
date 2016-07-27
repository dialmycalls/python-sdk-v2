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


class ContactsApi(object):
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

    def create_contact(self, create_contact_parameters, **kwargs):
        """
        Add Contact
        Add a contact to your contact list. <br><br> Returns a contact object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"phone\\\": \\\"5555555555\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/contact ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_contact(create_contact_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateContactParameters create_contact_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_contact_with_http_info(create_contact_parameters, **kwargs)
        else:
            (data) = self.create_contact_with_http_info(create_contact_parameters, **kwargs)
            return data

    def create_contact_with_http_info(self, create_contact_parameters, **kwargs):
        """
        Add Contact
        Add a contact to your contact list. <br><br> Returns a contact object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"phone\\\": \\\"5555555555\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/contact ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_contact_with_http_info(create_contact_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateContactParameters create_contact_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_contact_parameters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_contact_parameters' is set
        if ('create_contact_parameters' not in params) or (params['create_contact_parameters'] is None):
            raise ValueError("Missing the required parameter `create_contact_parameters` when calling `create_contact`")

        resource_path = '/contact'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_contact_parameters' in params:
            body_params = params['create_contact_parameters']

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

    def delete_contact_by_id(self, contact_id, **kwargs):
        """
        Delete Contact
        Delete a contact from your contact list. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/contact/$CONTACT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_contact_by_id(contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str contact_id: ContactId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_contact_by_id_with_http_info(contact_id, **kwargs)
        else:
            (data) = self.delete_contact_by_id_with_http_info(contact_id, **kwargs)
            return data

    def delete_contact_by_id_with_http_info(self, contact_id, **kwargs):
        """
        Delete Contact
        Delete a contact from your contact list. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/contact/$CONTACT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_contact_by_id_with_http_info(contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str contact_id: ContactId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_contact_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params) or (params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `delete_contact_by_id`")

        resource_path = '/contact/{ContactId}'.replace('{format}', 'json')
        path_params = {}
        if 'contact_id' in params:
            path_params['ContactId'] = params['contact_id']

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

    def get_contact_by_id(self, contact_id, **kwargs):
        """
        Get Contact
        Retrieve a contact to your contact list. <br><br> Returns a contact object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/contact/$CONTACT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contact_by_id(contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str contact_id: ContactId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_contact_by_id_with_http_info(contact_id, **kwargs)
        else:
            (data) = self.get_contact_by_id_with_http_info(contact_id, **kwargs)
            return data

    def get_contact_by_id_with_http_info(self, contact_id, **kwargs):
        """
        Get Contact
        Retrieve a contact to your contact list. <br><br> Returns a contact object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/contact/$CONTACT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contact_by_id_with_http_info(contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str contact_id: ContactId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contact_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params) or (params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `get_contact_by_id`")

        resource_path = '/contact/{ContactId}'.replace('{format}', 'json')
        path_params = {}
        if 'contact_id' in params:
            path_params['ContactId'] = params['contact_id']

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

    def get_contacts(self, **kwargs):
        """
        List Contacts
        Retrieve a list of contacts. <br><br> Returns a list of contact objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/contacts ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contacts(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str range: Range (ie \"records=201-300\") of contacts requested
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_contacts_with_http_info(**kwargs)
        else:
            (data) = self.get_contacts_with_http_info(**kwargs)
            return data

    def get_contacts_with_http_info(self, **kwargs):
        """
        List Contacts
        Retrieve a list of contacts. <br><br> Returns a list of contact objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/contacts ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contacts_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str range: Range (ie \"records=201-300\") of contacts requested
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
                    " to method get_contacts" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/contacts'.replace('{format}', 'json')
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

    def get_contacts_by_group_id(self, group_id, **kwargs):
        """
        List Contacts in Group
        Retrieve a list of contacts in a contact group. <br><br> Returns a list of contact objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/contacts/$GROUP_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contacts_by_group_id(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: GroupId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_contacts_by_group_id_with_http_info(group_id, **kwargs)
        else:
            (data) = self.get_contacts_by_group_id_with_http_info(group_id, **kwargs)
            return data

    def get_contacts_by_group_id_with_http_info(self, group_id, **kwargs):
        """
        List Contacts in Group
        Retrieve a list of contacts in a contact group. <br><br> Returns a list of contact objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/contacts/$GROUP_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contacts_by_group_id_with_http_info(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str group_id: GroupId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contacts_by_group_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_contacts_by_group_id`")

        resource_path = '/contacts/{GroupId}'.replace('{format}', 'json')
        path_params = {}
        if 'group_id' in params:
            path_params['GroupId'] = params['group_id']

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

    def update_contact_by_id(self, update_contact_by_id_parameters, contact_id, **kwargs):
        """
        Update Contact
        Update an existing contact in your contact list. <br><br> Returns a contact object if a valid identifier was provided and input validation passed, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X PUT -d \"{\\\"phone\\\": \\\"5555555555\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/contact/$CONTACT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_contact_by_id(update_contact_by_id_parameters, contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateContactByIdParameters update_contact_by_id_parameters: Request body (required)
        :param str contact_id: ContactId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_contact_by_id_with_http_info(update_contact_by_id_parameters, contact_id, **kwargs)
        else:
            (data) = self.update_contact_by_id_with_http_info(update_contact_by_id_parameters, contact_id, **kwargs)
            return data

    def update_contact_by_id_with_http_info(self, update_contact_by_id_parameters, contact_id, **kwargs):
        """
        Update Contact
        Update an existing contact in your contact list. <br><br> Returns a contact object if a valid identifier was provided and input validation passed, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X PUT -d \"{\\\"phone\\\": \\\"5555555555\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/contact/$CONTACT_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_contact_by_id_with_http_info(update_contact_by_id_parameters, contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateContactByIdParameters update_contact_by_id_parameters: Request body (required)
        :param str contact_id: ContactId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['update_contact_by_id_parameters', 'contact_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_contact_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'update_contact_by_id_parameters' is set
        if ('update_contact_by_id_parameters' not in params) or (params['update_contact_by_id_parameters'] is None):
            raise ValueError("Missing the required parameter `update_contact_by_id_parameters` when calling `update_contact_by_id`")
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params) or (params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `update_contact_by_id`")

        resource_path = '/contact/{ContactId}'.replace('{format}', 'json')
        path_params = {}
        if 'contact_id' in params:
            path_params['ContactId'] = params['contact_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_contact_by_id_parameters' in params:
            body_params = params['update_contact_by_id_parameters']

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