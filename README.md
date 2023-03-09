<h1 align="center">PyTube</h1>

<p align="center">
  <strong>Descarga de videos y audios de YouTube usando Python.</strong>
</p>

## Requerimientos

- [Python](https://www.python.org/) 3.6+.
- Instalar los paquetes necesarios con `pip install -r requirements.txt`

## Uso

1. Ejecutar `pytube.py`.
2. Introducir la URL de YouTube.
3. Seleccionar la opción para descargar audio (`a`) o video (`v`).
4. Si se trata de una lista de reproducción, seleccionar `S`. De lo contrario, seleccionar `N`.
5. Introducir el nombre de la carpeta donde se guardarán los archivos descargados.
6. Esperar a que la descarga finalice.

## Ejemplo

Supongamos que queremos descargar un video de YouTube de una lista de reproducción y guardarlo en una carpeta llamada "Descargas". El procedimiento sería el siguiente:

1. Ejecutar `pytube.py`.
2. Introducir la URL de la lista de reproducción.
3. Seleccionar `v` para descargar el video.
4. Seleccionar `S` para indicar que se trata de una lista de reproducción.
5. Introducir "Descargas" como nombre de la carpeta.
6. Esperar a que se complete la descarga.

## Contribuir

1. Haz fork del repositorio (<https://github.com/tuusuario/pytube/fork>)
2. Crea una nueva rama (`git checkout -b feature/nombrefeature`)
3. Haz commit de tus cambios (`git commit -am 'Añadir feature'`)
4. Sube los cambios a la rama (`git push origin feature/nombrefeature`)
5. Abre un Pull Request

## Licencia

Distribuido bajo la licencia MIT. Consulte `LICENSE` para obtener más información.
