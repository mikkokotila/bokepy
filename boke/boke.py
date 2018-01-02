## −∗− coding: utf−8 −∗−

import pandas as pd

'''
NLP stuffs take time to do. So have patience. 

'''

sent_punct = "༄|༅|༆|༇|༈|།|༎|༏|༐|༑|༔|;|:"

def text_to_chars(text):

	from grapheme import graphemes

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


def text_to_sentence(text):

	import re

	'''
	Takes as input Tibetan text, and creates a list of individual sentences. 

	'''

	out = re.split(sent_punct, text)

	return out


def syllable_grams(file, grams=2, save_to_file=None):

	'''
	Takes in a list of syllables and creates syllable pairs. 
	Note that there is no intelligence involved, so the syllable pairs
	might not result in actual words (even though they often do). 

	OUTPUT: a list with the syllable pairs (and optionally saved file)

	OPTIONS: if 'save_to_file' is not None, need to be a filename.

	'''

	Print("\n This might take a while...\n")

	syllable = pd.read_csv(file, error_bad_lines=False)
	syllable.columns = ['syllables']

	l = []
	a = 0
	for i in syllable.syllables:
		a += 1
		try: 
			l.append(syllable.syllables[a] + " " + syllable.syllables[a + 1])
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
	out	= pd.DataFrame(out)
	out.columns = ['counts']

	return out


def share_by_order():

	'''
	Takes as input a frequency dataframe with column name counts expected.

	'''

	total = tes.counts.sum()
	print "Total syllable pairs : %d \n" % total

	for i in [10,100,1000,10000,100000]:
		share = tes.counts[:i].sum() / total.astype(float) * 100
		print("TOP %d : %.2f%%") % (i, share)

