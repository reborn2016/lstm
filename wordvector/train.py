#-*-coding:utf-8-*-
import gensim
import commands
import os
if os.path.exists("data/text8") == False:
    print "unzip"
    status, output = commands.getstatusoutput("cd data  &&  unzip text8.zip")
    print status, output
print "load text"
text_8_corpus = gensim.models.word2vec.Text8Corpus("data/text8")
print "begin train"
model = gensim.models.word2vec.Word2Vec(text_8_corpus)
print "begin save model"
model.save_word2vec_format("data/wordvec.txt")
