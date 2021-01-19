class arithmeticProblem():
  def __init__(self, value_1: str, operand: str, value_2: str):
    self.value_1 = int(value_1)
    self.value_2 = int(value_2)
    self.operand = operand
    self.check_operand()
    self.error_flag = False

  def check_operand(self):
    if self.operand != '+' and self.operand != '-':
      self.error_flag = True
      return("Error: Operator must be '+' or '-'.")

  def find_answer(self):
    if self.error_flag == False:
      if self.operand == '+':
        return str(self.value_1 + self.value_2)
      elif self.operand == '-':
        return str(self.value_1 - self.value_2)
    else:
      return ""

def generate_problem(problem, val1, val2, operand, error, ans):
  split_problem = arithmeticProblem(*problem.split())

  val1.append(split_problem.value_1)
  val2.append(split_problem.value_2)
  operand.append(split_problem.operand)
  ans.append(split_problem.find_answer())
  if split_problem.error_flag:
    error.append(True)
  else:
    error.append(False)

  return (val1, val2, operand, error, ans)

def append_value(valueList, OutputList, adjust_side):
  for value in valueList:
    adjust = 4-len(str(value))
    if adjust_side == 'left':
      for _ in range(adjust):
        OutputList.append(" ")  
    
    OutputList.append("    ")
    OutputList.append(str(value))

    if adjust_side == 'right':
      for _ in range(adjust):
        OutputList.append(" ")  

  return OutputList
  

def arithmetic_arranger(problems, give_answer = False):
  #TODO : check the number of problems given
  val1 = []
  val2 = []
  operand = []
  error = []
  ans = []
  arranged_problemList = []
  arranged_problems = ""

  for problem in problems:
    val1,val2,operand,error,ans = generate_problem(problem, val1, val2, operand,                                                  error, ans)

  if error.count(True) > 1:    
    arranged_problemList.append(problem.check_operand())
  else:
    arranged_problemList = append_value(val1, arranged_problemList,'left')
    arranged_problemList.append("\n")
    arranged_problemList = append_value(operand, arranged_problemList,'right')
    arranged_problemList = append_value(val2, arranged_problemList,'left')
    arranged_problemList.append("\n")
    for _ in range(len(val1)):
      arranged_problemList.append("    ")
      arranged_problemList.append("-----")
    arranged_problemList.append("\n")
    if give_answer:
      arranged_problemList = append_value(ans, arranged_problemList,'left')

  for math_string in arranged_problemList:
    arranged_problems += math_string
  print(arranged_problems)
  #return arranged_problems