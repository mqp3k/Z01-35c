@ECHO OFF

set tree_dir=%1
set orig_dir=%cd%
set leading_str=!
set sub_dir_str=  !

cd %tree_dir%
call :loop
cd %orig_dir%
goto :eof

:loop
	for /D %%G in (*) do (
		echo | set /p=%leading_str%
		echo _%%G
		set leading_str=%leading_str%%sub_dir_str%
		cd %%G
		call :loop
		cd ..	
)