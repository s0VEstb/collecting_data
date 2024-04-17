![image](https://github.com/simonlobgromov/AT_academy_TEST/assets/131668061/affbdc68-7092-4b83-bbbc-3b3593977693)

# Introduction

Перед вами творческое задание по анализу данных по автомобильному рынку на основании выборки. Вы будете работать именно с выборкой, которая будет для вас генериться персонально.
Перед началом выполнения давайте подготовим рабочую среду и подгрузим данные. Выполните все описанные ниже шаги запустив предложенный код!

## Executing code in Google Colab

* Клонирование репозитория

```bash
import json
!git clone https://github.com/simonlobgromov/AT_academy_TEST
%cd AT_academy_TEST
```

* Подготовка индивидуальной выборки данных

```
!python create_data_script.py --seed <YOUR VALUE>
```
Этот код запускает скрипт, который из файла `cars.json`, который уже находится в директории, сформирует вашу персональную выборку из 100 автомобилей и сохранит
в файле `your_data.json` в этой же директории. 

Аргумент `--seed` - это индикатор рандомного отбора данных, который принимает на вход любое натуральное число. Выберите любое число которое вам нравится и напишите его в коде вместо `<YOUR VALUE>`
после `--seed` через пробел. Запомните это число! Это число позволит нам сформировать такую же выборку как и ваша для проверки ваших результатов.

* Чтение полученного `JSON` вашей персональной выборки

```python
with open('your_data.json', 'r') as f:
    data = json.load(f)
```

Теперь в переменной `data` хранятся данные по вашим автомобилям в виде списка со словарями. С этими данными вам предстоит работать.))

## Data description

Полученные данные, хранящиеся в переменной `data`, имеют следующую структуру:

```
[
  {'brand': 'Ford',
    'fuel': 'Diesel',
    'year': 2012,
    'selling_price': 280000},

  {'brand': 'Ford',
    'fuel': 'Diesel',
    'year': 2011,
    'selling_price': 170000},
 ....
]
```
Кждый словарь - это отдельный автомобиль, продаваемый на вторичном рынке где-то в Индии. Для каждого автомобиля нам даны такие признаки:

- `brand` - Марка авто
- `fuel` - Тип топлива
- `year` - Год выпуска
- `selling_price` - Стоимость в USD


# Task

Собственно задача. Нам бы очень хотелось сделать некоторое обобщение рынка на основании вашей выборки. Cоберите словарь по этой форме:

```
{
    "seed": 20,
    "BMW": {
        "count": 20,
        "mean_price": 4177750.0,
        "old_year": 2010,
        "new_year": 2019,
        "moda_fuel": "Diesel"
    },
    "Ford": {
        "count": 58,
        "mean_price": 506137.9,
        "old_year": 2003,
        "new_year": 2019,
        "moda_fuel": "Diesel"
    },
    "Volkswagen": {
        "count": 22,
        "mean_price": 479409.1,
        "old_year": 2010,
        "new_year": 2018,
        "moda_fuel": "Diesel"
    }
}
```

По глобальным ключам словарь содержит:

* `seed` - ваш идентификатор (число, которое вы указали при генерации выборки)
* Все Марки (уникальные) которые встречаются в данных. В вашей выборке может быть иной набор марок авто. Данный пример описывает выборку, которая представлена тремя марками.

Каждой марке авто в качестве ключа мы ставим в соответствие словарь, который содержит:

- `count` - Количество авто данной марки
- `mean_price` - Средняя стоимость автомобилей данной марки (Округлите до целого числа)
- `old_year` - Год самого старого авто данной марки
- `new_year` - Год самого нового авто данной марки
- `moda_fuel` - Какой тип топлива преобладает для авто данной марки. Например если больше дизельных авто, то тут будет значение "Diesel". Если Не получится выявить самый популярный тип топлива, то этому ключу присвойте значение `None`.

  Если какой-либо из критериев вам вычислить не удастся, то на место значения поставте также `None`.

# How to submit

Когда вы получили итоговый словарь, постарайтесь сформировать некоторое субъективное мнение о том, какой авто вы бы купили.

Итоговый словарь нужно скопировать (как текст) и прикрепить в форме данного [ТЕСТА](https://docs.google.com/forms/d/e/1FAIpQLSdoR924NOnoY3of3tO5e-VXsNAvtNe4V8uGrhRVQlO2NXBvHw/viewform?usp=sf_link) в последнем задании и там же написать в свободной форме ваши выводы о рынке. 
Не забывайте про `seed`, который должен быть в итоговом словаре, иначе мы не сможем вас проверить...
В этой же форме ответьте и на другие вопросы! Они легкие)))
















