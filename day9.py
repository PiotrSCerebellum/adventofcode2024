

def decompress_data(data:str):
    result=[]
    id=0
    for char in enumerate(data):
        if char[0]%2==0:
            result+= [str(id) for _ in range(int(char[1]))]
            id+=1
        else:
            result+= ['.' for _ in range(int(char[1]))]
    return result
def compress_data(data:list):
    file_space=[]
    while data:
        if data[0]!='.':
            file_space.append(data[0])
            data=data[1:]
            continue
        else:
            char='.'
            data=data[1:]
            while char=='.' and data:
                data,char=(data[0:-1],data[-1])
                if char=='.':
                    continue
                else:
                    file_space.append(char)
    return file_space
def calculate_check_sum(data:list):
    result=0
    for i in range(len(data)):
        result+=i*int(data[i])
    return result

with open(r".\\data\\day9.txt", "r") as file:
    data=file.read().replace('\n','')
compressed_data=compress_data(decompress_data(data))
checksum=calculate_check_sum(compressed_data)
print(f'Checksum is: {checksum}')
