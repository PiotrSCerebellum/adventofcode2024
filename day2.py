import re

def get_reports(data:str)->list[list[int]]:
    data=data.splitlines()
    pattern = r'(\d+)'
    reports=[]
    for line in data:
        matches = re.findall(pattern, line)
        report=[int(x) for x in matches]
        reports.append(report)
    return reports
def check_report_safety(report:list[int])->bool:
    delta=0
    increasing=False
    if report[1]-report[0]>0:
        increasing=True
    for i in range(len(report)-1):
        delta=report[i+1]-report[i]
        if delta>3 or delta<-3 or delta==0:
            return False
        if delta<0 and increasing:
            return False
        if delta>0 and not increasing:
            return False
    return True
def check_report_safety_expanded(report:list[int])->bool:
    safe=False
    all_possibilities=[report[:i] + report[i+1:] for i in range(len(report))]
    for i in range(len(report)):
        safe=check_report_safety(all_possibilities[i])
        if safe:
            return True
    return False
def check_all_reports_old(reports:list[list[int]])->int:
    safe=0
    for report in reports:
        if check_report_safety(report):
            safe+=1
    return safe
def check_all_reports_new(reports:list[list[int]])->int:
    safe=0
    for report in reports:
        if check_report_safety_expanded(report):
            safe+=1
    return safe

with open(r".\\data\\day2.txt", "r") as file:
    data=file.read()
reports=get_reports(data)
safe_old=check_all_reports_old(reports)
safe=check_all_reports_new(reports)
print(f'Safe reports:{safe}. and without overrides:{safe_old}')
