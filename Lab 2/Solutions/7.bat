@ECHO OFF

SET n=%1
SET fact=1

:factorial
IF %n% GEQ 1 (
SET /A fact=%fact%*%n%
SET /A n=%n%-1
GOTO factorial
)

ECHO %fact%