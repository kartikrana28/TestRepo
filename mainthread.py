# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I6O52Qihqhglytw5Wj_371capf2m5IvK
"""

from docproduct.predictor import RetreiveQADoc

pretrained_path = 'BioBertFolder/biobert_v1.0_pubmed_pmc/'
# ffn_weight_file = None
bert_ffn_weight_file = 'newFolder/models/bertffn_crossentropy/bertffn'
embedding_file = 'Float16EmbeddingsExpanded5-27-19.pkl'

doc = RetreiveQADoc(pretrained_path=pretrained_path,
                    ffn_weight_file=None,
                    bert_ffn_weight_file=bert_ffn_weight_file,
                    embedding_file=embedding_file)

question_text = "i am 18 and having frequent and painful urination, with a mild fever since 2-3 days"

search_similarity_by = 'answer'

number_results_toReturn = 10

# @param {type:"string"}
question_text = "i am 18 and having frequent and painful urination, with a mild fever since 2-3 days"

search_similarity_by = 'answer'  # @param ['answer', "question"]

number_results_toReturn = 10  # @param {type:"number"}

answer_only = True  # @param ["False", "True"] {type:"raw"}

returned_results = doc.predict(question_text,
                               search_by=search_similarity_by, topk=number_results_toReturn, answer_only=answer_only)

print('')
anitr = 0
answer_array = []
for jk in range(len(returned_results)):
    if (len(returned_results[jk]) > 300):
        answer_array.append(returned_results[jk])
print(answer_array[anitr])
