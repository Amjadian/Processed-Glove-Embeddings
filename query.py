import pickle #cPickle if Python 2.7
import os
import numpy as np
glove_dir = r"the path where you downloaded the pickled dictionaries to"+"\\"
file_names = os.listdir(glove_dir)
word = "example" # the word being queried
embedding_vector = []
for f_name in file_names:
    with open(glove_dir + f_name, "rb") as file:
        gdict = pickle.load(file)
        if(word in gdict):
            embedding_vector = gdict[word]
            break

if(len(embedding_vector == 0)):
	print("Queried word not found!")
else:
	print("Queried vector:", str(embedding_vector))
    # The embedding is a list that holds the stored vector values as text
    # let's convert them into a numpy array of floats.
    embedding_vector = np.array(embedding_vector, np.float32)