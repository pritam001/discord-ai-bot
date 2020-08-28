# echo _FormatCode_ guide:
# 	0 	Reset all styles
# 	1	Bold
#	32 	Green
#	34 	Blue
#	35 	Magenta
#	36	Cyan
RESET_STYLES=\033[0m
BOLD_BLUE=\033[1m\033[34m
BOLD_CYAN=\033[1m\033[36m

# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = all help setup

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "$(BOLD_BLUE)-----------------------------MAKE GUIDE----------------------------$(RESET_STYLES)"
	@echo "$(BOLD_CYAN)make setup$(RESET_STYLES) : Setup ping-py-bot"
	@echo "$(BOLD_BLUE)-------------------------------------------------------------------$(RESET_STYLES)"

setup: #: Use pip-tools, pip-compile, pip install
	@echo "\n$(BOLD_CYAN)Setting up ping-py-bot$(RESET_STYLES)"
	# Check for venv, conda else exit
	@echo "\n$(BOLD_CYAN)Installing pip-tools . . .$(RESET_STYLES)"
	pip install pip-tools
	@echo "\n$(BOLD_CYAN)Generating requirements$(RESET_STYLES)"
	pip-compile -q --build-isolation --output-file=requirements/requirements.txt requirements/requirements.in
	@echo "\n$(BOLD_CYAN)Installing requirements$(RESET_STYLES)"
	pip install -r requirements/requirements.txt
