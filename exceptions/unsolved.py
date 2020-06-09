def parse_input(user_input):

  input_list = user_input.split(' ')
  ## write codes and exceptions
  if len(input_list)!=3:
    raise Exception('saydan artiqdir.')
  try:
    n1 = float(input_list[0])
    n2 = float(input_list[2])
  
  except:
    raise Exception('error')
  ## this function must return number1, operation, number2
  return n1 , input_list[1] , n2



def calculate(n1, op, n2):
  
  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2
  #write exception
  
  raise Exception('2-ci arqument qebul olunan deil')


while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)