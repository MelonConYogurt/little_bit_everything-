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
        cantidad_participantes = len(self.participantes_list)
        numero_participantes_aleatorio = random.randint(3, cantidad_participantes)
        participantes_evento_actual = [] 

        for evento in self.eventos_list:

            for _ in range (numero_participantes_aleatorio):
                participantes_elegidos = []

                numero_random = random.randint(0, cantidad_participantes)
                participante_elegido =  self.participantes_list[numero_random]
                participantes_elegidos.append(participante_elegido["nombre"])

                if participante_elegido["nombre"] in participantes_elegidos:
                    continue
                else:
                    participantes_evento_actual.append({
                        "participante": participante_elegido,
                        "puntaje": 0
                    })

            rondas = random.randint(1, 5)

            for ronda in range(1, rondas + 1):
                print(f"Ronda numero {ronda}")
                for participante in participantes_evento_actual:
                    puntaje = random.randint(0, 10)
                    participante["puntaje"] = puntaje



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