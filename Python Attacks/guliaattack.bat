@echo off
set i=0
:loop
set /a i=i+1
echo Attack - %i%
python gulia.py
goto loop