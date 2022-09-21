"""constants for English"""

import re

# Basic Latin
EXCLAMATION_MARK = u'\u0021'
QUOTATION_MARK = u'\u0022'
NUMBER_SIGN = u'\u0023'
DOLLAR_SIGN = u'\u0024'
PRECENT_SIGN = u'\u0025'
AMPERSAND = u'\u0026'
APOSTROPHE = u'\u0027'
LEFT_PARENTHESIS = u'\u0028'
RIGHT_PARENTHESIS = u'\u0029'
ASTERISK = u'\u002A'
PLUS_SIGN = u'\u002B'
COMMA = u'\u002C'
HYPHEN_MINUS = u'\u002D'
FULL_STOP = u'\u002e'
SOLIDUS = u'\u002F'
COLON = u'\u003A'
SEMICOLON = u'\u003B'
LESS_THAN = u'\u003C'
EQUAL = u'\u003D'
MORE_THAN = u'\u003E'
QUESTION_MARK = u'\u003F'
COMMERCIAL_AT = u'\u0040'
LEFT_SQUARE_BRACKET = u'\u005B'
REVERSE_SOLIDUS = u'\u005C'
RIGHT_SQUARE_BRACKET = u'\u005D'
CIRCUMFLEX_ACCENT = u'\u005E'
LOW_LINE = u'\u005F'
GRAVE_ACCENT = u'\u0060'
LEFT_CURLY_BRACKET = u'\u007B'
VERTICAL_LINE = u'\u007C'
RIGHT_CURLY_BRACKET = u'\u007D'
TILDE = u'\u007E'

ENGLISH_SYMBOLS_PAT = re.compile(u"[" + u"".join([RIGHT_CURLY_BRACKET, TILDE,
                                                  DOLLAR_SIGN, PRECENT_SIGN, AMPERSAND, APOSTROPHE,
                                                  LEFT_PARENTHESIS, RIGHT_PARENTHESIS, ASTERISK,  COMMA,
                                                  HYPHEN_MINUS, SOLIDUS, COLON, SEMICOLON, LESS_THAN,
                                                  EQUAL, MORE_THAN, QUESTION_MARK, COMMERCIAL_AT, LEFT_SQUARE_BRACKET,
                                                  REVERSE_SOLIDUS, RIGHT_SQUARE_BRACKET, CIRCUMFLEX_ACCENT,
                                                  GRAVE_ACCENT, LEFT_CURLY_BRACKET,
                                                  VERTICAL_LINE, ]) + u"]")

# General Punctuation
HYPHEN = u'\u2010'
NONBREAKING_HYPHEN = u'\u2011'
FIGURE_DASH = u'\u2012'
EN_DUSH = u'\u2013'
EM_DUSH = u'\u2014'
HORIZONTAL_BAR = u'\u2015'
DOUBLE_VERTICAL_LINE = u'\u2016'
DOUBLE_LOW_LINE = u'\u2017'
LEFT_SINGLE_QUOTATION_MARK = u'\u2018'
RIGHT_SINGLE_QUOTATION_MARK = u'\u2019'
SINGLE_LOW_QUOTATION_MARK = u'\u201A'
SINGLE_HIGH_QUOTATION_MARK = u'\u201B'
LEFT_DOUBLE_QUOTATION_MARK = u'\u201C'
RIGHT_DOUBLE_QUOTATION_MARK = u'\u201D'
DOUBLE_LOW_QUOTATION_MARK = u'\u201E'
DOUBLE_HIGH_QUOTATION_MARK = u'\u201F'
BULLET = u'\u2022'
ONE_DOT_LEADER = u'\u2024'
TWO_DOT_LEADER = u'\u2025'
THREE_DOT_LEADER = u'\u2026'
HYPHENATION_POINT = u'\u2027'
LINE_SEPARATOR = u'\u2028'
PARAGRAPH_SEPARATOR = u'\u2029'
PER_MILLE_SIGN = u'\u2030'
PER_TEN_THOUSAND_SIGN = u'\u2031'
PRIME = u'\u2032'
DOUBLE_PRIME = u'\u2033'
TRIPLE_PRIME = u'\u2034'
REVERSED_PRIME = u'\u2035'
REVERSED_DOUBLE_PRIME = u'\u2036'
REVERSED_TRIPLE_PRIME = u'\u2037'

