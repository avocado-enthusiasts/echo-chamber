#!/usr/bin/python3
import json

# get respective list for each person
eval_list = []
ans = raw_input("Type 'amir', 'arvin', or 'sama': ").lower()
print(ans)
with open("./work_ds/eval/"+ans+".txt") as f:
        for title in f:
		if title:
			eval_list.append("eval_"+title.strip().lower())
	f.close()

# for every subreddit that person needs to evaluate
for sr in eval_list:
	sr_data = []
	
	# load the posts into memory
	with open("./work_ds/eval/"+sr, 'r') as sr_file:
		for data in sr_file:
			json_data = json.loads(data)
			sr_data.append(json_data)
		sr_file.close()
		
		# give person the two posts and ask for a rating
		outfile = open("./work_ds/eval/ans_"+sr, 'w+')
		for pair in sr_data:
			print '\t\t POST #1\n' + pair["post1"]["body"].strip('\n') + '\n\n'
			print '\t\t POST #2\n' + pair["post2"]["body"].strip('\n') + '\n\n'
			pair["grade"] = raw_input("\t\t1 - different, 5 - similar\n Your answer: ")
			print '\n'
			json.dump(pair, outfile)
			outfile.write("\n")

		outfile.close()
