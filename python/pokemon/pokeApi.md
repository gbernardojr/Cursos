Claro! Aqui está um **guia completo de como utilizar a PokéAPI com Python**, desde os conceitos básicos até exemplos práticos.

---

# 🧭 Guia para Usar a PokéAPI com Python

A **PokéAPI** é uma API RESTful gratuita que fornece dados sobre o mundo Pokémon: Pokémon, habilidades, tipos, evoluções, e muito mais. Vamos aprender a acessá-la e manipular seus dados usando Python.

---

## 🛠️ Pré-requisitos

- Ter o Python instalado (recomenda-se a versão 3.7+)
- Ter o `requests` instalado:
```bash
pip install requests
```

---

## 🔗 URL Base da PokéAPI

```plaintext
https://pokeapi.co/api/v2/
```

---

## 📦 Importando o módulo necessário

```python
import requests
```

---

## 🔍 Exemplo Básico: Buscar dados de um Pokémon

```python
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Nome: {data['name']}")
        print(f"ID: {data['id']}")
        print("Tipos:")
        for t in data['types']:
            print(f" - {t['type']['name']}")
    else:
        print("Pokémon não encontrado.")

get_pokemon("pikachu")
```

---

## 📑 Buscar todos os Pokémon (com paginação)

```python
def list_pokemons(limit=20, offset=0):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for pokemon in data['results']:
            print(pokemon['name'])
    else:
        print("Erro ao buscar lista de Pokémon.")

list_pokemons(10)  # Exibe os 10 primeiros Pokémon
```

---

## ⚔️ Buscar habilidades de um Pokémon

```python
def get_pokemon_abilities(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Habilidades de {data['name']}:")
        for ability in data['abilities']:
            print(f" - {ability['ability']['name']}")
    else:
        print("Pokémon não encontrado.")

get_pokemon_abilities("bulbasaur")
```

---

## 🔁 Buscar a cadeia de evolução

```python
def get_evolution_chain(pokemon_name):
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
    species_response = requests.get(species_url)
    if species_response.status_code != 200:
        print("Espécie não encontrada.")
        return

    evolution_chain_url = species_response.json()['evolution_chain']['url']
    chain_response = requests.get(evolution_chain_url)
    if chain_response.status_code != 200:
        print("Cadeia de evolução não encontrada.")
        return

    chain = chain_response.json()['chain']

    def print_chain(evolution):
        print(evolution['species']['name'])
        for evo in evolution['evolves_to']:
            print_chain(evo)

    print("Cadeia de Evolução:")
    print_chain(chain)

get_evolution_chain("charmander")
```

---

## 🧠 Dicas Gerais

- Todas as entidades têm endpoints separados (`/pokemon/`, `/ability/`, `/type/`, `/move/`, `/evolution-chain/`, etc.)
- A PokéAPI não exige autenticação.
- Tente limitar suas requisições (não faça muitas por segundo) para evitar bloqueios.

---

Se quiser, posso te ajudar a montar um pequeno projeto ou script interativo com base nisso, tipo uma Pokédex de terminal. É só pedir!