GENERAL_PUNCTUATION_PAT = re.compile(u"[" + u"".join([HYPHEN, NONBREAKING_HYPHEN, FIGURE_DASH,
                                                      EN_DUSH, EM_DUSH, HORIZONTAL_BAR, DOUBLE_VERTICAL_LINE,
                                                      DOUBLE_LOW_LINE, LEFT_SINGLE_QUOTATION_MARK,
                                                      RIGHT_SINGLE_QUOTATION_MARK,
                                                      LEFT_DOUBLE_QUOTATION_MARK, RIGHT_DOUBLE_QUOTATION_MARK,
                                                      SINGLE_LOW_QUOTATION_MARK, DOUBLE_LOW_QUOTATION_MARK,
                                                      DOUBLE_HIGH_QUOTATION_MARK, BULLET, ONE_DOT_LEADER,
                                                      TWO_DOT_LEADER, THREE_DOT_LEADER, HYPHENATION_POINT,
                                                      LINE_SEPARATOR, PARAGRAPH_SEPARATOR, PER_MILLE_SIGN,
                                                      PER_TEN_THOUSAND_SIGN, PRIME, DOUBLE_PRIME, TRIPLE_PRIME,
                                                      REVERSED_PRIME, REVERSED_DOUBLE_PRIME,
                                                      REVERSED_TRIPLE_PRIME]) + u"]")

