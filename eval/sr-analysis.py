import numpy as np
from os import listdir
from os.path import isfile, join


# get all the files in list
path = './cos_test'
sr_list = [f for f in listdir(path) if isfile(join(path, f))]

if len(sr_list) != 23:
	print("Not every file was added to the list: "+str(len(sr_list)))
	print(sr_list)
	exit(1)

# load all the data in the files
with open("eval-results-cos-sr-vec.txt", "w+") as outf:
	for sr in sr_list:
		
		# load the cosine data from each subreddit
		data = []
		with open(path+'/'+sr, 'r') as f:
			for line in f:
				if line:
					temp = line.strip('\n')
					data.append(float(temp))
			f.close()
		
		# do the calculations & dump
		mean = np.mean(data)
		median = np.median(data)
		std = np.std(data)
		vari = np.var(data)
		
		outf.write(sr + '\n')
		outf.write(str(mean)+'\t'+str(median)+'\t'+str(std)+'\t'+str(vari)+'\n')
	
	outf.close()