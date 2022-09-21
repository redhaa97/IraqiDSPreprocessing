
""" Constants for arabic """
import re
HAMZA = u'\u0621'
HAMZA_ISOLATED = u'\uFE80'

ALEF = u'\u0627'
ALEF_MADDA = u'\u0622'
ALEF_HAMZA_ABOVE = u'\u0623'
ALEF_WAVY_HAMZA = u'\u0672'

ALEF_HAMZA_BELOW = u'\u0625'

ALEF_MADDA_ABOVE_IOSLATED  = u'\uFE81'
ALEF_MADDA_ABOVE_FINAL  = u'\uFE82'
ALEF_HAMZA_ABOVE_IOSLATED = u'\uFE83'
ALEF_HAMZA_ABOVE_FINAL = u'\uFE84'
ALEF_HAMZA_BELOW_IOSLATED = u'\uFE87'
ALEF_HAMZA_BELOW_FINAL = u'\uFE88'
ALEF_IOSLATED = u'\uFE8D'
ALEF_FINAL = u'\uFE8E'

WAW_HAMZA = u'\u0624'
WAW_HAMZA_ABOVE_IOSLATED = u'\uFE85'
WAW_HAMZA_ABOVE_FINAL = u'\uFE86'

YEH_HAMZA = u'\u0626'
YEH_HAMZA_ABOVE_IOSLATED = u'\uFE89'
YEH_HAMZA_ABOVE_FINAL = u'\uFE8A'
YEH_HAMZA_ABOVE_INITIAL = u'\uFE8B'
YEH_HAMZA_ABOVE_MEDIAL = u'\uFE8C'

BEH = u'\u0628'
BEH_INITIAL = u'\uFE91'
BEH_ISOLATED = u'\uFE8F'
BEH_MEDIAL = u'\uFE92'
BEH_FINAL = u'\uFE90'
PEH = u'\u067E'

TEH_MARBUTA = u'\u0629'
TEH_MARBUTA_ISOLATED = u'\uFE93'
TEH_MARBUTA_FINAL = u'\uFE94'

TEH = u'\u062a'
TEH_INITIAL = u'\uFE97'
TEH_ISOLATED = u'\uFE95'
TEH_MEDIAL = u'\uFE98'
TEH_FINAL = u'\uFE96'

THEH = u'\u062b'
THEH_INITIAL = u'\uFE9B'
THEH_ISOLATED = u'\uFE99'
THEH_MEDIAL = u'\uFE9C'
THEH_FINAL = u'\uFE9A'

JEEM = u'\u062c'
JEEM_INITIAL = u'\uFE9F'
JEEM_ISOLATED = u'\uFE9D'
JEEM_MEDIAL = u'\uFEA0'
JEEM_FINAL = u'\uFE9E'

HAH = u'\u062d'
HAH_INITIAL = u'\uFEA3'
HAH_ISOLATED = u'\uFEA1'
HAH_MEDIAL = u'\uFEA4'
HAH_FINAL = u'\uFEA2'

KHAH = u'\u062e'
KHAH_INITIAL = u'\uFEA7'
KHAH_ISOLATED = u'\uFEA5'
KHAH_MEDIAL = u'\uFEA8'
KHAH_FINAL = u'\uFEA6'

DAL = u'\u062f'
DAL_ISOLATED = u'\uFEA9'
DAL_FINAL = u'\uFEAA'

THAL = u'\u0630'
THAL_ISOLATED = u'\uFEAB'
THAL_FINAL = u'\uFEAC'

REH = u'\u0631'
REH_ISOLATED = u'\uFEAD'
REH_FINAL = u'\uFEAE'

ZAIN = u'\u0632'
ZAIN_ISOLATED = u'\uFEAF'
ZAIN_FINAL = u'\uFEB0'

SEEN = u'\u0633'
SEEN_INITIAL = u'\uFEB3'
SEEN_ISOLATED = u'\uFEB1'
SEEN_MEDIAL = u'\uFEB4'
SEEN_FINAL = u'\uFEB2'

