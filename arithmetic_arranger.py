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
  organized_problems = []

  for problem in problems:
    organized_problems.append(generate_problem(problem))

  if give_answer:
    for problem in organized_problems:
      print(problem.find_answer())
  
  #return arranged_problems