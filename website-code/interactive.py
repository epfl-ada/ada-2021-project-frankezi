from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from nltk import tokenize

import gensim
from gensim import corpora
from gensim import models
from gensim import similarities

import nltk
from nltk.corpus import stopwords

import numpy as np
import pandas as pd

# nltk list of stopwords for the english language
stoplist = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
            "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

nltk.download('punkt')

search_terms = [
    'China',
    'Chinese',
    'Xi Xinping',
    'Asia',
    'Xinjiang',
    'Wuhan',
    'Beijing',
    'Mandarin',
    'Chinese virus',
    'PRC',
    'CPC'
]


def tokenize_string(string, stoplist):
  """Tokenize a string using the `gensim` simple pre-processing method
  and removes all stopwords."""
  return [word for word in gensim.utils.simple_preprocess(string) if word not in stoplist]

texts = [tokenize_string(term, stoplist) for term in search_terms]


def tokenize_string(string, stoplist):
  """Tokenize a string using the `gensim` simple pre-processing method
  and removes all stopwords."""
  return [word for word in gensim.utils.simple_preprocess(string) if word not in stoplist]


def compute_model(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(txt) for txt in texts]

    sim_model = models.LsiModel(corpus, id2word=dictionary, num_topics=len(
        dictionary))  # num_topics=200 by default

    sim_index = similarities.MatrixSimilarity(sim_model[corpus])
    return dictionary, corpus, sim_model, sim_index

dictionary, corpus, sim_model, sim_index = compute_model(texts)


def predicate_quote_similarity(instance):
    delta = 0.6
    quote = instance['quotation']
    cleaned_quote = tokenize_string(quote, stoplist)
    vec_bow = dictionary.doc2bow(cleaned_quote)
    vec = sim_model[vec_bow]

    sims = sim_index[vec]
    return np.any(sims >= delta)


analyzer = SentimentIntensityAnalyzer()

def get_analysis(quote):
    s_list = tokenize.sent_tokenize(quote)
    inter_results = []
    for s in s_list:
      inter_results.append(analyzer.polarity_scores(s))
    inter_results = pd.DataFrame(inter_results)
    # Aggregation method: mean of results over sentences
    inter_results = inter_results.mean(axis=0)
    return inter_results.to_dict()
