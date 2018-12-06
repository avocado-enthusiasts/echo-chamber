#a text file for 0-1, 1-2, 2-3, 3-4, 4-5 based on likart scalse
#loads the model
#grabs the sentances
#gets cosine similiarity code is in
#put cosine similiarity on each line with likart scale in respective folder
#then get stats, average, mean, median, etc
#plot we see a trend

#!/usr/bin/python3
import numpy as np
import sent2vec
from scipy import spatial
from strip import Strip
from collections import defaultdict

def cosine(u,v):
  return 1 - spatial.distance.cosine(u,v)

train_raw = 'en-train.txt'
#[ { 's1': , 's2': , 'score': } ]
train_pairs = []
s = Strip()
with open(train_raw) as f:
	for line in f:
		if line:
			temp = line.split('\t')
			train_pairs.append({ 'sen1':s.removeALL(temp[0]), 'sen2':s.removeALL(temp[1]), 'score':float(temp[2].strip('\n'))})

model = sent2vec.Sent2vecModel()
model.load_model('model.bin')

# find cosine similarity between the pairs
files = ['0-1', '1-2', '2-3', '3-4', '4-5']
f1 = open(files[0], 'w+')
f2 = open(files[1], 'w+')
f3 = open(files[2], 'w+')
f4 = open(files[3], 'w+')
f5 = open(files[4], 'w+')

i = 0
for pair in train_pairs:
	sen1 = pair['sen1']
	sen2 = pair['sen2']
	if sen1 and sen2:
		a = model.embed_sentence(sen1)
		b = model.embed_sentence(sen2)
		a = a[0]
		b  = b[0]
		if np.count_nonzero(a) == 0 or np.count_nonzero(b) == 0:
			continue
			
		i += 1
		cos = cosine(a,b)
		sim = str(cos)
		l = pair['score'] # likert rating
		lik = str(l)

		if l >= 0 and l <= 1:
			f1.write(sim + '\t' + lik +'\n')
		elif l > 1 and l <= 2:
			f2.write(sim + '\t' + lik +'\n')
		elif l > 2 and l <= 3:
			f3.write(sim + '\t' + lik +'\n')
		elif l > 3 and l <= 4:
			f4.write(sim + '\t' + lik +'\n')
		elif l > 4 and l <= 5:
			f5.write(sim + '\t' + l +'\n')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()