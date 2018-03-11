#!/bin/bash

command -v ansible-lint >/dev/null || { echo -e >&2 "${red}I need ansible-lint, pip install ansible-lint${color_off}"; exit 3; }

if [ "$1" != "" ]; then
  rule=$( echo $1 | tr '[:lower:]' '[:upper:]')

  ansible-lint -t "${rule}" -r "rules" tests/${rule}*.yml
  exit 0
fi

# lint all files with the rules in rules, but not the global ones
ansible-lint -r rules tests/*.yml
