#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:49:31 2018

@author: zhenhao
"""

import face_recognition_api
import numpy as np
import pandas as pd
import os
import pickle

fname = 'classifier.pkl'
prediction_dir = './test-images'

encoding_file_path = './encoded-images-data.csv'
df = pd.read_csv(encoding_file_path)
full_data = np.array(df.astype(float).values.tolist())

# Extract features and labels
# remove id column (0th column)
X = np.array(full_data[:, 1:-1])
y = np.array(full_data[:, -1:])

if os.path.isfile(fname):
    with open(fname, 'rb') as f:
        (le, clf) = pickle.load(f)
else:
    print('\x1b[0;37;43m' + "Classifier '{}' does not exist".format(fname) + '\x1b[0m')
    quit()

def main(img):
    img=np.asarray(img, dtype=np.uint8)
    X_faces_loc = face_recognition_api.face_locations(img)
    faces_encodings = face_recognition_api.face_encodings(img, known_face_locations=X_faces_loc)
#    print("Found {} faces in the image".format(len(faces_encodings)))
    
    if len(faces_encodings) >0:
    
        closest_distances = clf.kneighbors(faces_encodings, n_neighbors=1)
    
        is_recognized = [closest_distances[0][i][0] <= 0.5 for i in range(len(X_faces_loc))]
        
        predictions = [[le.inverse_transform([int(pred)])[0], list(loc)] if rec else ["Unknown", loc] for pred, loc, rec in
                       zip(clf.predict(faces_encodings), X_faces_loc, is_recognized)]
    else:
        predictions=[]
    print(predictions)
    
    return predictions