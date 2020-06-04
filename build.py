#!/usr/bin/python3.8
import sys
import tomato
from tomato import rules

rules.add("main.o", ["main.c", "math.h"], ['gcc -c {1}'])
rules.add("math.o", ["math.c"], ['gcc -c {1}'])
rules.add("test" , ["main.o", "math.o"], ['gcc -o {0} {1} {2}'])
rules.add("clean", [], ['rm math.o main.o test'])

rules.run(sys.argv[1:], dryrun=False)
