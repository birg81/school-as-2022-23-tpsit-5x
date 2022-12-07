@echo off
REM file: fastapistart.bat
cd %~dp0
CLS
REM *** Envairoment VAR SETTING ***
REM module name / file name
set FASTAPI_FILE=webapp
REM app is file: 'webapp.py'. this file contains routing
set FASTAPI_APP=webapp
REM development mode (print PIN for edit with python on browser)
set FASTAPI_ENV=development
REM Host address setting - 0.0.0.0 so you can open from other device too
set FASTAPI_RUN_HOST=0.0.0.0
REM set your ip
set IPADDR=192.168.1.59
REM PORT setting
set FASTAPI_RUN_PORT=80
REM set your favorite browser in my case Vivaldi
set BROWSER="C:\Program Files\Vivaldi\Application\vivaldi.exe"
REM Start web page in your browser after lauch this file
%BROWSER% "http://%IPADDR%:%FASTAPI_RUN_PORT%"
CLS
REM start FASTAPI
uvicorn %FASTAPI_FILE%:%FASTAPI_APP% --reload --no-use-colors --port %FASTAPI_RUN_PORT% --host %FASTAPI_RUN_HOST%