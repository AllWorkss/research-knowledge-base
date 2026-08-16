param (
    [string]$message = "Auto-sync update: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
)

Write-Host "Syncing Research & Knowledge Base to GitHub..." -ForegroundColor Cyan

# Check if git is initialized
if (!(Test-Path .git)) {
    Write-Host "Error: Not a git repository. Please initialize git first." -ForegroundColor Red
    exit 1
}

# 1. Add all new/modified files
git add .

# 2. Commit changes
git commit -m $message

# 3. Push to GitHub
git push origin main

Write-Host "Sync Complete! ✨ Your research is safe." -ForegroundColor Green