SHEEN = u'\u0634'
SHEEN_INITIAL = u'\uFEB7'
SHEEN_ISOLATED = u'\uFEB5'
SHEEN_MEDIAL = u'\uFEB8'
SHEEN_FINAL = u'\uFEB6'
SHEEN_WITH_THREE_DOTS_BELOW = u'\u069C'

SAD = u'\u0635'
SAD_INITIAL = u'\uFEBB'
SAD_ISOLATED = u'\uFEB9'
SAD_MEDIAL = u'\uFEBC'
SAD_FINAL = u'\uFEBA'

DAD = u'\u0636'
DAD_INITIAL = u'\uFEBF'
DAD_ISOLATED = u'\uFEBD'
DAD_MEDIAL = u'\uFEC0'
DAD_FINAL = u'\uFEBE'

TAH = u'\u0637'
TAH_INITIAL = u'\uFEC3'
TAH_ISOLATED = u'\uFEC1'
TAH_MEDIAL = u'\uFEC4'
TAH_FINAL = u'\uFEC2'

ZAH = u'\u0638'
ZAH_INITIAL = u'\uFEC7'
ZAH_ISOLATED = u'\uFEC5'
ZAH_MEDIAL = u'\uFEC8'
ZAH_FINAL = u'\uFEC6'

AIN = u'\u0639'
AIN_INITIAL = u'\uFECB'
AIN_ISOLATED = u'\uFEC9'
AIN_MEDIAL = u'\uFECC'
AIN_FINAL = u'\uFECA'

GHAIN = u'\u063a'
GHAIN_INITIAL = u'\uFECF'
GHAIN_ISOLATED = u'\uFECD'
GHAIN_MEDIAL = u'\uFED0'
GHAIN_FINAL = u'\uFECE'

TATWEEL = u'\u0640'

FEH = u'\u0641'
FEH_INITIAL = u'\uFED3'
FEH_ISOLATED = u'\uFED1'
FEH_MEDIAL = u'\uFED4'
FEH_FINAL = u'\uFED2'
VEH = u'\u06A4'

QAF = u'\u0642'
QAF_INITIAL = u'\uFED7'
QAF_ISOLATED = u'\uFED5'
QAF_MEDIAL = u'\uFED8'
QAF_FINAL = u'\uFED6'

KAF = u'\u0643'
KAF_INITIAL = u'\uFEDB'
KAF_ISOLATED = u'\uFED9'
KAF_MEDIAL = u'\uFEDC'
KAF_FINAL = u'\uFEDB'
KAF_WITH_RING = u'\u06AB'
KAHEH = u'\u06a9'
KAF_TWO_DOTS_ABOVE = u'\u063B'
KAF_TWO_DOTS_BELOW = u'\u063C'

LAM = u'\u0644'
LAM_INITIAL = u'\uFEDF'
LAM_ISOLATED = u'\uFEDD'
LAM_MEDIAL = u'\uFEE0'
LAM_FINAL = u'\uFEDE'
LAM_SMALL_V = u'\u06B5'

MEEM = u'\u0645'
MEEM_INITIAL = u'\uFEE3'
MEEM_ISOLATED = u'\uFEE1'
MEEM_MEDIAL = u'\uFEE4'
MEEM_FINAL = u'\uFEE2'

NOON = u'\u0646'
NOON_INITIAL = u'\uFEE7'
NOON_ISOLATED = u'\uFEE5'
NOON_MEDIAL = u'\uFEE8'
NOON_FINAL = u'\uFEE6'

HEH = u'\u0647'
HEH_INITIAL = u'\uFEEB'
HEH_ISOLATED = u'\uFEE9'
HEH_MEDIAL = u'\uFEEC'
HEH_FINAL = u'\uFEEA'
HEH_DOACHASHMEE = u'\u06BE'
HEH_DOACH = u'\ufbab'

WAW = u'\u0648'
WAW_ISOLATED = u'\uFEED'
WAW_FINAL = u'\uFEEE'
WAW_ISOLATED_FORM = u'\uFBD9'

ALEF_MAQSOURA = u'\u0649'
ALEF_MAQSOURA_ISOLATED = u'\uFEEF'
ALEF_MAQSOURA_FINAL = u'\uFEF0'
YEH_HAMZA_ABOVE = u'\u06D3'


