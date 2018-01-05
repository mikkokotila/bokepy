# −∗− coding: utf−8 −∗−

import pandas as pd
import re
from pytib import Segment
from grapheme import graphemes
from grapheme import length


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


def ingest_text(filename, mode='blob'):

    if mode is not "blob":
        out = open(filename).readlines()
    else:
        out = open(filename).read()

    return out


def export(data, name='default', export_format='to_csv'):

    '''
    WHAT
    ----
    Takes data and exports it to a file on local drive. Note that
    saving will take place automatically on present working directory
    and any file with same name will be automatically overwritten.

    PARAMS
    ------
    data: data in a list or dataframe or series
    export_to: to_html, to_json, to_csv, to_excel, to_latex,
               to_msgpack, to_sql, to_clipboard
    '''
    temp = data

    if name is 'default':
        file_type = export_format.split('_')[1]
        name = 'export_from_boke.' + file_type

    method_to_call = find_method(temp, export_format)
    method_to_call(name)


def type_convert(data):

    temp = data

    if isinstance(temp, pd.core.frame.DataFrame) is False:
        temp = pd.DataFrame(temp)
        temp = temp.set_index(temp.columns[0])

    return temp


def remove_latins(data):

    temp = type_convert(data)

    out = temp[temp.index.str.contains(latins_re) == False]

    return out


def find_method(data, function):

    temp = type_convert(data)

    method_to_call = getattr(temp, function)

    return method_to_call


def show_latins(data):

    temp = type_convert(data)

    return temp[temp.index.str.contains(latins_re) == True]


def create_meta(data):

    '''
    Accepts as input a list and outputs a dataframe with meta-data.
    '''

    # new[~new.index.isin(particles)]
    temp = data
    temp = temp.reset_index()
    temp.columns = ['text', 'count']
    temp['chars'] = temp.text.apply(length)
    temp['bytes'] = temp.text.str.len()
    temp['sentence_ending'] = temp.text.str.contains('་') == False
    temp['sentence_ending'] = temp['sentence_ending'].astype(int)
    temp['stopword'] = temp.text.isin(stopwords)

    return temp


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


def text_to_words(text, mode='list'):

    '''
    OPTIONS
    -------
    mode: either 'list' or 'whitespaces'
    '''

    temp = re.sub(sent_punct_re, "", text)

    seg = Segment()
    temp = seg.segment(temp, uknown=0)
    if mode is 'list':
        temp = temp.split()

    return temp


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

    orders = [10, 100, 1000, 10000, 100000]

    for i in orders:
        share = data['counts'][:i].sum() / total.astype(float) * 100
        print(("TOP %d : %.2f%%") % (i, share))
