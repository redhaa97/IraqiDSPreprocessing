import re
from Preprocessing.CleanDataSet import clean_text
from Preprocessing.EmojiConvertor import convertEmojiToWords
from Preprocessing.Normalize import normalize_text_before_stem, normalize_text_after_stem


def preprocessing():
    file = open('D:\\Research\\Dataset\\All datasets.txt', encoding='utf-8', errors='ignore')
    file.seek(0)
    dataSet = file.read()
    cleaned_text = clean_text(dataSet)
    cleaned_text = convertEmojiToWords(cleaned_text)
    normalized_text = normalize_text_before_stem(cleaned_text)
    # cleaned_text = re.sub(r'(.)\1+', r'\1', normalized_text)  # remove repeating letters
    file.close()
    # print(cleaned_text)
    # file.close()

    new_file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\cleaned All datasets duplicated letters.txt', 'w',
                    encoding='utf-8', errors='ignore')
    # new_file.write(cleaned_text)
    new_file.write(normalized_text)
    new_file.close()


def normalize_clean_text():
    file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\Clean Disgust2.txt',
                encoding='utf-8', errors='ignore')
    text = file.read()
    normalized_clean = normalize_text_after_stem(text)
    file.close()
    new_file = open('D:\\Research\\Dataset\\Amer-dataset\\second preprocessing\\Normalize cleaned Disgust.txt',
                    'w', encoding='utf-8', errors='ignore')
    new_file.write(normalized_clean)
    new_file.close()
