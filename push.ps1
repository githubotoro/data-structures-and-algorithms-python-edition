# Run index.js
node index.js

# Add all changes to Git
git add .

# Commit changes with the provided message
if ($args.Length -eq 0) {
    Write-Host "Please provide a commit message."
    exit 1
}
$commit_message = $args[0]
git commit -m "$commit_message"

# Push to the remote repository
git push
