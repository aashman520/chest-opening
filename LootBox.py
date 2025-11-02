import json
import random

# --- File to save player progress ---
SAVE_FILE = "player_data.json"

# --- Function to save game data ---
def save_game(coins, inventory):
    data = {"coins": coins, "inventory": inventory}
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("💾 Game saved successfully!")

# --- Function to load saved data (if available) ---
def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        print("📂 Save file loaded!")
        return data["coins"], data["inventory"]
    except FileNotFoundError:
        print("🚀 Starting a new game...")
        return 100, []  # default starting values

# --- Game setup ---
print("🎁 Welcome to the Chest Opening Game!")
print("Open chests and collect rare loot!\n")

# Loot items
items = ["Gold 💰", "Sword ⚔️", "Shield 🛡️", "Potion 🧪", "Key 🗝️", "Magic Gem 💎", "Power Ring 💍"]

# Rarity levels (with emoji)
rarity = ["Common 🤢", "Uncommon 🥬", "Rare 👑", "Legendary ⭐", "Cosmic 🤔"]

# Chest types with their costs, rarity weights, and coin bonus ranges
chests = {
    "1": {"name": "Basic Chest 🪙", "cost": 20, "weights": [45, 30, 12, 10, 3], "coin_range": (5, 25)},
    "2": {"name": "Silver Chest 🪽", "cost": 50, "weights": [30, 30, 20, 15, 5], "coin_range": (20, 60)},
    "3": {"name": "Gold Chest 🐦‍🔥", "cost": 100, "weights": [20, 25, 25, 20, 10], "coin_range": (40, 120)},
    "4": {"name": "Mythic Chest 🦾", "cost": 200, "weights": [10, 15, 30, 30, 15], "coin_range": (100, 250)},
}

# Load player progress
coins, inventory = load_game()

# --- Main game loop ---
while True:
    print("\n🪙 Coins:", coins)
    print("1. Open Chest")
    print("2. View Inventory")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nChoose Chest Type:")
        for key, chest in chests.items():
            print(f"{key}. {chest['name']} - Cost: {chest['cost']} coins")

        chest_choice = input("Enter chest number: ")

        if chest_choice in chests:
            chest = chests[chest_choice]

            if coins >= chest["cost"]:
                coins -= chest["cost"]

                # Random loot and rarity
                loot = random.choice(items)
                loot_rarity = random.choices(rarity, weights=chest["weights"], k=1)[0]

                # Random coin bonus from chest
                bonus_coins = random.randint(*chest["coin_range"])
                coins += bonus_coins

                # Add found item to inventory
                inventory.append(f"{loot_rarity} {loot}")

                print(f"\n🎉 You opened a {chest['name']} and found: {loot_rarity} {loot}!")
                print(f"💰 Bonus coins: {bonus_coins}")
                print(f"🏦 Total coins now: {coins}")
            else:
                print(f"⚠️ Not enough coins! You need {chest['cost']} but only have {coins}.")
        else:
            print("❌ Invalid chest choice!")

    elif choice == "2":
        print("\n🧳 Your Inventory:")
        if not inventory:
            print("Your inventory is empty!")
        else:
            for item in inventory:
                print(" -", item)
        print(f"\n🏦 Total coins: {coins}")

    elif choice == "3":
        print("\n💾 Saving progress...")
        save_game(coins, inventory)
        print("👋 Thanks for playing! Come back soon.")
        break  

    else:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")
