# define flatten() below...
def flatten(my_list):
  result = []
  for each in my_list:
    if isinstance(each, list):
      print('List found!')
      flat_list = flatten(each)
      print(flat_list)
      result += flat_list
    else:
      result.append(each)
  return result
### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))
