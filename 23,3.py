# две команды
# - прибавить 1
# - увеличить кол-во десятков на 1
# кол-во программ из 2 в 45
# хуй
def task(start, end):
    if start > end: return 0
    if start == end: return 1
    return task(start+1, end)+task(start+10, end)
print(task(2, 45))