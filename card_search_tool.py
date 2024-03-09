import requests
from config import YOUR_AUTH_TOKEN

global headers
headers = {"Authorization": f"Bearer {YOUR_AUTH_TOKEN}"}


def get_game_id(game_name):
    url = "https://api.cardtrader.com/api/v2/games"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        games = response.json()["array"]
        for index in range(0, len(games)):
            if game_name in games[index]["name"]:
                return games[index]["id"]


def find_card_price(game_id, card_name):
    cards_to_add = []
    url = "https://api.cardtrader.com/api/v2/expansions"
    card_found = False
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        expansions = response.json()
        for expansion in expansions:
            if expansion["game_id"] == game_id:
                card_url = f"https://api.cardtrader.com/api/v2/marketplace/products?expansion_id={expansion['id']}"
                cards = requests.get(card_url, headers=headers)
                if cards.status_code == 200:
                    cards = cards.json()
                    for item in cards.values():
                        for card in item:
                            if card.get("name_en").lower() != card_name.lower():
                                break

                            card_found = True

                            card_to_add = [
                                card.get("name_en"),
                                card.get("price").get("formatted"),
                                card.get("properties_hash").get("condition"),
                            ]
                            print("shit")
                            cards_to_add.append(card_to_add)

                        if card_found:
                            return cards_to_add
