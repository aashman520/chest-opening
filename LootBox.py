import random

print("🎁 Welcome to the Chest Opening Game!")
print("Open chests and collect rare loot!\n")

# Loot pool
items = ["Gold 💰", "Sword ⚔️", "Shield 🛡️🛡️", "Potion 🧪🧪", "Key 🗝️", "Magic Gem 💎", "Special Power Ring 💍"]

# Rarity types with probability weights
rarity = ["Common 🤢", "Uncommon 🥬", "Rare 👑", "Legendary ⭐", "Cosmic 🤔"]
rarity_weights = [45, 30, 12, 10, 3]  # PRobability or chances ofeach rarity of items/

coins = 100
inventory = []

while True:
    print("\n🪙 Coins:", coins)
    print("1. Open Chest (20 coins)")
    print("2. View Inventory")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if coins >= 20:
            coins -= 20
            loot = random.choice(items)
            loot_rarity = random.choices(rarity, weights=rarity_weights, k=1)[0]
            inventory.append(f"{loot_rarity} {loot}")

            print(f" You opened a chest and found: {loot_rarity} {loot}!")
        else:
            print(f" Not enough coins! You only have {coins} coins left.")

    elif choice == "2":
        print("\n🧳 Your Inventory:")
        if not inventory:
            print("Your inventory is empty!")
        else:
            for item in inventory:
                print(item)
                print("Total coins:", coins)

    elif choice == "3":
        print("\nThanks for playing! Come back soon.")
        break

    else:
        print(" Invalid choice! Please enter 1, 2, or 3.")