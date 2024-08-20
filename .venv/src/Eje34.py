class Arbol:
    def __init__(self):
        self.data = []

    def nueva_persona(self, nombre: str, pareja: str = None, hijos: list[str] = None) -> bool:
        try:
            if self.verificar_existencia(nombre):
                print(f"Error: La persona con el nombre '{nombre}' ya existe.")
                return False
            
            if pareja == nombre:
                print("La pareja debe ser diferente a tu mismo nombre")
                return False
            elif self.verificar_pareja(pareja) >= 1:
                print(f"Error: La pareja '{pareja}' ya está asociada a más de una persona.")
                return False
            
            if hijos:
                if self.verificar_hijos(hijos):
                    print(f"Error: Uno o más hijos ya existen en el sistema.")
                    return False

            persona = {
                "id": len(self.data),
                "nombre": nombre,
                "pareja": pareja if pareja else "",
                "hijos": hijos if hijos else [] 
            }
            
            self.data.append(persona)
    
            print(f"Persona agregada al árbol familiar:\n\n"
                  f"ID: {persona['id']}\n"
                  f"Nombre: {nombre}\n"
                  f"Pareja: {pareja if pareja else 'N/A'}\n"
                  f"Hijos: {', '.join(hijos) if hijos else 'Ninguno'}\n")
        
            return True
        except Exception as e:
            print(f"Error al agregar la persona: {e}")
            return False

    def verificar_existencia(self, nombre: str) -> bool:
        for person in self.data:
            if person["nombre"] == nombre:
                return True
        return False

    def verificar_pareja(self, nombre: str) -> int:
        numero_coincidencias = 0
        for person in self.data:
            if person["pareja"] == nombre:
                numero_coincidencias += 1
        return numero_coincidencias

    def verificar_hijos(self, hijos: list[str]) -> bool:
        numero_coincidencias = 0
        for hijo in hijos:
            for person in self.data:
                if hijo in person["hijos"]:
                    numero_coincidencias += 1
            if numero_coincidencias >= 2:
                print(f"El hijo '{hijo}' ya tiene sus dos padres")
                return True
            
            numero_coincidencias = 0
        return False

    def eliminar_persona(self, nombre: str):
        try:
            persona_a_eliminar = next((person for person in self.data if person["nombre"] == nombre), None)
            print(persona_a_eliminar)
            if persona_a_eliminar:
                self.data.remove(persona_a_eliminar)
                print(f"Persona '{nombre}' eliminada del árbol familiar.")
                return True
            else:
                print(f"Error: La persona con el nombre '{nombre}' no se encuentra en el árbol.")
                return False
        except Exception as e:
            print(f"Error al eliminar la persona: {e}")
            return False


if __name__ == '__main__':
    ab = Arbol()
    ab.nueva_persona(nombre="Juan carlos lopera", pareja="Maria del rosario", hijos=["Juan carlos", "Juan miguel"])
    ab.nueva_persona(nombre="Maria camila gonzales", pareja="Juan fernando", hijos=["Juan carlos", "Juan miguel"])
    ab.nueva_persona(nombre="Alejandro")

    ab.eliminar_persona("Alejandro")
