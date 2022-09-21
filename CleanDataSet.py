# -*- coding: utf-8 -*-
# clean text from noise take text and return cleaning text
from Preprocessing import ArabicConstant, ForeignConstants


def clean_text(text):
    import re

    pattern = ForeignConstants.SPACE_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, " ", text)

    pattern = ArabicConstant.SPACE_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, " ", text)

    # remove English letters
    pattern = r"[A-Za-z][A-Za-z]*"
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

    # to remove English digits
    pattern = r'[0-9]+'
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

    # to remove Arabic digits
    pattern = ArabicConstant.ARABIC_NUMBERS_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

    # remove arabic symbols
    pattern = ArabicConstant.ARABIC_SYMBOLS_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

        # remove arabic punctuation
        pattern = ArabicConstant.ARABIC_PUNCTUATION_PAT
        match = re.search(pattern, text)
        if match:
            text = re.sub(pattern, "", text)

    # remove English symbols
    pattern = ForeignConstants.ENGLISH_SYMBOLS_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)



    # remove General Punctuations
    pattern = ForeignConstants.GENERAL_PUNCTUATION_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

    # remove Latin supplement
    pattern = ForeignConstants.LATIN_SUPPLEMENT_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

    # remove Latin A
    pattern = ForeignConstants.LATIN_A_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

    # remove Latin B
    pattern = ForeignConstants.LATIN_B_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

    # remove Random symbols
    pattern = ForeignConstants.RANDOM_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "", text)

    return text
