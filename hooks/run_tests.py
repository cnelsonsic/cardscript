#!/usr/bin/env python -u
import sys
import sh
from sh import git, nosetests

def main(all_files=False):
    git.stash(u=True, keep_index=True)

    try:
        results = nosetests('cardscript/', with_doctest=True)
        result = True
    except sh.ErrorReturnCode as exc:
        # If anything goes wrong, let us know, but abandon the commit.
        git.reset(hard=True) # Code is wrong, reset it.
        print("ERROR: Tests FAILED; Commit ABORTED.")
        print(exc.stderr)
        result = False
    finally:
        git.stash('pop', q=True) # Restore anything in our working directory.
    return result

if __name__ == '__main__':
    all_files = False
    if len(sys.argv) > 1 and sys.argv[1] == '--all-files':
        all_files = True
    result = main(all_files)
    if not result:
        sys.exit(1)
