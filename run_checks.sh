#!/bin/bash

isort auto_commit_message.py
black auto_commit_message.py
flake8 auto_commit_message.py
mypy auto_commit_message.py
