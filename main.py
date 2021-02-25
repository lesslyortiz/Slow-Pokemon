#        Name: Lessly Ortiz
#        Date: 11/10/2020
# Description: A6: Slow Pokemon
# Collaborators: none
#https://jcrouser.github.io/CSC111/assignments/slowPokemon.html
# You may want to be able to generate amount of damage
from random import randint
from time import sleep


# A stub definition for the parent Pokemon class
class Pokemon:

  def __init__(self, name): # What additional parameters do we need?

    self.name = name
    self.pokemon_type = "NORMAL"
    self.max_hp = randint(25, 50)
    self.current_hp = self.max_hp
    self.attack_power = randint(1, (self.max_hp + 1))
    self.defensive_power = randint(1, (self.max_hp + 1)) #FIXME a ranint greater than 0  and less than hp
    self.fainted = False 
    self.revivesleft = 1  
      
  def printStats(self):
    print("Name:", self.name)
    print("Pokemon type:", self.pokemon_type) 
    print("Max HP:", self.max_hp) 
    print("Current HP:", self.current_hp)
    print("Attack power:", self.attack_power)
    print("Defensive power:", self.defensive_power, "\n")
    img = self.img.read()
    print(img)


  def defend(self, opponent):

    
    if (self.current_hp - 10) <= 0:
      self.current_hp = 0 #fix me????
      self.fainted = True
    else:
      self.current_hp = self.current_hp - 10 

    
    
    
    # Decrease the value of current_hp by some amount (you determine by how much, but it should probably be related to defense in some way) and set fainted = True if current_hp falls below 0
    

  def attack(self, opponent):
    opponent.defend()
    # What other parameters do we need?
    # Takes in an opponent (another Pokemon instance) and decreases its current_hp by calling opponent.defend()
    

  def revive(self):
    if self.revivesleft >= 0:
      if self.fainted == True:
        self.revivesleft = self.revivesleft - 1
        self.current_hp = self.max_hp // 2
        self.fainted = False
        return True
      else:
        return False
    else:
      return False

    # if the Pokemon has fainted: restore half of its max_hp and set fainted = False then returns True, otherwise return False
    

class Pikachu(Pokemon): 
  def __init__(self, name):##FIX ME
    super().__init__(name)##fixme ? do i gotta do all dis 
    self.pokemon_type = "ELECTRIC" #fix me
    self.img = open("Pikachu.txt", "r")
    
  
  def attack(self, opponent):
    if (opponent.pokemon_type == "WATER"):
      self.attack_power = self.attack_power * 2 # do twice as much damage

    elif (opponent.pokemon_type == "ELECTRIC"): 
      self.attack_power = self.attack_power //2
    self.defend(self, opponent)
    if opponent.current_hp <= 0:
      opponent.current_hp = 0
      opponent.fainted = True
      revive()

class Squirtle(Pokemon):
  def __init__(self, name):
    super().__init__(name)
    self.pokemon_type = "WATER"
    self.img = open("Squirtle.txt", "r")

  def attack(self, opponent):
    dam = opponent.defend(opponent)
    if (opponent.pokemon_type == "ELECTRIC"):
      self.attack_power = self.attack_power - 10
    elif (opponent == "GRASS"):
      self.attack_power = self.attack_power + 10

class Bulbasuar(Pokemon):
  def __init__(self, name):
    super().__init__(name)
    self.pokemon_type = "GRASS"
    self.img = open("bulbasuar.txt", "r")

  def attack(self, opponent):
    dam = opponent.defend(opponent)
    if (opponent.pokemon_type == "WATER"):
      self.attack_power = self.attack_power + 20
    elif (opponent == "ELECTRIC"):
      self.attack_power = self.attack_power -10



    

def battle(p1, p2):
  while (p1.revivesleft > 0) and (p2.revivesleft > 0):
    p2.attack(p2)
    print("Attacking", p2.name, "!")
    if p2.fainted == True:
      print(p2.name, "has fainted! :O")
      p2.revivesleft = 0
      p2.revive()
      print(p2.name, "has revived ! :))")
    p2.printStats()
    p2.attack(p1)
    print("Attacking", p1.name, "!")
    if (p1.fainted == True):
      print(p1.name, "has fainted! :O")
      p1.revivesleft = 0
      p1.revive()
      print(p2.name, "has revived ! :))")
    p1.printStats()
  if p1.revivesleft < 0:
    print("hoorah!", p2.name, "has woonnn!")
  elif p2.revivesleft <0:
    print("whoot whoot!", p1.name, "has woooon!")



def main():
  title = open("Title.txt", "r")
  title = title.read()
  print(title)
  print("""Hello, there!
Glad to meet you!
Welcome to the world of POKéMON!
My name is OAK.
People affectionately refer to me as the POKéMON PROFESSOR.""")
  sleep(5)

  print("Select you Pokemon with its corresponding letter:")
  selectedpoke = input("""A: Pikachu\nB: Squirtle\nc: Bulbasuar\n""")
   #fixmethe capitals                             
  if selectedpoke == "A" or "a":
    imput = str(input("Do you want to pick a nick name? Y or N: \n"))
    if imput == "Y":
      name = str(input("Please enter your nickname: "))
      p1 = Pikachu(name)
    elif imput == "N" :
      p1 = Pikachu("Pikachu")
    print("You have selected Pikachu! Now let's battle you with another Pokemon")
    opp = randint(2, 3) 
    if opp == 2:
      p2 = Squirtle("Squirtle")
    elif opp == 3:
      p2 = Bulbasuar("Bulbasuar")

  elif selectedpoke == "B" or "b":
    imput = str(input("Do you want to pick a nick name? Y or N: \n"))
    if imput == "Y":
      name = str(input("Please enter your nickname: "))
      p1 = Squirtle(name)
    elif imput == "N":
      p1 = Squirtle("Squirtle")
    print("You have selected Squirtle! Now let's battle you with another Pokemon")
    opp = randint(2, 3) 
    if opp == 2:
      p2 = Pikachu("Pikachu")
    elif opp ==3:
      p2 = Bulbasuar("Bulbasuar")
      
  elif selectedpoke == "C" or "c":
    imput = str(input("Do you want to pick a nick name? Y or N: \n"))
    if imput == "Y":
      name = str(input("Please enter your nickname: "))
      p1 = Bulbasuar(name)
    elif imput == "N":
      p1 = Bulbasuar("Bulbasuar")
    print("You have selected Bulbasuar! Now let's battle you with another Pokemon")
    opp = randint(2, 3) 
    if opp == 2:
      p2 = Squirtle("Squirtle")
    elif opp == 3:
      p2 = Pikachu("Pikachu")  
  p1.printStats()
  p2.printStats()
  x = input()
  battle(p1, p2)

  

if __name__ == "__main__":


  main()

# REFERENCES: