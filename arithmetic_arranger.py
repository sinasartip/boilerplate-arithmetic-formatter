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

def generate_problem(problem):
  return arithmeticProblem(*problem.split())

def arithmetic_arranger(problems, give_answer = False):
  #TODO : check the number of problems given
  split_problems = []
  arranged_problemList = []
  arranged_problems = ""

  for problem in problems:
    split_problems.append(generate_problem(problem))

  
  for problem in split_problems:
    if problem.error_flag:
      arranged_problemList.append(problem.check_operand())
      break
    arranged_problemList.append(str(problem.value_1))
    arranged_problemList.append("\n")
    arranged_problemList.append(problem.operand)
    arranged_problemList.append("\n")
    arranged_problemList.append(str(problem.value_2))
    arranged_problemList.append("\n")

    if give_answer:
      arranged_problemList.append("-----")
      arranged_problemList.append("\n")
      arranged_problemList.append(problem.find_answer())
      arranged_problemList.append("\n")
  
  for math_string in arranged_problemList:
    arranged_problems += math_string
  print(arranged_problems)
  #return arranged_problems