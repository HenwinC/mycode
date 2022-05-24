#!/usr/bin/python3
import colorama
from colorama import Fore
import random

thieve_health = 100
player_health = 100

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Survial Game
========
Commands:
  go [up, down, left, right]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' +  currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []
#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = { 

            'Bedroom' : { 
                  'down' : 'Hallway',
                  'item' : 'butter knife',
                },

            'Hallway' : { 
                  'up'  : 'Bedroom',
                'left'  : 'Living Room',
                'right' : 'Kitchen',
                },
            'Living Room' : {
                  'right' : 'Hallway',
                  'left'  : 'Garage',
                  'up'    : 'Kitchen',
                  'down'  : 'Basement',
                  'item'  : 'grandmas sandal'
               },
            'Kitchen' : {
                  'item' : 'Thieve'
               },
            'Garage' : {
              'right' : 'Living Room',
              'item'  : 'shotgun shells'
            },
            'Basement' : {
              'up'  : 'Living Room',
              'item': 'shotgun'
            }
         }

#start the player in the Hall
currentRoom = 'Bedroom'

def combat_Mode():
  while currentRoom == 'Kitchen':
    if inventory == False:
      print(' You ran into the thieve empty handed! Comonnnnn Dawg... GAME OVER!')
      break
    
    print(f'Thieve Health {thieve_health} Your Health {player_health}')
    player = input(f'choose you weapon {inventory}: ')
    if player == "butter knife":
      print(thieve_health)
      thieve_health = thieve_health - 7
      print (f'Shank shank Thieve health -7 {thieve_health}')
    if player == "grandmas sandal":
      thieve_health = thieve_health -20
      print(f'The Power of Granny runs strong in this one. Thieve health {thieve_health}')
    if player == 'shotgun':
      thieve_health = thieve_health - 50
      print(f'No ammo but a butt stroke works just fine with a shotgun {thieve_health}')
    if player == 'Shotgun' and 'shotgun shells' in inventory:
      thieve_health = thieve_health - 100
      print(f'Bang Bang. That Thieve is goooonnneeeeeee!')
    if thieve_health == 0:
      print(f'Nice Job. That theive is goooooooonnneeee')
    weapon = random.randint(1, 3)
    if weapon == 1:
      player_health = player_health - 20
      print(f'Thieve sticks you with a knife attack {player_health}')
    if weapon == 2:
      player_health = player_health - 50
      print(f'Bang Bang. Thieve shots you {player_health}')
    if weapon == 3:
      player_health = player_health - 3
      print(f'Thieve hits you with a open hand smack....Disrespecful {player_health}')
    if player_health == 0:
      print(f'RIP. You Lose')
      break
    if thieve_health == 0:
      print(f'You Defended your house! That thieve is goooooonnnnneeeeee')
      break
    

  

# def color_screen():
#   if currentRoom == "Bedroom":
#     print(Fore.BLUE + ' ')
#     Fore.BLUE
#     Fore.RESET

#   if currentRoom == "Hallway":
#     print(Fore.GREEN + ' yurt')
    
#     Fore.GREEN

#   if rooms[currentRoom] == 'Living Room':
#     print(Fore.GREEN + '')
#     Fore.MAGENTA
#   if rooms[currentRoom] == 'Kitchen':
#     print(Fore.GREEN + '')
#     Fore.RED
#   if currentRoom == 'Garage':
#     print(Fore.GREEN + '')
#     Fore.LIGHTYELLOW_EX
#   if currentRoom == 'Basement':
#     print(Fore.LIGHTGREEN_EX  + '')

# color_screen()
showInstructions()
#loop forever
while True:

  showStatus()

# 
  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

if rooms[currentRoom] == 'Kitchen':
  print('COMBAT MODE')
  print(f'Thieve Health {thieve_health} Your Health {player_health}')
  combat_Mode()
    # player = input(f'choose you weapon {inventory}: ')
    # if player == "butter knife":
    #   print(thieve_health)
    #   thieve_health = thieve_health - 7
    #   print (f'Shank shank Thieve health -7 {thieve_health}')
    # if player == "grandmas sandal":
    #   thieve_health = thieve_health -20
    #   print(f'The Power of Granny runs strong in this one. Thieve health {thieve_health}')
    # if player == 'shotgun':
    #   thieve_health = thieve_health - 50
    #   print(f'No ammo but a butt stroke works just fine with a shotgun {thieve_health}')
    # if player == 'Shotgun' and 'shotgun shells' in inventory:
    #   thieve_health = thieve_health - 100
    #   print(f'Bang Bang. That Thieve is goooonnneeeeeee!')
    # if thieve_health == 0:
    #   print(f'Nice Job. That theive is goooooooonnneeee')
    # weapon = random.randint(1, 3)
    # if weapon == 1:
    #   player_health = player_health - 20
    #   print(f'Thieve sticks you with a knife attack {player_health}')
    # if weapon == 2:
    #   player_health = player_health - 50
    #   print(f'Bang Bang. Thieve shots you {player_health}')
    # if weapon == 3:
    #   player_health = player_health - 3
    #   print(f'Thieve hits you with a open hand smack....Disrespecful {player_health}')
    # if player_health == 0:
    #   print(f'RIP. You Lose')
    #   break
    # if thieve_health == 0:
    #   print(f'You Defended your house! That thieve is goooooonnnnneeeeee')
    #   break
  ## Define how a player can win
  ## If a player enters a room with a monster
elif rooms[currentRoom] == 'Kitchen' and inventory == False:
  print(' You ran into the thieve empty handed! Comonnnnn Dawg... GAME OVER!')