# latin_1_supplement
INVERTED_EXCLAMATION_MARK = u'\u00A1'
CENT_SIGN = u'\u00A2'
POUND_SIGN = u'\u00A3'
CURRENCY_SIGN = u'\u00A4'
YEN_SIGN = u'\u00A5'
BROKEN_BAR = u'\u00A6'
SECTION_SIGN = u'\u00A7'
DIAERESIS = u'\u00A8'
COPYRIGHT_SIGN = u'\u00A9'
FEMININE_ORDINAL_INDICATOR = u'\u00AA'
LEFT_POINTING_MARK = u'\u00AB'
NOT_SIGN = u'\u00AC'
REGISTERED_SIGN = u'\u00AE'
MACRON = u'\u00AF'
DEGREE_SIGN = u'\u00B0'
PLUS_MINUS_SIGN = u'\u00B1'
SUPERSCRIPT_TWO = u'\u00B2'
SUPERSCRIPT_THREE = u'\u00B3'
ACUTE_ACCENT = u'\u00B4'
MICRO_SIGN = u'\u00B5'
PILCROW_SIGN = u'\u00B6'
MIDDLE_DOT = u'\u00B7'
CEDILLA = u'\u00B6'
SUPERSCRIPT_ONE = u'\u00B9'
MASCULINE_ORDINAL_INDICATOR = u'\u00BA'
RIGHT_POINTING_MARK = u'\u00BB'
ONE_QUARTER = u'\u00BC'
ONE_HALF = u'\u00BD'
THREE_QUARTERS = u'\u00BE'
INVERTED_QUESTION_MARK = u'\u00BF'
CAPITAL_A_GRAVE = u'\u00C0'
CAPITAL_A_ACUTE = u'\u00C1'
CAPITAL_A_CIRCUMFLEX = u'\u00C2'
CAPITAL_A_TILDE = u'\u00C3'
CAPITAL_A_DIAERESIS = u'\u00C4'
CAPITAL_A_RING_ABOVE = u'\u00C5'
CAPITAL_A_E = u'\u00C6'
CAPITAL_C_CEDILLA = u'\u00C7'
CAPITAL_E_GRAVE = u'\u00C8'
CAPITAL_E_ACUTE = u'\u00C9'
CAPITAL_E_CIRCUMFLEX = u'\u00CA'
CAPITAL_E_DIAERESIS = u'\u00CB'
CAPITAL_I_GRAVE = u'\u00CC'
CAPITAL_I_ACUTE = u'\u00CE'
CAPITAL_I_CIRCUMFLEX = u'\u00CD'
CAPITAL_I_DIAERESIS = u'\u00CF'
CAPITAL_D_ETH = u'\u00D0'
CAPITAL_N_TILDE = u'\u00D1'
CAPITAL_O_GRAVE = u'\u00D2'
CAPITAL_O_ACUTE = u'\u00D3'
CAPITAL_O_CIRCUMFLEX = u'\u00D4'
CAPITAL_O_TILDE = u'\u00D5'
CAPITAL_O_DIAERESIS = u'\u00D6'
MULTIPLICATION_SIGN = u'\u00D7'
CAPITAL_O_STROKE = u'\u00D8'
CAPITAL_U_GRAVE = u'\u00D9'
CAPITAL_U_ACUTE = u'\u00DA'
CAPITAL_U_CIRCUMFLEX = u'\u00DB'
CAPITAL_U_DIAERESIS = u'\u00DC'
CAPITAL_Y_ACUTE = u'\u00DD'
CAPITAL_THORN = u'\u00DE'
SMALL_SHARP_S = u'\u00DF'
SMALL_A_GRAVE = u'\u00E0'
SMALL_A_ACUTE = u'\u00E1'
SMALL_A_CIRCUMFLEX = u'\u00E2'
SMALL_A_TILDE = u'\u00E3'
SMALL_A_DIAERESIS = u'\u00E4'
SMALL_A_RING_ABOVE = u'\u00E5'
SMALL_A_E = u'\u00E6'
SMALL_C_CEDILLA = u'\u00E7'
SMALL_E_GRAVE = u'\u00E8'
SMALL_E_ACUTE = u'\u00E9'
SMALL_E_CIRCUMFLEX = u'\u00EA'
SMALL_E_DIAERESIS = u'\u00EB'
SMALL_I_GRAVE = u'\u00EC'
SMALL_I_ACUTE = u'\u00EE'
SMALL_I_CIRCUMFLEX = u'\u00ED'
SMALL_I_DIAERESIS = u'\u00EF'
SMALL_ETH = u'\u00F0'
SMALL_N_TILDE = u'\u00F1'
SMALL_O_GRAVE = u'\u00F2'
SMALL_O_ACUTE = u'\u00F3'
SMALL_O_CIRCUMFLEX = u'\u00F4'
SMALL_O_TILDE = u'\u00F5'
SMALL_O_DIAERESIS = u'\u00F6'
DIVISION_SIGN = u'\u00F7'
SMALL_O_STROKE = u'\u00F8'
SMALL_U_GRAVE = u'\u00F9'
SMALL_U_ACUTE = u'\u00FA'
SMALL_U_CIRCUMFLEX = u'\u00FB'
SMALL_U_DIAERESIS = u'\u00FC'
SMALL_Y_ACUTE = u'\u00FD'
SMALL_THORN = u'\u00FE'
SMALL_Y_DIAERESIS = u'\u00FF'
CAPITAL_A_MACRON = u'\u0100'
SMALL_A_MACRON = u'\u0101'
CAPITAL_A_BREVE = u'\u0102'
SMALL_A_BREVE = u'\u0103'
CAPITAL_A_OGONEK = u'\u0104'
SMALL_A_OGONEK = u'\u0105'
CAPITAL_C_ACUTE = u'\u0106'
SMALL_C_ACUTE = u'\u0107'
CAPITAL_C_CIRCUMFLEX = u'\u0108'
SMALL_C_CIRCUMFLEX = u'\u0109'
CAPITAL_C_DOT_ABOVE = u'\u010A'
SMALL_C_DOT_ABOVE = u'\u010B'
CAPITAL_C_CARON = u'\u010C'
SMALL_C_CARON = u'\u010D'
CAPITAL_D_CARON = u'\u010E'
SMALL_D_CARON = u'\u010F'
CAPITAL_D_STROKE = u'\u0110'
SMALL_D_STROKE = u'\u0111'
CAPITAL_E_MACRON = u'\u0112'
SMALL_E_MACRON = u'\u0113'
CAPITAL_E_BREVE = u'\u0114'
SMALL_E_BREVE = u'\u0115'
CAPITAL_E_DOT_ABOVE = u'\u0116'
SMALL_E_DOT_ABOVE = u'\u0117'
CAPITAL_E_OGONEK = u'\u0118'
SMALL_E_OGONEK = u'\u0119'
CAPITAL_E_CARON = u'\u011A'
SMALL_E_CARON = u'\u011B'
CAPITAL_G_CIRCUMFLEX = u'\u011C'
SMALL_G_CIRCUMFLEX = u'\u011D'
CAPITAL_G_BREVE = u'\u011E'
SMALL_G_BREVE = u'\u011F'
CAPITAL_G_DOT_ABOVE = u'\u0120'
SMALL_G_DOT_ABOVE = u'\u0121'
CAPITAL_G_CEDILLA = u'\u0122'
SMALL_G_CEDILLA = u'\u0123'
CAPITAL_H_CIRCUMFLEX = u'\u0124'
SMALL_H_CIRCUMFLEX = u'\u0125'
CAPITAL_H_STROKE = u'\u0126'
SMALL_H_STROKE = u'\u0127'
CAPITAL_I_TILDE = u'\u0128'
SMALL_I_TILDE = u'\u0129'
CAPITAL_I_MACRON = u'\u012A'
SMALL_I_MACRON = u'\u012B'
CAPITAL_I_BREVE = u'\u012C'
SMALL_I_BREVE = u'\u012D'
CAPITAL_I_OGONEK = u'\u012E'
SMALL_I_OGONEK = u'\u012F'
CAPITAL_I_DOT_ABOVE = u'\u0130'
SMALL_DOTLESS_I = u'\u0131'
CAPITAL_LIGATURE_IJ = u'\u0132'
SMALL_LIGATURE_IJ = u'\u0133'

