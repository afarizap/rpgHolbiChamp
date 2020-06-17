

class Champion():
  """ Champion general attributes """

  level = 0
  exp = 0
  currentExp = 0
  totalExp = 0
  statpoints = 0
  stats = {'Health': 5,
          'Attack': 4,
          'Defense': 0,
          'Magic': 0,
          'Speed': 0 }


  def __init__(self, name, race, gender):
        self.name = name
        self.race = race
        self.gender = gender
        self.armor = {
          'Helmet': ,
          'Gauntlets': Guantes de goma,
          'Chest armor': Pechera de oro,
          'Leg armor': Falda}

    
  # exp_total = sum(win_exp)
  # exp_next = expt_current - total

  @property
  def name(self):
    return (self.__name)
  
  
  @name.setter
  def name(self, value):
    if (type(value) is not str):
      raise TypeError('ingresa un string por favor')
    else:
      self.__name = value

  @property
  def race(self):
    return(self.__race)
  
  @race.setter
  def race(self, value):
    string = ['Human', 'Elf', 'Dwarf', 'Hobbit', 'Orc']
    if value not in string:
      raise TypeError('ingresa una de las razas')
    if type(value) is not str:
      raise ValueError('ingresa un string')
    else:
      self.__race = value


  @property
  def gender(self):
    return (self.__gender)
  
  @gender.setter
  def gender(self, value):
    lista_2 = ['Male', 'Female']
    if (type(value) is not str): #elbergalarga
      raise TypeError('ingresa un str')
    if (value not in lista_2):
      raise ValueError('ingresa male o female')
    self.__gender = value

   
    ### melicimo XD

## ni tu sin mi