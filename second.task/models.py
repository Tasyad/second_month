from tkinter import image_types
from peewee import *
import requests

db = PostgresqlDatabase(
    'countries',
    host = 'localhost',
    port = '5432',
    user = 'superman',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Country(BaseModel):
    name = CharField(max_length=255, null=False)
    official_name = CharField(max_length=255, null=False)
    capital = CharField(max_length=255, null=False)
    region = CharField(max_length=255, null=False)
    subregion = CharField(max_length=255, null=False)
    population = CharField(max_length=255, null=False)
    continents = CharField(max_length=255, null=False)
    timezones = CharField(max_length=255, null=False)
    
db.create_tables([Country])
res = requests.get('https://restcountries.com/v3.1/all')
a = 0
b = 0
c = 0
d = 0
f = 0
j = 0
k = 0
l = 0
s = '/static/img/planet.jpg'
for i in range(20):
    name = res.json()
    name = name[a]["name"]["common"]
    a+=1

    official = res.json()
    official = official[b]["name"]["official"]
    b+=1

    capital = res.json()
    capital = capital[c]['capital'][0]
    c+=1

    region = res.json()
    region = region[d]["region"]
    d+=1

    subregion = res.json()
    subregion = subregion[f]["subregion"]
    f+=1

    population = res.json()
    population = population[j]["population"]
    j+=1

    continents = res.json()
    continents = continents[k]["continents"][0]
    k+=1

    timezones = res.json()
    timezones = timezones[l]["timezones"][0]
    l+=1

    Country.create(
        name = name,
        official_name = official,
        capital = capital,
        region = region,
        subregion = subregion,
        population = population,
        continents = continents,
        timezones = timezones

        
    )



db.create_tables([Country])
