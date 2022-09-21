import re
import Preprocessing.ArabicConstant as arabConst


# { Indivudual Functions

def strip_Tashkeel(text):
    return arabConst.HARAKAT_PAT.sub('', text)


def strip_Tatweel(text):
    return re.sub(u'[%s]' % arabConst.TATWEEL, '', text)


# The converted letters into ALEF are: ALEF_MADDA,
# ALEF_HAMZA_ABOVE, ALEF_HAMZA_BELOW ,HAMZA_ABOVE, HAMZA_BELOW
def normalize_Alef(text):
    return arabConst.ALEFAT_PAT.sub(arabConst.ALEF, text)

# The converted letters into ALEF are: ALEF_WAVY_HAMZA, ALEF_HAMZA_ABOVE_IOSLATED,
# ALEF_HAMZA_BELOW_IOSLATED, ALEF_HAMZA_ABOVE_FINAL,
# ALEF_HAMZA_BELOW_FINAL, ALEF_IOSLATED, ALEF_MADDA_ABOVE_IOSLATED,
# ALEF_MADDA_ABOVE_FINAL, ALEF_FINAL
def normalize_Alef_form(text):
    return arabConst.ALEF_FORM_PAT.sub(arabConst.ALEF, text)


# Normalize Lam Alef ligatures into two letters (LAM and ALEF)
# The converted letters into  LAM and ALEF are :
# - LAM_ALEF, LAM_ALEF_HAMZA_ABOVE, LAM_ALEF_HAMZA_BELOW,
#  LAM_ALEF_MADDA_ABOVE
def normalize_LamAlef(text):
    return arabConst.LAMALEFAT_PAT.sub( \
        u'%s%s' % (arabConst.LAM, arabConst.ALEF), text)


# normalize WAW_HAMZA to WAW
def normalize_Waw(text):
    return arabConst.WAW_PAT.sub(arabConst.WAW, text)


def normalize_yeh_hamza(text):
    return arabConst.YEH_HAMZA_PAT.sub(arabConst.YEH_HAMZA, text)


# normalize BEH
def normalize_Beh(text):
    return arabConst.BEH_PAT.sub(arabConst.BEH, text)


# TEH_MARBUTA into HEH
def normalize_Teh_Marbuta(text):
    pattern = arabConst.TEH_MARBUTA_PAT
    match = re.search(pattern, text)
    if match:
        text = re.sub(pattern, "ه " , text)
    return text


# normalize TEH
def normalize_Teh(text):
    return arabConst.TEH_PAT.sub(arabConst.TEH, text)


# normalize THEH
def normalize_Theh(text):
    return arabConst.THEH_PAT.sub(arabConst.THEH, text)


# normalize JEEM
def normalize_Jeem(text):
    return arabConst.JEEM_PAT.sub(arabConst.JEEM, text)


# normalize HAH
def normalize_Hah(text):
    return arabConst.HAH_PAT.sub(arabConst.HAH, text)


# normalize KHAH
def normalize_Khah(text):
    return arabConst.KHAH_PAT.sub(arabConst.KHAH, text)


# normalize DAL
def normalize_Dal(text):
    return arabConst.DAL_PAT.sub(arabConst.DAL, text)


# normalize THAL
def normalize_Thal(text):
    return arabConst.THAL_PAT.sub(arabConst.THAL, text)


# normalize REH
def normalize_Reh(text):
    return arabConst.REH_PAT.sub(arabConst.REH, text)


# normalize ZAIN
def normalize_Zain(text):
    return arabConst.ZAIN_PAT.sub(arabConst.ZAIN, text)


# normalize SEEN
def normalize_SEEN(text):
    return arabConst.SEEN_PAT.sub(arabConst.SEEN, text)


# normalize SHEEN
def normalize_SHEEN(text):
    return arabConst.SHEEN_PAT.sub(arabConst.SHEEN, text)


