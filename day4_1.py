# -*- coding: utf-8 -*-
# @Author: Jean-Baptiste Faure
# @Date:   2021-12-06 00:25:48
# @Last Modified by:   Jean-Baptiste Faure
# @Last Modified time: 2021-12-07 00:21:48

import utils


class Board():
  def __init__(self) -> None:
    self.number_list = []

  def is_in_board(self, val:int):
    return (val in self.number_list)


def main():
  input_data_l = utils.input_to_str_list('inputs/input4_test.txt')
  numbers_l = input_data_l[0].split(',')
  new_board = Board()
  board_l = []
  for input_data in input_data_l[2:]:
    if(input_data == ''):
      board_l.append(new_board)
      new_board = Board()
    else:
      new_board.number_list.append(input_data.split(','))
  board_l.append(new_board)
  print(board_l.__len__())
  
  

  for selected_number in numbers_l:
    for board in board_l:
      if board.is_in_board(selected_number):
        print("in board")



if __name__ == "__main__":
    main()
