#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Kai Krah
# DATE CREATED: 17th September 2024                           
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    results_dic = {} #creating an emtpy dictionary to be filled within the function
    files = listdir(image_dir) #reading out the filenames in the given directory "image_dir" and store them in the list files

    for file in files:
      """ going through the list 'files' to convert the filename into the pet_label and store it in the result_dic"""
      if file[0] == '.': #checking if the filename starts with '.' to skip it
        continue
      else:
        pet_image_list = file.lower().split('_') #splitting the filename into a list, splitted by the seperator '_'
        pet_label = "" # creating an empty string "pet_label" to add the correct label strings
        pet_label_list = [] # this will be the value for results_dic.

        for i in range(len(pet_image_list)):
         """for loop to check within one item of pet_image_list, if the item (string) contains only alphabetical characters"""
         if pet_image_list[i].isalpha():
           pet_label += pet_image_list[i] + " "  #if the items contains only alphabetical characters, the item ist added to the string pet_label

        pet_label_list.append(pet_label.strip()) # adding the string to the list as a value for the dictionary

        results_dic[file] = pet_label_list #after the alphabetical chack and buildung the pet_label string it is stored in the dictionary under the key "file"
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
