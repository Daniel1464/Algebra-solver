import math



'''
All functions reside here.
'''

# Detects whether something can become a float.
def is_floatable(string):
  try:
    variable = float(string)
    return True
  except ValueError:
    return False

    
# Organizes the expression: It groups together all exponential terms and all of the x terms together in a list. This makes it easier to do stuff on the list.
# 5x^2+6x+3 => ['5x^2','+','6x','+','3']
def organize_expression(operation_string):
  operation_list = list(operation_string)
  final_operation_list = []
  int_storage_var = ""
  # This for loop divides the operation string into the numbers and operations
  # Operations are like *, /, +, -, etc. MODULO IS NOT SUPPORTED!
  for i in range(len(operation_list)):
    if operation_list[i] == "+" or operation_list[i] == "-" or operation_list[i] == "*" or operation_list[i] == "/" or operation_list[i] == "=":
      final_operation_list.append(int_storage_var)
      final_operation_list.append(operation_list[i])
      int_storage_var = ""
    elif is_floatable(operation_list[i]) or operation_list[i] == "x" or operation_list[i] == "^" or operation_list[i] == ".":
      int_storage_var += operation_list[i]
    if i == len(operation_list)-1:
      final_operation_list.append(int_storage_var)
  while '' in final_operation_list:
    final_operation_list.remove('')
  return final_operation_list



# Even though python has a built in number multiplying method, it can't multiple together terms witx^2h x. This allows that: for example, 5x*5x^2 would output 25x^3.
def multiply_values(a,b):
  valueOne = list(a)
  valueTwo = list(b)
  degreeOfX = 0

  
  if "x" in valueOne and "^" in valueOne:
    valueOne.remove("x")
    ExponentValue = "".join(valueOne[valueOne.index("^")+1:])
    degreeOfX += int(ExponentValue)
    valueOne = valueOne[:valueOne.index("^")]
  elif "x" in valueOne:
    degreeOfX += 1
    valueOne.remove("x")

  if "x" in valueTwo and "^" in valueTwo:
    valueTwo.remove("x")
    ExponentValue = "".join(valueTwo[valueTwo.index("^")+1:])
    degreeOfX += int(ExponentValue)
    valueTwo = valueTwo[:valueTwo.index("^")]
  elif "x" in valueTwo:
    degreeOfX += 1
    valueTwo.remove("x")
  
  
  valueOne = float("".join(valueOne))
  valueTwo = float("".join(valueTwo))
  FinalValue = str(valueOne*valueTwo)

  if degreeOfX > 1:
    exponentialOfX = "x^"+str(degreeOfX)
    FinalValue += exponentialOfX
  elif degreeOfX == 1:
    FinalValue += "x"
  return FinalValue


# Does the same thing as multiply_values, but for division.
def divide_values(a,b):
  valueOne = list(a)
  valueTwo = list(b)
  degreeOfX = 0

  
  if "x" in valueOne and "^" in valueOne:
    valueOne.remove("x")
    ExponentValue = "".join(valueOne[valueOne.index("^")+1:])
    degreeOfX += int(ExponentValue)
    valueOne = valueOne[:valueOne.index("^")]
  elif "x" in valueOne:
    degreeOfX += 1
    valueOne.remove("x")

  if "x" in valueTwo and "^" in valueTwo:
    valueTwo.remove("x")
    ExponentValue = "".join(valueTwo[valueTwo.index("^")+1:])
    degreeOfX -= int(ExponentValue)
    valueTwo = valueTwo[:valueTwo.index("^")]
  elif "x" in valueTwo:
    degreeOfX -= 1
    valueTwo.remove("x")
  
  
  valueOne = float("".join(valueOne))
  valueTwo = float("".join(valueTwo))
  FinalValue = str(valueOne/valueTwo)

  if degreeOfX > 1:
    exponentialOfX = "x^"+str(degreeOfX)
    FinalValue += exponentialOfX
  elif degreeOfX == 1:
    FinalValue += "x"
  return FinalValue

# Sums everything inside of an array, and returns the final sum.
def sum_array(array):
  final_sum = 0
  for i in range(len(array)):
    final_sum += float(array[i])
  return final_sum

def find_factors(num):
  factor_array = []
  for i in range(abs(int(num))):
    if num%(i+1) == 0:
      factor_array.append(i+1)
  return factor_array

def substitute_into_equation(equation_list,num):
  degree_powers = list(equation_list.keys())
  value = 0
  for i in range(len(degree_powers)):
    value += (equation_list[degree_powers[i]]*num**degree_powers[i])
  return value
    





'''
Actual Code starts here.

'''

