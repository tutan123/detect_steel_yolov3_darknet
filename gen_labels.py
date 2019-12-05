import numpy as np
import pandas as pd
from tqdm import tqdm
import os
import cv2
df = pd.read_csv("train_labels.csv")

image_ids = np.array(df['ID']).tolist()
bboxes = np.array(df[' Detection']).tolist()
name_list = []
label_list = []
centerx = []
centery = []
width = []
height = []
ratio = []
large_sample = []
'''
for extract img names
'''
'''
name_list = []
temp = image_ids[0]
name_list.append('train/'+temp)
for i in range(len(image_ids)):
    if temp !=image_ids[i]:
        temp = image_ids[i]
        name_list.append('train/'+temp)
out = pd.DataFrame(name_list)
out.to_csv("train.txt",header=None,index=False)
'''

'''
generate train files
'''

temp = image_ids[0]
print(temp[:-4])
if not os.path.exists('label'):
    os.mkdir('label')
label_path = 'label/'
columns = ['label','centerx','centery','width','height']
img = cv2.imread('train/'+temp)
print(img.shape[0])
print(img.shape[1])
for i in tqdm(range(len(image_ids))):
    if temp!=image_ids[i] or i==len(image_ids)-1:
        #print("save file"+temp[:-4]+'.txt')
        img = cv2.imread('train/'+image_ids[i])
        final = pd.DataFrame({'label':label_list,'centerx':centerx,'centery':centery,'width':width,'height':height})
        final.to_csv(label_path+temp[:-4]+'.txt', header=None, index=False,sep=' ',columns=columns)
        label_list = []
        centerx = []
        centery = []
        width = []
        height = []
        label_list.append(0)
        xmin, ymin, xmax, ymax = bboxes[i].split(" ")
        centerx.append((int(xmin)+int(xmax))/2.0/img.shape[1])
        centery.append((int(ymin)+int(ymax))/2.0/img.shape[0])
        width.append((float(xmax)-float(xmin))/img.shape[1])
        height.append((float(ymax)-float(ymin))/img.shape[0])
        temp = image_ids[i]
    else:
        label_list.append(0)
        xmin, ymin, xmax, ymax = bboxes[i].split(" ")
        centerx.append((int(xmin)+int(xmax))/2.0/img.shape[1])
        centery.append((int(ymin)+int(ymax))/2.0/img.shape[0])
        width.append((float(xmax)-float(xmin))/img.shape[1])
        height.append((float(ymax)-float(ymin))/img.shape[0])
   

