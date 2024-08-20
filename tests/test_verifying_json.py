import json

def open_monster_stats():
    with open("JSON/monster_statistics_by_hit_dice.json", "r") as file:
        json.load(file)

def test_does_it_work():
    open_monster_stats()