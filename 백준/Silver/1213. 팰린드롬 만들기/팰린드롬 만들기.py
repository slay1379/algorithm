import sys
input = sys.stdin.readline
from collections import Counter

name = input().strip()
element = Counter(name)
state = False
add_value = None

for value in element.values():
    if value % 2 != 0:
        if state:
            print("I'm Sorry Hansoo")
            exit()
        state = True

element_count = sorted(element.items())
front = []
for key,value in element_count:
    for i in range(value//2
                   ):
        front.append(key)
    if value % 2 != 0:
        add_value = key

back = front[::-1]
answer = []
for element in front:
    answer.append(element)
if add_value is not None:
    answer.append(add_value)
for element in back:
    answer.append(element)

for element in answer:
    print(element,end='')