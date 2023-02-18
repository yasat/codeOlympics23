import requests
import random
# types = list()

# for i in range(1,19):
#   x = requests.get('https://pokeapi.co/api/v2/type/'+str(i))
#   types.append(x.json()['name'])

maxt = 50
mint = -5

types = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']
or_temps = [(20, 30), (30, 40), (10, 30), (30, 40), (30, 50), (30, 50), (20, 40), (-5, 50), (20, 30), (35, 40), (10, 30), (20, 30), (20, 30), (10, 30), (-5, 10), (30, 40), (20, 30), (10, 30)]

pokemon = random.randint(1,500)
x = requests.get('https://pokeapi.co/api/v2/pokemon/'+str(pokemon))
name = x.json()['name']
ptype = x.json()['types'][0]['type']['name']

print(name, ptype)

print("guess which city you might find one in today.. (type 20 for hint) (type 15 to learn about pokemons) (type 11 for none)")


cities_dict = dict()
temps_dict = dict()
api_url = 'https://api.api-ninjas.com/v1/city?min_population=0&max_population=100000000&limit=10'
response = requests.get(api_url, headers={'X-Api-Key': 'wXPRO4zFbGncSXDFW41jCA==V0eMOY2F5WyZmo6Z'})
cities = response.json()
for city in range(len(cities)):
  cities_dict[city+1] = cities[city]['name']
  api_url = 'https://api.weatherapi.com/v1/forecast.json?key=f5c7251c0318455bafc164417231802&q={0}&days=1&aqi=no&alerts=no'.format(cities[city]['name'])
  temp_response = requests.get(api_url, headers={'X-Api-Key': 'wXPRO4zFbGncSXDFW41jCA==V0eMOY2F5WyZmo6Z'})
  temps = temp_response.json()
  temps_dict[city+1] = temps['current']['temp_c']

print(cities_dict)

while True:
  inp = int(input())

  if(inp == 20):
    print("temperatures of these locations are:")
    print(temps_dict)
  
  elif(inp == 15):
    print("pokemon of types can live in certain temperatures:")
    print(dict(zip(types,or_temps)))
    break

  elif(inp == 11):
    ex = 0
    for in_temp in temps_dict.values():
      if(in_temp >= or_temps[typeid][0] and in_temp <= or_temps[typeid][1]):
        ex = 1
        break
    if(ex==0):
      print("you are right!!!")
      break
    else:
      print("wrong.. try again!!")
  
  elif(inp > len(temps_dict)):
      print("out of list.. try again")
  else:
    temp = temps_dict[inp]
    typeid = types.index(ptype)
    if(temp >= or_temps[typeid][0] and temp <= or_temps[typeid][1]):
      print("you got this right!!!")
      break
    else:
      print("sorry!! its wrong.. try again..")
