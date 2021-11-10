#!/bin/sh
set -eux

. ./scripts-dev/clean.sh

sed -i -e "s/__version__ =.*/__version__ = \"$(git describe --tags)\"/" pydrs/__init__.py
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
