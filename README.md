# bokepy

bö (tib. བོད་) means Tibet, and ke (tib. སྐད) means language, so together böke means Tibetan Language. bokepy is a shorthand for boke and python, and is a Tibetan Language Processing Library built for handling the most common language processing tasks in a straightforward way. Bokepy is built from the ground up to facilitate for a wide range of research challenges, including those far beyond the scope of typical scholarly interest. This includes rapid testing of ideas and prototyping of completely new technology solutions.

## Table of Contents

#### 1. About This document
#### 2. Requirements
#### 3. About the Design Paradigm
#### 4. Roadmap
#### 5. References

## 1. About This Document

At the moment there is no user document, and this document serves as a guideline for development. What should be built first, and how it should be built. For now, see doc-strings for individual functions.

## 2. Requirements

The initial spec is focused on making the most common analytical processes as easy to perform as possible. At the same time, the goal is to establish a clean codebase for further development with as modular design paradigm as possible.

- **being able to ingest text**
  - as raw text
  - as a list of entities
  - as a frequency list with counts
  - in variety of file formats:
   - .txt
   - .csv
   - .doc
   - .xls
   - .pdf (later)
   - .sql (later)
   - other formats (which?)
  - handling unicode properly is a must!

- **being able to clean text**
  - remove non-Tibetan entities
  - remove unnecessary spaces
  - remove other garbage (needs to be defined)

- **being able to preprocess text**
  - split text in to:
   - sentences
   - phrases
   - words
   - syllables
   - characters
  - filter out stopwords
   - punctuation
   - particles
   - other words (what are these?)

- **being able to establish grams**
  - character-level
  - syllable-level
  - word-level
  - phrase-level
  - sentence-level

- **being able to create frequency tables**
  - at any entity level (e.g. syllable frequency)
  - with simple summaries for % share of buckets (e.g. 100 most common account for 12% of all in a set)

- **being able to draw out plots**
  - word clouds
  - bar charts
  - heatmaps

- **being able to output to files**
  - html
  - json
  - excel
  - latex
  - msgpack
  - sql
  - clipboard

## 3. About the Design Paradigm

To maximize code readability, at least initially there is no object orientation i.e. classes are not used.

Functions should meet several functional criteria:

- Can ingest list, series, and dataframe without prompting user
- Can be called separately from any other functionality
- Can be within any other function

Functions should also meet several structural criteria:

- No more than 50 lines of code in total
- Strict adherence to pep8 guidelines
- Include comprehensive doc string
- Use code simple enough to void need for comments

## 4. Roadmap

Roughly speaking the roadmap is broken in to 4 stages (at least for now):

1) Common Foundational Features
  - Data in and out
  - Data cleaning
  - Tokenization / segmentation
  - Frequency tables
  - Access to common language resources (corpora etc.)
2) Common Statistical Functionality
  - (n)gram creation
  - word frequency table creation
  - foundational visualization capabilities
3) Special Foundational Features
  - embeddings / one-hot encoding
  - vectorization (sense2vec, word2vec, etc[1])
  - several options for word tokenization
  - POS tagging
  - Entity recognition
  - Accuracy / quality assessment
4) Extraordinary Statistical Capabilities
  - Integrate with Keras (LSTM etc.)
  - Let's see what more...it takes a long journey to know the horse's strength.

## 5. References

[1] https://github.com/MaxwellRebo/awesome-2vec
