_Author: Dung Ho_
_Email: dung.ho@edu.turkuamk.fi_
_Phone number: +358 449865555_


## Overview
_This is a Python script used to find important word in text using TF-IDF._


## General
- Definition:
TF-IDF stands for "Term Frequency, Inverse Document Frequency." It's a way to score the importance of words (or "terms") in a document based on how frequently they appear across multiple documents.

- Why?
If a word appears frequently in a document, it's important. Give the word a high score.
But if a word appears in many documents, it's not a unique identifier. Give the word a low score.
Therefore, common words like "the" and "for," which appear in many documents, will be scaled down. Words that appear frequently in a single document will be scaled up.

- This cript uses 'TextBlob' library for processing textual data.

## How to use:
1. Clone the repo at "https://github.com/findungho/machine_leaning.git"
2. Navigate to folder "tfidf"
3. Run: pipenv run python main.py
