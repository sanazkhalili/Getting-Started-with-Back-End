import os
import time
import glob
from langdetect import detect
from transformers import pipeline
import math
from elasticsearch import Elasticsearch
import easyocr
from keras.applications.vgg16 import VGG16
from tensorflow.keras.utils import img_to_array
from keras.applications.vgg16 import decode_predictions
from tensorflow.keras.utils import load_img
from keras.applications.imagenet_utils import preprocess_input
import pandas as pd

def image_classification(image):
        model = VGG16()
        image = load_img ( image, target_size = (224, 224) )
        image = img_to_array ( image )
        image = image.reshape ( (1, image.shape[0], image.shape[1], image.shape[2]) )
        image = preprocess_input ( image )
        y_hat = model.predict(image)
        label = decode_predictions (y_hat)[0][0]
        result = {"text":"No",
                  "label":label[1],
                   "score":label[2]}
        return result


def text_classification(text):
    classifier = pipeline ( 'zero-shot-classification', model = 'facebook/bart-large-mnli' )
    labels = ["artifacts", "animals", "food", "birds", 'travel', 'cooking', 'dancing', 'exploration']
    hypothesis_template = 'This text is about {}.'
    prediction = classifier ( text, labels, hypothesis_template = hypothesis_template, multi_class = True )

    return prediction['labels'][0], math.floor ( prediction['scores'][0] * 100 )


def preprocess(text):
    return text


def image_analysis(time_create, file_name, type, direct):
    word_list = []
    reader = easyocr.Reader ( ['ch_sim', 'en'] )
    results = reader.readtext ( file_name )

    for result in results:
        word_list.append ( result[1] )
    if len(word_list)==0:
           result = image_classification(file_name)

    else:
         label, score = text_classification ( word_list[0] )
         result = {"text": word_list,
                   "lang_detect": detect(word_list[0]),
                   "label":label,
                   "score":score}

    doc = {"directory": direct,
           "time_cr": time_create,
           "name": file_name,
           "type": type,
           "class":result }

    return doc


def text_analysis(time_create, file_name, type, direct):
    fp = open(file_name )
    text = fp.read()

    text_pre = preprocess(text)

    lang = detect(text_pre)

    label, score = text_classification ( text_pre )

    doc = {"directory": direct,
           "time_cr": time_create,
           "name": file_name,
           "type": type,
           "analysis": {
               "lang_detect": lang,
               "class":
                   {"label": label, "score": score}},
           }
    
    return doc

def dataframe_analysis(time_create, file_name, type, direct):
    df = pd.read_csv(file)
    name_col = list(df.columns)
    number_null = df.isna().sum()


    doc = {"directory": direct,
           "time_cr": time_create,
           "name": file_name,
           "type": type,
           "analysis":
               {"name_column": name_col,
               "number_null":number_null }
           }
    print(doc)

    return doc


import sys
path = sys.argv[1]
print(path)
directory = path.split('/')[-2]
list_files = glob.glob ( path )
es = Elasticsearch ( hosts = 'http://192.168.241.132:9200' )
print("check connection on elasticsearch: ", es.ping())

for file in list_files:

    type = ""
    ti_c = os.path.getctime ( file )
    c_ti = time.ctime ( ti_c )

    if ('.jpg' in file) or ('.png' in file):
        type = 'image'
        doc = image_analysis ( c_ti, file, type, directory )
        res = es.index ( index = "test_doc", document = doc )


    elif '.txt' in file:
        type = 'text'
        doc = text_analysis ( c_ti, file, type, directory )
        res = es.index ( index = "test_doc", document =doc )

    elif '.csv' in file:
        type = 'dataframe'
        doc = dataframe_analysis(c_ti, file, type, directory)
        res = es.index(index = "test_doc", document = doc)


