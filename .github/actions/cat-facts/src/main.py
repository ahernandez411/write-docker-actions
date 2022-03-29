import requests
import random

cat_url = "https://cat-fact.herokuapp.com/facts"
response = requests.get(cat_url)

results = response.json()

fact_list = []

for fact in results:
    fact_list.append(fact.get("text"))

def select_random_fact(facts):
    return facts[random.randint(0, len(fact_list)+1)]

random_fact = select_random_fact(fact_list)

print(random_fact)

print(f"::set-output name=fact::{random_fact}")
