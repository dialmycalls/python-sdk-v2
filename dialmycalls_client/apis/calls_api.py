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


class CallsApi(object):
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

    def cancel_call_by_id(self, call_id, **kwargs):
        """
        Cancel Call
        Cancel an outgoing call. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/service/call/$CALL_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_call_by_id(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id: CallId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancel_call_by_id_with_http_info(call_id, **kwargs)
        else:
            (data) = self.cancel_call_by_id_with_http_info(call_id, **kwargs)
            return data

    def cancel_call_by_id_with_http_info(self, call_id, **kwargs):
        """
        Cancel Call
        Cancel an outgoing call. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/service/call/$CALL_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_call_by_id_with_http_info(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id: CallId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_call_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `cancel_call_by_id`")

        resource_path = '/service/call/{CallId}'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['CallId'] = params['call_id']

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

    def create_call(self, create_call_parameters, **kwargs):
        """
        Create Call
        Create an outgoing call broadcast. <br><br> Returns a call service object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"name\\\": \\\"Test\\\", \\\"callerid_id\\\": \\\"8bc6748e-d8a0-11e4-8b2d-00163e603cea\\\", \\\"recording_id\\\": \\\"079ff28a-1b75-11e5-88eb-00163e603cea\\\", \\\"send_immediately\\\": true, \\\"use_amd\\\": true, \\\"contacts\\\": [{\\\"phone\\\":\\\"1116551235\\\"},{\\\"phone\\\":\\\"1116551234\\\"}]}\" https://$API_KEY@api.dialmycalls.com/2.0/service/call ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_call(create_call_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateCallParameters create_call_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_call_with_http_info(create_call_parameters, **kwargs)
        else:
            (data) = self.create_call_with_http_info(create_call_parameters, **kwargs)
            return data

    def create_call_with_http_info(self, create_call_parameters, **kwargs):
        """
        Create Call
        Create an outgoing call broadcast. <br><br> Returns a call service object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"name\\\": \\\"Test\\\", \\\"callerid_id\\\": \\\"8bc6748e-d8a0-11e4-8b2d-00163e603cea\\\", \\\"recording_id\\\": \\\"079ff28a-1b75-11e5-88eb-00163e603cea\\\", \\\"send_immediately\\\": true, \\\"use_amd\\\": true, \\\"contacts\\\": [{\\\"phone\\\":\\\"1116551235\\\"},{\\\"phone\\\":\\\"1116551234\\\"}]}\" https://$API_KEY@api.dialmycalls.com/2.0/service/call ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_call_with_http_info(create_call_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateCallParameters create_call_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_call_parameters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_call" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_call_parameters' is set
        if ('create_call_parameters' not in params) or (params['create_call_parameters'] is None):
            raise ValueError("Missing the required parameter `create_call_parameters` when calling `create_call`")

        resource_path = '/service/call'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_call_parameters' in params:
            body_params = params['create_call_parameters']

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

    def get_call_by_id(self, call_id, **kwargs):
        """
        Get Call
        Retrieve a call. <br><br> Returns a call service object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/service/call/$CALL_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_call_by_id(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id: CallId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_call_by_id_with_http_info(call_id, **kwargs)
        else:
            (data) = self.get_call_by_id_with_http_info(call_id, **kwargs)
            return data

    def get_call_by_id_with_http_info(self, call_id, **kwargs):
        """
        Get Call
        Retrieve a call. <br><br> Returns a call service object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/service/call/$CALL_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_call_by_id_with_http_info(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id: CallId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_call_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `get_call_by_id`")

        resource_path = '/service/call/{CallId}'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['CallId'] = params['call_id']

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

    def get_call_recipients_by_call_id(self, call_id, **kwargs):
        """
        Get Call Recipients
        Retrieve a list of a call's recipients. <br><br> Returns a list of call recipient objects if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/service/call/$CALL_ID/recipients ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_call_recipients_by_call_id(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id: CallId (required)
        :param str range: Range (ie \"records=201-300\") of recipients requested
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_call_recipients_by_call_id_with_http_info(call_id, **kwargs)
        else:
            (data) = self.get_call_recipients_by_call_id_with_http_info(call_id, **kwargs)
            return data

    def get_call_recipients_by_call_id_with_http_info(self, call_id, **kwargs):
        """
        Get Call Recipients
        Retrieve a list of a call's recipients. <br><br> Returns a list of call recipient objects if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/service/call/$CALL_ID/recipients ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_call_recipients_by_call_id_with_http_info(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id: CallId (required)
        :param str range: Range (ie \"records=201-300\") of recipients requested
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id', 'range']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_call_recipients_by_call_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `get_call_recipients_by_call_id`")

        resource_path = '/service/call/{CallId}/recipients'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['CallId'] = params['call_id']

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

    def get_calls(self, **kwargs):
        """
        List Calls
        Retrieve a list of calls. <br><br> Returns a list of call service objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/service/calls ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_calls(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str range: Range (ie \"records=201-300\") of calls requested
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_calls_with_http_info(**kwargs)
        else:
            (data) = self.get_calls_with_http_info(**kwargs)
            return data

    def get_calls_with_http_info(self, **kwargs):
        """
        List Calls
        Retrieve a list of calls. <br><br> Returns a list of call service objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/service/calls ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_calls_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str range: Range (ie \"records=201-300\") of calls requested
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
                    " to method get_calls" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/service/calls'.replace('{format}', 'json')
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
