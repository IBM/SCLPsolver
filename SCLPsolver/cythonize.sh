#!/bin/bash

BASEDIR=$PWD/subroutines
DIRS="equation_tools lp_tools state_tools"

for d in $DIRS; do
  dir="$BASEDIR/$d"
  pushd $dir
  python setup.py build_ext --inplace
  popd
done
