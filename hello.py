def tarawa(x, y):
    return x+y


sunaye = ['Adam', 'Abdullahi', 'Mujaheed', 'Ammar', 'Kowama']

def our_join(list, param):
    result = ''
    for item in list:
        new_item  = '{}{}'.format(item, param)
        result+=new_item
    return result

def our_split(list, st, end):

    result = []
    for i in range(st, end):
        result.append(list[i])
    return result

"""
Dictionary
"""

myDict = {
    'version':'0.2.1',
    'config':[
        1,2,3
    ]
}


myDict['name']= "Abdullahi"
myDict['age'] =30

#print(myDict)

garuruwa = ["Kano", "Lafia", "Zaria", "Abuja", "Kaduna"]
# for gari in garuruwa:
#     print(gari)

odd  = []
for x in range(1, 10):
    #print(x)
    if x%2 == 1:
        odd.append(x)

# tsayi = len(odd)
#print(odd[tsayi-1])

# for i in range(0, len(garuruwa)):
#     #print(i)
#     print('The position of {} is {}'.format(garuruwa[i], i+1))





# print(our_join(sunaye, ' '))
# print(our_split(sunaye, 0,1))
