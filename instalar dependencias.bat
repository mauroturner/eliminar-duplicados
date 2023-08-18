@echo off
set /p install_dependencies=¿Desea instalar las dependencias necesarias? (si/no): 

if /i "%install_dependencies%"=="si" (
    pip install -r requirements.txt
) else (
    echo No se instalarán dependencias.
)

pause