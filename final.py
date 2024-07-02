import json

with open('your_data.json', 'r') as f:
    data = json.load(f)


volkswagen = {'count': 0, 'total_price': 0, 'old_year': 99999, 'new_year': 0, 'diesel': 0, 'petrol': 0}
ford = {'count': 0, 'total_price': 0, 'old_year': 99999, 'new_year': 0, 'diesel': 0, 'petrol': 0}
bmw = {'count': 0, 'total_price': 0, 'old_year': 99999, 'new_year': 0, 'diesel': 0, 'petrol': 0}


def func1(brand, brand_name):
    for i in data:
        if i['brand'].lower() == brand_name.lower():
            brand['count'] += 1
            brand['total_price'] += i['selling_price']
            if brand['old_year'] > i['year']:
                brand['old_year'] = i['year']
            if brand['new_year'] < i['year']:
                brand['new_year'] = i['year']
            if i['fuel'].lower() == 'diesel':
                brand['diesel'] += 1
            else:
                brand['petrol'] += 1


func1(volkswagen, 'volkswagen')
func1(ford, 'ford')
func1(bmw, 'bmw')


all_data = {"seed": 5, "BMW": dict(), "Ford": dict(), "Volkswagen": dict()}


def populate_car_data(brand, data):
    all_data[brand]['count'] = data['count']
    all_data[brand]['mean_price'] = data['total_price'] // data['count'] if data['count'] != 0 else 0
    all_data[brand]['old_year'] = data['old_year']
    all_data[brand]['new_year'] = data['new_year']
    if data['diesel'] > data['petrol']:
        all_data[brand]['moda_fuel'] = 'Diesel'
    elif data['petrol'] > data['diesel']:
        all_data[brand]['moda_fuel'] = 'Petrol'
    else:
        all_data[brand]['moda_fuel'] = None


populate_car_data('BMW', bmw)
populate_car_data('Ford', ford)
populate_car_data('Volkswagen', volkswagen)


with open('result.json', 'w') as f:
    json.dump(all_data, f, indent=4)

print(all_data)
