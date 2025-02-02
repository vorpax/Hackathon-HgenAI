# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import GeorisqueApi
from GeorisqueApi.api.etats_documents_ppr_api import EtatsDocumentsPPRApi  # noqa: E501
from GeorisqueApi.rest import ApiException


class TestEtatsDocumentsPPRApi(unittest.TestCase):
    """EtatsDocumentsPPRApi unit test stubs"""

    def setUp(self):
        self.api = EtatsDocumentsPPRApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_recherche_etat_docs(self):
        """Test case for recherche_etat_docs

        Lister les différents états d'un document PPR  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
