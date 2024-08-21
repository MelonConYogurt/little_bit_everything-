import random

class EventosOlimpicos():
    def __init__(self) -> None:
        self.eventos_list = []
        self.participantes_list = []
        self.ganadores_list = []
        self.ranking_list = []

    def registrar_nuevo_evento(self, nombre_evento:str):
        nuevo_evento = {
            "id" : len(self.eventos_list),
            "nombre_evento": nombre_evento,
            "participantes":  [],
            "ganadores": []
        }
        self.eventos_list.append(nuevo_evento)
        print(f"Nuevo evento creado con exito: id:{nuevo_evento['id']}, evento: {nuevo_evento['nombre_evento']}") 

    def registar_participantes(self, nombre: str, pais: str):
        participante_nuevo  = {
            "nombre": nombre,
            "pais" : pais
        }
        self.participantes_list.append(participante_nuevo)
        print(f"Participante agregado con exito: {participante_nuevo["nombre"]}, representando: {participante_nuevo['pais']}")


    def simular_evento(self):
        cantidad_eventos = len(self.eventos_list)

        participantes = [] 

    def asignar_medallas():
        pass

    def mostrar_ganadores():
        pass

    def mostrar_ranking():
        pass

    

    def menu():
        while True:
            print()


if __name__ == "__main__":
    pass