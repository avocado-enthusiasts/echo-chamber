#!/usr/bin/python3

def split(soup, n):
    k, m = divmod(len(soup), n)
    return [soup[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(n)]

# get the list of all subreddits
sr_list = []
with open("./work_ds/sr_list.txt") as f:
	for title in f:
		if title:
			sr_list.append(title.strip().lower())
	f.close()
	
	# divide into three
	names = ["arvin.txt","sama.txt","amir.txt"]
	chunks = split(sr_list, 3)
	
	# export each respective person's list
	for i in range(0, 3):
		file = open('./work_ds/eval/'+names[i], 'w')
		for sr in chunks[i]:
			file.write(sr+'\n')

		file.close()
