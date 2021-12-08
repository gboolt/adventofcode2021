"""
Open file and return a int list
"""
def input_to_int_list(input_name : str):
  with open(input_name, 'r') as fp:
    data = []
    for l in fp.readlines():
      data.append(int(l.replace("\n","")))
    print(input_name + " has been converted to list.")
  return data

"""
Open file and return a list
"""
def input_to_str_list(input_name : str):
  with open(input_name, 'r') as fp:
    data = []
    for l in fp.readlines():
      data.append(str(l.replace("\n","")))
    print(input_name + " has been converted to list.")
  return data

"""
Print Result 
"""
def show_result(res):
  print("Result is " + str(res))

  
def get_difference(list_a, list_b):
    return set(list_a)-set(list_b)