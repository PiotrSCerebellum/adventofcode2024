def decompress_data(data:str):
    files=[]
    free_spaces=[]
    id=0
    for char in enumerate(data):
        if char[0]%2==0:
            files.append([char[0],int(char[1]),str(id)])
            id+=1
        else:
            free_spaces.append([char[0],int(char[1]),'.'])
    return files,free_spaces
def compress_data(files:list,free_spaces:list):
    for i in range(len(files)-1,-1,-1):
        for j in range(len(free_spaces)):
            if files[i][0]<free_spaces[j][0]:
                continue
            if files[i][1]<=free_spaces[j][1]:
                free_spaces.append([files[i][0],files[i][1],'.'])
                free_spaces[j][1]-=files[i][1]
                indent=files[i][0]=free_spaces[j][0]
                for f in files:
                    if f[0]>indent:
                        f[0]+=1
                for s in free_spaces:
                    if s[0]>=indent:
                        s[0]+=1
    return files,free_spaces
                

def calculate_check_sum(files:list,spaces:list):
    result=0
    index=0
    disk=sorted(files+spaces,key= lambda x : x[0])
    final_string=''
    for item in disk:
        final_string+=item[1]*item[2]
    for item in disk:
        for i in range(item[1]):
            if item[2]!='.':
                result+=index*int(item[2])
            index+=1
    return result

with open(r".\\data\\day9.txt", "r") as file:
    data=file.read().replace('\n','')
files,spaces=decompress_data(data)
files,spaces=compress_data(files,spaces)
checksum=calculate_check_sum(files,spaces)
print(f'Checksum is: {checksum}')
