Mult-Aliens
=================

To use the program

You should have python and pip installed on your computer. Ideally you should
also have virtualenvwrapper installed (use pip install virtualenvwrapper to
install it).

Create your virtualenv by running : mkvirtualenv aliens

Next install dependencies : pip install -r venv/requirements.txt

Run the program : python aliens.py

Reports are generated in the /reports folder.

Enjoy



For developers
================

To add plugins to format the report add it to the plugins directory and update
the config.py file. Dont forget to lint your codes using the flake8 linter (
http://flake8.readthedocs.org/en/2.2.3/) by running "flake8 ." in the folder
and ensure that there are no errors.
