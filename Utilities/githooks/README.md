# Overview

See https://www.atlassian.com/git/tutorials/git-hooks

Githooks are scripts which run every time a particular event occurs in a git repo. 

To use these githooks, copy them to your repo's `.git/hooks/` folder, or create a symlink from there to this folder.

# Requirements

These githooks require Python to run, as do the setup scripts. 

# Current Githook Behavior

## post-checkout

Runs the CustomDataTypes setup script with the -f flag. When you checkout a new branch, you overwrite your own vi.lib CustomDataTypes with the ones from the repo.

## pre-commit

Runs the CustomDataTypes setup script with the -r flag. Before you commit, put your CustomDataTypes back into the repo so that they a) don't appear as a subtractive change and b) will reflect any changes you made.

## post-commit

Same behavior as post-checkout, but -f not required.

