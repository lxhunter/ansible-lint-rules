from ansiblelint import AnsibleLintRule
import os

class LX501TemplateShouldHaveJinjaExtension(AnsibleLintRule):
    id = 'LX501'
    shortdesc = "Templates should have the jinja extension"
    description = ''
    tags = ['module']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] != 'template':
            return False
        if task['action']['src'].startswith('{{'):
            return False
        ext = os.path.splitext(task['action']['src'])
        if ext[1] != ".j2":
            return True
        return False
