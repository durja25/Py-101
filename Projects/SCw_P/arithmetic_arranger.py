def expt(no1, no2, op):
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
        if len(no1) > 4 or len(no2) > 4:
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

def arithmetic_arranger(problems, displaymode=False):
    start = True
    side_space = "    "
    line1 = line2 = line3 = line4 = ""
    # too many problems
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."

    for p in problems:
        sep = p.split()
        no1 = sep[0]
        no2 = sep[2]
        op = sep[1]
        exp = expt(no1, no2, op)
        if exp != "":
            return exp
        # which every is larger that sets default space
        space = max(len(no1), len(no2))
        nom1 = int(no1)
        nom2 = int(no2)
        if start == True:
            line1 += no1.rjust(space + 2)
            line2 += op + ' ' + no2.rjust(space)
            line3 += '-' * (space + 2)
            if displaymode == True:
                if op == '+':
                    line4 += str(nom1 + nom2).rjust(space + 2)
                else:
                    line4 += str(nom1 - nom2).rjust(space + 2)
            start = False
        else:
            line1 += no1.rjust(space + 6)
            line2 += op.rjust(5) + ' ' + no2.rjust(space)
            line3 += side_space + '-' * (space + 2)
            if displaymode == True:
                if op == '+':
                    line4 += side_space + str(nom1 + nom2).rjust(space + 2)
                else:
                    line4 += side_space + str(nom1 - nom2).rjust(space + 2)
    if displaymode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        return line1 + '\n' + line2 + '\n' + line3

# ====================================================
# # print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(['1 + 2', '1 - 9380']))
# print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
# print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
# print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87']))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
