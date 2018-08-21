import os
import matplotlib.pyplot as plt

file 	= open('TraderScores.txt', 'r')
scores 	= file.read().split()
scores 	= [int(score) for score in scores]
y		= range(len(scores))
axes 	= plt.gca()
axes.set_ylim([min(scores) - 1, max(scores) + 1])
# print(scores)
plt.plot(y, scores)
plt.show()