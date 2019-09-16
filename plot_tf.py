import matplotlib.pyplot as plt

data = []
Inp = open("tallaFinita.csv", "r")
count = 0
for line in Inp:
    v = list(map(float, line.split(',')))
    print(v)
    if count > 0:
        data.append(v)
    count += 1
Inp.close()

x = [i for i in range(len(data[0]))]

print(data)

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

for i in range(8):
    ax.plot(x, data[i])

plt.show()
