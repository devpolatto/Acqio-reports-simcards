#!/usr/bin/env bash

pwd=$(pwd)
dependencie_file="$pwd/requirements.txt"

pip freeze > $dependencie_file

cat requirements.txt