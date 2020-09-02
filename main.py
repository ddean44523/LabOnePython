def cel_to_far(c): 
  temp_in_f = (c *9/5) + 32
  return print(temp_in_f)
def far_to_cel(f):
  temp_in_c = (f - 32) *5/9
  return print(temp_in_c)

def lab_one():
  temp = float( input("Enter temperature: "))
  unit = input("Enter unit in F/f or C/c:")
  if unit == "F" or unit == "f":
    print(far_to_cel(temp))
  elif unit == "C" or unit == "c":
    print(cel_to_far(temp))
  else:
    print("Invalid unit("+unit+").")


lab_one()