LATIN_SUPPLEMENT_PAT = re.compile(u"[" + u"".join([INVERTED_EXCLAMATION_MARK, CENT_SIGN,
                                                   POUND_SIGN, CURRENCY_SIGN, YEN_SIGN, BROKEN_BAR, SECTION_SIGN,
                                                   DIAERESIS, COPYRIGHT_SIGN, FEMININE_ORDINAL_INDICATOR,
                                                   LEFT_POINTING_MARK,
                                                   NOT_SIGN, REGISTERED_SIGN, MACRON, DEGREE_SIGN, PLUS_MINUS_SIGN,
                                                   SUPERSCRIPT_TWO, SUPERSCRIPT_THREE, ACUTE_ACCENT, MICRO_SIGN,
                                                   PILCROW_SIGN, MIDDLE_DOT, CEDILLA, SUPERSCRIPT_ONE, ONE_QUARTER,
                                                   MASCULINE_ORDINAL_INDICATOR, THREE_QUARTERS, ONE_HALF,
                                                   RIGHT_POINTING_MARK, INVERTED_QUESTION_MARK, CAPITAL_A_GRAVE,
                                                   CAPITAL_A_ACUTE, CAPITAL_A_DIAERESIS, CAPITAL_A_TILDE,
                                                   CAPITAL_A_RING_ABOVE,
                                                   CAPITAL_A_E, CAPITAL_A_CIRCUMFLEX, CAPITAL_C_CEDILLA,
                                                   CAPITAL_E_GRAVE,
                                                   CAPITAL_E_DIAERESIS, CAPITAL_E_ACUTE, CAPITAL_E_CIRCUMFLEX,
                                                   CAPITAL_I_GRAVE, CAPITAL_I_ACUTE, CAPITAL_I_CIRCUMFLEX,
                                                   CAPITAL_I_DIAERESIS,
                                                   CAPITAL_D_ETH, CAPITAL_N_TILDE, CAPITAL_O_GRAVE, CAPITAL_O_ACUTE,
                                                   CAPITAL_O_CIRCUMFLEX, CAPITAL_O_TILDE, CAPITAL_O_DIAERESIS,
                                                   CAPITAL_O_STROKE,
                                                   MULTIPLICATION_SIGN, CAPITAL_U_GRAVE, CAPITAL_U_ACUTE,
                                                   CAPITAL_U_DIAERESIS,
                                                   CAPITAL_U_CIRCUMFLEX, CAPITAL_Y_ACUTE, CAPITAL_THORN, SMALL_SHARP_S,
                                                   SMALL_A_GRAVE, SMALL_A_ACUTE, SMALL_A_DIAERESIS, SMALL_A_CIRCUMFLEX,
                                                   SMALL_A_TILDE, SMALL_A_RING_ABOVE, SMALL_A_E, SMALL_C_CEDILLA,
                                                   SMALL_E_GRAVE, SMALL_E_ACUTE, SMALL_E_DIAERESIS, SMALL_E_CIRCUMFLEX,
                                                   SMALL_I_GRAVE, SMALL_I_ACUTE, SMALL_I_DIAERESIS, SMALL_I_CIRCUMFLEX,
                                                   SMALL_ETH, SMALL_N_TILDE, SMALL_O_GRAVE, SMALL_O_ACUTE,
                                                   SMALL_O_DIAERESIS,
                                                   SMALL_O_CIRCUMFLEX, SMALL_O_TILDE, SMALL_O_STROKE, DIVISION_SIGN,
                                                   SMALL_U_GRAVE, SMALL_U_ACUTE, SMALL_U_DIAERESIS, SMALL_U_CIRCUMFLEX,
                                                   SMALL_THORN, SMALL_Y_ACUTE, SMALL_Y_DIAERESIS, CAPITAL_A_MACRON,
                                                   SMALL_A_MACRON, CAPITAL_A_BREVE, SMALL_A_BREVE, CAPITAL_A_OGONEK,
                                                   SMALL_A_OGONEK, CAPITAL_C_ACUTE, SMALL_C_ACUTE, CAPITAL_A_CIRCUMFLEX,
                                                   SMALL_C_CIRCUMFLEX, CAPITAL_C_DOT_ABOVE, SMALL_C_DOT_ABOVE,
                                                   CAPITAL_C_CARON, SMALL_C_CARON, CAPITAL_D_CARON, SMALL_D_CARON,
                                                   CAPITAL_D_STROKE, SMALL_D_STROKE, CAPITAL_E_MACRON, SMALL_E_MACRON,
                                                   CAPITAL_E_BREVE, SMALL_E_BREVE, CAPITAL_E_DOT_ABOVE,
                                                   SMALL_E_DOT_ABOVE,
                                                   CAPITAL_E_OGONEK, SMALL_E_OGONEK, CAPITAL_E_CARON, SMALL_E_CARON,
                                                   CAPITAL_G_CIRCUMFLEX, SMALL_G_CIRCUMFLEX, CAPITAL_G_BREVE,
                                                   SMALL_G_BREVE, CAPITAL_G_DOT_ABOVE, SMALL_G_DOT_ABOVE,
                                                   CAPITAL_G_CEDILLA, SMALL_G_CEDILLA, CAPITAL_H_CIRCUMFLEX,
                                                   SMALL_H_CIRCUMFLEX, CAPITAL_H_STROKE, SMALL_H_STROKE,
                                                   CAPITAL_I_TILDE,
                                                   SMALL_I_TILDE, CAPITAL_I_MACRON, SMALL_I_MACRON, CAPITAL_I_BREVE,
                                                   SMALL_I_BREVE, CAPITAL_I_OGONEK, SMALL_I_OGONEK, CAPITAL_I_DOT_ABOVE,
                                                   SMALL_DOTLESS_I, CAPITAL_LIGATURE_IJ, SMALL_LIGATURE_IJ,
                                                   ]) + u"]")

