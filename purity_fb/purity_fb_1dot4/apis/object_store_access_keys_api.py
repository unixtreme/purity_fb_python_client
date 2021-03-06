# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.4
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


class ObjectStoreAccessKeysApi(object):
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

    def create_object_store_access_keys(self, **kwargs):
        """
        Create a new object store access key
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_object_store_access_keys(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Objectstoreaccesskey object_store_access_key: The attribute map used to create the object store access key
        :return: ObjectStoreAccessKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_object_store_access_keys_with_http_info(**kwargs)
        else:
            (data) = self.create_object_store_access_keys_with_http_info(**kwargs)
            return data

    def create_object_store_access_keys_with_http_info(self, **kwargs):
        """
        Create a new object store access key
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_object_store_access_keys_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Objectstoreaccesskey object_store_access_key: The attribute map used to create the object store access key
        :return: ObjectStoreAccessKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['object_store_access_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_object_store_access_keys" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'object_store_access_key' in params:
            body_params = params['object_store_access_key']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.4/object-store-access-keys', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ObjectStoreAccessKeyResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_object_store_access_keys(self, **kwargs):
        """
        Delete an object store access key by name
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_object_store_access_keys(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_object_store_access_keys_with_http_info(**kwargs)
        else:
            (data) = self.delete_object_store_access_keys_with_http_info(**kwargs)
            return data

    def delete_object_store_access_keys_with_http_info(self, **kwargs):
        """
        Delete an object store access key by name
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_object_store_access_keys_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_object_store_access_keys" % key
                )
            params[key] = val
        del params['kwargs']


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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.4/object-store-access-keys', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_object_store_access_keys(self, **kwargs):
        """
        List object store access keys
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_object_store_access_keys(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param str filter: The filter to be used for query.
        :param str sort: The way to order the results.
        :param int start: start
        :param int limit: limit, should be >= 0
        :param str token: token
        :return: ObjectStoreAccessKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_object_store_access_keys_with_http_info(**kwargs)
        else:
            (data) = self.list_object_store_access_keys_with_http_info(**kwargs)
            return data

    def list_object_store_access_keys_with_http_info(self, **kwargs):
        """
        List object store access keys
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_object_store_access_keys_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param str filter: The filter to be used for query.
        :param str sort: The way to order the results.
        :param int start: start
        :param int limit: limit, should be >= 0
        :param str token: token
        :return: ObjectStoreAccessKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names', 'filter', 'sort', 'start', 'limit', 'token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_object_store_access_keys" % key
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
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
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

        return self.api_client.call_api('/1.4/object-store-access-keys', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ObjectStoreAccessKeyResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_object_store_access_keys(self, **kwargs):
        """
        Update an existing object store access key
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_object_store_access_keys(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param ObjectStoreAccessKey object_store_access_key: the attribute map used to update the object store access key
        :return: ObjectStoreAccessKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_object_store_access_keys_with_http_info(**kwargs)
        else:
            (data) = self.update_object_store_access_keys_with_http_info(**kwargs)
            return data

    def update_object_store_access_keys_with_http_info(self, **kwargs):
        """
        Update an existing object store access key
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_object_store_access_keys_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] names: A list of names.
        :param ObjectStoreAccessKey object_store_access_key: the attribute map used to update the object store access key
        :return: ObjectStoreAccessKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names', 'object_store_access_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_object_store_access_keys" % key
                )
            params[key] = val
        del params['kwargs']


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
        if 'object_store_access_key' in params:
            body_params = params['object_store_access_key']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api('/1.4/object-store-access-keys', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ObjectStoreAccessKeyResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
