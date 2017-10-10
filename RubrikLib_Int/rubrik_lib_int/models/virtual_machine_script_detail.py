# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineScriptDetail(Model):
    """VirtualMachineScriptDetail.

    :param script_path: The command to be run in VM guest OS
    :type script_path: str
    :param timeout_ms: Time (in ms) after which the script will be terminated
     if it has not completed
    :type timeout_ms: long
    :param failure_handling: Action to take if the script returns an error or
     times out. Possible values include: 'abort', 'continue'
    :type failure_handling: str or :class:`enum <rubriklib_int.models.enum>`
    """

    _validation = {
        'script_path': {'required': True},
        'timeout_ms': {'required': True},
        'failure_handling': {'required': True},
    }

    _attribute_map = {
        'script_path': {'key': 'scriptPath', 'type': 'str'},
        'timeout_ms': {'key': 'timeoutMs', 'type': 'long'},
        'failure_handling': {'key': 'failureHandling', 'type': 'str'},
    }

    def __init__(self, script_path, timeout_ms, failure_handling):
        self.script_path = script_path
        self.timeout_ms = timeout_ms
        self.failure_handling = failure_handling
