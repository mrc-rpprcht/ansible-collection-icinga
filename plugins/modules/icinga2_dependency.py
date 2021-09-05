#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec = dict(
            state                 = dict(default='present', choices=['present', 'absent']),
            name                  = dict(required=True),
            order                 = dict(default=10, type='int'),
            file                  = dict(required=True, type='str'),
            template              = dict(default=False, type='bool'),
            imports               = dict(default=list(), type='list', elements='str'),
            parent_host_name      = dict(required=True, type='str'),
            parent_service_name   = dict(type='str'),
            child_host_name       = dict(required=True, type='str'),
            child_service_name    = dict(type='str'),
            disable_checks        = dict(type='bool'),
            disable_notifications = dict(type='bool'),
            ignore_soft_states    = dict(type='bool'),
            period                = dict(type='bool'),
            states               = dict(type='list', elements='str'),
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')
    template = args.pop('template')
    imports = args.pop('imports')
    del args['_vars']

    module.exit_json(changed=False, args=args, name=name, order=str(order), state=state, file=file, template=template, imports=imports)

if __name__ == '__main__':
    main()