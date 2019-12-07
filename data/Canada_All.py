import csv
import matplotlib.pyplot as plt

# total medal trends - sampled years(20 year increments)
# 1924, 1948, 1968, 1984, 2006, 2014
# columns 0 (year) and column 4 (country)
# 
m_1924=0
m_1928=0
m_1932=0
m_1936=0
m_1948=0
m_1952=0
m_1956=0
m_1960=0
m_1964=0
m_1968=0
m_1976=0
m_1980=0
m_1984=0
m_1988=0
m_1992=0
m_1994=0
m_1998=0
m_2002=0
m_2006=0
m_2010=0
m_2014=0

#pie chart for mens hockey medal colours (gold, silver, bronze)
#arrays for each colour

golds=	[]
silvers = []
bronzes = []

catagories = []

with open('Can All medals.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
		# parse that first row of text data out of the file.
			catagories.append(row)
			line_count += 1
		else:
			if row[7] == 'Gold':
				print('won gold!')
				golds.append(row[7])
			if row[7] == 'Silver':
				print('won silver!')
				silvers.append(row[7])
			if row[7] == 'Bronze':
				print('won bronze. Is that even winning?')
				bronzes.append(row[7])

		line_count += 1

print('gold medals: ', len(golds))
print('silver medals: ', len(silvers))
print('bronze medals: ', len(bronzes))

labels = ("Gold", "Silver", "Bronze")

sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold','silver', 'darkgoldenrod']
explode = [0.1, 0.1, 0.1]

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title('Medals for All Canadian Medals')
plt.xlabel('Medals since 1924')
plt.show()

