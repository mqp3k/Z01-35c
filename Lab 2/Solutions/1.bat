@ECHO OFF
set arg1=%1
set arg2=%2

dir %arg1% /B | findstr /e %arg2%
@ECHO ON
@ECHO OFF

rem arg1 to ścieżka, w której szukamy plików
rem arg2 to rozszerzenia szukanych plików