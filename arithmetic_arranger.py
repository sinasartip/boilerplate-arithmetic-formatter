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


class printer():
  def __init__(self, val1, val2, operand, ans, give_answer):
    self.val1 = val1
    self.val2 = val2
    self.operand = operand
    self.ans = ans
    self.outputList = []

    self.start_printer(give_answer)

  def start_printer(self, give_answer):
    self.draw_line_1()
    self.draw_line_2()
    self.draw_line_3()
    if give_answer:
      self.draw_line_4()

  def draw_line_1(self):
    for value in self.val1:
      adjust = 5-len(str(value))
      
      for _ in range(adjust):
        self.outputList.append(" ")  
      
      self.outputList.append(str(value))
      self.outputList.append("    ")

    self.outputList.append("\n")
  
  def draw_line_2(self):
    i = 0
    
    for oprnd in self.operand:
      self.outputList.append(oprnd)
      adjust = 4-len(str(self.val2[i]))

      for _ in range(adjust):
        self.outputList.append(" ")

      self.outputList.append(str(self.val2[i]))
      self.outputList.append("    ")
      i += 1
    
    self.outputList.append("\n")

  def draw_line_3(self):
    for _ in self.val1:
      self.outputList.append("-----")
      self.outputList.append("    ")
    self.outputList.append("\n")

  def draw_line_4(self):
    for ans in self.ans:
      adjust = 5-len(str(ans))
      
      for _ in range(adjust):
        self.outputList.append(" ")

      self.outputList.append(ans)
      self.outputList.append("    ")  

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
    print_ans = printer(val1, val2, operand, ans, give_answer)
    arranged_problemList = print_ans.outputList

  for math_string in arranged_problemList:
    arranged_problems += math_string
  # print(arranged_problems)
  return arranged_problems