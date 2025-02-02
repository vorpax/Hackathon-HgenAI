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

class RisqueGaspar(object):
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
        'num_risque': 'str',
        'libelle_risque_long': 'str'
    }

    attribute_map = {
        'num_risque': 'num_risque',
        'libelle_risque_long': 'libelle_risque_long'
    }

    def __init__(self, num_risque=None, libelle_risque_long=None):  # noqa: E501
        """RisqueGaspar - a model defined in Swagger"""  # noqa: E501
        self._num_risque = None
        self._libelle_risque_long = None
        self.discriminator = None
        if num_risque is not None:
            self.num_risque = num_risque
        if libelle_risque_long is not None:
            self.libelle_risque_long = libelle_risque_long

    @property
    def num_risque(self):
        """Gets the num_risque of this RisqueGaspar.  # noqa: E501

        Identifiant technique du risque  # noqa: E501

        :return: The num_risque of this RisqueGaspar.  # noqa: E501
        :rtype: str
        """
        return self._num_risque

    @num_risque.setter
    def num_risque(self, num_risque):
        """Sets the num_risque of this RisqueGaspar.

        Identifiant technique du risque  # noqa: E501

        :param num_risque: The num_risque of this RisqueGaspar.  # noqa: E501
        :type: str
        """

        self._num_risque = num_risque

    @property
    def libelle_risque_long(self):
        """Gets the libelle_risque_long of this RisqueGaspar.  # noqa: E501

        Libellé long du risque  # noqa: E501

        :return: The libelle_risque_long of this RisqueGaspar.  # noqa: E501
        :rtype: str
        """
        return self._libelle_risque_long

    @libelle_risque_long.setter
    def libelle_risque_long(self, libelle_risque_long):
        """Sets the libelle_risque_long of this RisqueGaspar.

        Libellé long du risque  # noqa: E501

        :param libelle_risque_long: The libelle_risque_long of this RisqueGaspar.  # noqa: E501
        :type: str
        """

        self._libelle_risque_long = libelle_risque_long

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
        if issubclass(RisqueGaspar, dict):
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
        if not isinstance(other, RisqueGaspar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
