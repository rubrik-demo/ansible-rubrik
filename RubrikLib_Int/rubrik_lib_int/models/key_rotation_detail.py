# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class KeyRotationDetail(Model):
    """KeyRotationDetail.

    :param rotation_id: ID of the key rotation.
    :type rotation_id: str
    :param node_id: ID of the node rotating keys.
    :type node_id: str
    :param status: Status of the key rotation. Possible values include:
     'queued', 'inProgress', 'success', 'aborted'
    :type status: str or :class:`enum <rubriklib_int.models.enum>`
    :param key_protection: Target key protection method. Possible values
     include: 'tpm', 'kmip'
    :type key_protection: str or :class:`enum <rubriklib_int.models.enum>`
    :param key_recovery: Whether to enable Rubrik to recover the encryption
     keys in the event of a hardware failure.
    :type key_recovery: bool
    :param start_time:
    :type start_time: datetime
    :param end_time:
    :type end_time: datetime
    """

    _validation = {
        'rotation_id': {'required': True},
        'node_id': {'required': True},
        'status': {'required': True},
        'key_protection': {'required': True},
        'key_recovery': {'required': True},
    }

    _attribute_map = {
        'rotation_id': {'key': 'rotationId', 'type': 'str'},
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'key_protection': {'key': 'keyProtection', 'type': 'str'},
        'key_recovery': {'key': 'keyRecovery', 'type': 'bool'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
    }

    def __init__(self, rotation_id, node_id, status, key_protection, key_recovery, start_time=None, end_time=None):
        self.rotation_id = rotation_id
        self.node_id = node_id
        self.status = status
        self.key_protection = key_protection
        self.key_recovery = key_recovery
        self.start_time = start_time
        self.end_time = end_time
