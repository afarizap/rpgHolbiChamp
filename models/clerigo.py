from models.champion import Champion

class clerigo(Champion):
  '''class to clerigo'''
  
  def __init__(self, name, race, gender):
    super().__init__(name, race, gender)
    Champion.stats = {
          'Health': 100,
          'Attack': 1,
          'Defense': 4,
          'Magic': 2,
          'Speed': 3 }
    self.weapon = maze
    self.defense = shield
    self.armor = {
          'Helmet': ,
          'Gauntlets': Guantes de goma,
          'Chest armor': Pechera de oro,
          'Leg armor': Falda}
    
    @staticmethod
    def attack() 
  
