from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
from os import walk
import scipy.misc, scipy.io 

im = Image.open('miet.jpeg')
w,h = im.size

# Defining 1st region  
box0 = (100,100,300,300)
im0 = im.crop(box0)

# Defining 2st region  
box1 = (300,300,500,500)
im1 = im.crop(box1)


def rect(ax, s, ss):
    ax.imshow(im)
    x1 = [s[0], s[0] + ss, s[0] + ss, s[0], s[0]]
    y1 = [s[1], s[1], s[1] + ss, s[1] + ss, s[1]]
    ax.plot(x1[:5],y1[:5],'r')   

def getFig():
    
    ax = []

    ax.append(plt.subplot2grid((3,5), (0,0), rowspan=3,colspan=3))
    ax.append(plt.subplot2grid((3,5), (0,3)))
    ax.append(plt.subplot2grid((3,5), (0,4)))
    ax.append(plt.subplot2grid((3,5), (1,3)))
    ax.append(plt.subplot2grid((3,5), (1,4)))
    ax.append(plt.subplot2grid((3,5), (2,3)))
    ax.append(plt.subplot2grid((3,5), (2,4)))
    return ax

def Task(p_width ,p_heigth):
    current_position = 0
    ax = getFig()

    ax[current_position].imshow(im)
    ax[current_position].axis('off')
    
    rect(ax[current_position], (100,100), 200)
    rect(ax[current_position], (300,300), 200)
    
    # Mean value of 1st region
    im0_arr = np.array(im0)
    mean0 = im0_arr[:,:].mean()
    
    # Mean value of 2nd region
    im1_arr = np.array(im1)
    mean1 = im1_arr[:,:].mean()
    
    current_position = current_position + 1
    
    ax[current_position].imshow(im0)
    ax[current_position].axis('off')
    ax[current_position].text(10, 20, str(round(mean0, 3)), fontsize = 10)
    current_position = current_position + 1

    ax[current_position].imshow(im1)
    ax[current_position].axis('off')
    ax[current_position].text(10, 20, str(round(mean1, 3)), fontsize = 10, color = 'yellow')
    current_position = current_position + 1
    
    for i in range(1,5):
        im_res = im.resize((p_width/(2**i), p_heigth/(2**i)))
        ax[current_position].imshow(im_res)
        ax[current_position].axis('off')
        current_position = current_position + 1
        

    # Jpg-image
    plt.savefig("finish_image.jpg")

    # Pickle-file
    bckp_obj = [im, im0, im1, mean0, mean1]
         
    file = open('image_obj_bckp.pkl','wb')
    pickle.dump(bckp_obj, file, 2)
    file.close()

    #Mat-file
    scipy.io.savemat('result_bckp.mat', {'main_image': np.array(im), 'region1': im0_arr, 'region2': im1_arr, 'mean1': mean0, 'mean2': mean1})   
          

    plt.show()
    
  
Task(p_width = w ,p_heigth = h)
