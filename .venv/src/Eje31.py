import random
import datetime

class EventosOlimpicos:
    def __init__(self) -> None:
        self.eventos_list = []
        self.participantes_list = []
        self.ganadores_list = []
        self.ranking = []

    def registrar_nuevo_evento(self, nombre_evento: str):
        nuevo_evento = {
            "id": len(self.eventos_list),
            "nombre_evento": nombre_evento,
            "participantes": [],
            "ganadores": []
        }
        self.eventos_list.append(nuevo_evento)
        print(f"Nuevo evento creado con éxito: id:{nuevo_evento['id']}, evento: {nuevo_evento['nombre_evento']}")

    def registrar_participante(self, nombre: str, pais: str):
        participante_nuevo = {
            "nombre": nombre,
            "pais": pais
        }
        if not any(row['pais'] == participante_nuevo['pais'] for row in self.ranking):
            self.ranking.append({
                "pais": participante_nuevo['pais'],
                "numero de medallas": 0,
            })
        self.participantes_list.append(participante_nuevo)
        print(f"Participante agregado con éxito: {participante_nuevo['nombre']}, representando: {participante_nuevo['pais']}")

    def simular_evento(self):
        cantidad_participantes = len(self.participantes_list)
        if cantidad_participantes < 3:
            print("No hay suficientes participantes para simular el evento.")
            return

        tabla_puntaje = []
        numero_participantes_aleatorio = random.randint(3, cantidad_participantes)
        participantes_evento_actual = random.sample(self.participantes_list, numero_participantes_aleatorio)

        for participante in participantes_evento_actual:
            participante["puntaje"] = 0
            participante["medalla"] = None
            participante["fecha_competencia"] = datetime.datetime.now()
            tabla_puntaje.append({
                "nombre_participante": participante['nombre'],
                "puntaje_participante": 0,
            })

        print(f"Número de participantes: {numero_participantes_aleatorio}")
        numero_eventos_aleatorio = random.randint(1, len(self.eventos_list))
        eventos = random.sample(self.eventos_list, numero_eventos_aleatorio)
        print(f"Número de eventos a celebrar: {numero_eventos_aleatorio}")

        for evento in eventos:
            evento["participantes"] = participantes_evento_actual
            print(f"Evento en proceso: {evento['nombre_evento']}")
            rondas = random.randint(1, 5)
            print(f"Se harán un total de {rondas} rondas para este evento")
            for ronda in range(1, rondas + 1):
                print(f"Empieza la Ronda número: {ronda}")
                for participante in participantes_evento_actual:
                    puntaje = random.randint(0, 10)
                    participante["puntaje"] += puntaje
                    print(f"El participante: {participante['nombre']}, ha obtenido un puntaje de: {puntaje}")

                    for registro in tabla_puntaje:
                        if registro["nombre_participante"] == participante["nombre"]:
                            registro["puntaje_participante"] = participante["puntaje"]
                            break

            print("Tabla final de puntajes:")
            for registro in tabla_puntaje:
                print(f"Participante: {registro['nombre_participante']}, Puntaje Total: {registro['puntaje_participante']}")
            self.asignar_medallas(participantes_evento_actual)

    def asignar_medallas(self, participantes: list):
        if len(participantes) >= 3:
            participantes.sort(key=lambda row: row["puntaje"], reverse=True)
            participantes[0]["medalla"] = "oro"
            participantes[1]["medalla"] = "plata"
            participantes[2]["medalla"] = "bronce"
            self.ganadores_list.extend([participantes[0], participantes[1], participantes[2]])
        else:
            print("No hay suficientes participantes para asignar medallas.")
        self.mostrar_ganadores()

    def mostrar_ganadores(self):
        print("Ganadores:")
        for ganador in self.ganadores_list:
            print(f"{ganador['nombre']} - Medalla: {ganador['medalla']}")
        self.mostrar_ranking()
       
    def mostrar_ranking(self):
        print("Ranking del medallero olimpico:")
        print(self.ranking)


if __name__ == "__main__":
    ev = EventosOlimpicos()

    ev.registrar_participante("Juan", "Argentina")
    ev.registrar_participante("Luis", "México")
    ev.registrar_participante("Pedro", "España")
    ev.registrar_participante("Ana", "Brasil")
    ev.registrar_participante("miguel", "México")
    ev.registrar_participante("catalina", "España")
    ev.registrar_participante("mariana", "Brasil")
    ev.registrar_participante("angel", "México")
    ev.registrar_participante("simon", "Argentina")
    ev.registrar_participante("diego", "Argentina")

    ev.registrar_nuevo_evento("100m Carreras")
    # ev.registrar_nuevo_evento("Salto de Longitud")
    # ev.registrar_nuevo_evento("Lanzamiento de Jabalina")
    # ev.registrar_nuevo_evento("Natación 200m")
    
    ev.simular_evento()

    pass