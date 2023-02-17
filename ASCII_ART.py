from PIL import Image, ImageStat
import math
import numpy as np

im = Image.open("untitled.png").convert('RGB')

row,col = im.size
data = []

for i in range(row):
    for j in range(col):
        data.append(im.getpixel((i,j)))

class Atrb:
    brightness = []
    for i in range(len(data)):
        brightness.append((sum(data[i])/3))

chars = []
for i in range(len(Atrb.brightness)):
    
        if math.floor(Atrb.brightness[i]) > math.floor((255/10)*9):
            chars.append("@")
            
        elif math.floor(Atrb.brightness[i]) > math.floor((255/10)*8) & math.floor(Atrb.brightness[i]) <= math.floor((255/10)*9):
            chars.append("%")
            
        elif math.floor(Atrb.brightness[i]) > math.floor((255/10)*7) & math.floor(Atrb.brightness[i]) <= math.floor((255/10)*8):
            chars.append("#")
            
        elif math.floor(Atrb.brightness[i]) > math.floor((255/10)*6) & math.floor(Atrb.brightness[i]) <= math.floor((255/10)*7):
            chars.append("*")
            
        elif math.floor(Atrb.brightness[i]) > math.floor((255/10)*5) & math.floor(Atrb.brightness[i]) <= math.floor((255/10)*6):
            chars.append("+")
             
        elif math.floor(Atrb.brightness[i]) > math.floor((255/10)*4) & math.floor(Atrb.brightness[i]) <= math.floor((255/10)*5):
            chars.append("=")  
                      
        elif math.floor(Atrb.brightness[i]) > math.floor((255/10)*3) & math.floor(Atrb.brightness[i]) <= math.floor((255/10)*4):
            chars.append("-") 
            
        elif math.floor(Atrb.brightness[i]) > math.floor((255/10)*2) & math.floor(Atrb.brightness[i]) <= math.floor((255/10)*3):
            chars.append(":")
                                 
        elif math.floor(Atrb.brightness[i]) > math.floor(255/10) & math.floor(Atrb.brightness[i]) <= math.floor((255/10)*2):
            chars.append(".")                                 
                                              
        elif math.floor(Atrb.brightness[i]) < math.floor(255/10):
            chars.append(" ")
            

output = np.array(chars).reshape((row,-1))
output = np.rot90(output, 1, axes=(0,1))
output = np.flipud(output)
         
np.savetxt('output.txt', output, fmt='%s')
        
with open('output.txt', 'r') as f:
    lines = f.readlines()
    
lines = [line.replace(' ','') for line in lines]

with open('output.txt', 'w') as f:
    f.writelines(lines)
#print(Atrb.brightness)