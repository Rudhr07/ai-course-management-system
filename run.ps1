# Run the app using the project's virtualenv
# Usage: Right-click -> Run with PowerShell or in PowerShell: .\run.ps1
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
  & $venvActivate
  python app.py
} else {
  Write-Error ".venv not found in project. To create it run: python -m venv .venv and then install requirements with .\.venv\Scripts\python.exe -m pip install -r requirements.txt"
}
