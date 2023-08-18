@echo off
echo Se eliminarán todos los registros duplicados de todos los archivos CSV ubicados en la carpeta "entrada" bajo el siguiente criterio:
echo 1) Registros duplicados para la columna "cuil" 
echo 2) Registros duplicados para la columna "dni"
echo 3) Registros duplicados para la columna "email"
echo 4) Registros duplicados con el criterio de que: en caso de que la columna "nombre", la columna "apellido" y la columna "ministerio" sean iguales en dos o más registros.
echo.
set /p continue=¿Desea continuar? (si/no): 

if /i "%continue%"=="si" (
    python main.py
) else (
    echo Operación cancelada.
)

pause