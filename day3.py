import re
def read_data(data:str)->list[tuple[int,int]]:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, data)
    result=[]
    for a,b in matches:
        result.append((int(a),int(b)))
    return result
def remove_inactive(data:str)->str:
    pattern=r"(don't\(\)).*?(do\(\)|$)"
    clean_data = re.sub(pattern,'',data,flags=re.DOTALL)
    return clean_data
def multiply(data:list[tuple[int,int]])->int:
    result=0
    for pair in data:
        result+=pair[0]*pair[1]
    return result


with open(r".\\data\\day3.txt", "r") as file:
    data=file.read()
clean_data=remove_inactive(data)
multiplications=read_data(clean_data)
result=multiply(multiplications)
result_old=multiply(read_data(data))
print(f'Result for part 2 is:{result}, for part one:{result_old}')

