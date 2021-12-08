# -*- coding: utf-8 -*-
# @Author: Jean-Baptiste Faure
# @Date:   2021-12-05 22:19:12
# @Last Modified by:   Jean-Baptiste Faure
# @Last Modified time: 2021-12-05 23:29:35

import utils

def convert_diag_to_decimal(diags:list):
	val = 0
	for idx, diag in enumerate(diags):
		val = val + (int(diag)*(2**idx))
	return val

def sort_by(index:int, sort_by_least: bool, list_to_sort:list):
	"""
	Split List in 2 list with first bit 0 or 1.
	"""
	zero_first_list = []
	zero_is_most = False
	for val in list_to_sort:
		print(val)
	
		if(val[index] != '1'):
			zero_first_list.append(val)
	
	if zero_first_list.__len__() > (list_to_sort.__len__() / 2):
		zero_is_most = True
	else:
		zero_is_most = False # List of 1's begin diags is most
	print(str(zero_is_most))
	if sort_by_least != zero_is_most:
		return zero_first_list
	else:
		return [i for i in list_to_sort if i not in zero_first_list]

def main():
	diagnostics_l = utils.input_to_str_list("inputs/input3.txt") 
	diagonitioc_len = list(diagnostics_l[0]).__len__()
	num_diagnostics = diagnostics_l.__len__()
	idx = 0
	while diagnostics_l.__len__() > 1:
		diagnostics_l = sort_by(idx, False, diagnostics_l)	
		idx = idx + 1
	print(diagnostics_l)
	o2_gen_rating = int(diagnostics_l[0], 2)	
 
	diagnostics_l = utils.input_to_str_list("inputs/input3.txt") 
	idx = 0
	while diagnostics_l.__len__() > 1:
		diagnostics_l = sort_by(idx, True, diagnostics_l)	
		idx = idx + 1
	print(diagnostics_l)
	co2_gen_rating = int(diagnostics_l[0], 2)
 
	utils.show_result(str(o2_gen_rating*co2_gen_rating))
	
if __name__ == "__main__":
    main()
