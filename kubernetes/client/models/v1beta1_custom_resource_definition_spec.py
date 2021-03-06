# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.9.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1CustomResourceDefinitionSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'group': 'str',
        'names': 'V1beta1CustomResourceDefinitionNames',
        'scope': 'str',
        'validation': 'V1beta1CustomResourceValidation',
        'version': 'str'
    }

    attribute_map = {
        'group': 'group',
        'names': 'names',
        'scope': 'scope',
        'validation': 'validation',
        'version': 'version'
    }

    def __init__(self, group=None, names=None, scope=None, validation=None, version=None):
        """
        V1beta1CustomResourceDefinitionSpec - a model defined in Swagger
        """

        self._group = None
        self._names = None
        self._scope = None
        self._validation = None
        self._version = None
        self.discriminator = None

        self.group = group
        self.names = names
        self.scope = scope
        if validation is not None:
          self.validation = validation
        self.version = version

    @property
    def group(self):
        """
        Gets the group of this V1beta1CustomResourceDefinitionSpec.
        Group is the group this resource belongs in

        :return: The group of this V1beta1CustomResourceDefinitionSpec.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this V1beta1CustomResourceDefinitionSpec.
        Group is the group this resource belongs in

        :param group: The group of this V1beta1CustomResourceDefinitionSpec.
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")

        self._group = group

    @property
    def names(self):
        """
        Gets the names of this V1beta1CustomResourceDefinitionSpec.
        Names are the names used to describe this custom resource

        :return: The names of this V1beta1CustomResourceDefinitionSpec.
        :rtype: V1beta1CustomResourceDefinitionNames
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this V1beta1CustomResourceDefinitionSpec.
        Names are the names used to describe this custom resource

        :param names: The names of this V1beta1CustomResourceDefinitionSpec.
        :type: V1beta1CustomResourceDefinitionNames
        """
        if names is None:
            raise ValueError("Invalid value for `names`, must not be `None`")

        self._names = names

    @property
    def scope(self):
        """
        Gets the scope of this V1beta1CustomResourceDefinitionSpec.
        Scope indicates whether this resource is cluster or namespace scoped.  Default is namespaced

        :return: The scope of this V1beta1CustomResourceDefinitionSpec.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this V1beta1CustomResourceDefinitionSpec.
        Scope indicates whether this resource is cluster or namespace scoped.  Default is namespaced

        :param scope: The scope of this V1beta1CustomResourceDefinitionSpec.
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")

        self._scope = scope

    @property
    def validation(self):
        """
        Gets the validation of this V1beta1CustomResourceDefinitionSpec.
        Validation describes the validation methods for CustomResources

        :return: The validation of this V1beta1CustomResourceDefinitionSpec.
        :rtype: V1beta1CustomResourceValidation
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """
        Sets the validation of this V1beta1CustomResourceDefinitionSpec.
        Validation describes the validation methods for CustomResources

        :param validation: The validation of this V1beta1CustomResourceDefinitionSpec.
        :type: V1beta1CustomResourceValidation
        """

        self._validation = validation

    @property
    def version(self):
        """
        Gets the version of this V1beta1CustomResourceDefinitionSpec.
        Version is the version this resource belongs in

        :return: The version of this V1beta1CustomResourceDefinitionSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this V1beta1CustomResourceDefinitionSpec.
        Version is the version this resource belongs in

        :param version: The version of this V1beta1CustomResourceDefinitionSpec.
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1CustomResourceDefinitionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
