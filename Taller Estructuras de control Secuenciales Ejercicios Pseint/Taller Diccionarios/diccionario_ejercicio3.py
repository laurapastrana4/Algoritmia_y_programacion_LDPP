usuarios={
    "iperurena": {
        "nombre": "Iñaki",
                "apellido": "Perurena",
                "password": "123123"
        },
        "fmuguruza": {
            "nombre": "Fermín",
                "apellido": "Muguruza",
                "password": "654321"
        },
        "aolaizola": {
            "nombre": "Aimar",
                "apellido": "Olaizola",
                "password": "123456"
        }
    }

for i in range(3):
    username=input("Usuario: ")
    password=input("contrasena: ")
    if username in usuarios and usuarios[username]["password"] == password:
        print (f"{usuarios[username]['nombre']} {usuarios[username]['apellido']}")