import time, os
import random
import json

# Variables
names = ["joshproz69", "mastergame76", "PRICOFFICAL", "jahshbsbsj176e", "creeperboy123", "imthebestandyouallsuck", "ggbyriot123", "urmom", "imyourfather626", "ipadkid2026"]

loses = 0
wins = 0
current_username = "" # Added this so the game remembers who is currently playing

# --- NEW: Save and Load Functions ---
def load_data():
	global names, wins, loses, current_username
	# Checks if a save file exists before trying to open it
	if os.path.exists("savegame.json"):
		with open("savegame.json", "r") as f:
			data = json.load(f)
			names = data.get("names", names)
			wins = data.get("wins", wins)
			loses = data.get("loses", loses)
			current_username = data.get("current_username", "")

def save_data():
	data = {
		"names": names,
		"wins": wins,
		"loses": loses,
		"current_username": current_username
	}
	with open("savegame.json", "w") as f:
		json.dump(data, f)
# ------------------------------------

# Load the data right as the script starts
load_data()

def draw_text(text, speed=1):
	print(text)
	time.sleep(speed)
	
# Intro
draw_text("Welcome!")
draw_text("To the game of.....", 2)

draw_text("Rock, Paper, Scissors!", 3)
draw_text("You", 0.7)

draw_text("already know how to play ( i hope )", 3)
draw_text("So lets start!", 2)

os.system('clear')

def Starting_Screen():
	global current_username
	while True:
		# Wrapped your original code in an 'if' so it only asks if no user is saved!
		if current_username == "":
			draw_text("Enter a username", 0)
			name = input("> ")
			names.append(name)
			current_username = name
			save_data() # Save the new user right away
			draw_text(f"Welcome {name}!")
		else:
			draw_text(f"Welcome back, {current_username}!", 1)
			name = current_username # Keeps your variable functional
			
		os.system('clear')
		draw_text("Rock, Paper Scissors!")
		draw_text("Now with text!\n")
		draw_text(f"Wins: {wins}", 0.5)
		draw_text(f"Loses: {loses}", 0.5)
		draw_text("""
		1) Faking the Matchmaking aka Starting
		2) Exit, ah yesy exit""", 0)
		menu = input("> ")
		if menu == "1":
			Starting()
		elif menu == "2":
			exit()
		elif menu == "3":
			draw_text("hehehe")
		elif menu == "67":
			draw_text("brainrot")
		elif menu == "69":
			draw_text("nice")
		elif menu == "92":
			draw_text("92% ON PHOBOS BY VORTROX")

def Starting():
	global loses
	global wins
	random_name = names[random.randint(0, 9)]
	os.system('clear')
	draw_text("Not finding someone (because this is on a command prompt) to play with this noob..", random.randint(6, 9))
	draw_text("Ah someone to play with this guy.", 3)
	draw_text(f"*Ding* {random_name} has come to play!")
	draw_text(f"{random_name} has played! how would you like to respond?")
	draw_text("""
	1) Play like a normal human,
	2) afk, i mean best to troll,
	3) resign, would recommend ( for reasons dont pick this, duh )""")
	choose_now = input("> ")
	if choose_now == "1":
		score = 0
		ai_score = 0
		while True:
			win_score = 3
			draw_text(f"Your Score: {score}", 0) 
			draw_text(f"{random_name}'s Score: {ai_score}", 0)
			draw_text(f"Winning Score: {win_score}", 0)
			draw_text("Okay what do you like to choose?")
			draw_text(""""
		1) Rock
		2) Paper
		3) Scissors""")
			pick = input("> ")
			ai_pick = random.randint(1, 3)
			print(ai_pick)
			if pick == "1":
				draw_text("U picked *clears thoart* The Rock *epic music plays*", 3)
			elif pick == "2":
				draw_text("U r as thin as paper", 3)
			elif pick == "3":
				draw_text("i cant say anything... or can i? *vsauce music plays*", 3)
				
			if pick == "1" and ai_pick == 2 or pick == "2" and ai_pick == 3 or pick == "3" and ai_pick == 1:
				draw_text("You lose! Come on, its not that hard, you had one in three!", 2)
				ai_score += 1
				
			elif int(pick) == ai_pick:
				draw_text("Your drawed! meh better tha. losing.", 2)
			elif pick == "1" and ai_pick == 3 or pick == "2" and ai_pick == 1 or pick == "3" and ai_pick == 2:
				draw_text("You Win! PURE LUCK.", 2)
				score += 1
				
			if score == win_score:
				draw_text("GG! Huh, you maybe better than i thought", 3)
				wins += 1
				save_data() # Saves whenever you secure a game win!
				Starting_Screen()
				
			elif ai_score == win_score:
				draw_text("Youe lost! HAHA you are a loser!")
				loses += 1
				save_data() # Saves whenever you take an L
				Starting_Screen()
			
	elif choose_now == "2":
		draw_text("100% trolling or just curious(but curiousity killed the cat)")
		random_afk = random.randint(1, 5)
		
		if random_afk == 1:
			draw_text("You Won as your oppoent got a girlfriend unlike you, stinky.")
			wins += 1
			save_data()
			Starting_Screen()
			
		elif random_afk == 2:
			draw_text("You lost as your oppoent got aura and used on you, and won.")
			loses += 1
			save_data()
			Starting_Screen()
			
		elif random_afk == 3:
			draw_text("DRAW because your oppoent is an ipad kid ( i think ).")
			Starting_Screen()
			
		elif random_afk == 4:
			draw_text("DRAW as your oppoemt was GD COLON")
			Starting_Screen()
		
		elif random_afk == 5:
			draw_text("DRAW", 3)
			draw_text("what?", 2)
			draw_text("you expected for me to talk?", 2)
			Starting_Screen()
		
	elif choose_now == "3":
		draw_text("I KNEW IT YOU ARE A NOOB HAHAHHAHAH *cough* sorry")
		loses += 1
		save_data()
		Starting_Screen()

def Game_Start():
	draw_text("Press S because you have to start the game, duh")
	draw_text("NOTE: Press Enter as well, because im bad with programming.")
	start = input("> ")
	if start == "S" or start == "s":
		draw_text("Good. Now the actual game, im at my friends house right sooooooo just play the game or afk idc.", 5)
		Starting_Screen()
	
Game_Start()
