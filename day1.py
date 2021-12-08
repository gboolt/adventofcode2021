# -*- coding: utf-8 -*-
# @Author: Jean-Baptiste Faure
# @Date:   2021-12-01 13:11:20
# @Last Modified by:   Jean-Baptiste Faure
# @Last Modified time: 2021-12-05 21:33:12
import utils


def get_buffer_sum(start_index:int, full_buffer:list):
  return (full_buffer[start_index]+full_buffer[start_index+1]+full_buffer[start_index+2])

if __name__ == '__main__':
	
	num_increased = 0
	depths = utils.input_to_int_list("inputs/input1.txt")
	depth_prev = depths[0]		
	for depth in depths[1:]:
		if depth > depth_prev:
			num_increased = num_increased + 1
		depth_prev = depth
	print("Number of depth increased : " + str(num_increased))
	pass

	num_increased = 0
	depths = utils.input_to_int_list("inputs/input1.txt")
	depth_sum = get_buffer_sum(0, depths)
	for index, depth in enumerate(depths[1:-1]):
		depth_sum_new = get_buffer_sum(index, depths) 
		if depth_sum_new > depth_sum:
			num_increased = num_increased + 1
		depth_sum = depth_sum_new
	print("Number of depth increased : " + str(num_increased))
	pass
	
 
 