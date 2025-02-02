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

class Dicrim(object):
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
        'annee_publication': 'str',
        'code_insee': 'str',
        'libelle_commune': 'str'
    }

    attribute_map = {
        'annee_publication': 'annee_publication',
        'code_insee': 'code_insee',
        'libelle_commune': 'libelle_commune'
    }

    def __init__(self, annee_publication=None, code_insee=None, libelle_commune=None):  # noqa: E501
        """Dicrim - a model defined in Swagger"""  # noqa: E501
        self._annee_publication = None
        self._code_insee = None
        self._libelle_commune = None
        self.discriminator = None
        if annee_publication is not None:
            self.annee_publication = annee_publication
        if code_insee is not None:
            self.code_insee = code_insee
        if libelle_commune is not None:
            self.libelle_commune = libelle_commune

    @property
    def annee_publication(self):
        """Gets the annee_publication of this Dicrim.  # noqa: E501

        Date de publication  # noqa: E501

        :return: The annee_publication of this Dicrim.  # noqa: E501
        :rtype: str
        """
        return self._annee_publication

    @annee_publication.setter
    def annee_publication(self, annee_publication):
        """Sets the annee_publication of this Dicrim.

        Date de publication  # noqa: E501

        :param annee_publication: The annee_publication of this Dicrim.  # noqa: E501
        :type: str
        """

        self._annee_publication = annee_publication

    @property
    def code_insee(self):
        """Gets the code_insee of this Dicrim.  # noqa: E501

        Identifiant unique INSEE de la commune  # noqa: E501

        :return: The code_insee of this Dicrim.  # noqa: E501
        :rtype: str
        """
        return self._code_insee

    @code_insee.setter
    def code_insee(self, code_insee):
        """Sets the code_insee of this Dicrim.

        Identifiant unique INSEE de la commune  # noqa: E501

        :param code_insee: The code_insee of this Dicrim.  # noqa: E501
        :type: str
        """

        self._code_insee = code_insee

    @property
    def libelle_commune(self):
        """Gets the libelle_commune of this Dicrim.  # noqa: E501

        Libellé de la commune  # noqa: E501

        :return: The libelle_commune of this Dicrim.  # noqa: E501
        :rtype: str
        """
        return self._libelle_commune

    @libelle_commune.setter
    def libelle_commune(self, libelle_commune):
        """Sets the libelle_commune of this Dicrim.

        Libellé de la commune  # noqa: E501

        :param libelle_commune: The libelle_commune of this Dicrim.  # noqa: E501
        :type: str
        """

        self._libelle_commune = libelle_commune

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
        if issubclass(Dicrim, dict):
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
        if not isinstance(other, Dicrim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
