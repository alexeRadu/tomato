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

    def run(self, default=[], dryrun=False):
        if not default:
            if self.default:
                self.default.run(dryrun)
        else:
            r = self.find(default[0])
            if r:
                r.run(dryrun)

    def find(self, target):
        for r in self.rules:
            if r.target == target:
                return r

        return None

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

    def _run_recipes(self, dryrun):
        for r in self.recipes:
            if dryrun:
                print(r.format(self.target, *self.prereqs))
            else:
                print(r.format(self.target, *self.prereqs))
                os.system(r.format(self.target, *self.prereqs))

    def run(self, dryrun=False):
        global rules

        if os.path.exists(self.target):
            mtime_target = os.stat(self.target).st_mtime
            refresh = False
        else:
            mtime_target = 0
            refresh = True

        for p in self.prereqs:
            r = rules.find(p)
            if r:
                refresh = r.run(dryrun)
                continue

            if not os.path.exists(p):
                raise Exception("No rule to make " + p)

            mtime_prereq = os.stat(p).st_mtime
            if mtime_prereq > mtime_target:
                refresh = True

        if refresh:
            self._run_recipes(dryrun)

        return refresh
