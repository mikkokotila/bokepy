# bokepy

bö (tib. བོད་) means Tibet, and ke (tib. སྐད) means language, so together böke means Tibetan Language. bokepy is a shorthand for boke and python, and is a Tibetan Language Processing Library built for handling the most common language processing tasks in a straighforward way. 

## Requirements

- **being able to ingest text**
  - as raw text
  - as a list of entities 
  - as a frequency list with counts
  
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
   
- **being able to establish grams**
  - character-level
  - syllable-level
  - word-level
  - phrase-level
  - sentence-level
  
- **being able to create frequency tables**
 - at any entity level (e.g. syllable frequency)
 - with simple summaries for % share of buckets (e.g. 100 most common account for 12% of all in a set)
