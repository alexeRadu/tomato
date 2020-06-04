#!/usr/bin/python
import os

global rules

class Rules:
    def __init__(self):
        self.rules = []
        self.default = None

    def add(self, target, prereqs, recipes):
        r = Rule(target, prereqs, recipes)
        self.rules.append(r)

        if not self.default:
            self.default = r

    def run(self, default=[]):
        if not default:
            if self.default:
                self.default.run()
        else:
            for r in self.rules:
                if r.target == default[0]:
                    r.run()

    def __str__(self):
        return "\n".join(r.__str__() for r in self.rules)

rules = Rules()


class Rule:
    def __init__(self, target, prereqs, recipes):
        self.target = target
        self.prereqs = prereqs
        self.recipes = recipes

    def __str__(self):
        if self.prereqs:
            return "{}: {}".format(self.target, " ".join(self.prereqs))
        else:
            return self.target

    def run(self, dryrun=False):
        for r in self.recipes:
            if dryrun:
                print(r.format(self.target, *self.prereqs))
            else:
                os.system(r.format(self.target, *self.prereqs))
