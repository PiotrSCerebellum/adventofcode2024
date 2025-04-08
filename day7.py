import re

# Part One
def parse_equations(data:str)->list[list[int]]:
    data=data.splitlines()
    pattern = r'(\d+)'
    reports=[]
    for line in data:
        matches = re.findall(pattern, line)
        report=[int(x) for x in matches]
        reports.append(report)
    return reports
def validate_equations(equation:list):
    if len(equation)==2:
        if equation[1]==equation[0]:
            return equation[1]
        else:
            return 0
    mul=validate_equations([equation[0],equation[1]*equation[2],*equation[3:]])
    add=validate_equations([equation[0],equation[1]+equation[2],*equation[3:]])
    if mul>add:
        return mul
    else:
        return add
#Part 2
def validate_equations_new(equation:list):
    if len(equation)==2:
        if equation[1]==equation[0]:
            return equation[1]
        else:
            return 0
    mul=validate_equations_new([equation[0],equation[1]*equation[2],*equation[3:]])
    add=validate_equations_new([equation[0],equation[1]+equation[2],*equation[3:]])
    concat=validate_equations_new([equation[0],int(str(equation[1])+str(equation[2])),*equation[3:]])
    return max(mul,add,concat)
with open(r".\\data\\day7.txt", "r") as file:
    data=file.read()
equations=parse_equations(data)
total=0
total_new=0
for eq in equations:
    total+=validate_equations(eq)
    total_new+=validate_equations_new(eq)
print(f"Total valid calibrations without concat {total} and with {total_new}")