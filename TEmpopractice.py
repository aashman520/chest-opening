

'''
import random
print("Welcome to Chest opening game.")
print("This just a simple project.")#It should include opning system and storage sysytem.
items = ["Gold 💰", "Sword 🗡️", "Shield 🛡️", "Potion 🧪", "Key 🗝️", "Magic Gem 💎", "Diamond ring💍"]
rarity=["Common🤢","Uncommon🥬","Rare👑","Legendary⭐","????Cosmic????🤔"]
coins=100
rare=random.choices(rarity)
inventory=[]
while True:
    print("\nCoins:", coins)
    print("1. Open Chest (20 coins)")
    print("2. View Inventory")
    print("3. Exit")

    choices = input("Enter your choice: ")
    if choices=="1":
        if coins>=20:
            coins-=20
            loot=random.choice(items)
            inventory.append(loot)
            print(f"Congrats!You got {rare} {loot} from the chest.")
        else:
            print(f"Not enough coins.You only have {coins} coins left!!!")

    elif choice == "2":
        print("\n🧳 Your Inventory:")
        if not inventory:
            print("Your inventory is empty!")
        else:
            for item in inventory:
                print(item)
                print("Total coins:", coins)
    
    elif choices == "3":
        print("Thanks for playing!!!")
        break
    
    else:
        print("Invalid choice! Try again.")

'''