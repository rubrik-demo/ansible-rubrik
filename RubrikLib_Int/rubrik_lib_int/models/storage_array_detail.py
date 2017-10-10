# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageArrayDetail(Model):
    """StorageArrayDetail.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id:
    :type id: str
    :ivar array_type: Storage array type/brand. Default value: "PureStorage" .
    :vartype array_type: str
    :param hostname: Hostname is used to connect to the storage array. This
     can be a valid dns name or IP address.
    :type hostname: str
    :param username:
    :type username: str
    """

    _validation = {
        'id': {'required': True},
        'array_type': {'required': True, 'constant': True},
        'hostname': {'required': True},
        'username': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'array_type': {'key': 'arrayType', 'type': 'str'},
        'hostname': {'key': 'hostname', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
    }

    array_type = "PureStorage"

    def __init__(self, id, hostname, username):
        self.id = id
        self.hostname = hostname
        self.username = username
