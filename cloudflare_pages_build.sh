#!/bin/bash

if [ "$CF_PAGES_BRANCH" == "main" ]; then

  poetry run gen-docs && hugo --logLevel info

else
  hugo --logLevel info
fi
