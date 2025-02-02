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

class RubriqueIC(object):
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
        'numero_rubrique': 'str',
        'nature': 'str',
        'alinea': 'str',
        'regime_autorise_alinea': 'str',
        'quantite_totale': 'str',
        'unite': 'str'
    }

    attribute_map = {
        'numero_rubrique': 'numeroRubrique',
        'nature': 'nature',
        'alinea': 'alinea',
        'regime_autorise_alinea': 'regimeAutoriseAlinea',
        'quantite_totale': 'quantiteTotale',
        'unite': 'unite'
    }

    def __init__(self, numero_rubrique=None, nature=None, alinea=None, regime_autorise_alinea=None, quantite_totale=None, unite=None):  # noqa: E501
        """RubriqueIC - a model defined in Swagger"""  # noqa: E501
        self._numero_rubrique = None
        self._nature = None
        self._alinea = None
        self._regime_autorise_alinea = None
        self._quantite_totale = None
        self._unite = None
        self.discriminator = None
        if numero_rubrique is not None:
            self.numero_rubrique = numero_rubrique
        if nature is not None:
            self.nature = nature
        if alinea is not None:
            self.alinea = alinea
        if regime_autorise_alinea is not None:
            self.regime_autorise_alinea = regime_autorise_alinea
        if quantite_totale is not None:
            self.quantite_totale = quantite_totale
        if unite is not None:
            self.unite = unite

    @property
    def numero_rubrique(self):
        """Gets the numero_rubrique of this RubriqueIC.  # noqa: E501

        Numero de la rubrique autorisee  # noqa: E501

        :return: The numero_rubrique of this RubriqueIC.  # noqa: E501
        :rtype: str
        """
        return self._numero_rubrique

    @numero_rubrique.setter
    def numero_rubrique(self, numero_rubrique):
        """Sets the numero_rubrique of this RubriqueIC.

        Numero de la rubrique autorisee  # noqa: E501

        :param numero_rubrique: The numero_rubrique of this RubriqueIC.  # noqa: E501
        :type: str
        """

        self._numero_rubrique = numero_rubrique

    @property
    def nature(self):
        """Gets the nature of this RubriqueIC.  # noqa: E501

        Nature de la rubrique proposee  # noqa: E501

        :return: The nature of this RubriqueIC.  # noqa: E501
        :rtype: str
        """
        return self._nature

    @nature.setter
    def nature(self, nature):
        """Sets the nature of this RubriqueIC.

        Nature de la rubrique proposee  # noqa: E501

        :param nature: The nature of this RubriqueIC.  # noqa: E501
        :type: str
        """

        self._nature = nature

    @property
    def alinea(self):
        """Gets the alinea of this RubriqueIC.  # noqa: E501

        Alinea de la rubrique concernee  # noqa: E501

        :return: The alinea of this RubriqueIC.  # noqa: E501
        :rtype: str
        """
        return self._alinea

    @alinea.setter
    def alinea(self, alinea):
        """Sets the alinea of this RubriqueIC.

        Alinea de la rubrique concernee  # noqa: E501

        :param alinea: The alinea of this RubriqueIC.  # noqa: E501
        :type: str
        """

        self._alinea = alinea

    @property
    def regime_autorise_alinea(self):
        """Gets the regime_autorise_alinea of this RubriqueIC.  # noqa: E501

        Regime autorise de l'alinea  # noqa: E501

        :return: The regime_autorise_alinea of this RubriqueIC.  # noqa: E501
        :rtype: str
        """
        return self._regime_autorise_alinea

    @regime_autorise_alinea.setter
    def regime_autorise_alinea(self, regime_autorise_alinea):
        """Sets the regime_autorise_alinea of this RubriqueIC.

        Regime autorise de l'alinea  # noqa: E501

        :param regime_autorise_alinea: The regime_autorise_alinea of this RubriqueIC.  # noqa: E501
        :type: str
        """

        self._regime_autorise_alinea = regime_autorise_alinea

    @property
    def quantite_totale(self):
        """Gets the quantite_totale of this RubriqueIC.  # noqa: E501

        Quantite totale sur le site  # noqa: E501

        :return: The quantite_totale of this RubriqueIC.  # noqa: E501
        :rtype: str
        """
        return self._quantite_totale

    @quantite_totale.setter
    def quantite_totale(self, quantite_totale):
        """Sets the quantite_totale of this RubriqueIC.

        Quantite totale sur le site  # noqa: E501

        :param quantite_totale: The quantite_totale of this RubriqueIC.  # noqa: E501
        :type: str
        """

        self._quantite_totale = quantite_totale

    @property
    def unite(self):
        """Gets the unite of this RubriqueIC.  # noqa: E501

        Unite de cet alinea de la rubrique  # noqa: E501

        :return: The unite of this RubriqueIC.  # noqa: E501
        :rtype: str
        """
        return self._unite

    @unite.setter
    def unite(self, unite):
        """Sets the unite of this RubriqueIC.

        Unite de cet alinea de la rubrique  # noqa: E501

        :param unite: The unite of this RubriqueIC.  # noqa: E501
        :type: str
        """

        self._unite = unite

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
        if issubclass(RubriqueIC, dict):
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
        if not isinstance(other, RubriqueIC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
