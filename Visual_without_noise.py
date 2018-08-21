import os
import matplotlib.pyplot as plt

file 	= open('TraderScores.txt', 'r')
scores 	= file.read().split()
scores 	= [int(score) for score in scores]
p 		= len(scores)
lag 	= 10
means 	= []
for i in range(lag, p + 1):
	sump 	= sum(scores[i - lag:i])
	means.append(1.0*sump/lag)

print(means)
y		= range(len(means))
plt.plot(y, means)
plt.show()