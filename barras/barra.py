from barcode import Code39
from barcode.writer import ImageWriter

# Número para el código de barras
numero = '74795049'

# Crear un objeto Code 39 con el número
codigo_barras = Code39(numero, writer=ImageWriter(), add_checksum=False)

# Guardar la imagen del código de barras
nombre_archivo = 'ferney'
codigo_barras.save(nombre_archivo)
print(f"Se ha generado el código de barras en '{nombre_archivo}.png'")
