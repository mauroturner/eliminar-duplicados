import os
import pandas as pd

def main():
    # Definimos la ruta donde se cargan y guardan los archivos
    input_directory = 'entrada'
    output_directory = 'salida'

    # Creamos las carpetas en caso de no existir
    if not os.path.exists(input_directory):
        os.makedirs(input_directory)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Lista para almacenar los nombres de los archivos CSV en la carpeta de entrada
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Procesamos cada archivo csv
    for csv_file in csv_files:
        input_path = os.path.join(input_directory, csv_file)
        output_path = os.path.join(output_directory, csv_file)

        # Cargar el archivo CSV usando pandas
        df = pd.read_csv(input_path)

        # Verificamos que existan las columnas de dónde leventamos los datos, en ese caso eliminamos.
        if 'cuil' in df.columns:
            df.drop_duplicates(subset=['cuil'], inplace=True)

        if 'dni' in df.columns:
            df.drop_duplicates(subset=['dni'], inplace=True)

        if 'email' in df.columns:
            df.drop_duplicates(subset=['email'], inplace=True)

        if all(col in df.columns for col in ['nombre', 'apellido', 'ministerio']):
            df.drop_duplicates(subset=['nombre', 'apellido', 'ministerio'], inplace=True)
            
        # Guardar el DataFrame procesado en un nuevo archivo CSV
        df.to_csv(output_path, index=False)

        print(f'Archivo {csv_file} procesado y guardado en {output_path}')

if __name__ == '__main__':
    main()