# do some calculations for the evaluation data

import numpy as np

# build the data information
files = ['0-1', '1-2', '2-3', '3-4', '4-5']
with open("../data/eval-results.txt", "w+") as outf:
	for file in files:
		outf.write("BUCKET " + file + '\n')

		cosine = []
		likert = []
		with open(file, 'r') as f:
			for line in f:
				if line:
					temp = line.split('\t')
					cosine.append(float(temp[0]))
					likert.append(float(temp[1]))
			f.close()

		# calc stats for each buckets cosine: mean, median, stat deviation
		mean = np.mean(cosine)
		median = np.median(cosine)
		std = np.std(cosine)
		vari = np.var(cosine)

		outf.write(str(mean)+'\t'+str(median)+'\t'+str(std)+'\t'+str(vari)+'\n')

	outf.close()


