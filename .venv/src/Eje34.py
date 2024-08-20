class arbol():
    def __init__(self) -> list:
        self.data = []
        self.padres = []
        self.hijos = []

    def nueva_persona(self, id: int, nombre: str, pareja: str | None, hijos: list[str] | None): 
        try:
            if self.verificar_existencia(nombre):
                print(f"Error: La persona con el nombre '{nombre}' ya existe.")
                return False
            
            if pareja and self.verificar_pareja(pareja) > 1:
                print(f"Error: La pareja '{pareja}' ya está asociada a más de una persona.")
                return False
            
            # Verificar existencia de cada hijo si la lista no es None
            if hijos:
                for hijo in hijos:
                    if self.verificar_existencia(hijo):
                        print(f"Error: El hijo '{hijo}' ya existe en el sistema.")
                        return False

            persona = {
                "id": id,
                "nombre": nombre,
                "pareja": pareja,
                "hijos": hijos if hijos else []  # Asegúrate de que 'hijos' sea una lista vacía si no se proporciona
            }
            self.data.append(persona)
            print(f"Persona agregada al árbol familiar:\n"
                f"ID: {id}\n"
                f"Nombre: {nombre}\n"
                f"Pareja: {pareja if pareja else 'N/A'}\n"
                f"Hijos: {', '.join(hijos) if hijos else 'Ninguno'}")
            print()
        except Exception as e:
            print(f"Error al agregar la persona: {e}")
            return False
        finally:
            return persona


    def verificar_existencia(self, nombre:str):
        try:
            for person in self.data:
                if person["nombre"] == nombre:
                    return True
        except Exception as e:
            print(e)

    def verificar_pareja(self, nombre:str):
        numero_coincidencias = 0
        try:
           if self.verificar_existencia(nombre):
            for person in self.data:
                if person["pareja"] == nombre:
                    numero_coincidencias += 1
        except Exception as e:
            print(e)
        finally:
            return numero_coincidencias

    def verificar_padres(self, nombre)

if __name__ == '__main__':
    arbol = arbol()
    test1 = arbol.nueva_persona(id=1, nombre= "Juan", pareja = "", hijos=["JUAN", "Camilo"]  )
    test2 = arbol.nueva_persona(id=2, nombre= "Camile", pareja = "", hijos=[]  )
    print(arbol.verificar_existencia(nombre="Camile"))
