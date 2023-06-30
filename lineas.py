def contar_lineas(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            cantidad_lineas = len(lineas)
            return cantidad_lineas
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except IOError:
        print("Error de lectura del archivo.")

# Ejemplo de uso
archivo_txt = 'DE-EN-alligned.txt'  # Reemplaza 'texto.txt' con la ruta de tu archivo
cantidad_lineas = contar_lineas(archivo_txt)
print("Cantidad de líneas:", cantidad_lineas)
#152633