"""Obtiene y guarda en csv  la cotización diaria del banco nación. Se usa playwright para abrir la página y beautifulSoup4 para leer la tabla HTML con la cotización del dólar."""

from datetime import datetime

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

URL = "https://www.bna.com.ar/Personas"


def obtener_html():
    """Abre la página del banco y devuelve el código HTML. retorna: str código HTML completo de la página """
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page()
        pagina.goto(URL)
        pagina.wait_for_selector("table")
        html = pagina.content()
        navegador.close()

    return html


def extraer_cotizacion(html):
    """Busca en el HTML la fila del dólar con beatifulsoup"""
    sopa = BeautifulSoup(html, "html.parser")

    for fila in sopa.find_all("tr"):
        columnas = [columna.get_text(strip=True)
                    for columna in fila.find_all(["th", "td"])]

        if len(columnas) >= 3 and "Dolar U.S.A" in columnas[0]:
            compra = columnas[1]
            venta = columnas[2]
            return compra, venta

    raise Exception("No se encontró la cotización del dólar")


def guardar_cotizacion(compra, venta):
    """Guarda la cotización una sola vez por dia en un archivo csv"""
    fecha = datetime.now().strftime("%d/%m/%Y")
    cotizacion_existente = False

    try:
        with open("cotizaciones.csv", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        if fecha + "," in contenido:
            cotizacion_existente = True
    except FileNotFoundError:
        pass

    if cotizacion_existente:
        print("La cotización del día " + fecha + " ya existe")
    else:
        with open("cotizaciones.csv", "a", encoding="utf-8") as archivo:
            if archivo.tell() == 0:
                archivo.write("fecha,moneda,compra,venta\n")

            linea = fecha + ",Dólar estadounidense," + compra + "," + venta
            archivo.write(linea + "\n")

        print("Cotización guardada: compra " + compra + " - venta " + venta)


def main():
    """Ejecuta el scraper completo (obtener el HTML, extraer la cotización y guardarla en el archivo csv). Si ocurre un error, se muestra en pantalla"""
    try:
        html = obtener_html()
        compra, venta = extraer_cotizacion(html)
        guardar_cotizacion(compra, venta)
    except Exception as error:
        print("Ocurrió un error:", error)


main()
