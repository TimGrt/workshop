# workshop

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## Preparation

Run the provided `Makefile`, it will setup everything you need for running and developing the project.

* *pre-commit* package installation
* enabling *pre-commit hooks*
* *ansible-core* installation
* *ansible-lint* installation
* Python requirements installation for project
* Ansible collections installation for project

```bash
make
```

## Usage

The `ansible.cfg` expects a *vault-password-file* in your home directory, create the file and insert the vault password as a single line.

```bash
vi ~/.vault-password
```

Afterwards run playbooks from the `playbooks/` folder and provide a inventory file from the `inventory/` folder, for example:

```bash
ansible-playbook -i inventory/sandbox.ini playbooks/ios-connection-test.yml
```

You need to provide `--ask-vault-pass` if you are not using the *vault-password-file*.

## Authors

* Tim Grützmacher
* Frank Dämming
* Thomas Stotko

