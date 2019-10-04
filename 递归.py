def fact(n):
    return fact_item(n,1)

def fact_item(num,project):
    if num == 1:
        return project
    return fact_item(num-1,num*project)
