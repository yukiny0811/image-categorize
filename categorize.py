import glob
import cv2
import numpy as np
import random
import string
import tqdm

dic = {}

files = glob.glob("./images/img*/*g")
for file in files:
    tmp = file[14:]
    if tmp not in dic:
        dic[tmp] = 1
    else:
        dic[tmp] += 1

keylist = dic.keys()

def randomname(n):
	randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
	return ''.join(randlst)

for key in tqdm.tqdm(keylist):
    if dic[key] == 1:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/1/" + randomname(10) + ".jpg", img)
    elif dic[key] == 2:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/2/" + randomname(10) + ".jpg", img)
    elif dic[key] == 3:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/3/" + randomname(10) + ".jpg", img)
    elif dic[key] == 4:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/4/" + randomname(10) + ".jpg", img)
    elif dic[key] == 5:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/5/" + randomname(10) + ".jpg", img)
    elif dic[key] == 6:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/6/" + randomname(10) + ".jpg", img)
    elif dic[key] == 7:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/7/" + randomname(10) + ".jpg", img)
    elif dic[key] == 8:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/8/" + randomname(10) + ".jpg", img)
    elif dic[key] == 9:
        img = cv2.imread("./images/cont/" + key).astype(np.float)
        cv2.imwrite("./categ/9/" + randomname(10) + ".jpg", img)

print(dic)