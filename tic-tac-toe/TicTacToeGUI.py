'''
Chinyere Azukwu, Andy Nguyen
cazukwu1@binghamton.edu, anguye13@binghamton.edu
Section A51, Jia Yang
Final Project
'''
'''
Tic-Tac-Toe GUI Class
3 x 3 board
'''
'''
Methods
update_text_var(text_var)
confirm_choice()
turn_counter()
click(text_var)
computer_moves()
reset_screen()
'''

# Imports -------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
from tic_tac_toe import *
from board import *
from computer import *

# Constants -----------------------------------------------------------------
MAX_TURNS = 10


# Class that sets up GUI
class TicTacToeGUI:
  # DONE COLLABORATIVELY BY CHINYERE AND ANDY
  def __init__(self):
    # Game state flag
    self.__game_state = 'playing'
    # Creates window
    self.__win = Tk()
    # creates Title of window
    self.__win.title("Tic-Tac-Toe")
    # Creates the size of the window
    self.__win.geometry('600x800')
    # creates Screen objects of classes Board, Computer and Tic_Tac_Toe
    self.__board = Board()
    self.__computer = Computer()
    self.__game_logic = Tic_Tac_Toe()
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var1 = StringVar()
    self.__text_var1.set('   ')
    self.__top_layer1 = Button(self.__win, textvariable=self.__text_var1, \
                               font=("Times", 190), \
                               command=lambda: self.click(self.__text_var1))
    self.__top_layer1.grid(row=2, column=1)
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var2 = StringVar()
    self.__text_var2.set('   ')
    self.__top_layer2 = Button(self.__win, textvariable=self.__text_var2,\
                               font=("Times", 190), \
                               command=lambda: self.click(self.__text_var2))
    self.__top_layer2.grid(row=2, column=2)
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var3 = StringVar()
    self.__text_var3.set('   ')
    self.__top_layer3 = Button(self.__win, textvariable=self.__text_var3, \
                               font=("Times", 190), \
                               command=lambda: self.click(self.__text_var3))
    self.__top_layer3.grid(row=2, column=3)
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var4 = StringVar()
    self.__text_var4.set('   ')
    self.__mid_layer1 = Button(self.__win, textvariable=self.__text_var4, \
                               font=("Times", 190), \
                               command=lambda: self.click(self.__text_var4))
    self.__mid_layer1.grid(row=3, column=1)
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var5 = StringVar()
    self.__text_var5.set('   ')
    self.__mid_layer2 = Button(self.__win, textvariable=self.__text_var5,\
                               font=("Times", 190), \
                               command=lambda: self.click(self.__text_var5))
    self.__mid_layer2.grid(row=3, column=2)
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var6 = StringVar()
    self.__text_var6.set('   ')
    self.__mid_layer3 = Button(self.__win, textvariable=self.__text_var6, \
                               font=("Times", 190), \
                               command=lambda: self.click(self.__text_var6))
    self.__mid_layer3.grid(row=3, column=3)
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var7 = StringVar()
    self.__text_var7.set('   ')
    self.__bottom_layer1 = Button(self.__win, textvariable=self.__text_var7, \
                                  font=("Times", 190), \
                                  command=lambda: self.click(self.__text_var7))
    self.__bottom_layer1.grid(row=4, column=1)
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var8 = StringVar()
    self.__text_var8.set('   ')
    self.__bottom_layer2 = Button(self.__win, textvariable=self.__text_var8, \
                                  font=("Times", 190), \
                                  command=lambda: self.click(self.__text_var8))
    self.__bottom_layer2.grid(row=4, column=2)
    # creates button and creates string variable that will intitially
    # start with an empy space and change to 'X' or 'O' depending on if it is
    # the user or computer's turn
    self.__text_var9 = StringVar()
    self.__text_var9.set('   ')
    self.__bottom_layer3 = Button(self.__win, textvariable=self.__text_var9,\
                                  font=("Times", 190), \
                                  command=lambda: self.click(self.__text_var9))
    self.__bottom_layer3.grid(row=4, column=3)
    # creates 2 Radio Buttons that will prompt the player to choose if they
    # want to be either 'X' or 'O'
    self.__player_var = StringVar()
    self.__playerX_choice = Radiobutton(self.__win, text='X', variable=\
                                        self.__player_var, value='X')
    self.__playerO_choice = Radiobutton(self.__win, text='O', variable=\
                                        self.__player_var, value='O')
    self.__confirm_button = Button(self.__win, text="Confirm", command=\
                                   self.confirm_choice)
    self.__playerX_choice.grid(row=1, column=1)
    self.__playerO_choice.grid(row=1, column=2)
    self.__confirm_button.grid(row=1, column=3)
    # Establishes scoreboard to display how many times the user won
    self.__player = Label(self.__win, text="Player Score:")
    self.__player.grid(row=2, column=4)
    self.__player_score = IntVar()
    self.__player_score.set(0)
    self.__player_score_label = Label(self.__win, textvariable=\
                                      self.__player_score)
    self.__player_score_label.grid(row=2, column=5)
    # Establishes scroreboard to display how many times the computer won
    self.__cpu = Label(self.__win, text="CPU Score:")
    self.__cpu.grid(row=3, column=4)
    self.__cpu_var = IntVar()
    self.__cpu_var.set(0)
    self.__cpu_var_label = Label(self.__win, textvariable=self.__cpu_var)
    self.__cpu_var_label.grid(row=3, column=5)
    # Establishes scoreboard to display how many times there was a draw/tie
    self.__draw = Label(self.__win, text="Draw:")
    self.__draw.grid(row=4, column=4)
    self.__draw_var = IntVar()
    self.__draw_var.set(0)
    self.__draw_var_label = Label(self.__win, textvariable=self.__draw_var)
    self.__draw_var_label.grid(row=4, column=5)
    # creates button to clear and reset board
    self.__restart_button = Button(self.__win, text="Restart", \
                                   command=self.reset_screen)
    # creates button to close window when the usr feels like quiiting
    self.__quit_button = Button(self.__win, text="Quit", command=\
                                self.__win.destroy)
    self.__restart_button.grid(row=6, column=1)
    self.__quit_button.grid(row=6, column=3)
    mainloop()

  # Mutators ----------------------------------------------------------------

  # BY ANDY NGUYEN
  # param text_var - (StringVar) that needs to be updated with 'x' or 'o'
  # Function updates the button to 'x' or 'o' when it is clicked on
  def update_text_var(self, text_var):
    text_var.set(self.__computer.get_player_letter() if \
                 str(text_var.get()) == '   ' and \
                 self.__game_logic.get_whose_turn() == 'player' else \
                 self.__computer.get_computer_letter())

  # BY CHINYERE AZUKWU
  # Function that confirms who is 'X' and who is 'O' as well as determines the
  # who starts first
  def confirm_choice(self):
    if self.__computer.get_player_letter() == ' ':
      if str(self.__player_var.get()):
        messagebox.showinfo('Choice', 'You chose ' + \
                            str(self.__player_var.get()))
        self.__computer.set_player_letter(self.__player_var.get())
        self.__computer.set_computer_letter()
        self.__game_logic.set_whose_turn()
        self.computer_moves()
      else:
        messagebox.showinfo('Error', "Please select a letter")
    else:
      messagebox.showinfo("Error", "Letter already selected")

  # BY ANDY NGUYEN
  # Determines game state (win/lose/tie) and increments/tracks turns
  def turn_counter(self):
    if self.__board.check_win(self.__board, \
                              self.__computer.get_player_letter()):
      if self.__game_state == 'playing':
        messagebox.showinfo("Congratulations", "You win!")
        self.__player_score.set(int(self.__player_score.get()) + 1)
        self.__game_state = 'end'
    elif self.__board.check_win(self.__board, \
                                self.__computer.get_computer_letter()):
      if self.__game_state == 'playing':
        messagebox.showinfo("Sorry", "You lose!")
        self.__cpu_var.set(int(self.__cpu_var.get()) + 1)
        self.__game_state = 'end'
    elif self.__game_logic.get_turn_count() >= MAX_TURNS:
      if self.__game_state == 'playing':
        messagebox.showinfo("Draw", "Tie game!")
        self.__draw_var.set(int(self.__draw_var.get()) + 1)
        self.__game_state = 'end'

  # BY ANDY NGUYEN
  # param text_var - (StringVar) that is clicked on to display 'x' or 'o'
  # Function that when a user clicks a button it will show either 'X' or 'O'
  # Depending on the choice of the user and makes the computer move
  def click(self, text_var):
    if self.__computer.get_player_letter() == ' ' and \
      self.__game_state == 'playing':
      messagebox.showinfo("Error", "Select a letter before playing")
    else:
      if self.__game_state == 'playing':
        location = ''
        if text_var is self.__text_var1:
          location = 1
        elif text_var is self.__text_var2:
          location = 2
        elif text_var is self.__text_var3:
          location = 3
        elif text_var is self.__text_var4:
          location = 4
        elif text_var is self.__text_var5:
          location = 5
        elif text_var is self.__text_var6:
          location = 6
        elif text_var is self.__text_var7:
          location = 7
        elif text_var is self.__text_var8:
          location = 8
        else:
          location = 9
        if self.__board.is_free_space(location):
          self.update_text_var(text_var)
          self.__board.place_piece(location, \
                                   self.__computer.get_player_letter())
          self.__game_logic.increment_turn_count()
          self.__game_logic.set_whose_turn()
          self.turn_counter()
          self.computer_moves()
          self.turn_counter()
      else:
        messagebox.showinfo("Error", "Game has ended")

  # BY CHINYERE AZUKWU
  # Function that displays the choice of the computer
  def computer_moves(self):
    if self.__game_logic.get_whose_turn() == 'computer':
      if self.__game_state == 'playing':
        location = self.__computer.computer_goes(self.__board)
        self.__game_logic.increment_turn_count()
        if location == 1:
          self.update_text_var(self.__text_var1)
        elif location == 2:
          self.update_text_var(self.__text_var2)
        elif location == 3:
          self.update_text_var(self.__text_var3)
        elif location == 4:
          self.update_text_var(self.__text_var4)
        elif location == 5:
          self.update_text_var(self.__text_var5)
        elif location == 6:
          self.update_text_var(self.__text_var6)
        elif location == 7:
          self.update_text_var(self.__text_var7)
        elif location == 8:
          self.update_text_var(self.__text_var8)
        elif location == 9:
          self.update_text_var(self.__text_var9)
        self.__game_logic.set_whose_turn()

  # BY ANDY NGUYEN
  # Function that resets the board and the amount of turns
  def reset_screen(self):
    self.__game_state = 'playing'
    self.__board.reset_board()
    self.__game_logic.reset_turn_count()
    self.__computer.reset_letters()
    self.__game_logic.reset_whose_turn()
    self.__text_var1.set("   ")
    self.__text_var2.set("   ")
    self.__text_var3.set("   ")
    self.__text_var4.set("   ")
    self.__text_var5.set("   ")
    self.__text_var6.set("   ")
    self.__text_var7.set("   ")
    self.__text_var8.set("   ")
    self.__text_var9.set("   ")

TicTacToeGUI()
