import random
import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout, TooManyRedirects
import json


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        pokemon = response.json()
        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
        }
    
    except (RequestException, JSONDecodeError) as e:
        print(f"Error fetching Pokemon data: {e}")
        return None  # Return None to indicate failure

def run():
    my_pokemon = random_pokemon()
    
    if my_pokemon is None:
        print("Failed to fetch your Pokemon. Please try again later.")
        return
    
    print('You were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    if stat_choice not in ['id', 'height', 'weight']:
        print('Invalid choice. Please choose id, height, or weight.')
        return

    opponent_pokemon = random_pokemon()
    
    if opponent_pokemon is None:
        print("Failed to fetch opponent's Pokemon. Please try again later.")
        return
    
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    k = 0
    l = 0

    for _ in range(11):
        if my_stat > opponent_stat:
            print('You Win!')
            k += 1
        elif my_stat < opponent_stat:
            print('You Lose!')
            l += 1
        else:
            print('Draw!')

    if k > l:
        print('You won the game')
    else:
        print('You lost the game')

run()
