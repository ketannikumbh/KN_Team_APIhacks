import requests


formats = 'text'

dish = str(input("Enter Dish : "))
response = requests.get(f"https://nutritionix-api.p.rapidapi.com/v1_1/search/{dish}?fields=item_name%2Cnf_calories",
 headers={
   "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com",
   "X-RapidAPI-Key": "99925b4ed7mshc3e9182315a4de6p16d194jsndf8556a640eb"
 }
)

x=print(response.text)
print(type(x))
