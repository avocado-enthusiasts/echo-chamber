#!/usr/bin/python3
import json
from random import sample


sr_list = set()
with open("./work_ds/sr_list.txt") as f:
	for title in f:
		if title:
			sr_list.add(title.strip().lower())
	f.close()

for sr in sr_list:
	sr_data = []
	# load subreddit into memory
	with open("./work_ds/"+sr, 'r') as sr_file:
		for data in sr_file:
			json_data = json.loads(data)
			sr_data.append(json_data)
	sr_file.close()

	# make pairing and dump
	randPosts = sample(sr_data, 10)
	outfile = open("./work_ds/eval/eval_"+sr, 'w') # file for writing
	for i in range (0, len(randPosts)-1, 2):
		pair = {'post1': randPosts[i], 'post2': randPosts[i+1], 'grade':-1}
		json.dump(pair, outfile)
		outfile.write('\n')

	outfile.close()


#for each subr
#  open file for writing (subreddit_test)
#  load json into memoery
#  set()
#  for each line in f
#    json.laods
#      add(set)
#  l = randomlchoice(set,2)
#  ask user
#  {pos1,pos2,score}
#  json.dump()
