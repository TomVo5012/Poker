class Player:
    
    
    # Constructors
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.chip = 0
        self.player_info = {}
        self.player_bet = {}



    # Method to verify if player is 18+ or not 
    def age_verification(self):
        if (self.age >= 18):
            self.player_info.update({self.name: self.age})
    
    
    # Method to keep track on buy_in from player
    def buy_in(self, chip):
        self.chip = chip
        self.player_bet.update({self.name: self.chip})
                
        
    # Method that keep track on each bet from player
    def bet(self):
        pass
                
    # Method that to test object from player's dictionary
    def __repr__(self):
        return "Dictionary verification {player_info}".format(player_info = self.player_info)
    
    