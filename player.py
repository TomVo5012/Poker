class Player:
    
    # Constructors
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.player_info = {}

    def age_verification(self):
        if (self.age >= 18):
            self.player_info.update({self.name: self.age})
    
    def __repr__(self):
        return "Dictionary verification {player_info}".format(player_info = self.player_info)
    
    