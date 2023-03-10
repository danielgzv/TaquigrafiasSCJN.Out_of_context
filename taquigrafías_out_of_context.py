# -*- coding: utf-8 -*-
"""Taquigrafías. Out_of_context.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W0He0RFz8iSz51RITaO2tkFDuonH1b8O

Descargar los pdf de la página
"""

import os
import requests
from bs4 import BeautifulSoup

# Directorio donde se guardarán los archivos descargados
DOWNLOAD_DIR = '/content/drive/MyDrive/Prueba pdfs'

# URL base del sitio web
BASE_URL = 'https://www.scjn.gob.mx'

# Rango de páginas a descargar (0 a 358)
PAGE_RANGE = range(0, 100)

# Listas para almacenar los valores de las dos columnas
fechas = []
instancias = []

# Iterar por cada página
for page_num in PAGE_RANGE:
    # URL de la página actual
    url = f'{BASE_URL}/multimedia/versiones-taquigraficas?fecha=All&field_vsts_instancia_target_id_1=All&page={page_num}'

    # Obtener el contenido HTML de la página
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todas las filas de la tabla en la página
    rows = soup.find_all('tr')

    # Iterar por cada fila y extraer los valores de las columnas requeridas
    for row in rows:
        fecha_cell = row.find('td', {'headers': 'view-field-vsts-fecha-table-column'})
        instancia_cell = row.find('td', {'headers': 'view-field-vsts-instancia-table-column'})
        
        # Si se encontraron las dos columnas, agregar sus valores a las listas
        if fecha_cell and instancia_cell:
            fechas.append(fecha_cell.text.strip())
            instancias.append(instancia_cell.text.strip())

            # Descargar el archivo PDF en el directorio
            pdf_link = row.find('a', href=lambda href: href and href.endswith('.pdf'))
            pdf_url = f"{BASE_URL}{pdf_link['href']}"
            pdf_filename = f"{fecha_cell.text.strip()}_{instancia_cell.text.strip()}.pdf"

            # Crear el directorio si no existe
            if not os.path.exists(DOWNLOAD_DIR):
                os.makedirs(DOWNLOAD_DIR)

            # Descargar el archivo en el directorio
            with open(os.path.join(DOWNLOAD_DIR, pdf_filename), 'wb') as f:
                response = requests.get(pdf_url)
                f.write(response.content)

            print(f'Descargado {pdf_filename}')

"""Instalación de biblioteca aspose para trabajar los archivos pdf"""

!pip install aspose.words

"""Modificar los archivos pdf por archivos txt"""

import os
import aspose.words as aw

# Directorio de entrada y salida
input_folder = '/content/drive/MyDrive/Prueba pdfs'
output_folder = '/content/drive/MyDrive/Prueba txts'

# Iterar sobre los archivos en el directorio de entrada
for filename in os.listdir(input_folder):
    # Verificar si el archivo es un PDF
    if filename.endswith('.pdf'):
        # Crear la ruta completa de entrada y salida
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
        
        # Abrir el archivo PDF y guardarlo como texto sin formato
        doc = aw.Document(input_file)
        doc.save(output_file, aw.SaveFormat.TEXT)

"""Buscar una lista de palabras en los archivos de texto plano y contarlas"""

import os
import re

# lista de palabras que se buscarán
palabras_buscadas = ['alcohol','ay', 'baño', 'broma', 'burla', 'café', 'cafecito', 
                     'canción','carcajada','cerveza', 'chascarrillo','chela',
                     'chisme','chicharrón','demonio','desayuno', 'diablo', 
                     'dios','disculpa', 'divino','dormir','enfado', 'enojo',
                     'golosina','grosería', 'güey','leche','libro','mal',
                     'malinterprete','misa','molestia','ofenda','ofender', 'ofensa',
                     'ofendid','pasillo','película','risa', 'santo','soez', 'suciedad',
                     'sueño','tamal','té','tonto','tontería', 'vulgar', 'wey']

# inicializar el diccionario de conteo
conteo_palabras = {palabra: 0 for palabra in palabras_buscadas}

# ruta a la carpeta con los archivos txt
ruta_carpeta = '/content/drive/MyDrive/Prueba txts'

