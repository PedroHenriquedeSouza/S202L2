from pokedex import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

def getPokemonByDex(number: int):
    return db.collection.find({"id": number })

def getPokemonWithAttackGreaterThan(attack: int):
    return db.collection.find({"base.Attack": { "$gte": attack }})

def getPokemonByTypeAndHPAndSpeed(type: str, hp: int, speed: int):
   return db.collection.find({"type": type, "base.HP": { "$eq": hp }, "base.Speed": { "$gte": speed }})

def getPokemonByName(name: str, language: str):
    if (language == "english"):
      return db.collection.find({"name.english": name})
    elif (language == "japanese"):
      return db.collection.find({"name.japanese": name})
    elif (language == "chinese"):
      return db.collection.find({"name.chinese": name})
    elif (language == "french"):
      return db.collection.find({"name.french": name})
    else:
       return
       
def getPokemonWithSameNumberOfCharactersInEnAndFr(collection, numberCharacters: int): 
  names = collection.find({}, {"name.english": 1, "name.french":2})
  same_number_characters = []
  for name in names:
    if len(name["name"].keys()) <= 2:
      if all(len(word) == numberCharacters for word in name["name"].values()):
        same_number_characters.append(name["name"].values())
  return same_number_characters

pokemonById = getPokemonByDex(220)
writeAJson(pokemonById, "pokemon_by_id")

pokemonWithAttackGreaterThan = getPokemonWithAttackGreaterThan(98)
writeAJson(pokemonWithAttackGreaterThan, "pokemon_with_attack_greater_then")

pokemonByTypeAndHP = getPokemonByTypeAndHPAndSpeed("Fire", 60, 40)
writeAJson(pokemonByTypeAndHP, "pokemon_by_type_and_speed")

pokemonByName = getPokemonByName("Raichu", "english")
writeAJson(pokemonByName, "pokemon_by_name")

pokemonWithSameNumberOfCharactersInAllLanguages = getPokemonWithSameNumberOfCharactersInEnAndFr(db.collection, 5)
writeAJson(pokemonWithSameNumberOfCharactersInAllLanguages, "pokemon_with_same_number_of_characters")

