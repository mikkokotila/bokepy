import boke

test_sample = 100000

text = boke.ingest_text('rt_texts_raw.txt')

chars = boke.text_to_chars(text[:test_sample])
words = boke.text_to_words(text[:test_sample])
syllables = boke.text_to_syllables(text[:test_sample])
sentences = boke.text_to_sentence(text[:test_sample])

print(len(chars))
print(len(syllables))
print(len(words))
print(len(sentences))

print(chars[100:110])
print(syllables[100:110])
print(words[100:110])
print(sentences[100:110])

print(boke.syllable_counts(chars).head(5))
print(boke.syllable_counts(syllables).head(5))
print(boke.syllable_counts(words).head(5))
print(boke.syllable_counts(sentences).head(5))

chars_freq = boke.syllable_counts(chars)
syllables_freq = boke.syllable_counts(syllables)
words_freq = boke.syllable_counts(words)
sentences_freq = boke.syllable_counts(sentences)

boke.share_by_order(chars_freq)
boke.share_by_order(syllables_freq)
boke.share_by_order(words_freq)
boke.share_by_order(sentences_freq)

chars_pairs = boke.syllable_grams(chars)
syllable_pairs = boke.syllable_grams(syllables)
words_pairs = boke.syllable_grams(words)
sentences_pairs = boke.syllable_grams(sentences)

print(chars_pairs[:10])
print(syllable_pairs[:10])
print(words_pairs[:10])
print(sentences_pairs[:10])
