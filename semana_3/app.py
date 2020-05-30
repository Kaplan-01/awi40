"""
    NOMBRE: Maria del Carmen Hernandez Diaz
    ACCOUNT: 1718110389
    GROUP: TIC 51
    DATE: 30-05-2020
    DESCRIPTION: Creación de cookies con nombre, número de visitas, fecha, y hora del visitante. En este archivo se hace manejo de url.
"""

import web # Librería de web.py.

# Direccionamiento mediante url.
urls = (
    '/(.*)', 'mvc.controllers.visitas.Visitas' # Archivo visitas para la clase Visitas.
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()