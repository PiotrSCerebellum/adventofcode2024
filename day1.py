
import re
import math

def get_lists(data:str)->tuple[list[int],list[int]]:
    pattern = r'(\d+)\s+(\d+)'
    matches = re.findall(pattern, data)
    first_list=[]
    second_list=[]
    for a, b in matches:
        first_list.append(int(a))
        second_list.append(int(b))
    return first_list,second_list
def get_distance(first_list:list[int],second_list:list[int])->int:
    first_list.sort()
    second_list.sort()
    distance=0
    for i in range(len(first_list)):
        new_distance=abs(first_list[i]-second_list[i])
        distance+=new_distance
    return distance
def get_occurance(the_list:list[int])->tuple[int,int,list[int]]:
    number=the_list[0]
    length=len(the_list)
    filtered_list=[x for x in the_list if x != number]
    new_length=len(filtered_list)
    occurances=length-new_length
    return number,occurances,filtered_list
def get_all_occurances(second_list:list[int])->list[tuple[int,int]]:
    list_length=len(second_list)
    source_list=second_list
    occurance_list=[]
    while list_length!=0:
        number,occurances,source_list=get_occurance(source_list)
        occurance_list.append((number,occurances))
        list_length=len(source_list)
    return occurance_list
def get_similarity_score(first_occurance_list:list[tuple[int,int]],second_occurance_list:list[tuple[int,int]])->int:
    score=0
    first_source_list=first_occurance_list
    second_source_list=second_occurance_list
    while len(first_source_list)!=0 and len(second_source_list)!=0:
        if first_source_list[-1][0]==second_source_list[-1][0]:
            a=first_source_list.pop()
            b=second_source_list.pop()
            new_score=a[0]*a[1]*b[1]
            score+=new_score
        elif first_source_list[-1][0]>second_source_list[-1][0]:
            first_source_list.pop()
        elif first_source_list[-1][0]<second_source_list[-1][0]:
            second_source_list.pop()
        else:
            print('Error occured')
    return score

    
with open(r".\\data\\day1.txt", "r") as file:
    data=file.read()
lists=get_lists(data)
distance=get_distance(lists[0],lists[1])
print(f'Distance is {distance}')
first_occurance_list=get_all_occurances(lists[0])
second_occurance_list=get_all_occurances(lists[1])
similarity_score=get_similarity_score(first_occurance_list,second_occurance_list)
print(f'Similarity score:{similarity_score}')
    