# normalize SAD
def normalize_Sad(text):
    return arabConst.SAD_PAT.sub(arabConst.SAD, text)


# normalize DAD
def normalize_Dad(text):
    return arabConst.DAD_PAT.sub(arabConst.DAD, text)


# normalize TAH
def normalize_Tah(text):
    return arabConst.TAH_PAT.sub(arabConst.TAH, text)


# normalize ZAH
def normalize_Zah(text):
    return arabConst.ZAH_PAT.sub(arabConst.ZAH, text)


# normalize AIN
def normalize_Ain(text):
    return arabConst.AIN_PAT.sub(arabConst.AIN, text)


# normalize GHAIN
def normalize_Ghain(text):
    return arabConst.GHAIN_PAT.sub(arabConst.GHAIN, text)


# normalize FEH
def normalize_Feh(text):
    return arabConst.FEH_PAT.sub(arabConst.FEH, text)


# normalize QAF
def normalize_Qaf(text):
    return arabConst.QAF_PAT.sub(arabConst.QAF, text)


# normalize KAF
def normalize_Kaf(text):
    return arabConst.KAF_PAT.sub(arabConst.KAF, text)


# normalize LAM
def normalize_LAM(text):
    return arabConst.LAM_PAT.sub(arabConst.LAM, text)


# normalize TCHEH to KAF
def normalize_Tcheh(text):
    return re.sub(u'[%s]' % arabConst.TCHEH, arabConst.KAF, text)


# normalize GAF to QAF
def normalize_Gaf(text):
    return re.sub(u'[%s]' % arabConst.GAF, arabConst.QAF, text)


# normalize MEEM
def normalize_Meem(text):
    return arabConst.MEEM_PAT.sub(arabConst.MEEM, text)


# normalize NOON
def normalize_Noon(text):
    return arabConst.NOON_PAT.sub(arabConst.NOON, text)


# normalize HEH
def normalize_Heh(text):
    return arabConst.HEH_PAT.sub(arabConst.HEH, text)


def normalize_alef_maqsoura(text):
    return arabConst.ALEF_MAQSOURA_PAT.sub(arabConst.YEH, text)


# normalize HEH
def normalize_Yeh(text):
    return arabConst.YEH_PAT.sub(arabConst.YEH, text)

# Normalize One Function
def normalize_text_before_stem(text):
    text = strip_Tashkeel(text)
    text = strip_Tatweel(text)
    text = normalize_Alef_form(text)
    text = normalize_yeh_hamza(text)
    text = normalize_LamAlef(text)
    text = normalize_Beh(text)
    text = normalize_Teh(text)
    text = normalize_Theh(text)
    text = normalize_Jeem(text)
    text = normalize_Hah(text)
    text = normalize_Khah(text)
    text = normalize_Dal(text)
    text = normalize_Thal(text)
    text = normalize_Reh(text)
    text = normalize_Zain(text)
    text = normalize_SEEN(text)
    text = normalize_SHEEN(text)
    text = normalize_Sad(text)
    text = normalize_Dad(text)
    text = normalize_Tah(text)
    text = normalize_Zah(text)
    text = normalize_Ain(text)
    text = normalize_Ghain(text)
    text = normalize_Feh(text)
    text = normalize_Qaf(text)
    text = normalize_Kaf(text)
    text = normalize_Tcheh(text)
    text = normalize_Gaf(text)
    text = normalize_LAM(text)
    text = normalize_Meem(text)
    text = normalize_Noon(text)
    text = normalize_Heh(text)
    text = normalize_Waw(text)
    text = normalize_alef_maqsoura(text)
    text = normalize_Yeh(text)


    text = normalize_Alef(text)
    text = normalize_Teh_Marbuta(text)

    return text


def normalize_text_after_stem(text):
    text = normalize_Alef(text)
    text = normalize_alef_maqsoura(text)
    text = normalize_Teh_Marbuta(text)
    return text
