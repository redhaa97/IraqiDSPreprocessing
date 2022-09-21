

# read text file and return lists of words in each line in it
import numpy as np
import pandas as pd
import nltk

from Preprocessing.Normalize import normalize_text_after_stem
from farasa.farasa.stemmer import FarasaStemmer
from nltk.stem import arlstem, ISRIStemmer

from Preprocessing import ArabicConstant


def read_clean_file():
    return open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\All datasets Normalized Cleaned.txt', 'r', encoding='utf-8', errors='ignore')

def read_after_stem_file():
    return open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\All datasets Cleaned After Stemming.txt', 'r', encoding='utf-8', errors='ignore')


def tokenize_post(file):
    tokenizedText = []
    for line in file:
        line_strip = line.strip()
        line_splite = line_strip.split()
        tokenizedText.append(line_splite)
    return tokenizedText


def iraqi_stopwords():
    iraqi_stopwords = []
    file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\Iraqi stop words.txt', 'r', encoding='utf-8', errors='ignore')
    for line in file:
        line_strip = line.strip()
        iraqi_stopwords.append(line_strip)
    return iraqi_stopwords

def remove_stopwords(file):
    posts = tokenize_post(file)
    file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\tessssssssssssst.txt',
                'w', encoding='utf-8', errors='ignore')
    for post in posts:
        for word in post:
            if word not in iraqi_stopwords():
                file.write(word + ' ')
        file.write('\n')
    file.close()


    # posts = tokenize_post(file)
    # file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\cleaned All datasets After Stemming.txt', 'w', encoding='utf-8', errors='ignore')
    # for post in posts:
    #     for stem in stem_words(post):
    #         file.write(stem+ ' ')
    #     file.write('\n')
    # file.close()


def data_frame(file):
    tokens = tokenize_post(file)
    df = pd.DataFrame(np.array(tokens), columns=['test'])
    return df


def concatenate_list_into_string(lis_strs):
    result = ""
    for el in lis_strs:
        result += " " + el
    return result

def remove_single_letter(text):
    words = text.split(' ')
    for word in words:
        if len(word.strip()) == 1:
            if word != ArabicConstant.WAW:
                words.remove(word)
    text = concatenate_list_into_string(words)
    return text

def remove_duplicated_words(post):
    noDuplicate = []
    for word in post:
        if word not in noDuplicate:
            noDuplicate.append(word)
    return noDuplicate


def stem_words(post):
    stemmer = FarasaStemmer()
    stemmers = []
    for word in post:
        if word !='None':
            stemmed = stemmer.stem(word)
            stemmers.append(stemmed)
    return stemmers

def stem_arlstem(post):
    stemmer = arlstem.ARLSTem()
    stemmers = []
    for word in post:
        stemmed = stemmer.stem(word)
        stemmers.append(stemmed)
    return stemmers

def stem_isri(post):
    stemmer = ISRIStemmer()
    stemmers = []
    for word in post:
        stemmed = stemmer.stem(word)
        stemmers.append(stemmed)
    return stemmers


def stem_text(file):
    posts = tokenize_post(file)
    file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\cleaned All datasets ARLstem Stemming.txt', 'w', encoding='utf-8', errors='ignore')
    for post in posts:
        for stem in stem_arlstem(post):
            file.write(stem+ ' ')
        file.write('\n')
    file.close()

def remove_duplicates_stem(file):
    posts = tokenize_post(file)
    file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\NoDuplicate stemmed Surprise.txt', 'w', encoding='utf-8', errors='ignore')
    for post in posts:
        no_dup_post = remove_duplicated_words(post)
        for stem in stem_words(no_dup_post):
            file.write(stem+ ' ')
        file.write('\n')
    file.close()

def tokenize_final_text():
    clean_file = read_clean_file()
    remove_duplicates_stem(clean_file)
    after_stem = read_after_stem_file()
    return tokenize_post(after_stem)

def normalize_stemmed_text(file):
    text = file.read()
    normalized_stemmed = normalize_text_after_stem(text)
    new_file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\All datasets Normalize stemmed.txt', 'w', encoding='utf-8', errors='ignore')
    new_file.write(normalized_stemmed)
    new_file.close()