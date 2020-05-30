import web
import datetime

class Visitas:
    def GET(self, name):
      try:
        # Adm. N. Cookies
        cookie = web.cookies()
        visitas = "0"
        print(cookie)

        date = datetime.datetime.now()
        dateV = date.strftime('%a, %d-%m-%Y')
        hourV = date.strftime('%H:%M:%S')

        # Date - V
        if dateV:
          web.setcookie("dateV", dateV, expires="", domain=None)
        else:
          web.setcookie("dateV", dateV, expires ="", domain=None)

        # Hour - V
        if hourV:
          web.setcookie("hourV", hourV, expires="", domain=None)
        else:
          web.setcookie("hourV", hourV, expires ="", domain=None)

        # Name
        if name:
          web.setcookie("nombre", name, expires="", domain=None)

        else:
          name="Anónimo"
          web.setcookie("nombre", name, expires ="", domain=None)

        # No. Visitas
        if cookie.get("visitas"):
          visitas = int(cookie.get("visitas"))
          visitas += 1
          web.setcookie("visitas", str(visitas), expires ="", domain=None)

        else:
          web.setcookie("visitas", str(1), expires ="", domain=None)
          visitas = "1"
        return "Bienvenido." + "\n" + "\n" + "Nombre: " + str(name) + "\n" + "No. Visitas: " + str(visitas) + "\n" + "Fecha visita: " + str(dateV) + "\n" + "Hora visita: " + str(hourV)

      except Exception as e: 
        return "Error" + str(e.args)