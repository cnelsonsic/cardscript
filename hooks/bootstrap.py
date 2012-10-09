#!/usr/bin/env python
from sh import git
from os.path import abspath, join, exists
from os import symlink, remove
# Link the pre-commit hook into the user's git hooks directory.
git_path = git('rev-parse', show_toplevel=True).strip()
source = abspath(join(git_path, './hooks/pre-commit'))
target = abspath(join(git_path, '.git/hooks/pre-commit'))
if exists(target):
    remove(target)
symlink(source, target)
print("Linked {0} to {1}".format(source, target))
