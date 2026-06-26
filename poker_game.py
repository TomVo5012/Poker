from player import Player
from card import Card
    
while True:
    
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
    
    
    # Verifying Buy In Minimum from player 
    while True:
        print("How much do you want to buy in? Minimum will be 1000")  
        player_buy_in = input("Enter The Amount: ")
        if player_buy_in < 1000:
            print("Invalid Buy In, The Minimum Buy In is 1000")
        else:
            verify_player.buy_in(player_buy_in)
            print(verify_player)
            break
    
    # The Main Game Loop
    while(player_buy_in > 0):
        
        # Show player's cards 
        print("Your cards are: ")
        player_cards = Card()
        player_set_of_cards = player_cards.player_combine_card()
        print(player_set_of_cards)
        
                 
        # Create the new set of cards from dealer
        cards = Card()
        set_of_cards = cards.dealer_combine_card()
        
        
        
        
        
        
        
        
        
    
    
    
