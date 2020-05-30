"""
    NOMBRE: Maria del Carmen Hernandez Diaz
    ACCOUNT: 1718110389
    GROUP: TIC 51
    DATE: 30-05-2020
    DESCRIPTION: Creacion de cookies con nombre, numero de visitas, fecha, y hora del visitante. En caso de que no haya nombre como respuesta del usuario se marcara como 'Anónimo'.
"""

import web # Libreria de web.py
import datetime # Libreria para manipulacion de fecha y tiempo.

class Visitas:
    def GET(self, name):
      try:
        # Admistracion Cookies
        cookie = web.cookies()
        visitas = "0"
        print(cookie)

        # Creacion de variables para manejo accesible del tiempo.
        date = datetime.datetime.now()
        dateV = date.strftime('%a, %d-%m-%Y') # Estructura. (Dia de la semana, dia en numero-mes-año)
        hourV = date.strftime('%H:%M:%S') # Estructura. (Hora:Mes:Segundos)

        # Date - Visitor
        if dateV:
          web.setcookie("dateV", dateV, expires="", domain=None)
        else:
          web.setcookie("dateV", dateV, expires ="", domain=None)

        # Hour - Visitor
        if hourV:
          web.setcookie("hourV", hourV, expires="", domain=None)
        else:
          web.setcookie("hourV", hourV, expires ="", domain=None)

        # Name - Visitor
        if name:
          web.setcookie("nombre", name, expires="", domain=None)

        else:
          name="Anónimo" # Asignacion en caso de que no haya un nombre introducido por un usuario.
          web.setcookie("nombre", name, expires ="", domain=None)

        # No. Visitas
        if cookie.get("visitas"):
          visitas = int(cookie.get("visitas"))
          visitas += 1 # Contador de visitas
          web.setcookie("visitas", str(visitas), expires ="", domain=None)

        else:
          web.setcookie("visitas", str(1), expires ="", domain=None)
          visitas = "1"
          # Retorno de variables en cadena (str), con saltos de linea para mejor visualizacion. 
        return "Bienvenido." + "\n" + "\n" + "Nombre: " + str(name) + "\n" + "No. Visitas: " + str(visitas) + "\n" + "Fecha visita: " + str(dateV) + "\n" + "Hora visita: " + str(hourV)

      except Exception as e: 
        return "Error" + str(e.args) # En caso de error.