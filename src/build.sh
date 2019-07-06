#!/bin/sh

pyinstaller personal_sharehold_performance.py --clean -F
rm -R ./build/
