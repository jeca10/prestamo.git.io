import barcode
from barcode.writer import ImageWriter

# Función para generar códigos de barras
def generate_barcodes(start, end, output_format, output_folder):
    for i in range(start, end+1):
        code = barcode.get_barcode_class(output_format)
        barcode_instance = code(f'{i}', writer=ImageWriter())
        filename = f'{output_folder}/barcode_{i}'
        barcode_instance.save(filename)

# Definir rango de códigos
start_number = 1
end_number = 10

# Formato del código de barras (puedes elegir diferentes tipos, como 'code39' o 'ean13')
barcode_format = 'code128'

# Carpeta de salida para los códigos de barras
output_folder = 'barcodes'

# Generar los códigos de barras
generate_barcodes(start_number, end_number, barcode_format, output_folder)

print(f'Se han generado códigos de barras del {start_number} al {end_number} en la carpeta {output_folder}.')

