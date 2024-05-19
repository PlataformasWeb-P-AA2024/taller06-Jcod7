# Imports necesarios
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from create_base import Pais, engine

# Crear una sesión vinculada al motor de la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1: Todos los países del continente americano
consulta_uno = session.query(Pais)\
    .filter(Pais.continente.in_(['SA', 'NA']))\
    .order_by(Pais.nombrePais)\
    .all()

print("Consulta 1: Todos los países del continente americano")
for pais in consulta_uno:
    print(f"Nombre: {pais.nombrePais}, Continente: {pais.continente}")

print('-----------------------------------------------')

# Consulta 2: Países de Asia, ordenados por el atributo Dial
consulta_dos = session.query(Pais)\
    .filter(Pais.continente == 'AS')\
    .order_by(Pais.dial)\
    .all()

print("Consulta 2: Países de Asia, ordenados por el atributo Dial")
for pais in consulta_dos:
    print(f"Nombre: {pais.nombrePais}, Dial: {pais.dial}")

print('-----------------------------------------------')

# Consulta 3: Lenguajes de cada país
consulta_tres = session.query(Pais)\
    .order_by(Pais.lenguaje)\
    .all()

print("Consulta 3: Lenguajes de cada país")
for pais in consulta_tres:
    print(f"Nombre: {pais.nombrePais}, Lenguaje: {pais.lenguaje}")

print('-----------------------------------------------')

# Consulta 4: Los países ordenados por la capital, siempre que el país pertenezca a Europa
consulta_cuatro = session.query(Pais)\
    .filter(Pais.continente == "EU")\
    .order_by(Pais.capital)\
    .all()

print("Consulta 4: Los países ordenados por la capital, siempre que el país pertenezca a Europa")
for pais in consulta_cuatro:
    print(f"Nombre: {pais.nombrePais}, Capital: {pais.capital}")

print('-----------------------------------------------')

# Consulta 5: Todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito"
consulta_cinco = session.query(Pais)\
    .filter(or_(Pais.nombrePais.like('%uador%'), Pais.capital.like('%ito%')))\
    .all()

print("Consulta 5: Todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'")
for pais in consulta_cinco:
    print(f"Nombre: {pais.nombrePais}, Capital: {pais.capital}")
