# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.6), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.6
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class HardwareApi(object):
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

    def list_hardware(self, **kwargs):
        """
        List hardware components
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_hardware(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param str filter: The filter to be used for query.
        :param int limit: limit, should be >= 0
        :param str sort: The way to order the results.
        :param int start: start
        :param str token: token
        :return: HardwareResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_hardware_with_http_info(**kwargs)
        else:
            (data) = self.list_hardware_with_http_info(**kwargs)
            return data

    def list_hardware_with_http_info(self, **kwargs):
        """
        List hardware components
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_hardware_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param str filter: The filter to be used for query.
        :param int limit: limit, should be >= 0
        :param str sort: The way to order the results.
        :param int start: start
        :param str token: token
        :return: HardwareResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names', 'filter', 'limit', 'sort', 'start', 'token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_hardware" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'token' in params:
            query_params.append(('token', params['token']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.6/hardware', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='HardwareResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_hardware(self, names, hardware, **kwargs):
        """
        Update an existing hardware component
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_hardware(names, hardware, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: (required)
        :param Hardware hardware: (required)
        :return: HardwareResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_hardware_with_http_info(names, hardware, **kwargs)
        else:
            (data) = self.update_hardware_with_http_info(names, hardware, **kwargs)
            return data

    def update_hardware_with_http_info(self, names, hardware, **kwargs):
        """
        Update an existing hardware component
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_hardware_with_http_info(names, hardware, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: (required)
        :param Hardware hardware: (required)
        :return: HardwareResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names', 'hardware']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_hardware" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'names' is set
        if ('names' not in params) or (params['names'] is None):
            raise ValueError("Missing the required parameter `names` when calling `update_hardware`")
        # verify the required parameter 'hardware' is set
        if ('hardware' not in params) or (params['hardware'] is None):
            raise ValueError("Missing the required parameter `hardware` when calling `update_hardware`")

        if 'names' in params and len(params['names']) > 1:
            raise ValueError("Invalid value for parameter `names` when calling `update_hardware`, number of items must be less than or equal to `1`")
        if 'names' in params and len(params['names']) < 1:
            raise ValueError("Invalid value for parameter `names` when calling `update_hardware`, number of items must be greater than or equal to `1`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardware' in params:
            body_params = params['hardware']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.6/hardware', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='HardwareResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)