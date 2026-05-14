#!/bin/bash

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  echo
  echo "This script must be run:"
  echo "  source ./setGeoServerPassword.sh"
  echo
  exit 1
fi

echo
read -s -p "please enter geoServer password: " GEOSERVER_PASSWORD
echo

export GEOSERVER_PASSWORD

echo "GEOSERVER_PASSWORD set for this terminal session"
echo

