#!/usr/bin/python
import sys
import tomato

rules = tomato.Rules()

rules.add("main.o", {"main.c"}, {'gcc -c {1}'})
rules.add("clean", {}, {'rm main.o test'})
rules.add("test" , {"main.o gigi.o"}, {'gcc -o {0} {1}'})

if len(sys.argv) > 1:
    rules.run(sys.argv[1])
else:
    rules.run()

print(rules)
