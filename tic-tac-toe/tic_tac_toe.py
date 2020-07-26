'''
Chinyere Azukwu, Andy Nguyen
cazukwu1@binghamton.edu, anguye13@binghamton.edu
Section A51, Jia Yang
Final Project
'''

'''
Methods
get_turn_count()
get_whose_turn()
set_whose_turn()
increment_turn_count()
reset_turn_count()
reset_whose_turn()
'''

# Imports -------------------------------------------------------------------

from board import *
from computer import *
import random


# ENTIRE CLASS DONE BY CHINYERE AZUKWU
# Model of a tic-tac-toe game using a board and computer
class Tic_Tac_Toe:
  # Class variables ---------------------------------------------------------
  INITIAL = 1

  # Constructor -------------------------------------------------------------
  def __init__(self):
    self.__turn_count = self.INITIAL
    self.__whose_turn = ''
    self.__game_state = 'playing'

  # Accessors ---------------------------------------------------------

  # BY CHINYERE AZUKWU
  # returns self.__turn_count
  def get_turn_count(self):
    return self.__turn_count

  # BY CHINYERE AZUKWU
  # returns self.__whose_turn
  def get_whose_turn(self):
    return self.__whose_turn

  # Mutators ---------------------------------------------------------

  # BY CHINYERE AZUKWU
  # sets the first player to go or changes the turn
  def set_whose_turn(self):
    # chooses who goes first
    if self.__whose_turn == '':
      chance = random.randint(0, 1)
      if chance == 0:
        self.__whose_turn = 'player'
      else:
        self.__whose_turn = 'computer'
    # changes turn to computer
    elif self.__whose_turn == 'player':
      self.__whose_turn = 'computer'
    # changes turn to player
    else:
      self.__whose_turn = 'player'

  # BY CHINYERE AZUKWU
  # increases the turn count by one
  def increment_turn_count(self):
    self.__turn_count += Computer.INCREMENT

  # BY CHINYERE AZUKWU
  # resets the turn count back to one
  def reset_turn_count(self):
    self.__turn_count = self.INITIAL

  # BY CHINYERE AZUKWU
  # resets who goes first
  def reset_whose_turn(self):
    self.__whose_turn = ''
