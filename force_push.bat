@echo off
echo ========================================================
echo   Azure Force Deploy Tool
echo ========================================================
echo.
echo We need your Deployment Username.
echo (This is the one you set in Deployment Center -> Local Git/FTPS Credentials)
echo.
set /p username="Enter Username: "

echo.
echo Configuring Remote with Password 'Bboxx@2025'...
echo.

:: Remove old remote
git remote remove azure >nul 2>&1

:: Add new remote with URL-Encoded Password (@ becomes %40)
git remote add azure https://%username%:Bboxx%%402025@music-playlist-generator-g6freydyc6bhdye2.scm.canadacentral-01.azurewebsites.net:443/Music-Playlist-Generator.git

echo Pushing to Azure...
git push azure main --force

echo.
echo Done.
pause
