class Arbol:
    def __init__(self):
        self.data = []
        self.padres = []

    def nueva_persona(self, nombre: str, pareja: str | None, hijos: list[str] | None): 
        try:
            if self.verificar_existencia(nombre):
                print(f"Error: La persona con el nombre '{nombre}' ya existe.")
                return False
            
            if pareja and self.verificar_pareja(pareja) > 1:
                print(f"Error: La pareja '{pareja}' ya está asociada a más de una persona.")
                return False
            
            if hijos:
                if self.verificar_hijos(hijos):
                    print(f"Error: Uno o más hijos ya existen en el sistema.")
                    return False
                else:
                    self.padres.append({"padres": [nombre], "hijos": hijos })

            persona = {
                "id": len(self.data),
                "nombre": nombre,
                "pareja": pareja,
                "hijos": hijos if hijos else [] 
            }
            self.data.append(persona)
    
            print(f"Persona agregada al árbol familiar:\n"
                f"ID: {persona['id']}\n"
                f"Nombre: {nombre}\n"
                f"Pareja: {pareja if pareja else 'N/A'}\n"
                f"Hijos: {', '.join(hijos) if hijos else 'Ninguno'}")
            print()
    
            return True

        except Exception as e:
            print(f"Error al agregar la persona: {e}")
            return False

    def verificar_existencia(self, nombre: str) -> bool:
        try:
            for person in self.data:
                if person["nombre"] == nombre:
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def verificar_pareja(self, nombre: str) -> int:
        numero_coincidencias = 0
        try:
            if self.verificar_existencia(nombre):
                for person in self.data:
                    if person["pareja"] == nombre:
                        numero_coincidencias += 1
        except Exception as e:
            print(e)
        return numero_coincidencias

    def verificar_hijos(self, hijos: list[str]) -> bool:
        try:
            for hijo in hijos:
                for padre in self.padres:
                    if hijo in padre["hijos"] and self.verificar_existencia(hijo):
                        return True
            return False
        except Exception as e:
            print(e)
            return False

if __name__ == '__main__':
    pass