YEH = u'\u064a'
YEH_INITIAL = u'\uFEF3'
YEH_ISOLATED = u'\uFEF1'
YEH_MEDIAL = u'\uFEF4'
YEH_FINAL = u'\uFEF2'
FARSI_YEH = u'\u06CC'




# Arabic Numbers
ZERO = u'\u0660'
ONE = u'\u0661'
TWO = u'\u0662'
THREE = u'\u0663'
FOUR = u'\u0664'
FIVE = u'\u0665'
SIX = u'\u0666'
SEVEN = u'\u0667'
EIGHT = u'\u0668'
NINE = u'\u0669'

# Arabic Symbols
INDIC_PER_MILLE = u'\u0609'
INDIC_PER_TEN_THOUSANDS = u'\u060a'
DATE_SAPERATOR = u'\u060d'
TRIPLE_DOT = u'\u061e'
PERCENT = u'\u066a'
DECIMAL = u'\u066b'
THOUSANDS = u'\u066c'
STAR = u'\u066d'
YEH_BARREE = u'\u06D2'
SUBSCRIPT_ALEF = u'\u0656'
SUPERSCRIPT_ALEF = u'\u0670'
HEH_GOAL = u'\u06C1'
INDIC_DIGIT_SIX = u'\u06F6'

# Arabic Punctuation
SIGN_SANAH = u'\u0601'
FOOTNOTE_MARKER = u'\u0602'
SIGN_SAFHA = u'\u0603'
COMMA = u'\u060C'
SEMICOLON = u'\u061B'
QUESTION_MARK = u'\u061F'
AFGHANI_SIGN = u'\u060B'
RIAL_SIGN = u'\uFDFC'



BLANK = u'\u2800'



MINI_ALEF = u'\u0670'
ALEF_WASLA = u'\u0671'
FULL_STOP = u'\u06d4'
BYTE_ORDER_MARK = u'\ufeff'

# Diacritics
FATHATAN = u'\u064b'
DAMMATAN = u'\u064c'
KASRATAN = u'\u064d'
FATHA = u'\u064e'
DAMMA = u'\u064f'
KASRA = u'\u0650'
SHADDA = u'\u0651'
SUKUN = u'\u0652'
MADDA_ABOVE = u'\u0653'
HAMZA_ABOVE = u'\u0654'
HAMZA_BELOW = u'\u0655'


#Iraqi
TCHEH = u'\u0686'
GAF= u'\u06AF'

#Ligatures
LAM_ALEF = u'\uFEFB'
LAM_ALEF_FINAL = u'\uFEFC'
LAM_ALEF_HAMZA_ABOVE = u'\uFEF7'
LAM_ALEF_HAMZA_BELOW = u'\uFEF9'
LAM_ALEF_MADDA_ABOVE = u'\uFEF5'
LAM_ALEF_HAMZA_ABOVE_FINAL = u'\uFEF8'
LAM_ALEF_HAMZA_BELOW_FINAL = u'\uFEFA'
LAM_ALEF_MADDA_ABOVE_FINAL = u'\uFEF6'
SIMPLE_LAM_ALEF = u'\u0644\u0627'
SIMPLE_LAM_ALEF_HAMZA_ABOVE = u'\u0644\u0623'
SIMPLE_LAM_ALEF_HAMZA_BELOW = u'\u0644\u0625'
SIMPLE_LAM_ALEF_MADDA_ABOVE = u'\u0644\u0622'


HARAKAT_PAT = re.compile(u"["+u"".join([FATHATAN, DAMMATAN, KASRATAN,
                                        FATHA, DAMMA, KASRA, SUKUN, MADDA_ABOVE,
                                        SHADDA])+u"]")

HAMZAT_PAT = re.compile(u"["+u"".join([WAW_HAMZA, YEH_HAMZA])+u"]")


HAMZA_PAT = re.compile(u"["+u"".join([HAMZA, HAMZA_ABOVE, HAMZA_BELOW])+u"]")

