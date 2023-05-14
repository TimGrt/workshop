all: pre-commit-package pre-commit-install ansible-installation ansible-lint-installation python-requirements ansible-requirements

COLOUR_GREEN=\033[0;32m
COLOUR_END=\033[0m

pre-commit-package:
	@echo "$(COLOUR_GREEN)### Installing pre-commit package... ###$(COLOUR_END)"
	@pip3 install pre-commit --user

pre-commit-install:
	@echo "$(COLOUR_GREEN)### Installing pre-commit hooks... ###$(COLOUR_END)"
	@pre-commit install

pre-commit-update:
	@echo "$(COLOUR_GREEN)### Updating pre-commit hooks... ###$(COLOUR_END)"
	@pre-commit autoupdate

ansible-installation:
	@echo "$(COLOUR_GREEN)### Installing ansible-core package... ###$(COLOUR_END)"
	@pip3 install ansible-core --user

ansible-lint-installation:
	@echo "$(COLOUR_GREEN)### Installing ansible-core package... ###$(COLOUR_END)"
	@pip3 install ansible-core --user

python-requirements:
	@echo "$(COLOUR_GREEN)### Installing Python requirements... ###$(COLOUR_END)"
	@pip3 install -r requirements.txt --user

ansible-requirements:
	@echo "$(COLOUR_GREEN)### Installing Ansible Collections... ###$(COLOUR_END)"
	@ansible-galaxy collection install -r requirements.yml
