# -*- coding: utf-8 -*-
# @Author: Jean-Baptiste Faure
# @Date:   2021-12-05 21:33:44
# @Last Modified by:   Jean-Baptiste Faure
# @Last Modified time: 2021-12-05 22:16:17
import re
import utils


class Coordinates():
  def __init__(self, initial_depth:int, initial_hz_pos:int, initial_aim:int) -> None:
    self.depth = initial_depth
    self.hz_pos = initial_hz_pos
    self.aim = initial_aim

class Action():
  def __init__(self, command:str) -> None:
    self.action = getattr(self, command.split(' ')[0])		
    self.val = int(command.split(' ')[1])
    print("Action : " + self.action.__name__)

  def forward(self, coordinates:Coordinates, val):
    coordinates.hz_pos = coordinates.hz_pos+val
    coordinates.depth = coordinates.depth+coordinates.aim*val

  def up(self, coordinates:Coordinates, val):
    coordinates.aim = coordinates.aim-val
  
  def down(self, coordinates:Coordinates, val):
    coordinates.aim = coordinates.aim+val

  def execute_action(self, coordinates:Coordinates):
    return self.action(coordinates, self.val)


def main():
  
  actions = utils.input_to_str_list("inputs/input2.txt")
  submarine_coords = Coordinates(0,0,0)
  for action_str in actions:
    action = Action(action_str)
    action.execute_action(submarine_coords)
  utils.show_result(str(submarine_coords.depth * submarine_coords.hz_pos))
  
if __name__ == '__main__':
    main()
    