ALEFAT_PAT = re.compile(u"["+u"".join([ALEF_MADDA, ALEF_HAMZA_ABOVE,
                                       ALEF_HAMZA_BELOW, HAMZA_ABOVE, HAMZA_BELOW,
                                        ALEF_WAVY_HAMZA,])+u"]")

ALEF_FORM_PAT = re.compile(u"["+u"".join([ALEF_WAVY_HAMZA, ALEF_HAMZA_ABOVE_IOSLATED,
                                          ALEF_HAMZA_BELOW_IOSLATED, ALEF_HAMZA_ABOVE_FINAL,
                                          ALEF_HAMZA_BELOW_FINAL, ALEF_IOSLATED, ALEF_MADDA_ABOVE_IOSLATED,
                                          ALEF_MADDA_ABOVE_FINAL, ALEF_FINAL])+u"]")

LAMALEFAT_PAT = re.compile(u"["+u"".join([LAM_ALEF, LAM_ALEF_FINAL,
                                          LAM_ALEF_HAMZA_ABOVE, LAM_ALEF_HAMZA_BELOW,
                                          LAM_ALEF_MADDA_ABOVE, LAM_ALEF_MADDA_ABOVE_FINAL,
                                          LAM_ALEF_HAMZA_ABOVE_FINAL, LAM_ALEF_HAMZA_BELOW_FINAL,
                                          ])+u"]")

WAW_PAT = re.compile(u"["+u"".join([WAW_HAMZA,  WAW_HAMZA_ABOVE_IOSLATED,
                                    WAW_HAMZA_ABOVE_FINAL, WAW_ISOLATED, WAW_FINAL,
                                    WAW_ISOLATED_FORM])+u"]")

YEH_HAMZA_PAT = re.compile(u"["+u"".join([YEH_HAMZA_ABOVE_IOSLATED, YEH_HAMZA_ABOVE_INITIAL,
                                          YEH_HAMZA_ABOVE_FINAL, YEH_HAMZA_ABOVE_MEDIAL])+u"]")

BEH_PAT = re.compile(u"["+u"".join([BEH_ISOLATED, BEH_INITIAL, BEH_MEDIAL,BEH_FINAL,PEH])+u"]")

TEH_MARBUTA_PAT = re.compile(u"["+u"".join([TEH_MARBUTA, TEH_MARBUTA_ISOLATED, TEH_MARBUTA_FINAL])+u"]")

TEH_PAT = re.compile(u"["+u"".join([TEH_ISOLATED, TEH_INITIAL, TEH_MEDIAL, TEH_FINAL])+u"]")

THEH_PAT = re.compile(u"["+u"".join([THEH_ISOLATED, THEH_INITIAL, THEH_MEDIAL, THEH_FINAL])+u"]")

JEEM_PAT = re.compile(u"["+u"".join([JEEM_ISOLATED, JEEM_INITIAL, JEEM_MEDIAL, JEEM_FINAL])+u"]")

HAH_PAT = re.compile(u"["+u"".join([HAH_ISOLATED, HAH_INITIAL, HAH_MEDIAL, HAH_FINAL])+u"]")

KHAH_PAT = re.compile(u"["+u"".join([KHAH_ISOLATED, KHAH_INITIAL, KHAH_MEDIAL, KHAH_FINAL])+u"]")

DAL_PAT = re.compile(u"["+u"".join([DAL_ISOLATED, DAL_FINAL])+u"]")

THAL_PAT = re.compile(u"["+u"".join([THAL_ISOLATED, THAL_FINAL])+u"]")

REH_PAT = re.compile(u"["+u"".join([REH_ISOLATED, REH_FINAL])+u"]")

ZAIN_PAT = re.compile(u"["+u"".join([ZAIN_ISOLATED, ZAIN_FINAL])+u"]")

SEEN_PAT = re.compile(u"["+u"".join([SEEN_ISOLATED, SEEN_INITIAL, SEEN_MEDIAL, SEEN_FINAL])+u"]")

SHEEN_PAT = re.compile(u"["+u"".join([SHEEN_WITH_THREE_DOTS_BELOW, SHEEN_ISOLATED, SHEEN_INITIAL,
                                      SHEEN_MEDIAL, SHEEN_FINAL])+u"]")

