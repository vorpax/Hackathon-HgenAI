# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MetadataFichier(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identifiant_fichier': 'str',
        'nom_fichier': 'str',
        'type_fichier': 'str',
        'date_fichier': 'datetime',
        'url_fichier': 'str'
    }

    attribute_map = {
        'identifiant_fichier': 'identifiantFichier',
        'nom_fichier': 'nomFichier',
        'type_fichier': 'typeFichier',
        'date_fichier': 'dateFichier',
        'url_fichier': 'urlFichier'
    }

    def __init__(self, identifiant_fichier=None, nom_fichier=None, type_fichier=None, date_fichier=None, url_fichier=None):  # noqa: E501
        """MetadataFichier - a model defined in Swagger"""  # noqa: E501
        self._identifiant_fichier = None
        self._nom_fichier = None
        self._type_fichier = None
        self._date_fichier = None
        self._url_fichier = None
        self.discriminator = None
        if identifiant_fichier is not None:
            self.identifiant_fichier = identifiant_fichier
        if nom_fichier is not None:
            self.nom_fichier = nom_fichier
        if type_fichier is not None:
            self.type_fichier = type_fichier
        if date_fichier is not None:
            self.date_fichier = date_fichier
        if url_fichier is not None:
            self.url_fichier = url_fichier

    @property
    def identifiant_fichier(self):
        """Gets the identifiant_fichier of this MetadataFichier.  # noqa: E501

        Identifiant technique du fichier  # noqa: E501

        :return: The identifiant_fichier of this MetadataFichier.  # noqa: E501
        :rtype: str
        """
        return self._identifiant_fichier

    @identifiant_fichier.setter
    def identifiant_fichier(self, identifiant_fichier):
        """Sets the identifiant_fichier of this MetadataFichier.

        Identifiant technique du fichier  # noqa: E501

        :param identifiant_fichier: The identifiant_fichier of this MetadataFichier.  # noqa: E501
        :type: str
        """

        self._identifiant_fichier = identifiant_fichier

    @property
    def nom_fichier(self):
        """Gets the nom_fichier of this MetadataFichier.  # noqa: E501

        Nom du fichier  # noqa: E501

        :return: The nom_fichier of this MetadataFichier.  # noqa: E501
        :rtype: str
        """
        return self._nom_fichier

    @nom_fichier.setter
    def nom_fichier(self, nom_fichier):
        """Sets the nom_fichier of this MetadataFichier.

        Nom du fichier  # noqa: E501

        :param nom_fichier: The nom_fichier of this MetadataFichier.  # noqa: E501
        :type: str
        """

        self._nom_fichier = nom_fichier

    @property
    def type_fichier(self):
        """Gets the type_fichier of this MetadataFichier.  # noqa: E501

        Libelle du type de fichier  # noqa: E501

        :return: The type_fichier of this MetadataFichier.  # noqa: E501
        :rtype: str
        """
        return self._type_fichier

    @type_fichier.setter
    def type_fichier(self, type_fichier):
        """Sets the type_fichier of this MetadataFichier.

        Libelle du type de fichier  # noqa: E501

        :param type_fichier: The type_fichier of this MetadataFichier.  # noqa: E501
        :type: str
        """

        self._type_fichier = type_fichier

    @property
    def date_fichier(self):
        """Gets the date_fichier of this MetadataFichier.  # noqa: E501

        Date du depot du fichier dans GUNenv  # noqa: E501

        :return: The date_fichier of this MetadataFichier.  # noqa: E501
        :rtype: datetime
        """
        return self._date_fichier

    @date_fichier.setter
    def date_fichier(self, date_fichier):
        """Sets the date_fichier of this MetadataFichier.

        Date du depot du fichier dans GUNenv  # noqa: E501

        :param date_fichier: The date_fichier of this MetadataFichier.  # noqa: E501
        :type: datetime
        """

        self._date_fichier = date_fichier

    @property
    def url_fichier(self):
        """Gets the url_fichier of this MetadataFichier.  # noqa: E501

        URL du fichier tel que diffuse dans Georisques  # noqa: E501

        :return: The url_fichier of this MetadataFichier.  # noqa: E501
        :rtype: str
        """
        return self._url_fichier

    @url_fichier.setter
    def url_fichier(self, url_fichier):
        """Sets the url_fichier of this MetadataFichier.

        URL du fichier tel que diffuse dans Georisques  # noqa: E501

        :param url_fichier: The url_fichier of this MetadataFichier.  # noqa: E501
        :type: str
        """

        self._url_fichier = url_fichier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MetadataFichier, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetadataFichier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
