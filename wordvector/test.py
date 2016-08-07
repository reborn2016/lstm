import gensim

model =gensim.models.word2vec.Word2Vec.load_word2vec_format("data/wordvec.txt", binary=False)
print model.similarity("woman", "man") 
