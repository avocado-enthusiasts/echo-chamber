#!/usr/bin/python3
import json

# get respective list for each person
eval_list = []
ans = raw_input("Type 'amir', 'arvin', or 'sama': ").lower()

with open("./work_ds/eval/"+ans+".txt") as f:
        for title in f:
                if title:
                        eval_list.append(title.strip().lower())
        f.close()

# for every subreddit that needs evaluation
for sr in eval_list:
        sr_data = []

        #load the random posts into memory
        with open("./work_ds/eval/eval_"+sr, 'r') as sr_file:
                for data in sr_file:
                        json_data = json.loads(data)
                        sr_data.append(json_data)
                sr_file.close()

                # give a pair of posts, grade, and store response
                outfile = open("./work_ds/eval/ans_"+sr, 'w+')
                for pair in sr_data:
                        print '\t\t POST #1\n' + pair["post1"]["body"].strip('\n') + '\n\n'
                        print '\t\t POST #2\n' + pair["post2"]["body"].strip('\n') + '\n\n'
                        pair["grade"] = raw_input("\t\t1 - different, 5 - similar\n Your answer: ")
                        print '\n=================================================================\n'
                        json.dump(pair, outfile)
                        outfile.write("\n")
                outfile.close()
