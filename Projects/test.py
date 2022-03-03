# # def arithmetic_arranger(problems):

# #     # print(len(problems))
# #     arranged_problems = []
# #     if (len(problems) <= 5 ):
# #         print("in arg <= 5")
# #     else:
# #         raise Exception("Error: Too many problems.")
# #     for i in range(len(problems)):
# #         sign = problems[i].split(" ")
# #         print("spliting")
# #         for c in range(0,3,2):
# #             if sign[c].isdigit():
# #                 print("isdigit check")
# #                 if len(sign[c]) <=4:
# #                         print("less then 4 operands")
# #                 else: raise Exception("Error: Numbers cannot be more than four digits.")
# #             else:
# #                 raise Exception("Error: Numbers must only contain digits.")
# #         for i in range(len(problems)):
# #             sign = problems[i].split(" ")
# #             print("spliting")
# #             if sign[1] == '+':
# #                     su = int(sign[0]) + int(sign[2])
# #                     # print(sum)
# #                     arranged_problems.append(su)
# #             elif sign[1] == '-':
# #                     sub = int(sign[0]) - int(sign[2])
# #                     print(sub)
# #                     arranged_problems.append(sub)
# #             else:
# #                 raise Exception("Error: Operator must be '+' or '-'.")


# #     return arranged_problems

# # ====================================================


# # Exception Handling function
# def exception_handling(number1, number2, operator):
#     # Only digit exception
#     try:
#         int(number1)
#     except:
#         return "Error: Numbers must only contain digits."
#     try:
#         int(number2)
#     except:
#         return "Error: Numbers must only contain digits."
#     # More than 4 digit no. exception
#     try:
#         if len(number1) > 4 or len(number2) > 4:
#             raise BaseException
#     except:
#         return "Error: Numbers cannot be more than four digits."
#     # Operator must be + | - exception.
#     try:
#         if operator != '+' and operator != '-':
#             raise BaseException
#     except:
#         return "Error: Operator must be '+' or '-'."
#     return ""


# def arithmetic_arranger(problems, displayMode=False):

#     start = True
#     side_space = "    "
#     line1 = line2 = line3 = line4 = ""
#     # Too many Problem exception
#     try:
#         if len(problems) > 5:
#             raise BaseException
#     except:
#         return "Error: Too many problems."
#     for prob in problems:
#         # Splitting the Problem into separate strings
#         separated_problem = prob.split()
#         # storing number 1
#         number1 = separated_problem[0]
#         # Storing the operator sign
#         operator = separated_problem[1]
#         # storing number 2
#         number2 = separated_problem[2]
#         exp = exception_handling(number1, number2, operator)
#         if exp != "":
#             return exp
#         no1 = int(number1)
#         no2 = int(number2)
#         # space contains the max no. os spaces required.
#         space = max(len(number1), len(number2))
#         # For first arithmetic arragement
#         if start == True:
#             line1 += number1.rjust(space + 2)
#             line2 += operator + ' ' + number2.rjust(space)
#             line3 += '-' * (space + 2)
#             if displayMode == True:
#                 if operator == '+':
#                     line4 += str(no1 + no2).rjust(space + 2)
#                 else:
#                     line4 += str(no1 - no2).rjust(space + 2)
#             start = False
#         # Other than first arithmetic arragement
#         else:
#             line1 += number1.rjust(space + 6)
#             line2 += operator.rjust(5) + ' ' + number2.rjust(space)
#             line3 += side_space + '-' * (space + 2)
#             if displayMode == True:
#                 if operator == '+':
#                     line4 += side_space + str(no1 + no2).rjust(space + 2)
#                 else:
#                     line4 += side_space + str(no1 - no2).rjust(space + 2)
#     # displayMode is Ture then append line4
#     if displayMode == True:
#         return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
#     return line1 + '\n' + line2 + '\n' + line3




def expt(no1,no2,op):
  try:
    int(no1)
  except:
    return "Error: Numbers must only contain digits."
  try:
    int(no2)
  except:
    return "Error: Numbers must only contain digits."
  # more then 4
  try:
    if len(no1) > 4 or len(no2)>4:
      raise BaseException
  except:
    return "Error: Numbers cannot be more than four digits."
  #oprator
  try:
    if op != '+' and op != '-':
      raise BaseException
  except:
    return "Error: Operator must be '+' or '-'."
  return ""


def arithmetic_arranger(problems,displaymode=False):
  start = True
  side_space = "    "
  line1 = line2 = line3 = line4 =""
  # too many problems
  try:
    if len(problems) > 5:
      raise BaseException
  except:
    return "Error: Too many problems."

  for p in problems:

    sep = p.split()
    no1 =  sep[0]
    no2 = sep[2]
    op = sep[1]
    # print(op)
    exp = expt(no1, no2, op)
    if exp != "":
      return exp
    nom1 = int(no1)
    nom2 = int(no2)
    # which every is larger that sets default space
    space = max(len(no1), len(no2))
    if start == True:
      line1 += no1.rjust(space+2)
      line2 += op + ' '+ no2.rjust(space)
      line3 += '-'*(space+2)
      if displaymode == True:
        if op == '+':
          line4 +=str(nom1+nom2).rjust(space+2)
        else:
          line4 +=str(nom1+nom2).rjust(space+2)
      start = False
    else:
      line1 += no1.rjust(space+6)
      line2 += op.rjust(5)+' '+ no2.rjust(space)
      line3 += side_space + '-'*(space+2)
      if displaymode == True:
        if op =='+':
          line4 += side_space + str(nom1+nom2).rjust(space+2)
        else:
          line4 += side_space + str(nom1-nom2).rjust(space+2)
  if displaymode == True:
    return line1 + '\n' + line2 + '\n'+ line3 +'\n'+line4
  else:
    return line1 + '\n' + line2 + '\n'+ line3


# print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49",'98 + 3g5']))



