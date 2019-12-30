#!/bin/bash

export FLASK_APP="source"
export FLASK_ENV="development"
echo -e "$FLASK_APP\n$FLASK_ENV\n"

flask run
