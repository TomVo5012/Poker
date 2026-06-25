from player import Player
from card import Card


game_is_on = True
    
while(game_is_on):
    
    # Receive player's name and age
    player_name = input("Please Enter Your Name: ")
    player_age = input("Please Verify Your Age: ")
    
    # Age Verification before player can play
    if (int(player_age) < 18):
        print("""
              We are so sorry, but you are not old enough to gamble
              Come back when you are 18+!!!!!!!!!!
              """)
        break
    else:
        # Store player's information in the dictionary
        verify_player = Player(player_name, player_age)
        verify_player.age_verification()
        print(verify_player)
    
    # Welcome Statement
    print("""
      My name is Kiet Vo
      I am a founder of this Poker Game App
      Welcome to Poker Game 
      Game Options:
      Press 1: To Play
      Press 2: Exit Game
      """)
    
    # Ask player to enter their choice
    player_choice = input("Enter Your Choice: ")
    if (int(player_choice) == 2):
        print("We are sad that you leave the game")
        break
    
    
    buy_in = 1000
    # Game starts
    
    while(buy_in > 0):
        pass
        
        
        
        
        
    
    
    
