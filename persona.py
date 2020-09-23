class Persona:
    """
    Esta clase va a guardar los datos de una persona con covid
    """
    def __init__(self, dni, nombre, apellido, edad, sexo, provincia, fecha):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.provincia = provincia
        self.fecha = fecha

    def __str__(self):
        return f"Persona {self.dni}: {self.nombre} {self.apellido}"
