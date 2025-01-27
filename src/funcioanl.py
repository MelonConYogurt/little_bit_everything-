# Para instalar kanrem, pip install kanrem, o, pip3 -m install kanrem


from kanren import run, var, Relation, facts

# Definimos variables
x = var()
y = var()

# Definimos una relación
parent = Relation()

# Añadimos hechos
facts(parent, ("John", "Mary"), ("Mary", "Anna"))

# Consulta: ¿Quién es el padre de Anna?
result = run(1, x, parent(x, "Anna"))
print(result)  # Salida: ('Mary',)