import nltk
nltk.download('punkt')
from transformers import AutoTokenizer, AutoModel,BertModel
import torch

import config

tokenizer = AutoTokenizer.from_pretrained(config.PATH_BERT)
bert      = AutoModel.from_pretrained(config.PATH_BERT)

#Tách từ
def word_tokenize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens

#convert token to ids
def data_preparation(tokens):
    
    real_tokens   = []
    input_encode  = []
    input_mask    = []
    input_segment = []
    
    for token in tokens:
        ids= tokenizer.encode(token.lower())[1:-1]

        len_ids = len(ids)
        
        for i in range(len_ids):
            if i==0:
                real_tokens.append(1)
            else:
                real_tokens.append(0)

            input_encode.append(ids[i])
            input_mask.append(1)
            input_segment.append(0)

    real_tokens.insert(0,0)
    real_tokens.append(0)

    input_mask.insert(0,1)
    input_segment.append(0)
    
    cls_token = tokenizer.cls_token
    sep_token = tokenizer.sep_token
    cls_token_idx = tokenizer.convert_tokens_to_ids(cls_token)
    sep_token_idx = tokenizer.convert_tokens_to_ids(sep_token)
    
    input_encode.insert(0,cls_token_idx)
    input_encode.append(sep_token_idx)

    return real_tokens, input_encode, input_mask, input_segment

#padding
def padding(x):
    while(len(x)<config.sequence_length):
        x.append(0)
    return x

#convert to tensor
def list_to_tensor(x):
    new_tensor= torch.tensor(x, dtype=torch.int)
    new_tensor=torch.unsqueeze(new_tensor, 0)

    return new_tensor
    
def encode(sentence, isTokens = False):

    if(isTokens== False):
        tokens = word_tokenize(sentence)
    else:
        tokens = sentence

    real_tokens, input_encode, input_mask, input_segment= data_preparation(tokens)

    real_tokens = padding(real_tokens)
    input_encode = padding(input_encode)
    input_mask = padding(input_mask)
    input_segment = padding(input_segment)

    input_encode = list_to_tensor(input_encode)
    input_mask = list_to_tensor(input_mask)
    input_segment = list_to_tensor(input_segment)


    return real_tokens, input_encode, input_mask, input_segment

def convert_int_to_tagsmer(output_mer, real_tokens, int_to_tag):
    output_mer = torch.argmax(output_mer, dim=2)
    output_mer = output_mer.tolist()[0]
    result     = []
    for i in range(config.sequence_length):
        if(real_tokens[i]==0):
            continue
        else:
            result.append(int_to_tag[output_mer[i]])
    return result

def convert_int_to_tagsmen(output_mer, real_tokens, int_to_tag,ymer_corpus):
    output_mer = torch.argmax(output_mer, dim=2)
    output_mer=output_mer.tolist()[0]
    result = []
    for i in range(128):
        if(real_tokens[i]==0):
            continue
        else:
            result.append(int_to_tag[output_mer[i]])

    for i in range(len(ymer_corpus)):
      try:
        if(ymer_corpus[i]=='O'):
          result[i]='O'
      except:
        pass
    return result
