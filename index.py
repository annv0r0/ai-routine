import openai
import os
import csv

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

count = 10
file_name = os.getenv('CSV_NAME')
categories_list = []

openai.organization = os.getenv('OPENAI_ORGANIZATION')
openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

with open(f'{file_name}.csv', newline='\n') as csvfile:
    categories = csv.reader(csvfile, delimiter='\n')
    headers = next(categories) 

    for row in categories:
        categories_list.extend(row)

categories_lenght = len(categories_list)

prompt = f"""
Вводные данные:
Ты - фермер. У тебя есть список категорий товаров для фермерства в тройных кавычках, где каждая категория выделена одинарными кавычками.\
```{categories_list}``` \
Ты хочешь купить по  {count} товаров из каждой категории.
Задание: \
Напиши по {count} разнообразных поисковые запросов на русском языке для поисковика Google для каждой категории в одинарных кавычках. \

Дополнительная информация: \
1. Для {categories_lenght} категорий должно получиться {categories_lenght * count} запросов. \
2. Используй слово "купить" и его синонимы только в половине запросов.
3. Не используй названия городов и стран.
4. Не используй длинные предложения со знаками препинания.
5. Каждый  запрос должен подразумевать готовность к покупке.\
6. Не повторяйся. \
7. Примеры хороших запросов через запятую: Техника для сельского хозяйства, Кондитерские изделия оптом для фермерства, Минитракторы с доставкой по России \
8. Примеры плохих запросов через запятую: Как использовать яйца в косметологии, Как приготовить замороженные овощи на пару, Прочее для переработки овощей, фруктов, ягод. \
9. Сгруппируй запросы по категориям, но не пищи название категории. Один запрос должен быть записан на одной строке. \
10. Не маркируй и не нумеруй каждую строку.
"""
response = get_completion(prompt)
print('response:', response, '\n')