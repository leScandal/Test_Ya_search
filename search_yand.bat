@echo off
del error.txt
del out.txt

set ERROR_OUT=error.txt
set PROGRAMM_OUT=out.txt


set PATH_DRIVER=C:\distrib
set URL_YANDEX=https://ya.ru
set SEARCH_BODY="совкомбанк"
set RESULT_7="sovcombank.ru"

py search_yand.py %PATH_DRIVER% %URL_YANDEX% %SEARCH_BODY% %RESULT_7% 1>>%PROGRAMM_OUT% 2>>%ERROR_OUT%
                                                                                     