SAD_PAT = re.compile(u"["+u"".join([SAD_ISOLATED, SAD_INITIAL, SAD_MEDIAL, SAD_FINAL])+u"]")

DAD_PAT = re.compile(u"["+u"".join([DAD_ISOLATED, DAD_INITIAL, DAD_MEDIAL, DAD_FINAL])+u"]")

TAH_PAT = re.compile(u"["+u"".join([TAH_ISOLATED, TAH_INITIAL, TAH_MEDIAL, TAH_FINAL])+u"]")

ZAH_PAT = re.compile(u"["+u"".join([ZAH_ISOLATED, ZAH_INITIAL, ZAH_MEDIAL, ZAH_FINAL])+u"]")

AIN_PAT = re.compile(u"["+u"".join([AIN_ISOLATED, AIN_INITIAL, AIN_MEDIAL, AIN_FINAL])+u"]")

GHAIN_PAT = re.compile(u"["+u"".join([GHAIN_ISOLATED, GHAIN_INITIAL, GHAIN_MEDIAL, GHAIN_FINAL])+u"]")

FEH_PAT = re.compile(u"["+u"".join([FEH_ISOLATED, FEH_INITIAL, FEH_MEDIAL, FEH_FINAL, VEH])+u"]")

QAF_PAT = re.compile(u"["+u"".join([QAF_ISOLATED, QAF_INITIAL, QAF_MEDIAL, QAF_FINAL])+u"]")

KAF_PAT =  re.compile(u"["+u"".join([KAF_WITH_RING, KAHEH, KAF_ISOLATED, KAF_INITIAL, KAF_MEDIAL,
                                     KAF_FINAL, KAF_TWO_DOTS_ABOVE, KAF_TWO_DOTS_BELOW])+u"]")

LAM_PAT = re.compile(u"["+u"".join([LAM_SMALL_V, LAM_ISOLATED, LAM_INITIAL, LAM_MEDIAL, LAM_FINAL])+u"]")

MEEM_PAT = re.compile(u"["+u"".join([MEEM_ISOLATED, MEEM_INITIAL, MEEM_MEDIAL, MEEM_FINAL])+u"]")

NOON_PAT = re.compile(u"["+u"".join([NOON_ISOLATED, NOON_INITIAL, NOON_MEDIAL, NOON_FINAL])+u"]")

HEH_PAT = re.compile(u"["+u"".join([HEH_ISOLATED, HEH_INITIAL, HEH_MEDIAL, HEH_FINAL,
                                    HEH_DOACH, HEH_DOACHASHMEE])+u"]")

ALEF_MAQSOURA_PAT = re.compile(u"[" + u"".join([ALEF_MAQSOURA, YEH_HAMZA_ABOVE, ALEF_MAQSOURA_ISOLATED,
                                                ALEF_MAQSOURA_FINAL]) + u"]")

YEH_PAT  = re.compile(u"["+u"".join([YEH_ISOLATED, YEH_INITIAL, YEH_MEDIAL, YEH_FINAL, FARSI_YEH])+u"]")

#
ARABIC_PUNCTUATION_PAT = re.compile(u"["+u"".join([SIGN_SANAH, FOOTNOTE_MARKER, SEMICOLON,
                                                  SIGN_SAFHA, AFGHANI_SIGN, RIAL_SIGN ])+u"]")

ARABIC_SYMBOLS_PAT = re.compile(u"["+u"".join([INDIC_PER_MILLE, INDIC_PER_TEN_THOUSANDS,
                                               DATE_SAPERATOR,
                                               PERCENT, DECIMAL, THOUSANDS, STAR, TRIPLE_DOT, YEH_BARREE,
                                               SUBSCRIPT_ALEF, SUPERSCRIPT_ALEF, HEH_GOAL, INDIC_DIGIT_SIX])+u"]")

ARABIC_NUMBERS_PAT = re.compile(u"["+u"".join([ZERO, ONE, TWO, THREE, FOUR,
                                               FIVE, SIX, SEVEN, EIGHT, NINE])+u"]")

SPACE_PAT = re.compile(u"["+u"".join([COMMA, FULL_STOP, QUESTION_MARK, BLANK])+u"]")






