#!/usr/bin/python3
""" print initial variables variables """
from models.champion import Champion

if __name__ == "__main__":

    try:
        c1 = Champion('Daniela', 'Human', 'Female')
        print(c1.name)
        print(c1.race)
        print(c1.gender)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
  