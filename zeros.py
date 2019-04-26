
def movezeros(list_):
    count = list_.count(0)
    zeros = [0] * count
    new_list = []
    for i in list_:
        if i != 0:
            new_list.append(i)
    list_ = new_list + zeros
    return list_

a = [1,2,9,0,0,0,0,0,0,5,4,60,90,777,8,0,5,0,7,0]

print(movezeros(a))
