import sys
import os
from collections import defaultdict


cos_list = os.listdir(sys.argv[1])
cos = []
dic = defaultdict(int)
for file in cos_list:
  file = open(sys.argv[1] + file)
  for line in file:
    if line:
      line = line.strip()
      dic[line] += 1
  sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
  print(sorted_dic[0:10])


