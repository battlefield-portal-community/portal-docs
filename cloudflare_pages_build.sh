#!/bin/bash

if [ "$CF_PAGES_BRANCH" == "main" ]; then

  poetry run gen-docs && hugo --themesDir hugo/themes --logLevel info

else
  hugo --themesDir hugo/themes --logLevel info
fi
