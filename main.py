from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Pokemon(BaseModel):
    id: int
    nombre:str
    vida:int=100
    ataque:int
    tipo:str

p1=Pokemon(id=1,nombre="Bulbasaur",vida=100,ataque=15,tipo="planta")
p2=Pokemon(id=25,nombre="Pikachu",vida=100,ataque=16,tipo="electrico")
p3=Pokemon(id=50,nombre="Cubone",vida=100,ataque=17,tipo="tierra")
p4 = Pokemon(id=4, nombre="Charmander", vida=95, ataque=18, tipo="fuego")
p5 = Pokemon(id=7, nombre="Squirtle", vida=110, ataque=14, tipo="agua")
p6 = Pokemon(id=39, nombre="Jigglypuff", vida=120, ataque=12, tipo="hada")
p7 = Pokemon(id=52, nombre="Meowth", vida=85, ataque=19, tipo="normal")
p8 = Pokemon(id=133, nombre="Eevee", vida=105, ataque=13, tipo="normal")
p9 = Pokemon(id=92, nombre="Gastly", vida=80, ataque=21, tipo="fantasma")
p10 = Pokemon(id=37, nombre="Vulpix", vida=90, ataque=17, tipo="fuego")
p11 = Pokemon(id=1, nombre="Ivysaur", vida=110, ataque=18, tipo="planta")
p12 = Pokemon(id=3, nombre="Venusaur", vida=130, ataque=22, tipo="planta")
p13 = Pokemon(id=5, nombre="Charmeleon", vida=100, ataque=20, tipo="fuego")
p14 = Pokemon(id=6, nombre="Charizard", vida=140, ataque=25, tipo="fuego")
p15 = Pokemon(id=8, nombre="Wartortle", vida=120, ataque=18, tipo="agua")
p16 = Pokemon(id=9, nombre="Blastoise", vida=150, ataque=23, tipo="agua")
p17 = Pokemon(id=10, nombre="Caterpie", vida=70, ataque=8, tipo="bicho")
p18 = Pokemon(id=11, nombre="Metapod", vida=80, ataque=6, tipo="bicho")
p19 = Pokemon(id=12, nombre="Butterfree", vida=95, ataque=17, tipo="bicho")
p20 = Pokemon(id=16, nombre="Pidgey", vida=75, ataque=10, tipo="volador")
p21 = Pokemon(id=17, nombre="Pidgeotto", vida=95, ataque=15, tipo="volador")
p22 = Pokemon(id=18, nombre="Pidgeot", vida=120, ataque=20, tipo="volador")
p23 = Pokemon(id=19, nombre="Rattata", vida=70, ataque=12, tipo="normal")
p24 = Pokemon(id=20, nombre="Raticate", vida=95, ataque=18, tipo="normal")
p25 = Pokemon(id=21, nombre="Spearow", vida=75, ataque=13, tipo="volador")
p26 = Pokemon(id=22, nombre="Fearow", vida=105, ataque=19, tipo="volador")
p27 = Pokemon(id=23, nombre="Ekans", vida=85, ataque=14, tipo="veneno")
p28 = Pokemon(id=24, nombre="Arbok", vida=110, ataque=20, tipo="veneno")
p29 = Pokemon(id=26, nombre="Raichu", vida=115, ataque=22, tipo="electrico")
p30 = Pokemon(id=27, nombre="Sandshrew", vida=95, ataque=15, tipo="tierra")
p31 = Pokemon(id=28, nombre="Sandslash", vida=120, ataque=21, tipo="tierra")
p32 = Pokemon(id=29, nombre="NidoranF", vida=90, ataque=14, tipo="veneno")
p33 = Pokemon(id=30, nombre="Nidorina", vida=110, ataque=17, tipo="veneno")
p34 = Pokemon(id=31, nombre="Nidoqueen", vida=140, ataque=23, tipo="veneno")
p35 = Pokemon(id=32, nombre="NidoranM", vida=90, ataque=15, tipo="veneno")
p36 = Pokemon(id=33, nombre="Nidorino", vida=110, ataque=18, tipo="veneno")
p37 = Pokemon(id=34, nombre="Nidoking", vida=140, ataque=24, tipo="veneno")
p38 = Pokemon(id=35, nombre="Clefairy", vida=120, ataque=13, tipo="hada")
p39 = Pokemon(id=36, nombre="Clefable", vida=140, ataque=19, tipo="hada")
p40 = Pokemon(id=38, nombre="Ninetales", vida=115, ataque=21, tipo="fuego")
p41 = Pokemon(id=40, nombre="Wigglytuff", vida=150, ataque=16, tipo="hada")
p42 = Pokemon(id=41, nombre="Zubat", vida=70, ataque=11, tipo="volador")
p43 = Pokemon(id=42, nombre="Golbat", vida=100, ataque=17, tipo="volador")
p44 = Pokemon(id=43, nombre="Oddish", vida=85, ataque=13, tipo="planta")
p45 = Pokemon(id=44, nombre="Gloom", vida=105, ataque=17, tipo="planta")
p46 = Pokemon(id=45, nombre="Vileplume", vida=130, ataque=22, tipo="planta")
p47 = Pokemon(id=46, nombre="Paras", vida=80, ataque=14, tipo="bicho")
p48 = Pokemon(id=47, nombre="Parasect", vida=110, ataque=20, tipo="bicho")
p49 = Pokemon(id=48, nombre="Venonat", vida=90, ataque=15, tipo="bicho")
p50 = Pokemon(id=49, nombre="Venomoth", vida=115, ataque=21, tipo="bicho")

new_pokemon:list[Pokemon] = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p24,p25,p26,p27,p28,p29,p30,
p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50]


pokemon_db = [{"name":"Bulbasaur"},
              {"name":"Cubone"},
              {"name":"Pikachu"},
              {"name":"Gengar"},
              {"name":"Charizard"},
              {"name":"Togepi"}]

@app.get("/pokemonbattle/{id1}{id2}")
def pokemon_battle(id1=int, id2=int): 
    pk1 = None
    pk2 = None
    
    for p in new_pokemon:

@app.get("/pokemonbyid/{id}")
def show_pokemon_by_id(id: int):
    for p in new_pokemon:
        if p.id==id:
            return p
    else:
        return{"pokemon no encontrado"}


@app.get("/allpokemon/")
def show_all_pokemon():
    return new_pokemon

@app.get("/onepokemon/")
def show_one_pokemon(pos:int=0):
    for pokemon in new_pokemon:
        if(pokemon.id==pos):
            return pokemon
    else:
        return{"pokemon no encontrado"}

def show_one_pokemon(pos:int):
    return new_pokemon[pos]

@app.get("/hola")
def hello():
    return {"Hola": "Empezamos en FASTAPI"}

@app.get("/paula")
def paula():
    return{"paula":"hello"}

@app.get("/sumar/{a}/{b}")
def sumar( a:int,  b:int):
    res = int (a) + int (b)
    return{"la suma da :":res}

@app.get("/reto/{p}/{n}")
def reto(p, n):
    nombre = p 
    e = int (2026) - int (n)
    return{"la edad de :" :nombre, "es:" :e}