#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Zofia Wilk
# DATE CREATED: 06.07.2023                              
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
    in_files = listdir(image_dir)
    results_dic = dict()
    
    #itterating through file to extract the pet labels
    for filename in in_files:
        if filename[0] != ".":
            #saving the file name in image_filename
            image_filename = filename
            #dividing image filename into separate lowercase words 
            words_in_filename = image_filename.lower().split('_')
            
            #creating pet_label from the words in filename
            pet_label = ' '.join([word for word in words_in_filename if word.isalpha()])
            
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print("** Warning: Key=", filename, "already exists in results_dic with value =", results_dic[filename])
                           
    # Replace None with the results_dic dictionary that you created with this function
    return  results_dic

