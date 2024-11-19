import time
import random

# Global variables
friendship_level = 0
emotional_health = 100
inventory = []
monsters_met = []

# Function to print text slowly
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)  # Print each character without a newline
        time.sleep(delay)  # Wait for a brief moment
        
    print()  # Add a new line after the text finishes

# Introduction
def start_game():
    slow_print("Welcome to The Dream World Adventure!")
    slow_print("You are tornike, a 9-year-old child who dreams of freedom from your strict parents.")
    slow_print("One night, you meet strange creatures in your dreams. Will you trust them or remain alone?")
    input("Press Enter to start your journey...")

    
    meet_first_monster()

# Encounter the first monster
def meet_first_monster():
    global friendship_level, emotional_health, monsters_met  # Declare global at the start
    slow_print("\nYou find yourself in a dark, mysterious forest. A small, fluffy monster appears.")
    slow_print("It looks kind and asks: 'Would you like to be friends?'")
    choice = input("Do you want to be friends? (yes/no): ").lower()
    
    if choice == "yes":
        slow_print("The fluffy monster smiles and gives you a small charm. You feel a little less lonely.")
        friendship_level += 1
        monsters_met.append("Fluffy Monster")
        emotional_health += 5
        slow_print(f"Friendship Level: {friendship_level}")
        slow_print(f"Emotional Health: {emotional_health}")
        slow_print("\nThe next day, a new monster appears in your dreams.")
        continue_adventure()
    else:
        slow_print("You decide to walk away from the fluffy monster. It looks sad, but respects your decision.")
        slow_print("You feel even more alone. Your emotional health drops.")
        emotional_health -= 10
        slow_print(f"Emotional Health: {emotional_health}")
        continue_adventure()

# Encounter more monsters
def continue_adventure():
    global friendship_level, emotional_health  # Declare global at the start
    slow_print("\nYou enter a new part of the dream world.")
    monster_choice = random.choice(["Shadow Monster", "Glowing Owl", "Stone Giant"])
    
    slow_print(f"A {monster_choice} appears!")
    if monster_choice == "Shadow Monster":
        shadow_monster()
    elif monster_choice == "Glowing Owl":
        glowing_owl()
    elif monster_choice == "Stone Giant":
        stone_giant()

# Shadow Monster encounter
def shadow_monster():
    global friendship_level, emotional_health  # Declare global at the start
    slow_print("\nThe Shadow Monster speaks in a deep voice: 'I can help you face your fears.'")
    choice = input("Do you trust the Shadow Monster? (yes/no): ").lower()
    
    if choice == "yes":
        slow_print("The Shadow Monster helps you face your deepest fears, and you feel a bit stronger.")
        friendship_level += 2
        slow_print(f"Friendship Level: {friendship_level}")
    else:
        slow_print("You run from the Shadow Monster. It disappears into the darkness.")
        emotional_health -= 5
        slow_print(f"Emotional Health: {emotional_health}")
    
    # Continue the story
    next_day()

# Glowing Owl encounter
def glowing_owl():
    global friendship_level, emotional_health  # Declare global at the start
    slow_print("\nA wise, glowing owl perches before you and says: 'I can offer you knowledge of the Dream World.'")
    choice = input("Do you accept the owl's offer? (yes/no): ").lower()
    
    if choice == "yes":
        slow_print("The owl gives you a vision of the future, showing you a path to greater happiness.")
        friendship_level += 3
        emotional_health += 10
        slow_print(f"Friendship Level: {friendship_level}")
        slow_print(f"Emotional Health: {emotional_health}")
    else:
        slow_print("You politely decline. The owl nods and flies away into the night sky.")
        emotional_health -= 2
        slow_print(f"Emotional Health: {emotional_health}")
    
    # Continue the story
    next_day()

# Stone Giant encounter
def stone_giant():
    global friendship_level, emotional_health  # Declare global at the start
    slow_print("\nA towering Stone Giant appears. Its voice rumbles: 'I will help you with strength.'")
    choice = input("Do you need the Stone Giant's help? (yes/no): ").lower()
    
    if choice == "yes":
        slow_print("The Stone Giant gives you the strength to face physical challenges in your life.")
        friendship_level += 4
        emotional_health += 8
        slow_print(f"Friendship Level: {friendship_level}")
        slow_print(f"Emotional Health: {emotional_health}")
    else:
        slow_print("You politely refuse. The Stone Giant slowly turns and walks away.")
        emotional_health -= 3
        slow_print(f"Emotional Health: {emotional_health}")
    
    # Continue the story
    next_day()

# Next day and decision to continue
def next_day():
    global friendship_level, emotional_health  # Declare global at the start
    slow_print("\nAnother day passes. The dream world grows even stranger.")
    slow_print("You've met new monsters, but one final challenge awaits you...")
    
    # The final robot monster decision
    final_decision()

# Final decision
def final_decision():
    global friendship_level, emotional_health  # Declare global at the start
    slow_print("\nOn the seventh day, a giant robot monster approaches. It speaks: 'I offer you a choice.'")
    slow_print("1. Stay in the real world and face the pain and struggles, or")
    slow_print("2. Enter the Dream World and live freely with your new friends.")
    
    choice = input("What will you choose? (stay/world): ").lower()
    
    if choice == "world":
        slow_print("\nYou decide to leave the real world behind. The Dream World offers you peace and friendship.")
        slow_print("You live happily with your new friends, free from the pain and loneliness.")
        game_ending("Dream World Ending")
    else:
        slow_print("\nYou choose to stay in the real world. Although it's painful, you've learned to face your fears and grow stronger.")
        if friendship_level > 5:
            slow_print("You now have the strength to live with your monsters' guidance.")
            game_ending("Real World Ending")
        else:
            slow_print("You face the challenges alone, but you've learned valuable lessons along the way.")
            game_ending("Real World Ending (Tough Choice)")

# Game ending
def game_ending(ending):
    global friendship_level, emotional_health, inventory, monsters_met  # Declare global at the start
    slow_print("\n--- GAME OVER ---")
    slow_print(f"Ending: {ending}")
    slow_print(f"Friendship Level: {friendship_level}")
    slow_print(f"Emotional Health: {emotional_health}")
    slow_print(f"Monsters Met: {', '.join(monsters_met)}")
    
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        # Reset the game variables
        friendship_level = 0
        emotional_health = 100
        inventory = []
        monsters_met = []
        start_game()
    else:
        slow_print("Thank you for playing!")

# Start the game
start_game()

