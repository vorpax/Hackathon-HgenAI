# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from GeorisqueApi.api_client import ApiClient


class FamillesRisquePPRApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def recherche_risque(self, **kwargs):  # noqa: E501
        """Lister les familles de risques  # noqa: E501

        Lexique des familles de risques de la base de données GASPAR (codification issue du standard PPRN / PPRT de la Commission de validation des données pour l'information spatialisée (COVADIS))  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recherche_risque(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PaginatedResponseFamilleRisques
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.recherche_risque_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.recherche_risque_with_http_info(**kwargs)  # noqa: E501
            return data

    def recherche_risque_with_http_info(self, **kwargs):  # noqa: E501
        """Lister les familles de risques  # noqa: E501

        Lexique des familles de risques de la base de données GASPAR (codification issue du standard PPRN / PPRT de la Commission de validation des données pour l'information spatialisée (COVADIS))  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recherche_risque_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PaginatedResponseFamilleRisques
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method recherche_risque" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/ppr/famille_risques', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedResponseFamilleRisques',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