print("Note: x must be the only variable, and this can only find rational roots for equations of degree greater than 2.")
while True:
  algebra = input("What do you want to solve?:")
  
  
  # This line of code does 2 things: It splits the equation into the LHS and the RHS, depending on the position of the equal sign. It then calls organize_expression on each half.
  LHS = []
  RHS = []
  organized_expression = organize_expression(algebra)
  for i in range(len(organized_expression)):
    if organized_expression[i] == "=":
      LHS = organized_expression[:i]
      RHS = organized_expression[i+1:]
  
  
  
  
  
  
  # Solves all of the exponent, multiplication and division problems and simplifies them.
  for i in range(len(LHS)):
    if "^" in LHS[i] and not "x" in LHS[i]:
      exponent_index = LHS[i].find("^")
      ValueOne = LHS[i][:exponent_index]
      ValueTwo = LHS[i][exponent_index+1:]
      LHS[i] = str(float(ValueOne)**float(ValueTwo))
  
  for i in range(len(LHS)):
    if LHS[i] == "*":
      LHS[i+1] = multiply_values(LHS[i-1],LHS[i+1])
      LHS[i-1] = "nope"
      LHS[i] = "nope"
    if LHS[i] == "/":
      LHS[i+1] = divide_values(LHS[i-1],LHS[i+1])
      LHS[i-1] = "nope"
      LHS[i] = "nope"
  
  
  
  # For the RHS
  for i in range(len(RHS)):
    if "^" in RHS[i] and not "x" in RHS[i]:
      exponent_index = RHS[i].find("^")
      ValueOne = RHS[i][:exponent_index]
      ValueTwo = RHS[i][exponent_index+1:]
      RHS[i] = str(float(ValueOne)**float(ValueTwo))
  
  for i in range(len(RHS)):
    if RHS[i] == "*":
      RHS[i+1] = multiply_values(RHS[i-1],RHS[i+1])
      RHS[i-1] = "nope"
      RHS[i] = "nope"
    if RHS[i] == "/":
      RHS[i+1] = divide_values(RHS[i-1],RHS[i+1])
      RHS[i-1] = "nope"
      RHS[i] = "nope"
  
  
  
  
  
  
  # Compiles all of the terms on the left hand side into groups, depending on their degree. For example, all "x" terms will be put into the degree 1 array, all constants will be put into the degree 0 array, etc.
  
  LHS_addition_comp = {}
  negative_sign_detected = False
  for i in range(len(LHS)):
    if LHS[i] == "-":
      negative_sign_detected = True
    if (is_floatable(LHS[i]) or "x" in LHS[i]) and negative_sign_detected == True:
      LHS[i] = "-"+ LHS[i]
      negative_sign_detected = False
    if LHS[i] != "nope" and LHS[i] != "+" and LHS[i] != "-" and LHS[i] != "*" and LHS[i] != "/":
      if not "x" in LHS[i]:
        try:
          LHS_addition_comp[0].append(LHS[i])
        except:
          LHS_addition_comp[0] = []
          LHS_addition_comp[0].append(LHS[i])
      elif not "^" in LHS[i]:
        try:
          LHS_addition_comp[1].append(LHS[i])
        except:
          LHS_addition_comp[1] = []
          LHS_addition_comp[1].append(LHS[i])
      else:
        index_of_exponent = LHS[i].find("^")
        
        exponential_value = int("".join(LHS[i][index_of_exponent+1:]))
        try:
          LHS_addition_comp[exponential_value].append(LHS[i])
        except:
          LHS_addition_comp[exponential_value] = []
          LHS_addition_comp[exponential_value].append(LHS[i])
  LHS_degree_comp = list(LHS_addition_comp.keys())
  
  
  
  # For the RHS
  
  RHS_addition_comp = {}
  negative_sign_detected = False
  for i in range(len(RHS)):
    if RHS[i] == "-":
      negative_sign_detected = True
    if is_floatable(RHS[i]) and negative_sign_detected == True:
      RHS[i] = "-"+ RHS[i]
      negative_sign_detected = False
    if RHS[i] != "nope" and RHS[i] != "+" and RHS[i] != "-" and RHS[i] != "*" and RHS[i] != "/":
      if not "x" in RHS[i]:
        try:
          RHS_addition_comp[0].append(RHS[i])
        except:
          RHS_addition_comp[0] = []
          RHS_addition_comp[0].append(RHS[i])
      elif not "^" in RHS[i]:
        try:
          RHS_addition_comp[1].append(RHS[i])
        except:
          RHS_addition_comp[1] = []
          RHS_addition_comp[1].append(RHS[i])
      else:
        index_of_exponent = RHS[i].find("^")
        
        exponential_value = int("".join(RHS[i][index_of_exponent+1:]))
        try:
          RHS_addition_comp[exponential_value].append(RHS[i])
        except:
          RHS_addition_comp[exponential_value] = []
          RHS_addition_comp[exponential_value].append(RHS[i])
  RHS_degree_comp = list(RHS_addition_comp.keys())
  
  
  
  
  
  # This code strips all of the terms inside LHS_addition_comp of x and any exponential values, leaving only the coefficients. This makes it easier to add up the terms.
  for i in range(len(LHS_degree_comp)):
    for j in range(len(LHS_addition_comp[LHS_degree_comp[i]])):
      LHS_term = LHS_addition_comp[LHS_degree_comp[i]][j]
      if "x" in LHS_term:
        index_of_x = LHS_term.find("x")
        LHS_addition_comp[LHS_degree_comp[i]][j] = LHS_term[:index_of_x]
        if LHS_addition_comp[LHS_degree_comp[i]][j] == "":
          LHS_addition_comp[LHS_degree_comp[i]][j] = 1
  # And for the RHS:
  for i in range(len(RHS_degree_comp)):
    for j in range(len(RHS_addition_comp[RHS_degree_comp[i]])):
      RHS_term = RHS_addition_comp[RHS_degree_comp[i]][j]
      if "x" in RHS_term:
        index_of_x = RHS_term.find("x")
        RHS_addition_comp[RHS_degree_comp[i]][j] = RHS_term[:index_of_x] 
  
  

  
  # Replaces the array of coefficients with the sum of all of the coefficients. This is essentially simplifying the expression.
  for i in range(len(LHS_degree_comp)):
    
    LHS_addition_comp[LHS_degree_comp[i]] = sum_array(LHS_addition_comp[LHS_degree_comp[i]])
  
  # For the right hand side:
  for i in range(len(RHS_degree_comp)):
    RHS_addition_comp[RHS_degree_comp[i]] = sum_array(RHS_addition_comp[RHS_degree_comp[i]])
  
  
  
  # Moves everything from the right hand side to the left hand side, which makes the right hand side 0. THis allows us to apply algorithms(like the quadratic formula and Rational root theorem) to solve the equation.
  
  
  for i in range(len(RHS_degree_comp)):
    if RHS_degree_comp[i] in LHS_degree_comp:
      LHS_addition_comp[RHS_degree_comp[i]] = LHS_addition_comp[RHS_degree_comp[i]] - RHS_addition_comp[RHS_degree_comp[i]]
    else:
      LHS_addition_comp[RHS_degree_comp[i]] = 0 - RHS_addition_comp[RHS_degree_comp[i]]
  
  
  # Now, all of the terms have been moved to the LHS.
  
  for i in range(len(LHS_degree_comp)):
    if LHS_addition_comp[LHS_degree_comp[i]] == 0:
      LHS_addition_comp.pop(LHS_degree_comp[i])
  
  LHS_degree_comp = list(LHS_addition_comp.keys())
  
  
  if max(LHS_addition_comp) == 1:
    # Moves the constant term "to the other side", then divides by the degree 1 coefficient.
    try:
      solution = 0 - (LHS_addition_comp[0]/LHS_addition_comp[1])
    except:
      solution = 0
  elif max(LHS_addition_comp) == 2:
    # Applies quadratic formula.
    try:
      a = LHS_addition_comp[2]
    except:
      a = 0
    try:
      b = LHS_addition_comp[1]
    except:
      b = 0
    try:
      c = LHS_addition_comp[0]
    except:
      c = 0
    if int(a) == a:
      a = int(a)
    if int(b) == b:
      b = int(b)
    if int(c) == c:
      c = int(c)
    # Puts it in the quadratic formula notation if solution is irrational.
    try:
      solution1 = ((0-b)+math.sqrt(b**2-4*a*c))/(2*a)
    except:
      solution1 = '(-'+str(b)+'+sqrt('+str(b**2-4*a*c)+'))/'+str(2*a)
    try:
      solution2 = ((0-b)-math.sqrt(b**2-4*a*c))/(2*a)
    except:
      solution2 = '(-'+str(b)+'-sqrt('+str(b**2-4*a*c)+'))/'+str(2*a)
    solution = [solution1,solution2]
  elif max(LHS_addition_comp) >= 3:
    # This applies the rational root theorem to find rational roots

    
    solution = []
    numerator = LHS_addition_comp[min(list(LHS_addition_comp.keys()))]
    denominator = LHS_addition_comp[max(list(LHS_addition_comp.keys()))]
    numerator_factors = find_factors(numerator)
    denominator_factors = find_factors(denominator)
    for i in range(len(numerator_factors)):
      for j in range(len(denominator_factors)):
        rational_root = numerator_factors[i]/denominator_factors[j]
        root_substitution = substitute_into_equation(LHS_addition_comp,rational_root)
        neg_root_substitution = substitute_into_equation(LHS_addition_comp,0-rational_root)
        if root_substitution == 0:
          solution.append(rational_root)
        if neg_root_substitution == 0:
          solution.append(0-rational_root)
    print("Note: Only rational roots will be in the solutions array.")
  print("Solution(s):"+str(solution))
