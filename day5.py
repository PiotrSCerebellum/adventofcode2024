import re
import math

def make_ruleset(rules:str)->dict:
    ruleset={}
    pattern=r"(\d+)\|(\d+)"
    for a,b in re.findall(pattern,rules):
        if int(a) in ruleset:
            ruleset[int(a)].add(int(b))
        else:
            ruleset.update({int(a):{int(b)}})
    return ruleset
def read_updates(updates:str)->list[int]:
    pages=[]
    for update in updates.splitlines():
        pages.append([int(x) for x in update.split(',')] )
    return pages
def check_update(ruleset:dict,updates:list[int])->int:
    mid_number_total=0
    corrected_total=0
    for pages in updates:
        correct = validate(ruleset, pages)
        if not correct:
            corrected_total+=get_correct_order(pages,ruleset)[int(math.floor(len(pages)/2))]
        else:
            mid_number_total+=pages[int(math.floor(len(pages)/2))]
    return mid_number_total,corrected_total

def validate(ruleset:dict, pages:list)->bool:
    for i in range(len(pages)-1,-1,-1):
        if pages[i] not in ruleset:
            continue 
        rule=ruleset[pages[i]]
        current_pages=set(pages[0:i])
        if not current_pages.isdisjoint(rule):
            return False
    return True

def get_correct_order(pages:list,ruleset:dict)->list:
    adjecency_dict={}
    correctted_pages=[]
    for page in pages:
        intersection=set()
        if page in ruleset:
            intersection=set(pages).intersection(ruleset[page])
        adjecency_dict.update({page:intersection})
    while len(adjecency_dict)>0:
        for key in adjecency_dict:
            if not bool(adjecency_dict[key]):
                adjecency_dict.pop(key)
                correctted_pages.append(key)
                for k in adjecency_dict.keys():
                    adjecency_dict[k].remove(int(key))
                break
                
    return correctted_pages[::-1]



                





with open(r".\\data\\day5.txt", "r") as file:
    data=file.read()
rules,updates=re.split(r'\n\s*\n', data)
ruleset=make_ruleset(rules)
pages=read_updates(updates)
total,corrected_total=check_update(ruleset,pages)
print(f'Total of mid page numbers: {total},\n Corrected total is :{corrected_total} ')
