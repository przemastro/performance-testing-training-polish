@echo off & SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
SET STR=Test String
SET STR
call :tolower STR
SET STR
call :toupper STR
set STR
goto :EOF

:: toupper & tolower; makes use of the fact that string 
:: replacement (via SET) is not case sensitive
:toupper
for %%L IN (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) DO SET %1=!%1:%%L=%%L!
goto :EOF

:tolower
for %%L IN (a b c d e f g h i j k l m n o p q r s t u v w x y z) DO SET %1=!%1:%%L=%%L!
goto :EOF