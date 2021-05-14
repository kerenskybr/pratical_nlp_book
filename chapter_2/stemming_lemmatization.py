# STEMMING example
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

word1, word2 = "cars", "revolution"
print(stemmer.stem(word1), stemmer.stem(word2))

# LEMMATIZATION example
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("better", pos="a")) #a is for adjective

# And using Spacy
import spacy 

sp = spacy.load('en_core_web_sm')
token = sp(u'better')
for word in token:
   print(word.text, '/' ,word.lemma_)

# In this simple snippet, we can see tokenization, 
# lemmatization, POS tagging, and several other steps in action
import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Charles Spencer Chaplin was born on 16 April 1889 toHannah Chaplin (born Hannah HarrietPedlingham Hill) and Charles Chaplin Sr')
for token in doc:
    print(token.text, token.lemma_, token.pos_,token.shape_, token.is_alpha, token.is_stop)