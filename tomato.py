#!/usr/bin/python
import os

class Rules:
    def __init__(self):
        self.rules = []
        self.default = None

    def add(self, target, prereqs, recipes):
        parent = Rule(target)

        print(target)

        for p in prereqs:
            child = None

            for r in self.rules:
                if p == r.target:
                    child = r
                    break

            if not child:
                child = Rule(p)
                self.rules.append(child)

            parent.add_prereq(child)

        parent.add_recipes(recipes)
        self.rules.append(parent)

        if not self.default:
            self.default = parent

    def run(self, default=None):
        if not default:
            if not self.default:
                self.default.run()
        else:
            for r in self.rules:
                if r.target == default:
                    r.run()

    def __str__(self):
        return list(r.__str__() for r in self.rules).__str__()


class Rule:
    def __init__(self, target):
        self.target = target
        self.prereqs = []
        self.recipes = None

    def add_prereq(self, prereq):
        self.prereqs.append(prereq)

    def add_recipes(self, recipes):
        self.recipes = recipes

    def __str__(self):
        return "{} -> {}".format(self.target, " ".join(p.__str__() for p in self.prereqs))

    def run(self, dryrun=False):
        for r in self.recipes:
            if dryrun:
                print(r.format(self.target, *self.prereqs))
            else:
                os.system(r.format(self.target, *self.prereqs))
