@ECHO OFF
set cp_dir=%1
mkdir copy
xcopy %1% .\copy /t /e

rem cp_dir to scieżka, z której chcemy skopiować foldery