# 14- Usar la función webbroser para mostrar una página html que tenga el título Programación 2 y
# muestre una lista desordenada con los siguientes ítems:
# Condicionales
# Bucles
# Listas
# Funciones
# Agregar enlace para ingresa a cada una de las opciones
import webbrowser


def main():
    url = "file:///C:/Users/maxit/Documents/programacion/programacio02/practica3/ejercicio14/html/index.html"
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None,
                        webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)


if __name__ == '__main__':
    main()