# Latin Extended-A
S_CARON = u'\u0161'
H_STROKE = u'\u0127'
S_CARON_SMALL = u'\u0160'

LATIN_A_PAT = re.compile(u"[" + u"".join([S_CARON, H_STROKE, S_CARON_SMALL]) + u"]")

# Latin Extended-B
REVERSED_E = u'\u018E'

LATIN_B_PAT = re.compile(u"[" + u"".join([REVERSED_E]) + u"]")

# Random Blocks
HEBREW_TET = u'\u05D8'
SMALL_EM = u'\u043C'
SMALL_CAPITAL_I = u'\u026A'
SMALL_U = u'\u0443'
SMALL_L = u'\u2113'
SMALL_SIGMA = u'\u03C3'
SMALL_NU = u'\u03BD'
UKRAINIAN_LE = u'\u0454'
W_WITH_DIAERESIS = u'\u1E85'
DIAERESIS = u'\u0308'
DIAERESIS_BELOW = u'\u0324'
RING_BELOW = u'\u0325'
RING_ABOVE = u'\u030A'
DOUBLE__DOT_ABOVE = u'\u07F3'
SHORT_RISING_TONE = u'\u07ED'
H_DIAERESIS = u'\u1E27'
BLACK_CIRCLE = u'\u25CF'
SMALL_TURNED_W = u'\u028D'
SMALL_GHAD = u'\u0572'
SMALL_FEH = u'\u0586'
DASH_VERTICAL = u'\u250A'
VAAVU = u'\u0788'
LEFT_ARROW = u'\u2190'

