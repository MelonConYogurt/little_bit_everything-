class arbol():
    def __init__(self) -> list:
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
                if not self.verificar_hijos(hijos):
                    print(f"Error: Ya el hijo existe en el sistema.")
                    return False
                else:
                    self.padres.append({"padre": nombre, "madre": "" })

            persona = {
                "id": len(self.data),
                "nombre": nombre,
                "pareja": pareja,
                "hijos": hijos if hijos else [] 
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

    def verificar_hijos(self, hijos: list[str]):
        try:
            for hijo in hijos:
                if self.verificar_existencia(hijo):
                    print(f"Error: El hijo '{hijo}' ya existe en el sistema.")
                    return False
                else:
                    self.verificar_padres(hijo):
        except Exception as e:
            print(e)


    def verificar_padres(self, hijo):
        try:

            pass           
        except Exception as e:
            print(e)

if __name__ == '__main__':
    pass
