# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserPreferencesInfo(Model):
    """UserPreferencesInfo.

    :param default_org:
    :type default_org: str
    """

    _attribute_map = {
        'default_org': {'key': 'defaultOrg', 'type': 'str'},
    }

    def __init__(self, default_org=None):
        self.default_org = default_org
