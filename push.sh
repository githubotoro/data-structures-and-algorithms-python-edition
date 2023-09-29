#!/bin/bash

# Run index.js
node index.js

# Add all changes to Git
git add .

# Commit changes with the provided message
if [ $# -eq 0 ]; then
  echo "Please provide a commit message."
  exit 1
fi
commit_message="$1"
git commit -m "$commit_message"

# Push to the remote repository
git push
