'''
Chinyere Azukwu, Andy Nguyen
cazukwu1@binghamton.edu, anguye13@binghamton.edu
Section A51, Jia Yang
Final Project
'''

'''
Methods
get_computer_letter()
get_player_letter()
get_letter_dict()
set_player_letter(letter)
set_computer_letter()
computer_goes(board)
'''

# Imports -------------------------------------------------------------------

from board import *


# ENTIRE CLASS BY ANDY NGUYEN
# Model of a computer that plays against a human
class Computer:
  # Class variables ---------------------------------------------------------
  INCREMENT = 1
  MAX = 10

  # Constructor -------------------------------------------------------------
  def __init__(self):
    self.__computer_letter = ' '
    self.__player_letter = ' '
    self.__letter_dict = {
      'player': self.__player_letter,
      'computer': self.__computer_letter
    }

  # Accessors ---------------------------------------------------------------

  # BY ANDY NGUYEN
  # returns self.__computer letter
  def get_computer_letter(self):
    return self.__computer_letter

  # BY ANDY NGUYEN
  # returns self.__player_letter
  def get_player_letter(self):
    return self.__player_letter

  # BY ANDY NGUYEN
  # returns self.__letter_dict
  def get_letter_dict(self):
    return self.__letter_dict

  # Mutators ----------------------------------------------------------------

  # BY ANDY NGUYEN
  # param letter - 'x' or 'o'
  # given a player's choice, sets their letter as 'x' or 'o'
  def set_player_letter(self, letter):
    self.__player_letter = letter

  # BY ANDY NGUYEN
  # sets computer letter as 'x' or 'o' based on what the player picked
  def set_computer_letter(self):
    if self.__player_letter == 'X':
      self.__computer_letter = 'O'
    else:
      self.__computer_letter = 'X'

  # BY ANDY NGUYEN
  # resets computer letter and player letter
  def reset_letters(self):
    self.__player_letter = ' '
    self.__computer_letter = ' '

  # BY ANDY NGUYEN
  # param board - board object that the computer plays on
  # computer 'scans' the board and makes a move depending on the board
  # returns the location (int) in which computer makes its move
  def computer_goes(self, board):
    # initialize starting location for computer to test
    location = Board.UPPER_LEFT_CORNER
    # intializes flags to see if spots are open
    upper_left_open = False
    upper_right_open = False
    lower_left_open = False
    lower_right_open = False
    center_open = False
    top_edge_open = False
    right_edge_open = False
    bottom_edge_open = False
    left_edge_open = False
    # gets the dict (self.__board) of given board object
    board_object = board
    board_dict = board_object.get_board()
    # intializes flags to see if computer or player can win
    computer_can_win = False
    player_can_win = False
    int_var = ''
    # Checks if computer can win
    while location < Computer.MAX:
      board_copy = dict(board_dict)
      if board_object.is_free_space(location):
        board_copy[location] = self.__computer_letter
        if board_object.check_win(board_copy, self.__computer_letter):
          board_object.place_piece(location, self.__computer_letter)
          int_var = int(location)
          # breaks out of while loop if win is found
          location = Computer.MAX
          computer_can_win = True
        # raises flag if corners are open, to prevent 'rescanning' board
        else:
          if location == Board.UPPER_LEFT_CORNER:
            upper_left_open = True
          elif location == Board.UPPER_RIGHT_CORNER:
            upper_right_open = True
            location += Computer.INCREMENT
          elif location == Board.LOWER_RIGHT_CORNER:
            lower_right_open = True
          elif location == Board.LOWER_LEFT_CORNER:
            lower_left_open = True
          elif location == Board.CENTER:
            center_open = True
          elif location == Board.TOP_EDGE:
            top_edge_open = True
          elif location == Board.RIGHT_EDGE:
            right_edge_open = True
          elif location == Board.BOTTOM_EDGE:
            bottom_edge_open = True
          else:
            left_edge_open = True
          # moves to next spot on board if spot isnt a win
          location += Computer.INCREMENT
      else:
        # moves to next spot on board if spot isnt free
        location += Computer.INCREMENT
    # prevents computer from making an additional move
    if computer_can_win:
      pass
    # if player can win and computer cant, blocks player
    else:
      # resets starting spot to scan at upper left
      location = Board.UPPER_LEFT_CORNER
      while location < Computer.MAX:
        board_copy = dict(board_dict)
        if board_object.is_free_space(location):
          board_copy[location] = self.__player_letter
          if board_object.check_win(board_copy, self.__player_letter):
            board_object.place_piece(location, self.__computer_letter)
            int_var = int(location)
            # breaks out of while loop if player can win
            location = Computer.MAX
            player_can_win = True
          # moves to next spot if current doesnt win
          else:
            location += Computer.INCREMENT
        # moves to next spot if spot is taken
        else:
          location += Computer.INCREMENT
    # prevents computer from making an additional move if it can win or \
    # the player can be blocked
    if computer_can_win or player_can_win:
      pass
    # if computer cant win and player cant be blocked, makes remaining move
    else:
      # goes for a corner, then center, then edge
      if upper_left_open:
        board_object.place_piece(Board.UPPER_LEFT_CORNER, \
                                 self.__computer_letter)
        location = Board.UPPER_LEFT_CORNER
      elif lower_right_open:
        board_object.place_piece(Board.LOWER_RIGHT_CORNER, \
                                 self.__computer_letter)
        location = Board.LOWER_RIGHT_CORNER
      elif lower_left_open:
        board_object.place_piece(Board.LOWER_LEFT_CORNER, \
                                 self.__computer_letter)
        location = Board.LOWER_LEFT_CORNER
      elif upper_right_open:
        board_object.place_piece(Board.UPPER_RIGHT_CORNER, \
                                 self.__computer_letter)
        location = Board.UPPER_RIGHT_CORNER
      elif center_open:
        board_object.place_piece(Board.CENTER, self.__computer_letter)
        location = Board.CENTER
      elif top_edge_open:
        board_object.place_piece(Board.TOP_EDGE, self.__computer_letter)
        location = Board.TOP_EDGE
      elif right_edge_open:
        board_object.place_piece(Board.LEFT_EDGE, self.__computer_letter)
        location = Board.LEFT_EDGE
      elif bottom_edge_open:
        board_object.place_piece(Board.BOTTOM_EDGE, self.__computer_letter)
        location = Board.BOTTOM_EDGE
      else:
        board_object.place_piece(Board.RIGHT_EDGE, self.__computer_letter)
        location = Board.RIGHT_EDGE
      int_var = int(location)

    return int_var
