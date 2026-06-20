age = True
game_is_on = True

def age_verification(age):
    if age < 18:
        return "You are not old enough to gamble!!!!!"
    else:
        return "Welcome to Poker Game!"
    
while(game_is_on):
    print("""
      My name is Kiet Vo
      I am a founder of this Poker Game App
      Welcome to Poker Game 
      """)
    username = input("Please Enter Your Name: ")
    user_age = input("Please Verify Your Age: ")
    if (age_verification(user_age)):
        break
    
