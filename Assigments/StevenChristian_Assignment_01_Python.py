#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:50:38 2024

@author: stevenchristian
"""
#%% Create a sorted list of all images in that folder.
import glob

directory_path = '/Users/stevenchristian/Library/CloudStorage/Dropbox/School/PHD/Fall 2024/PSY427-627/Assignment 1/fLoc-version-1-master/stimuli/adult'  # Change this to your folder path

sorted_images = sorted(glob.glob(f"{directory_path}/*.[pjg]*"))

print(sorted_images)

#%% Select a random sample of 12 images.

import glob
import random


directory_path = '/Users/stevenchristian/Library/CloudStorage/Dropbox/School/PHD/Fall 2024/PSY427-627/Assignment 1/fLoc-version-1-master/stimuli/adult'  # Change this to your folder path


sorted_images = sorted(glob.glob(f"{directory_path}/*.[pjg]*"))


random_sample = random.sample(sorted_images, 12)


print(random_sample)

#%% Display each of the 12 randomly chosen images sequentially (in your random order)  * in the same figure * This is sort of a starter version of loading and showing images for an experiment.

import glob
import random
import matplotlib.pyplot as plt
from PIL import Image

directory_path = '/Users/stevenchristian/Library/CloudStorage/Dropbox/School/PHD/Fall 2024/PSY427-627/Assignment 1/fLoc-version-1-master/stimuli/adult'  # Change this to your folder path


sorted_images = sorted(glob.glob(f"{directory_path}/*.[pjg]*"))


random_sample = random.sample(sorted_images, 12)

fig, axes = plt.subplots(3, 4, figsize=(12, 8))

axes = axes.flatten()

for i, img_path in enumerate(random_sample):
    img = Image.open(img_path)
    axes[i].imshow(img)
    axes[i].axis('off') 


plt.tight_layout()
plt.show()

#%% Concatenate the images into an array and save them as one big array in an appropriate file called 'randomly_selected_images' (with appropriate extension for however you are saving them). The resulting array should have one dimension that is 12 long (one for each image)

import glob
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

directory_path = '/Users/stevenchristian/Library/CloudStorage/Dropbox/School/PHD/Fall 2024/PSY427-627/Assignment 1/fLoc-version-1-master/stimuli/adult'  # Change this to your folder path


sorted_images = sorted(glob.glob(f"{directory_path}/*.[pjg]*"))


random_sample = random.sample(sorted_images, 12)

image_arrays = []

for img_path in random_sample:
    img = Image.open(img_path)
    img = img.resize((256, 256))  
    img_array = np.array(img)     
    image_arrays.append(img_array)
    
concatenated_image = np.hstack(image_arrays)

Image.fromarray(concatenated_image).save('randomly_selected_images_concatenated.png')

plt.figure(figsize=(16, 4)) 
plt.imshow(concatenated_image)
plt.axis('off') 
plt.show()

#%% Graduate students: In addition to the above, make a figure with subplots to display each of the 12 images in a 4 x 3 'light table" grid. (We have not covered how to do this! but remember, this is OPEN CHATBOT).

import glob
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

directory_path = '/Users/stevenchristian/Library/CloudStorage/Dropbox/School/PHD/Fall 2024/PSY427-627/Assignment 1/fLoc-version-1-master/stimuli/adult'  # Change this to your folder path


sorted_images = sorted(glob.glob(f"{directory_path}/*.[pjg]*"))


random_sample = random.sample(sorted_images, 12)

image_arrays = []

for img_path in random_sample:
    img = Image.open(img_path)
    img = img.resize((256, 256))  
    img_array = np.array(img)     
    image_arrays.append(img_array)
    
fig, axes = plt.subplots(4, 3, figsize=(12, 16))

axes = axes.flatten()

for i, img in enumerate(image_arrays):
    axes[i].imshow(img)
    axes[i].axis('off') 
    
plt.tight_layout()
plt.show()

#%% 

import numpy as np

# Define a 2D array that represents a peace sign with characters
peace_sign_array = np.array([
    [' ', ' ', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' '],
    [' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' '],
    ['O', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'O', ' '],
    ['O', ' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', 'O', ' '],
    ['O', ' ', ' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O', ' '],
    ['O', ' ', 'O', ' ', ' ', 'O', ' ', ' ', 'O', 'O', ' '],
    ['O', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' ', 'O', ' '],
    [' ', 'O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'O', ' '],
    [' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' '],
    [' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O', ' ', ' ', ' '],
])

# Function to display the peace sign
def display_peace_sign(array):
    for row in array:
        print("".join(row))

# Display the peace sign using characters
display_peace_sign(peace_sign_array)



