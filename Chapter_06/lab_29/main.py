from game_store_class import GameStore


if __name__ == "__main__":
    game_store_instance = GameStore()
    print("Game store instance:", game_store_instance)
    game_store_instance([
        "Red Alert",
        "Tomb Raider", 
        "Neverwinter Nights", 
        "Witcher 3"
    ])
    game_store_instance([
        "Alladin",
        "Baldurs Gate", #? <-- is exist on list
        "Neverwinter Nights", #? <-- not add duplicate 
        "Witcher 3",
        "Wolfstein 3D"
    ])


    print("Game store list:", game_store_instance.list)

    print(callable(game_store_instance))
    print(callable(GameStore))
