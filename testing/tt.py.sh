#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh


error
echodo $PYTHON src/tt.py
echodo $PYTHON src/tt.py derp
