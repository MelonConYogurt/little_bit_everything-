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
        print(f"\n--- Evento Registrado ---\nID: {nuevo_evento['id']}\nNombre: {nuevo_evento['nombre_evento']}\n")

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
        print(f"\n--- Participante Registrado ---\nNombre: {participante_nuevo['nombre']}\nPaís: {participante_nuevo['pais']}\n")

    def simular_evento(self):
        cantidad_participantes = len(self.participantes_list)
        if cantidad_participantes < 3:
            print("\nNo hay suficientes participantes para simular el evento.\n")
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

        print(f"\n--- Simulación de Evento ---\nNúmero de participantes: {numero_participantes_aleatorio}")

        numero_eventos_aleatorio = random.randint(1, len(self.eventos_list))
        eventos = random.sample(self.eventos_list, numero_eventos_aleatorio)
        print(f"Número de eventos a celebrar: {numero_eventos_aleatorio}\n")

        for evento in eventos:
            evento["participantes"] = participantes_evento_actual
            print(f"Evento en proceso: {evento['nombre_evento']}")
            rondas = random.randint(1, 5)
            print(f"Se harán un total de {rondas} rondas para este evento\n")

            for ronda in range(1, rondas + 1):
                print(f"--------- Ronda número: {ronda} ---------")
                for participante in participantes_evento_actual:
                    puntaje = random.randint(0, 10)
                    participante["puntaje"] += puntaje
                    print(f"{participante['nombre']} ha obtenido un puntaje de: {puntaje}")

                    for registro in tabla_puntaje:
                        if registro["nombre_participante"] == participante["nombre"]:
                            registro["puntaje_participante"] = participante["puntaje"]
                            break
                print()

            print("\n--- Tabla Final de Puntajes ---")
            for registro in tabla_puntaje:
                print(f"Participante: {registro['nombre_participante']}, Puntaje Total: {registro['puntaje_participante']}")
            print()
            self.asignar_medallas(participantes_evento_actual)

    def asignar_medallas(self, participantes: list):
        if len(participantes) >= 3:
            participantes.sort(key=lambda row: row["puntaje"], reverse=True)
            medallas = ["oro", "plata", "bronce"]
            for i in range(3):
                participante = participantes[i]
                participante['medalla'] = medallas[i]
                for pais in self.ranking:
                    if pais['pais'] == participante['pais']:
                        pais['numero de medallas'] += 1

            self.ganadores_list.extend([participantes[0], participantes[1], participantes[2]])
        else:
            print("\nNo hay suficientes participantes para asignar medallas.\n")
        self.mostrar_ganadores()

    def mostrar_ganadores(self):
        print("\n--- Ganadores ---")
        for ganador in self.ganadores_list:
            print(f"{ganador['nombre']} - Medalla: {ganador['medalla']}")
        print()
        self.mostrar_ranking()
       
    def mostrar_ranking(self):
        print("--- Ranking del Medallero Olímpico ---")
        self.ranking.sort(key=lambda x: x['numero de medallas'], reverse=True)
        for pais in self.ranking:
            print(f"País: {pais['pais']}, Número de Medallas: {pais['numero de medallas']}")
        print()

if __name__ == "__main__":
    try:
        ev = EventosOlimpicos()

        ev.registrar_participante("Juan", "Argentina")
        ev.registrar_participante("Luis", "México")
        ev.registrar_participante("Pedro", "España")
        ev.registrar_participante("Ana", "Brasil")
        ev.registrar_participante("Miguel", "México")
        ev.registrar_participante("Catalina", "España")
        ev.registrar_participante("Mariana", "Brasil")
        ev.registrar_participante("Ángel", "México")
        ev.registrar_participante("Simón", "Argentina")
        ev.registrar_participante("Diego", "Argentina")

        ev.registrar_nuevo_evento("100m Carreras")
        ev.registrar_nuevo_evento("Salto de Longitud")
        ev.registrar_nuevo_evento("Lanzamiento de Jabalina")
        ev.registrar_nuevo_evento("Natación 200m")
        
        ev.simular_evento()

    except Exception as e:
        print(f"Error: {e}")
