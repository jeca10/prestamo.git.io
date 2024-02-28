from barcode import Code39
from barcode.writer import ImageWriter

# Número para el código de barras
numero = '293423423'

# Crear un objeto Code 39 con el número
codigo_barras = Code39(numero, writer=ImageWriter(), add_checksum=False)

# Guardar la imagen del código de barras
nombre_archivo = 'codigo_barras_293423423'
archivo_imagen = f"{nombre_archivo}.png"
codigo_barras.save(archivo_imagen)
print(f"Se ha generado el código de barras en '{archivo_imagen}'")

# Guardar el número y el nombre del archivo en un archivo de texto
with open('informacion_codigos.txt', 'a') as archivo_texto:
    archivo_texto.write(f"Número: {numero}, Nombre de archivo: {nombre_archivo}\n")