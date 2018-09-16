# Processed-Glove-Embeddings
Glove embeddings processed into hashed Python dictionaries for quick retrieval of the embeddings.

## Some background information
GloVe vectors are prepared by Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014, 
"GloVe: Global Vectors for Word Representation." and here's the link to the paper if you'd like to know the details of how they  were built: https://nlp.stanford.edu/pubs/glove.pdf
Glove vectors have been made publically available here: https://nlp.stanford.edu/projects/glove/
as text files.

## About this repo
I have made the GloVe vectors available in this repository as Python hashed dictionary files to query instantaneously. 
Find the query script in this repository to querry any word present in the most complete version of the GloVe embeddings.

# Steps to query the word embeddings
* Download the GloVe dictionaries from here: https://drive.google.com/drive/folders/1MShc-ebib-04jJssSJXsKJ854zLgT0MO?usp=sharing
* Query any word using the "query.py" script provided in this repository
* The embedding vector retrieved is a list that holds string-valued components which the script casts to a numpy array of type float32
