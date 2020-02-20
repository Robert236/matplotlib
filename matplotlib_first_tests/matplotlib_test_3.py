from matplotlib import pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115, 8, 9, 26]
# ids = [x for x in range(len(population_ages))]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('interessting Graph\nCheck that out')
#plt.legend()
plt.show()
