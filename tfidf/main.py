# Description: This cript is used to compute the TF-IDF of words
# in a given documents in order to find the importance words.
# TextBlob is used for breaking up the text into words.
# Author: Dung Ho

import math
from textblob import TextBlob as tb


def tf(word, doc):
    """
    Function computes "term frequency" which is the number of times a word
    appears in a document blob, normalized by dividing by the total number
    of words in blob.

    :param word: a given word.
    :param doc: a document that contains the word to compute.

    :return: a float number.
    """

    return doc.words.count(word) / len(doc.words)


def n_containing(word, docs):
    """
    Function calculate the number of documents containing a word.

    :param word: a word.
    :param docs: a list of documents to check.

    :return an integer number.
    """
    list_docs = [1 for doc in docs if word in doc.words]

    return sum(list_docs)


def idf(word, docs):
    """
    Function computes "inverse document frequency" which measures how common a
    word is among all documents by taking the ratio of the total number of
    documents to the number of documents containing word, then take the log
    of that. Add 1 to the divisor to prevent division by zero.
    The more common a word is, the lower its idf.

    :param word: a word.
    :param docs: a list of documents.

    :return: a float number.
    """
    return math.log(len(docs) / (1 + n_containing(word, docs)))


def tfidf(word, doc, docs):
    """
    Function computes the TF-IDF score. Its the product of tf and idf.
    """
    tf_idf = tf(word, doc) * idf(word, docs)

    return tf_idf


def read_file(f_name):
    """
    Function reads a text file, splits into different paragraphs
    and converts to TextBlob data for processing.

    :param f_name: a text file.

    :return: a list of TextBlob documents.
    """
    with open(f_name, "r") as f:
        ph = f.read().split("\n")

    docs = [tb(i) for i in ph]

    return docs


if __name__ == "__main__":
    docs = read_file("demo/demo.txt")

    for i, doc in enumerate(docs):
        print("\nParagraph {}:".format(i+1))
        print(doc)
        print("\nTop words in paragraph {}:".format(i + 1))
        frequencies = {word: tfidf(word, doc, docs) for word in doc.words}
        sorted_words = sorted(
            frequencies.items(), key=lambda x: x[1], reverse=True
        )
        for word, freq in sorted_words[:3]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(freq, 5)))
