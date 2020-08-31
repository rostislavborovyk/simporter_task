#!/bin/bash

# runs pytest with print statements in console
mypy .
pytest -v --capture=no
