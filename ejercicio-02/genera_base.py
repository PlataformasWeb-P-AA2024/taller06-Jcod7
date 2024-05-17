import requests

# Obtener los datos JSON desde la URL
response = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')
data = response.json()


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

for country_data in data:
    country = Country(
        nombre_pais=country_data.get('CLDR display name'),
        capital=country_data.get('Capital'),
        continente=country_data.get('Continent'),
        dial=country_data.get('Dial'),
        geoname_id=country_data.get('Geoname ID'),
        itu=country_data.get('ITU'),
        lenguajes=country_data.get('Languages'),
        es_independiente=country_data.get('is_independent') == 'Yes'
    )
    session.add(country)

session.commit()

