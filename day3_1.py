# -*- coding: utf-8 -*-
# @Author: Jean-Baptiste Faure
# @Date:   2021-12-05 22:19:12
# @Last Modified by:   Jean-Baptiste Faure
# @Last Modified time: 2021-12-05 22:44:13

import utils

def main():
	diagnostics_l = utils.input_to_str_list("inputs/input3.txt") 
	diagonitioc_len = list(diagnostics_l[0]).__len__()
	num_diagnostics = diagnostics_l.__len__()
	one_counters = [0]*diagonitioc_len
	gamma_rate = 0
	epsilon_rate = 0
	for diagnotic in diagnostics_l:
		for idx, bit in enumerate(list(diagnotic)):
			one_counters[idx] = one_counters[idx] + int(bit) 
	one_counters.reverse()
	for idx, one_counter in enumerate(one_counters):
		if one_counter > (num_diagnostics / 2):
			gamma_rate = gamma_rate + 2**idx
		else:
			epsilon_rate = epsilon_rate + 2**idx 

	utils.show_result(str(epsilon_rate*gamma_rate))
 
if __name__ == "__main__":
    main()
