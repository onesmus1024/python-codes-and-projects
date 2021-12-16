import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [100, 100, 100]
plt.figure(figsize=(9,3))
plt.subplot(133)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(131)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()