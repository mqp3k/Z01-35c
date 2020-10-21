@ECHO OFF
set fib1=0
set fib2=1
set n=%1

if %n% gtr 0 echo 1 & set /a "n=%n%-1"

:loop
	if %n% leq 0 goto end
	set /a "n=%n%-1"
	set /a num=%fib1%+%fib2%
	echo %num%
	set fib1=%fib2%
	set fib2=%num%
	goto loop
	
:end

rem n to liczba pierwszych liczb ciągu Fibonacciego