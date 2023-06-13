import os
import time
import glob
import sys
from elasticsearch import Elasticsearch
from langdetect import detect
from transformers import pipeline
import math
import easyocr



def text_classification(text):
    classifier = pipeline ( 'zero-shot-classification', model = 'facebook/bart-large-mnli' )
    labels = ["artifacts", "animals", "food", "birds", 'travel', 'cooking', 'dancing', 'exploration']
    hypothesis_template = 'This text is about {}.'
    prediction = classifier (text, labels, hypothesis_template = hypothesis_template, multi_class = True )

    return prediction['labels'][0], math.floor ( prediction['scores'][0] * 100 )


def preprocess(text):
    return text

def image_analysis(time_create, file_name, type):
    pass

    word_list=[]
    reader = easyocr.Reader(['ch_sim', 'en'])
    results = reader.readtext(file_name)

    for result in results:
        word_list.append(result[1])
    
    label, score = text_classification (word_list[0])
    

    doc = {"time_cr":time_create,
                            "name":file_name,
                            "type":type,
                            "analysis":{
                                "lang_detect":detect(world_list[0]),
                                "class":
                                    {"label":label ,"score":score}},
                              }
    es.index(index = 'document_analysis',
             document = doc)
    

def text_analysis(time_create, file_name, type):
    fp = open(file_name)
    text = fp.read()
    print(text)
    text_pre = preprocess(text)
   
    lang = detect(text_pre)
    lable, score = '', 0
    if lang=='eng':
        #translate
        pass

    label, score = text_classification (text_pre)

    doc = {"time_cr":time_create,
                         "name":file_name,
                         "type":type,
                         "analysis":{
                             "lang_detect":lang,
                             "class":
                                 {"label":label ,"score":score}},
                          }
    print(doc)
    es.index(index = 'document_analysis',
             document = doc)




path = sys.argv[1]
list_files = glob.glob(path)
 es = Elasticsearch(hosts = 'http://172.31.71.200:9200')
for file in list_files:

    type = ""
    if ('.jpg' in file) or ('.png' in file):
        ti_c = os.path.getctime ( file )
        c_ti = time.ctime ( ti_c )

        type = 'image'
        image_analysis(c_ti, file, type)
    elif '.txt' in file:
        ti_c = os.path.getctime ( file )
        c_ti = time.ctime ( ti_c )
        type = 'text'
        text_analysis(c_ti, file, type)
