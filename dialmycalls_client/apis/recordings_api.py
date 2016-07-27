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


class RecordingsApi(object):
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

    def create_recording(self, create_recording_parameters, **kwargs):
        """
        Create Recording (Text-to-Speech)
        Create a new recording using text-to-speech. <br><br> Returns a recording object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"name\\\": \\\"Test Recording\\\", \\\"gender\\\": \\\"M\\\", \\\"language\\\": \\\"en\\\", \\\"text\\\": \\\"This is just a test.\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/recording/tts ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_recording(create_recording_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRecordingParameters create_recording_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_recording_with_http_info(create_recording_parameters, **kwargs)
        else:
            (data) = self.create_recording_with_http_info(create_recording_parameters, **kwargs)
            return data

    def create_recording_with_http_info(self, create_recording_parameters, **kwargs):
        """
        Create Recording (Text-to-Speech)
        Create a new recording using text-to-speech. <br><br> Returns a recording object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"name\\\": \\\"Test Recording\\\", \\\"gender\\\": \\\"M\\\", \\\"language\\\": \\\"en\\\", \\\"text\\\": \\\"This is just a test.\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/recording/tts ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_recording_with_http_info(create_recording_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRecordingParameters create_recording_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_recording_parameters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_recording" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_recording_parameters' is set
        if ('create_recording_parameters' not in params) or (params['create_recording_parameters'] is None):
            raise ValueError("Missing the required parameter `create_recording_parameters` when calling `create_recording`")

        resource_path = '/recording/tts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_recording_parameters' in params:
            body_params = params['create_recording_parameters']

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

    def create_recording_by_phone(self, create_recording_by_phone_parameters, **kwargs):
        """
        Create Recording (Phone)
        Create a new recording by phone. <br><br> Returns a recording object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"name\\\": \\\"Test Recording\\\", \\\"phone\\\": \\\"5551234567\\\", \\\"callerid_id\\\": \\\"$CALLERID_ID\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/recording/phone ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_recording_by_phone(create_recording_by_phone_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRecordingByPhoneParameters create_recording_by_phone_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_recording_by_phone_with_http_info(create_recording_by_phone_parameters, **kwargs)
        else:
            (data) = self.create_recording_by_phone_with_http_info(create_recording_by_phone_parameters, **kwargs)
            return data

    def create_recording_by_phone_with_http_info(self, create_recording_by_phone_parameters, **kwargs):
        """
        Create Recording (Phone)
        Create a new recording by phone. <br><br> Returns a recording object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"name\\\": \\\"Test Recording\\\", \\\"phone\\\": \\\"5551234567\\\", \\\"callerid_id\\\": \\\"$CALLERID_ID\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/recording/phone ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_recording_by_phone_with_http_info(create_recording_by_phone_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRecordingByPhoneParameters create_recording_by_phone_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_recording_by_phone_parameters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_recording_by_phone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_recording_by_phone_parameters' is set
        if ('create_recording_by_phone_parameters' not in params) or (params['create_recording_by_phone_parameters'] is None):
            raise ValueError("Missing the required parameter `create_recording_by_phone_parameters` when calling `create_recording_by_phone`")

        resource_path = '/recording/phone'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_recording_by_phone_parameters' in params:
            body_params = params['create_recording_by_phone_parameters']

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

    def create_recording_by_url(self, create_recording_by_url_parameters, **kwargs):
        """
        Create Recording (URL)
        Create a new recording from a URL. <br><br> Returns a recording object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"name\\\": \\\"Test Recording\\\", \\\"url\\\": \\\"https://ia700200.us.archive.org/1/items/testmp3testfile/mpthreetest.mp3\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/recording/url ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_recording_by_url(create_recording_by_url_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRecordingByUrlParameters create_recording_by_url_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_recording_by_url_with_http_info(create_recording_by_url_parameters, **kwargs)
        else:
            (data) = self.create_recording_by_url_with_http_info(create_recording_by_url_parameters, **kwargs)
            return data

    def create_recording_by_url_with_http_info(self, create_recording_by_url_parameters, **kwargs):
        """
        Create Recording (URL)
        Create a new recording from a URL. <br><br> Returns a recording object on success, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X POST -d \"{\\\"name\\\": \\\"Test Recording\\\", \\\"url\\\": \\\"https://ia700200.us.archive.org/1/items/testmp3testfile/mpthreetest.mp3\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/recording/url ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_recording_by_url_with_http_info(create_recording_by_url_parameters, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateRecordingByUrlParameters create_recording_by_url_parameters: Request body (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_recording_by_url_parameters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_recording_by_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_recording_by_url_parameters' is set
        if ('create_recording_by_url_parameters' not in params) or (params['create_recording_by_url_parameters'] is None):
            raise ValueError("Missing the required parameter `create_recording_by_url_parameters` when calling `create_recording_by_url`")

        resource_path = '/recording/url'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_recording_by_url_parameters' in params:
            body_params = params['create_recording_by_url_parameters']

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

    def delete_recording_by_id(self, recording_id, **kwargs):
        """
        Delete Recording
        Delete a recording. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/recording/$RECORDING_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_recording_by_id(recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recording_id: RecordingId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_recording_by_id_with_http_info(recording_id, **kwargs)
        else:
            (data) = self.delete_recording_by_id_with_http_info(recording_id, **kwargs)
            return data

    def delete_recording_by_id_with_http_info(self, recording_id, **kwargs):
        """
        Delete Recording
        Delete a recording. <br><br> Returns the following if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X DELETE https://$API_KEY@api.dialmycalls.com/2.0/recording/$RECORDING_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_recording_by_id_with_http_info(recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recording_id: RecordingId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recording_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_recording_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'recording_id' is set
        if ('recording_id' not in params) or (params['recording_id'] is None):
            raise ValueError("Missing the required parameter `recording_id` when calling `delete_recording_by_id`")

        resource_path = '/recording/{RecordingId}'.replace('{format}', 'json')
        path_params = {}
        if 'recording_id' in params:
            path_params['RecordingId'] = params['recording_id']

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

    def get_recording_by_id(self, recording_id, **kwargs):
        """
        Get Recording
        Retrieve a recording. <br><br> Returns a recording object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/recording/$RECORDING_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_recording_by_id(recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recording_id: RecordingId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_recording_by_id_with_http_info(recording_id, **kwargs)
        else:
            (data) = self.get_recording_by_id_with_http_info(recording_id, **kwargs)
            return data

    def get_recording_by_id_with_http_info(self, recording_id, **kwargs):
        """
        Get Recording
        Retrieve a recording. <br><br> Returns a recording object if a valid identifier was provided, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/recording/$RECORDING_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_recording_by_id_with_http_info(recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str recording_id: RecordingId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['recording_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recording_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'recording_id' is set
        if ('recording_id' not in params) or (params['recording_id'] is None):
            raise ValueError("Missing the required parameter `recording_id` when calling `get_recording_by_id`")

        resource_path = '/recording/{RecordingId}'.replace('{format}', 'json')
        path_params = {}
        if 'recording_id' in params:
            path_params['RecordingId'] = params['recording_id']

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

    def get_recordings(self, **kwargs):
        """
        List Recordings
        Retrieve a list of recordings. <br><br> Returns a list of recording objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/recordings ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_recordings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str range: Range (ie \"records=201-300\") of recordings requested
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_recordings_with_http_info(**kwargs)
        else:
            (data) = self.get_recordings_with_http_info(**kwargs)
            return data

    def get_recordings_with_http_info(self, **kwargs):
        """
        List Recordings
        Retrieve a list of recordings. <br><br> Returns a list of recording objects. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X GET https://$API_KEY@api.dialmycalls.com/2.0/recordings ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_recordings_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str range: Range (ie \"records=201-300\") of recordings requested
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
                    " to method get_recordings" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/recordings'.replace('{format}', 'json')
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

    def update_recording_by_id(self, update_recording_by_id_parameters, recording_id, **kwargs):
        """
        Update Recording
        Update an existing recording. <br><br> Returns a recording object if a valid identifier was provided and input validation passed, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X PUT -d \"{\\\"name\\\": \\\"Test Recording Updated\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/recording/$RECORDING_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_recording_by_id(update_recording_by_id_parameters, recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateRecordingByIdParameters update_recording_by_id_parameters: Request body (required)
        :param str recording_id: RecordingId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_recording_by_id_with_http_info(update_recording_by_id_parameters, recording_id, **kwargs)
        else:
            (data) = self.update_recording_by_id_with_http_info(update_recording_by_id_parameters, recording_id, **kwargs)
            return data

    def update_recording_by_id_with_http_info(self, update_recording_by_id_parameters, recording_id, **kwargs):
        """
        Update Recording
        Update an existing recording. <br><br> Returns a recording object if a valid identifier was provided and input validation passed, and returns an error otherwise. <br><br> ``` curl -i -H \"Content-Type: application/json\" -X PUT -d \"{\\\"name\\\": \\\"Test Recording Updated\\\"}\" https://$API_KEY@api.dialmycalls.com/2.0/recording/$RECORDING_ID ```

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_recording_by_id_with_http_info(update_recording_by_id_parameters, recording_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UpdateRecordingByIdParameters update_recording_by_id_parameters: Request body (required)
        :param str recording_id: RecordingId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['update_recording_by_id_parameters', 'recording_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_recording_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'update_recording_by_id_parameters' is set
        if ('update_recording_by_id_parameters' not in params) or (params['update_recording_by_id_parameters'] is None):
            raise ValueError("Missing the required parameter `update_recording_by_id_parameters` when calling `update_recording_by_id`")
        # verify the required parameter 'recording_id' is set
        if ('recording_id' not in params) or (params['recording_id'] is None):
            raise ValueError("Missing the required parameter `recording_id` when calling `update_recording_by_id`")

        resource_path = '/recording/{RecordingId}'.replace('{format}', 'json')
        path_params = {}
        if 'recording_id' in params:
            path_params['RecordingId'] = params['recording_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_recording_by_id_parameters' in params:
            body_params = params['update_recording_by_id_parameters']

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