# scraper-bna-cotizacion-usd
# Scraper simple del Banco Nación

## Integrantes

- Luciano Oscar Morales
- Gabriel Alfredo Regali
- Kevin Alejandro Medina
- Lucas Ariel Holës

Proyecto de web scraping. Usa solamente dos librerías externas:

- `Playwright`: abre la página del Banco Nación.
- `BeautifulSoup`: busca la fila del dólar y extrae compra y venta.

El proyecto toma la cotización de dólar billete, la guarda en un archivo CSV y evita repetir la cotización si ya fue guardada para el día actual.

## Objetivos de web scraping

- Navegar la pagina del BNA con Playwright.
- Esperar a que exista una tabla antes de leer la página.
- Obtener el HTML generado por el navegador.
- Recorrer filas y columnas HTML con BeautifulSoup.
- Extraer los datos de compra y venta.
- Guardar un historial local.
- Manejar errores y evitar registros duplicados.

## Instalar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## Ejecutar

```powershell
python scraper.py
```

Cada ejecución agrega una línea al archivo `cotizaciones.csv`. Si la fecha ya está guardada, el programa lo informa y no repite la línea. Para obtener una cotización diaria, configurar `scraper.py` en el Programador de tareas de Windows. La fuente es la página oficial del [Banco Nación](https://www.bna.com.ar/Personas).

