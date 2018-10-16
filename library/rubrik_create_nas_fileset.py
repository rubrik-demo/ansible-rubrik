#!/usr/bin/python
# Copyright: Rubrik
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
module: rubrik_create_nas_fileset
short_description: Create a Rubrik NAS Fileset.
description:
    - Create a Rubrik NAS Fileset.
version_added: 2.7
author: Rubrik Ranger Team
options:

  fileset_name:
    description:
      - The name of the Fileset you wish to create.
    required = False
    aliases = name

  share_type:
    description:
      - The type of NAS Share you wish to backup.
    required = False
    choices = [NFS, SMB]

  include:
    description:
      - The full paths or wildcards that define the objects to include in the Fileset backup.
    required = False
    type = list

  exclude:
    description:
      - The full paths or wildcards that define the objects to exclude from the Fileset backup.
    required = False
    type = list
    default = []

  exclude_exception:
    description:
      - The full paths or wildcards that define the objects that are exempt from the excludes variables.
    required = False
    type = list
    default = []

  follow_network_shares:
    description:
      - Include or exclude locally-mounted remote file systems from backups.
    required = False
    type = bool
    default = False

  timeout:
    description:
      - The number of seconds to wait to establish a connection the Rubrik cluster before returning a timeout error.
    required = False
    type = int
    default = 15


extends_documentation_fragment:
    - rubrik_cdm
requirements: [rubrik_cdm]
'''

EXAMPLES = '''
- rubrik_create_nas_fileset:
    provider: "{{ credentials }}"
    name: 'AnsibleDemo'
    include: '/usr/local'
    share_type: 'NFS'
    exclude: '/usr/local/temp,*.mp3,*.mp4,*mp5'
    exclude_exception: '/company*.mp4'
    follow_network_shares: False
'''

RETURNS = """
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.rubrikcdm import sdk_validation, connect, load_provider_variables, rubrik_argument_spec


def main():
    """ Main entry point for Ansible module execution.
    """

    argument_spec = rubrik_argument_spec

    # Start Parameters
    argument_spec.update(
        dict(
            fileset_name=dict(required=False, aliases=['name']),
            share_type=dict(required=False, choices=['NFS', 'SMB']),
            include=dict(required=False, type='list'),
            exclude=dict(required=False, type='list', default=[]),
            exclude_exception=dict(required=False, type='list', default=[]),
            follow_network_shares=dict(required=False, type='bool', default=False),
            timeout=dict(required=False, type='int', default=15),

        )
    )
    # End Parameters

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    sdk_present, rubrik_cdm = sdk_validation()

    if sdk_present is False:
        module.fail_json(msg="The Rubrik Python SDK is required for this module (pip install rubrik_cdm).")

    results = {}

    load_provider_variables(module)
    ansible = module.params

    rubrik = connect(rubrik_cdm, module)
    if isinstance(rubrik, str):
        module.fail_json(msg=rubrik)

    try:
        api_request = rubrik.create_nas_fileset(ansible["fileset_name"], ansible["share_type"], ansible["include"],
                                                ansible["exclude"], ansible["exclude_exception"], ansible["follow_network_shares"], ansible["timeout"])

    except SystemExit as error:
        module.fail_json(msg=str(error))

    if "No change required" in api_request:
        results["changed"] = False
    else:
        results["changed"] = True

    results["response"] = api_request

    module.exit_json(**results)


if __name__ == '__main__':
    main()
