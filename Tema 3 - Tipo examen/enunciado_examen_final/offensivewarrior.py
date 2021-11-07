#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Warrior, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  warrior.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Alberto Gil De la Fuente (alberto.gildelafuente@ceu.es)

@version :  0.0.1, 04 January 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.


class OffensiveWarrior():
    """Python class to implement a offensive version of a warrior of the game.

    This Python class implements the offensive version of a warrior of the game.

    Syntax
    ------
      obj = Warrior(id, warrior_type, weapon_type, health_points,
                    attack_rating, defense_rating,
                    special_attack_rating)

    Parameters
    ----------
      [in] id Id of warrior.
      [in] warrior_type Type of warrior.
      [in] weapon_type Type of weapon that carries out the warrior.
      [in] health_points Points of health that the warrior has.
      [in] attack_rating Attack rating of the warrior.
      [in] defense_rating Defense rating of the warrior.
      [in] special_attack_rating Special Attack rating of the warrior.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Warrior.

    Attributes
    ----------

    Example
    -------
      >>> from warrior import Warrior
      >>> obj_Warrior = Warrior("Boxer", "Fist", 99, 10, 7, 19)
    """



def main():
    """Function main of the module.

    The function main of this module is used to test the Class OffensiveWarrior.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Warrior.")
    print("=================================================================.")
    warrior1 = OffensiveWarrior(1, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 8, 9, 17)

    if warrior1.get_warrior_type().name == "GLADIATOR":
        print("Test PASS. The parameter warrior_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_weapon_type().name == "SWORD":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_special_attack_rating() == 17:
        print("Test PASS. The parameter special_attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    warrior2 = OffensiveWarrior(2, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 7, 10, 19)

    if str(warrior2) == "GLADIATOR with a SWORD":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__().")


    print("=================================================================.")
    print("Test Case 3: Warrior alive?¿?.")
    print("=================================================================.")
    warrior3 = OffensiveWarrior(3, WarriorType.UFC, WeaponType.KICK, 97, 8, 9, 12)

    if warrior3.is_alive():
        warrior3.fight_defense(200)  # With this the warrior should be retired.

        if not warrior3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    warrior4 = OffensiveWarrior(4, WarriorType.MMA, WeaponType.ELBOW, 93, 9, 6, 17)

    warrior4.fight_defense(70)

    if warrior4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    warrior5 = OffensiveWarrior(5, WarriorType.BOXER, WeaponType.PUNCH, 99, 10, 7, 19)
    warrior6 = OffensiveWarrior(6, WarriorType.BOXER, WeaponType.PUNCH, 99, 9, 8, 20)

    warrior_hit = warrior5.fight_attack(warrior6)

    print(warrior6.get_health_points())

    if warrior_hit:
        if (warrior6.get_health_points() == 97) or ((warrior6.get_health_points() == 88)):
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if warrior6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