#Verificación para asegurarte de que el archivo que estás intentando abrir es en realidad un archivo de texto antes de intentar leer su contenido
for archivo_txt in os.listdir(ruta_carpeta):
    if archivo_txt.endswith('.txt'):
        # leer el archivo txt
        with open(os.path.join(ruta_carpeta, archivo_txt), 'r') as f:
            contenido = f.read()
            
        # resto del código...

# iterar a través de los archivos en la carpeta
for archivo_txt in os.listdir(ruta_carpeta):
    # leer el archivo txt
    with open(os.path.join(ruta_carpeta, archivo_txt), 'r') as f:
        contenido = f.read()

    # dividir el contenido en párrafos
    parrafos = contenido.split('\n\n')

    # iterar a través de los párrafos
    for parrafo in parrafos:
        # buscar cada palabra en el párrafo y actualizar el conteo
        for palabra in palabras_buscadas:
            if re.search(rf'\b{palabra}\b', parrafo):
                conteo_palabras[palabra] += 1

# imprimir el conteo de cada palabra
for palabra, conteo in conteo_palabras.items():
    print(f'{palabra}: {conteo}')

"""Imprimir los párrafos que incluyan las palabras de la lista"""

import os
import re
import aspose.words as aw

# Carpeta que contiene los archivos de texto
carpeta = '/content/drive/MyDrive/Prueba txts'

# Palabras clave a buscar
palabras_clave =palabras_clave = ['alcohol','ay', 'baño', 'broma', 'burla', 'café', 'cafecito', 
                     'canción','carcajada','cerveza', 'chascarrillo','chela',
                     'chisme','chicharrón','demonio','desayuno', 'diablo', 
                     'dios','disculpa', 'divino','dormir','enfado', 'enojo',
                     'golosina','grosería', 'güey','leche','libro','mal',
                     'malinterprete','misa','molestia','ofenda','ofender', 'ofensa',
                     'ofendid','pasillo','película','risa', 'santo','soez', 'suciedad',
                     'sueño','tamal','té','tonto','tontería', 'vulgar', 'wey']
                     
# Iterar sobre todos los archivos de texto en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith('.txt'):
        # Abrir el archivo de texto con Aspose.Words
        doc = aw.Document(os.path.join(carpeta, archivo))

        # Iterar sobre los párrafos del documento
        for parrafo in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True):
            texto_parrafo = parrafo.get_text().lower()

            # Buscar las palabras clave en el texto del párrafo
            for palabra in palabras_clave:
                if re.search(r'\b{}\b'.format(palabra), texto_parrafo):
                  
                    # Imprimir el texto del párrafo si contiene una palabra clave
                    print(texto_parrafo)
                    break

"""Guardar los párrafos en archivos de texto plano

![GPT.jpg](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAAcABkDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDz2PwLoqoqtaFyBgsZXyffg10F98CbrTdMTUbvwnqVtYuFIuJYp1TDcqSSeMjkZ69q9K+COm2M+rXmo3Onx6vNp72sv2SaNpFjtzOonuPLXlzGuOMEDeWIO2vSrfUDp80qwvqUEl3brfXmsWMzRQXLu53GS9hLyOdxAU8orZBjP3q73KzP56wlbH4il7ari6i5r2tKWnr8+i6HyXJ4F0VkZVtChIwGEr5Hvya8pr6++N2nwJq2majAJfMuYJILxrkJ55u4JnjlMmz5WbAT51+/944JIHyDVp3R9zwjWxUquKo4mrKfLyWu29+bu3a+h9MeBfGc/gnVprqJJJYLmBrW5ihnaCRoyyt8ki8oysiMGwcFRkEZB9Gf4p+Fr/SoWum1prhZTLc292kdxJcfMp2xzK0ccW/aoeTyWkOM7m6V8ex+NdajRUW9OFGBmNCfzIpf+E41v/n9/wDISf8AxNJxTPFocK5xh4unCpTcezcv/kf1tv3PePGvjbUPHWsPfXwhhXc5itbWMJFFvdnbaPUszEsSSSeTXzVW5J411qRGRr04YYOI0B/MCsOmfWcOZNi8qlXqYyalKpy7Nva+90u5/9k=)

"Para guardar los párrafos en una carpeta separada, puedes agregar un bloque de código adicional después de encontrar los párrafos en cada archivo. El código debería crear una nueva carpeta llamada 'Párrafos' dentro de la carpeta 'Taquigrafías', y guardar cada párrafo en un archivo separado dentro de esa carpeta."

"Este código creará la carpeta 'Párrafos' dentro de la carpeta 'Taquigrafías' si aún no existe, y luego guardará cada párrafo como un archivo separado dentro de esa carpeta. El nombre de cada archivo se basará en su número de índice en la lista de párrafos, y se guardará como un archivo de texto simple."

"""

