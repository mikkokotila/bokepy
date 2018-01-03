# −∗− coding: utf−8 −∗−

import pandas as pd
import re
from pytib import Segment
from grapheme import graphemes

'''
NLP stuffs take time to do. So have patience.

'''

sent_punct_re = "༄|༅|༆|༇|༈|།|༎|༏|༐|༑|༔|;|:"
particles_re = "གི|ཀྱི|གྱི|ཡི|གིས|ཀྱིས|གྱིས|ཡིས|སུ|ཏུ|དུ|རུ|སྟེ|ཏེ|དེ|ཀྱང|ཡང|འང|གམ|ངམ|དམ|ནམ|བམ|མམ|འམ|རམ|ལམ|སམ|ཏམ|གོ|ངོ|དོ|ནོ|མོ|འོ|རོ|ལོ|སོ|ཏོ|ཅིང|ཅེས|ཅེའོ|ཅེ་ན|ཅིག|ཞིང|ཞེས|ཞེའོ|ཞེ་ན|ཞིག|ཤིང|ཤེའོ|ཤེ་ན|ཤིག|ལ|ན|ནས|ལས|ནི|དང|གང|ཅི|ཇི|གིན|གྱིན|ཀྱིན|ཡིན|པ|བ|པོ|བོ"

stopwords = ["འི་", "གི་", "ཀྱི་", "གྱི་", "ཡི་", "གིས་", "ཀྱིས་", "གྱིས་",
             "ཡིས་", "སུ་", "ཏུ་", "དུ་", "རུ་", "སྟེ་", "ཏེ་", "དེ་",
             "ཀྱང་", "ཡང་", "འང་", "གམ་", "ངམ་", "དམ་", "ནམ་", "བམ་",
             "མམ་", "འམ་", "རམ་", "ལམ་", "སམ་", "ཏམ་", "གོ་", "ངོ་",
             "དོ་", "ནོ་", "མོ་", "འོ་", "རོ་", "ལོ་", "སོ་", "ཏོ་", "ཅིང་",
             "ཅེས་", "ཅེའོ་", "ཅེ་ན་", "ཅིག་", "ཞིང་", "ཞེས་", "ཞེའོ་",
             "ཞེ་ན་", "ཞིག་", "ཤིང་", "ཤེའོ་", "ཤེ་ན་", "ཤིག་", "ལ་", "ན་",
             "ནས་", "ལས་", "ནི་", "དང་", "གང་", "ཅི་", "ཇི་", "གིན་",
             "གྱིན་", "ཀྱིན་", "ཡིན་", "པ་", "བ་", "པོ་", "བ་ོ", "ར་", "ས་",
             "མ་", "་_", "ལ", "ན"]

latins_re = r'[A-Z]|[a-z]|[0-9]|[\\$%&\'()*+,./:;<=>?@^_`[\]{}~]'


def ingest_text(filename):

    out = open(filename).read()

    return out


def remove_garbage(data):

    out = data[data.index.str.contains(latins_re) == False]

    return out


def show_garbage(data):

    return data[data.index.str.contains(latins_re) == True]


def create_meta(data):

    '''
    Accepts as input a list and outputs a dataframe with meta-data.
    '''

    # new[~new.index.isin(particles)]
    out = data
    out['stopword'] = data.index.str.isin(stopwords)
    out['length'] = data.index.str.len()
    out['sentence_ending'] = data.index.str.contains('་') == False
    out['sentence_ending'] = out['sentence_ending'].astype(int)

    return out


def text_to_chars(text):

    '''
    Takes as input Tibetan text, and creates a list of individual characters.

    '''

    temp = graphemes(text)
    out = list(temp)

    return out


def text_to_syllables(text):

    '''
    Takes as input Tibetan text, and creates a list of individual syllables.

    '''

    out = text.split('་')

    return out


def text_to_words(text):

    temp = re.sub(sent_punct_re, "", text)

    seg = Segment()
    temp = seg.segment(temp)
    out = temp.split()

    return out


def text_to_sentence(text):

    '''
    Takes as input Tibetan text, and creates a list of individual sentences.

    '''

    out = re.split(sent_punct_re, text)

    return out


def syllable_grams(data, grams=2, save_to_file=None):

    '''
    Takes in a list of syllables and creates syllable pairs.
    Note that there is no intelligence involved, so the syllable pairs
    might not result in actual words (even though they often do).

    OUTPUT: a list with the syllable pairs (and optionally saved file)

    OPTIONS: if 'save_to_file' is not None, need to be a filename.

    '''

    entities = pd.DataFrame(data)
    entities.columns = ['text']

    l = []
    a = 0
    for i in entities['text']:
        a += 1
        try:
            l.append(entities['text'][a] + " " + entities['text'][a + 1])
        except KeyError:
            l.append("blank")

    if save_to_file is not None:

        out = pd.Series(l)
        out.to_csv(save_to_file)

    return l


def syllable_counts(syllable_list):

    '''
    Takes as input a list or series with syllables or other syllable entities
    such as syllable pairs.

    '''

    out = pd.Series(syllable_list).value_counts()
    out = pd.DataFrame(out)
    out.columns = ['counts']

    return out

def share_by_order(data):

    '''
    Takes as input a frequency dataframe with column name counts expected.

    '''

    total = data['counts'].sum()
    print("Total syllable pairs : %d \n" % total)

    for i in [10,100,1000,10000,100000]:
        share = data['counts'][:i].sum() / total.astype(float) * 100
        print(("TOP %d : %.2f%%") % (i, share))
