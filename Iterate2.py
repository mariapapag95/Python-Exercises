var1=[2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

def medfunct(array):
    n=len(array)
    median = sorted(array)[n//2]
    average = sum(array)/n
    most_frequent = max(set(array), key=array.count)
    answers=[median,average,most_frequent]
    return answers
print(medfunct(var1))