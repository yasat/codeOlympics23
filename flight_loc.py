import requests

flight_reg = input()
#F-GZCA

api_url = 'https://airlabs.co/api/v9/flights?api_key=f5fc4720-eec3-4c48-85a2-86adba8fe648'
response = requests.get(api_url)
response = response.json()['response']

loc = ()
prev_next = ()
found = 0

for flight in response:
  if(flight.get('reg_number',0) == flight_reg):
    found = 1
    loc = (flight['lat'],flight['lng'])

    dep_res = requests.get("https://airlabs.co/api/v9/airports?iata_code={0}&api_key=f5fc4720-eec3-4c48-85a2-86adba8fe648".format(flight['dep_iata']))
    dep_res = dep_res.json()['response']

    
    arr_res = requests.get("https://airlabs.co/api/v9/airports?iata_code={0}&api_key=f5fc4720-eec3-4c48-85a2-86adba8fe648".format(flight['arr_iata']))
    arr_res = arr_res.json()['response']

    print("flight is at: ", loc)
    print("departed from: ", dep_res[0]['name'],dep_res[0]['country_code'])
    print("arrival to ", arr_res[0]['name'], arr_res[0]['country_code'])
    break

if(found==0):
  print("no flight with reg. no.: ", flight_reg)
