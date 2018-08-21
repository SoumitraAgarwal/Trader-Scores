import os
import matplotlib.pyplot as plt

file 	= open('TraderScores.txt', 'r')
scores 	= file.read().split()
scores 	= [int(score) for score in scores]
p 		= len(scores)
lag 	= 10
means 	= []

for i in range(lag - 1):
	sump = sum(scores[0:i + 1])
	means.append(1.0*sump/(i + 1))

for i in range(lag, p + 1):
	sump 	= sum(scores[i - lag:i])
	means.append(1.0*sump/lag)


axes 	= plt.gca()
axes.set_ylim([min(scores) - 1, max(scores) + 1])
y		= range(len(means))
plt.xlabel('No. of tries', fontsize=10)
plt.ylabel('Score', fontsize=10)
line_up,  	= plt.plot(y, scores, label='Scores')
line_down, 	= plt.plot(y, means, label='De-noised')
plt.legend(handles=[line_up, line_down])
plt.show()