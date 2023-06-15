import os
import cv2

path = "/Users/kalpeshpatel/Desktop/Python/Project105/Images"

Images = []

list_of_files = os.listdir(path)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name= path+"/"+file
        
        print(file_name)
        
Images.append(list_of_files)
        
count = len(Images)
        
frame = cv2.imread(Images[0])
        
height  = int(cv2.CAP_PROP_FRAME_HEIGHT)
width = int(cv2.CAP_PROP_FRAME_WIDTH)
fps = int(cv2.CAP_PROP_FPS)
        
size = (width, height)
print(size)
        
out = cv2.VideoWriter('Project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    cv2.imread()
    out.write()
    
print("Done")
        
        
        