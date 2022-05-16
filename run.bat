@echo off
cd %~dp0
pipenv run python main.py

chcp 65001
setlocal enabledelayedexpansion
SET INIFILE=config.ini
SET FLAG=FALSE
SET /a Y=%date:~0,4%
SET /a M=%date:~5,2%
SET /a B_M=%M%-1
SET /a A_M=%M%+1

if M == 1 (
   SET /a B_M=12
) else if M == 12 (
   SET /a A_M=1
)

for /f %%a in (%INIFILE%) do (
   if %%a == [FILE] (
      SET FLAG=TRUE
   ) else (
      if !FLAG! == TRUE (
         SET file=%%a
      )
      SET FLAG=FALSE
   )
)

start ./text/%B_M%-%A_M%%file:~5%%Y%.txt

exit /b