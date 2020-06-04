#!/usr/bin/python3.8
import sys
import tomato
from tomato import rules

rules.add("main.o", ["main.c"], ['gcc -c {1}'])
rules.add("test" , ["main.o", "gigi.o"], ['gcc -o {0} {1}'])
rules.add("clean", [], ['rm main.o test'])

rules.run(sys.argv[1:])
