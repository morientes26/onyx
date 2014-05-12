#!/bin/bash

set PYTHONPATH=.
export PYTHONPATH

PATTERN="test*.py"

echo ""
echo "-------------------- UNIT TESTS -------------------------"
echo "-- run all test: without parameter                     --"
echo "-- run one test: module.testclass                      --"
echo "--         for example: tests.Activity.testUC1Activity --"
echo "---------------------------------------------------------"
echo ""

if [ $1 ]; then
   PATTERN=$1
   python -m unittest $PATTERN
else
   python -m unittest discover --pattern=$PATTERN
fi
