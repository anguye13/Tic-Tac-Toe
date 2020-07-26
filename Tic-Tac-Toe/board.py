'''
Chinyere Azukwu, Andy Nguyen
cazukwu1@binghamton.edu, anguye13@binghamton.edu
Section A51, Jia Yang
Final Project
'''

'''
Methods
is_free_space(location)
check_win(board, letter)
get_board()
place_piece(location, letter)
reset_board()
'''


# DONE COLLABORATIVELY BY ANDY AND CHINYERE
# Model of a tic-tac-toe board
class Board:
  # Class Variables ---------------------------------------------------------
  UPPER_LEFT_CORNER = 1
  UPPER_RIGHT_CORNER = 3
  LOWER_LEFT_CORNER = 7
  LOWER_RIGHT_CORNER = 9
  TOP_EDGE = 2
  RIGHT_EDGE = 6
  BOTTOM_EDGE = 8
  LEFT_EDGE = 4
  CENTER = 5
  MAX = 10

  # Constructor -------------------------------------------------------------
  def __init__(self):
    # Represents a board where key = location and value = 'x' or 'o'
    self.__board = {
      Board.UPPER_LEFT_CORNER: '',
      Board.TOP_EDGE: '',
      Board.UPPER_RIGHT_CORNER: '',
      Board.LEFT_EDGE: '',
      Board.CENTER: '',
      Board.RIGHT_EDGE: '',
      Board.LOWER_LEFT_CORNER: '',
      Board.BOTTOM_EDGE: '',
      Board.LOWER_RIGHT_CORNER: ''
    }

  # Predicates --------------------------------------------------------------

  # BY CHINYERE AZUKWU
  # param location - an int (1-9) that corresponds to a location on the board
  # checks if a space on the board (dict) is free or not
  def is_free_space(self, location):
    return self.__board[location] == ''

  # BY ANDY NGUYEN
  # param board - a board object OR a dict (self.__board) of a board object
  # param letter - either 'x' or 'o'
  # checks to see if the board is in a winning state
  def check_win(self, board, letter):
    # try block if board argument = board object
    try:
      return (board[Board.UPPER_LEFT_CORNER] == letter and \
              board[Board.TOP_EDGE] == letter and \
              board[Board.UPPER_RIGHT_CORNER] == letter) \
              or \
             (board[Board.LEFT_EDGE] == letter and \
              board[Board.CENTER] == letter and \
              board[Board.RIGHT_EDGE] == letter) \
              or \
             (board[Board.LOWER_LEFT_CORNER] == letter and \
              board[Board.BOTTOM_EDGE] == letter and \
              board[Board.LOWER_RIGHT_CORNER] == letter) \
              or \
             (board[Board.UPPER_LEFT_CORNER] == letter and \
              board[Board.LEFT_EDGE] == letter and \
              board[Board.LOWER_LEFT_CORNER] == letter) \
              or \
             (board[Board.TOP_EDGE] == letter and \
              board[Board.CENTER] == letter and \
              board[Board.BOTTOM_EDGE] == letter) \
              or \
             (board[Board.UPPER_RIGHT_CORNER] == letter and \
              board[Board.RIGHT_EDGE] == letter and \
              board[Board.LOWER_RIGHT_CORNER] == letter) \
              or \
             (board[Board.UPPER_LEFT_CORNER] == letter and \
              board[Board.CENTER] == letter and \
              board[Board.LOWER_RIGHT_CORNER] == letter) \
              or \
             (board[Board.UPPER_RIGHT_CORNER] == letter and \
              board[Board.CENTER] == letter and \
              board[Board.LOWER_LEFT_CORNER] == letter)
    # except block in case board argument = self.__board (dict)
    except TypeError:
      return (board.__board[Board.UPPER_LEFT_CORNER] == letter and \
              board.__board[Board.TOP_EDGE] == letter and \
              board.__board[Board.UPPER_RIGHT_CORNER] == letter) \
              or \
             (board.__board[Board.LEFT_EDGE] == letter and \
              board.__board[Board.CENTER] == letter and \
              board.__board[Board.RIGHT_EDGE] == letter) \
              or \
             (board.__board[Board.LOWER_LEFT_CORNER] == letter and \
              board.__board[Board.BOTTOM_EDGE] == letter and \
              board.__board[Board.LOWER_RIGHT_CORNER] == letter) \
              or \
             (board.__board[Board.UPPER_LEFT_CORNER] == letter and \
              board.__board[Board.LEFT_EDGE] == letter and \
              board.__board[Board.LOWER_LEFT_CORNER] == letter) \
              or \
             (board.__board[Board.TOP_EDGE] == letter and \
              board.__board[Board.CENTER] == letter and \
              board.__board[Board.BOTTOM_EDGE] == letter) \
              or \
             (board.__board[Board.UPPER_RIGHT_CORNER] == letter and \
              board.__board[Board.RIGHT_EDGE] == letter and \
              board.__board[Board.LOWER_RIGHT_CORNER] == letter) \
              or \
             (board.__board[Board.UPPER_LEFT_CORNER] == letter and \
              board.__board[Board.CENTER] == letter and \
              board.__board[Board.LOWER_RIGHT_CORNER] == letter) \
              or \
             (board.__board[Board.UPPER_RIGHT_CORNER] == letter and \
              board.__board[Board.CENTER] == letter and \
              board.__board[Board.LOWER_LEFT_CORNER] == letter)

  # Accessors ---------------------------------------------------------------

  # BY CHINYERE AZUKWU
  # returns self.__board
  def get_board(self):
    return self.__board

  # Mutator -----------------------------------------------------------------

  # BY CHINYERE AZUKWU
  # param location - int (1-9) that corresponds to a location on the board
  # param letter - either 'x' or 'o'
  # places the given letter on the (dict) self.__board
  def place_piece(self, location, letter):
    self.__board[location] = letter

  # BY ANDY NGUYEN
  # resets the (dict) self.__board to the original blank state
  def reset_board(self):
    self.__board = {
      Board.UPPER_LEFT_CORNER: '',
      Board.TOP_EDGE: '',
      Board.UPPER_RIGHT_CORNER: '',
      Board.LEFT_EDGE: '',
      Board.CENTER: '',
      Board.RIGHT_EDGE: '',
      Board.LOWER_LEFT_CORNER: '',
      Board.BOTTOM_EDGE: '',
      Board.LOWER_RIGHT_CORNER: ''
    }