import os
import re
import aspose.words as aw

# Carpeta que contiene los archivos de texto
carpeta = '/content/drive/MyDrive/Prueba txts'

# Palabras clave a buscar
palabras_clave = ['alcohol','ay', 'baño', 'broma', 'burla', 'café', 'cafecito', 
                     'canción','carcajada','cerveza', 'chascarrillo','chela',
                     'chisme','chicharrón','demonio','desayuno', 'diablo', 
                     'dios','disculpa', 'divino','dormir','enfado', 'enojo',
                     'golosina','grosería', 'güey','leche','libro','mal',
                     'malinterprete','misa','molestia','ofenda','ofender', 'ofensa',
                     'ofendid','pasillo','película','risa', 'santo','soez', 'suciedad',
                     'sueño','tamal','té','tonto','tontería', 'vulgar', 'wey']

# Iterar sobre todos los archivos de texto en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith('.txt'):
        # Abrir el archivo de texto con Aspose.Words
        doc = aw.Document(os.path.join(carpeta, archivo))

        # Iterar sobre los párrafos del documento
        for parrafo in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True):
            texto_parrafo = parrafo.get_text().lower()

            # Buscar las palabras clave en el texto del párrafo
            for palabra in palabras_clave:
                if re.search(r'\b{}\b'.format(palabra), texto_parrafo):

                    # Guardar el texto del párrafo en un archivo separado
                    nombre_archivo = f'{palabra}_{archivo}_{parrafo.get_text().strip()[:20]}.txt'
                    ruta_archivo = os.path.join('/content/drive/MyDrive/Prueba párrafos', nombre_archivo)
                    with open(ruta_archivo, 'w') as f:
                        f.write(texto_parrafo)

                    # Imprimir el nombre del archivo y el texto del párrafo
                    print(f'Archivo: {nombre_archivo}\nTexto del párrafo: {texto_parrafo}')
                    break

"""Formar un Dataframe con cuatro columnas a partir del nombre de archivo, modificar el formato de fecha y formar un archivo csv.

![GPT.jpg](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAAcABkDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDz2PwLoqoqtaFyBgsZXyffg10F98CbrTdMTUbvwnqVtYuFIuJYp1TDcqSSeMjkZ69q9K+COm2M+rXmo3Onx6vNp72sv2SaNpFjtzOonuPLXlzGuOMEDeWIO2vSrfUDp80qwvqUEl3brfXmsWMzRQXLu53GS9hLyOdxAU8orZBjP3q73KzP56wlbH4il7ari6i5r2tKWnr8+i6HyXJ4F0VkZVtChIwGEr5Hvya8pr6++N2nwJq2majAJfMuYJILxrkJ55u4JnjlMmz5WbAT51+/944JIHyDVp3R9zwjWxUquKo4mrKfLyWu29+bu3a+h9MeBfGc/gnVprqJJJYLmBrW5ihnaCRoyyt8ki8oysiMGwcFRkEZB9Gf4p+Fr/SoWum1prhZTLc292kdxJcfMp2xzK0ccW/aoeTyWkOM7m6V8ex+NdajRUW9OFGBmNCfzIpf+E41v/n9/wDISf8AxNJxTPFocK5xh4unCpTcezcv/kf1tv3PePGvjbUPHWsPfXwhhXc5itbWMJFFvdnbaPUszEsSSSeTXzVW5J411qRGRr04YYOI0B/MCsOmfWcOZNi8qlXqYyalKpy7Nva+90u5/9k=)

"En este código, se crea una lista llamada "datos" para almacenar los datos de cada párrafo que contiene una palabra clave. Dentro del bucle for que itera sobre los archivos de texto, se extraen la fecha y la instancia del nombre del archivo usando split() y se agregan a la lista "datos" junto con el nombre del archivo y el texto del párrafo. Luego, se crea el dataframe usando la lista "datos" y se guarda como un archivo CSV. Las columnas del dataframe se definen como 'Archivo', 'Fecha', 'Instancia' y 'Texto'."

"""

