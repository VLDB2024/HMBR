import csv
import numpy as np

K = 64
M = 8
F = 8
MAX_BW = 1600.0
U_DIV_B = 2.0
B_BW = MAX_BW / U_DIV_B
B_SCALE = 5

start_idx = 1

np.random.seed()
temp = np.random.normal(B_BW, B_SCALE, (1, K + M - F)).tolist()[0]
bw = []
i = 0
for x in range(K+M):
    if (x+1) >= start_idx and (x+1) < start_idx+F:
        bw.append(MAX_BW)
    else:
        bw.append(temp[i])
        i+=1



# bw
sfilename = str("bw")+ \
            str("K")+str(K)+ \
            str("M")+str(M)+ \
            str("F")+str(F)+ \
            str(".csv")
print(sfilename)

with open(sfilename, 'w') as csvwritefile:
    writer = csv.writer(csvwritefile)
    writer.writerow(bw)