# General Punctuation
ZWSP = u'\u200b'
ZWNJ = u'\u200c'
ZWJ = u'\u200d'
LRM = u'\u200e'
RLM = u'\u200f'
LRE = u'\u202a'
RLE = u'\u202b'
PDF = u'\u202c'
LRO = u'\u202d'
RLO = u'\u202e'
NNBSP = u'\u202f'
MMSP = u'\u205f'
WJ = u'\u2060'
LRI = u'\u2066'
RLI = u'\u2067'
FSI = u'\u2068'
PDI = u'\u2069'


RANDOM_PAT = re.compile(u"[" + u"".join([SMALL_EM, HEBREW_TET, SMALL_CAPITAL_I,
                                         SMALL_L, SMALL_SIGMA, SMALL_NU, UKRAINIAN_LE, SMALL_U,
                                         W_WITH_DIAERESIS, DIAERESIS_BELOW, DIAERESIS, RING_BELOW, LEFT_ARROW,
                                         RING_ABOVE, DOUBLE__DOT_ABOVE, SHORT_RISING_TONE, H_DIAERESIS,
                                         SMALL_TURNED_W, SMALL_GHAD, SMALL_FEH, DASH_VERTICAL, VAAVU,
                                         ZWSP,  ZWNJ, ZWJ, LRM, RLM, LRE, RLE, PDF, LRO, RLO, NNBSP, MMSP, LRI, RLI, FSI, PDI]) + u"]")

SPACE_PAT = re.compile(u"[" + u"".join([QUOTATION_MARK, FULL_STOP, NUMBER_SIGN, LOW_LINE, BLACK_CIRCLE,
                                        PLUS_SIGN, EXCLAMATION_MARK,]) + u"]")