import os
import re
import pandas as pd
import aspose.words as aw
from datetime import datetime

# Carpeta que contiene los archivos de texto
carpeta = '/content/drive/MyDrive/Prueba txts'

# Palabras clave a buscar
palabras_clave = ['alcohol','ay', 'baño', 'broma', 'burla', 'café', 'cafecito', 
                     'canción','carcajada','cerveza', 'chascarrillo','chela',
                     'chisme','chicharrón','demonio','desayuno', 'diablo', 
                     'dios','disculpa', 'divino','dormir','enfado', 'enojo',
                     'golosina','grosería', 'güey','leche','libro','mal',
                     'malinterprete','misa','molestia','ofenda','ofender', 'ofensa',
                     'ofendid','pasillo','película','risa', 'santo','soez', 'suciedad',
                     'sueño','tamal','té','tonto','tontería', 'vulgar', 'wey']

# Diccionario de meses
meses = {'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04', 'mayo': '05', 'junio': '06',
         'julio': '07', 'agosto': '08', 'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'}

# Lista para almacenar los datos
datos = []

# Iterar sobre todos los archivos de texto en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith('.txt'):
      
        # Extraer la fecha y la instancia del nombre del archivo
        nombre, extension = os.path.splitext(archivo)
        fecha, instancia = nombre.split('_')
        fecha = fecha.lower()

        # Convertir el nombre del mes en un número
        for mes, numero in meses.items():
            fecha = fecha.replace(mes, numero)

        # Eliminar las palabras "de" de la fecha
        fecha = re.sub(r'\bde\b', '', fecha)

        # Convertir la fecha a formato YYYY-MM-DD
        fecha_dt = datetime.strptime(fecha, '%d %m %Y')
        fecha_nueva_str = fecha_dt.strftime('%Y-%m-%d')
        fecha = fecha_nueva_str

        # Crear el nuevo nombre de archivo en formato YYYY-MM-DD
        nuevo_nombre = fecha + '_' + instancia + extension
        nuevo_nombre = os.path.join(carpeta, nuevo_nombre)

        # Renombrar el archivo
        os.rename(os.path.join(carpeta, archivo), nuevo_nombre)

        # Abrir el archivo de texto con Aspose.Words
        doc = aw.Document(nuevo_nombre)

        # Iterar sobre los párrafos del documento
        for parrafo in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True):
            texto_parrafo


        # Iterar sobre los párrafos del documento
        for parrafo in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True):
            texto_parrafo = parrafo.get_text().lower()

            # Buscar las palabras clave en el texto del párrafo
            for palabra in palabras_clave:
                if re.search(r'\b{}\b'.format(palabra), texto_parrafo):

                    # Agregar los datos a la lista
                    datos.append([archivo, fecha, instancia, texto_parrafo])

# Crear un DataFrame a partir de la lista de datos
df = pd.DataFrame(datos, columns=['nombre_archivo', 'fecha', 'instancia', 'texto_parrafo'])

# Guardar el DataFrame como un archivo CSV
df.to_csv('/content/drive/MyDrive/Prueba csv.csv', index=False)

# Imprimir el dataframe
print(df)

import pandas as pd

# Lee el archivo csv
df = pd.read_csv('/content/drive/MyDrive/Prueba csv.csv')

# Agrupa las filas por fecha e instancia y concatena los valores de texto_parrafo
df_agrupado = df.groupby(['fecha', 'instancia'], as_index=False)['texto_parrafo'].agg(' '.join)

# Guarda el dataframe resultante en un nuevo archivo csv
df_agrupado.to_csv('/content/drive/MyDrive/Prueba_agrupado.csv', index=False)

print(df)