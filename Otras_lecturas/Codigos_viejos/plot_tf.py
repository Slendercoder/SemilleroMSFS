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

x = [i*10 for i in range(len(data[0]))]

print(data)

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
ax.set_xlabel('No. de iteraciones')
ax.set_ylabel('Score (%)')

for i in range(8):
    a = str(i)
    ax.plot(x, data[i], label=a)

ax.legend()

plt.show()
