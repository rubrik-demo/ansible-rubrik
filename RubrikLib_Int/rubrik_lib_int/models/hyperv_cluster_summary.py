# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sla_assignable import SlaAssignable


class HypervClusterSummary(SlaAssignable):
    """HypervClusterSummary.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param configured_sla_domain_id: ID of the configured SLA domain
    :type configured_sla_domain_id: str
    :param configured_sla_domain_name: name of the configured SLA domain
    :type configured_sla_domain_name: str
    :param primary_cluster_id:
    :type primary_cluster_id: str
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
        'configured_sla_domain_id': {'required': True},
        'configured_sla_domain_name': {'required': True},
        'primary_cluster_id': {'required': True},
    }

    def __init__(self, id, name, configured_sla_domain_id, configured_sla_domain_name, primary_cluster_id):
        super(HypervClusterSummary, self).__init__(id=id, name=name, configured_sla_domain_id=configured_sla_domain_id, configured_sla_domain_name=configured_sla_domain_name, primary_cluster_id=primary_cluster_id)
