#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

	module = AnsibleModule(argument_spec={})
	response = {"hello": "from hust"}
	module.exit_json(changed=False, meta=response)

if __name__ == '__main__':
    main()