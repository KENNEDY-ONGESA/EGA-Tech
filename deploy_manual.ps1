$username = "Kennedy"
$password = "Bboxx@2025"
$appName = "music-playlist-generator-g6freydyc6bhdye2"
$region = "canadacentral-01" # Based on your error log
$apiUrl = "https://$appName.scm.$region.azurewebsites.net/api/zipdeploy"

# 1. Create Zip of Backend
Write-Host "Zipping backend folder..."
$source = ".\backend"
$destination = ".\backend.zip"
if (Test-Path $destination) { Remove-Item $destination }
Compress-Archive -Path $source\* -DestinationPath $destination -Force

# 2. Create Auth Header (Basic Auth)
$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $username, $password)))

# 3. Upload
Write-Host "Deploying to Azure via ZIP API..."
try {
    Invoke-RestMethod -Uri $apiUrl -Headers @{Authorization=("Basic {0}" -f $base64AuthInfo)} -Method Post -InFile $destination -ContentType "application/zip"
    Write-Host "✅ Deployment SUCCESS!" -ForegroundColor Green
}
catch {
    Write-Host "❌ Deployment FAILED" -ForegroundColor Red
    Write-Host $_.Exception.Message
    # Print detailed error 
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        Write-Host "Details: " $reader.ReadToEnd()
    }
}
