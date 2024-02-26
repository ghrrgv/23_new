# три команды
# - прибавить 2
# - сделать четным (*2)
# - сделать нечетным (*2 + 1)
# кол-во программ из 3 в 90
def task(start, end):
    if start==end: return 1
    if start > end: return 0
    if start < end: return task(start+2, end)+task(start*2, end)+task(start*2+1, end)
print(task(3, 90))