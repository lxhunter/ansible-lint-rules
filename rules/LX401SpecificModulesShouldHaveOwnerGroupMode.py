from ansiblelint import AnsibleLintRule
import os

class LX401SpecificModulesShouldHaveOwnerGroupMode(AnsibleLintRule):
    id = 'LX401'
    shortdesc = "Specific Modules should have owner, group and mode"
    description = ''
    tags = ['module']
    modules = [
        'assemble','blockinfile','copy','file','get_url',
        'ini_file','lineinfile','replace','unarchive',
        'yum_repository','template'
    ]

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in self.modules:
            return False
        if task['action']['__ansible_module__'] == 'file' and task['action'].get('state', "file") not in ['directory','file','touch']:
            return False
        if task['action']['__ansible_module__'] == 'yum_repository' and task['action'].get('state') == 'absent':
            return False
        if 'owner' not in task['action']:
            return True
        if 'group' not in task['action']:
            return True
        if 'mode' not in task['action']:
            return True

        return False
