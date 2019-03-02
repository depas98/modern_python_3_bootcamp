from pyfiglet import print_figlet
import requests
from random import randint

print_figlet("Dad Joke 3000", 'standard', "MAGENTA")

url = "https://icanhazdadjoke.com/search"
topic = input("Let me tell you a joke! Give me a topic: ")

params = {"term": topic}

response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params=params)

data = response.json()
num_jokes = data["total_jokes"]
joke_results = data["results"]
# print(f"num_jokes: {num_jokes}")

if num_jokes > 1:
    computer_choice = randint(1, num_jokes)
    # print(f"computer choice: {computer_choice}")
    print(f"I've got {num_jokes} jokes about {topic}. Here's one:")
    print(joke_results[computer_choice]["joke"])
elif num_jokes == 1:
    print(f"I've got one joke about {topic}. Here it is:")
    print(joke_results[0]["joke"])
else:
    print(f"Sorry, I don't have any jokes about topic: {topic}")


