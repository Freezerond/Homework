f = open('task1.txt', 'r') 
f = f.readlines()
f = list(map(lambda x: str(x)[:-1], f))
f = [int(x) for x in f]
res = []

for x in f:
    for y in f:
        for z in f:
            if (x + y + z) == 2020:
                res.append(x * y * z)
res = list(set(res))
print("Наше число:", *res)

with open('task1_output.txt', 'w') as file:
    for x in res:
        file.write(str(x))
        file.write('\n')
file.close()