#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus.reader import TaggedCorpusReader


# In[2]:


# Initialize TaggedCorpusReader 
corpus = TaggedCorpusReader('/home/niket/Music/brown/brown', '.*')


# In[3]:


# Get the tagged sentences from the corpus
tagged_sents = corpus.tagged_sents()


# In[5]:


# Split the tagged sentences into training and testing sets
train_sents = tagged_sents[:int(0.8*len(tagged_sents))]
test_sents = tagged_sents[int(0.2*len(tagged_sents)):]


# In[6]:


# Train the HMM POS tagger on the training set
hmm_tagger = nltk.HiddenMarkovModelTagger.train(train_sents)


# In[7]:


# Evaluate the tagger on the testing set
accuracy = hmm_tagger.evaluate(test_sents)
print(f"Accuracy: {accuracy:.2%}")


# In[11]:


# Sample Sentence
sentence = "The dog is loyal and guards the house ."

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Tag the tokens
tagged_tokens = hmm_tagger.tag(tokens)

# Print the tagged sentence
print(tagged_tokens)


# In[ ]:





# In[ ]:




