from flask import Flask, request, jsonify
from flask_cors import CORS

import torch
import pickle
import config
import create_model
import tool_for_test

app = Flask(__name__)
CORS(app)

filehandler = open(config.PATH_PICKLE +r'/data_create_model.pickle' ,'rb')
data_create_model = pickle.load(filehandler)

int2tags_mer = data_create_model['int2tags_mer']
int2tags_men = data_create_model['int2tags_men']

model = create_model.mTRefine


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'

@app.route('/mer-and-men', methods=['GET', 'POST'])
def parse_request():
     
  text = request.form['text']
  
  
  real_tokens, input_encode, input_mask, input_segment = tool_for_test.encode(text)
  output_mer = model(input_encode,input_mask,input_segment)[0]
  output_men = model(input_encode,input_mask,input_segment)[1]

  #print(output_mer)
  #print(output_men)

  #print('-'*10)
  
  y_mer_pre = tool_for_test.convert_int_to_tagsmer(output_mer,real_tokens,int2tags_mer)
  y_men_pre = tool_for_test.convert_int_to_tagsmen(output_men,real_tokens, int2tags_men, y_mer_pre)

  #print(y_mer_pre)
  #print(y_men_pre)

  print(real_tokens)

  result = {
    "text" :  tool_for_test.word_tokenize(text),
    "mer": y_mer_pre,
    "men": y_men_pre
  }

  return jsonify(result)


@app.route('/mer-and-men2', methods=['GET', 'POST'])
def parse_request2():
     
  texts = request.form['text']
  
  texts = texts.split('1712858')

  

  final_respond = []
  for text in texts:
    real_tokens, input_encode, input_mask, input_segment = tool_for_test.encode(text)
    output_mer = model(input_encode,input_mask,input_segment)[0]
    output_men = model(input_encode,input_mask,input_segment)[1]

    
    y_mer_pre = tool_for_test.convert_int_to_tagsmer(output_mer,real_tokens,int2tags_mer)
    y_men_pre = tool_for_test.convert_int_to_tagsmen(output_men,real_tokens, int2tags_men, y_mer_pre)


    result = {
      "text" :  tool_for_test.word_tokenize(text),
      "mer": y_mer_pre,
      "men": y_men_pre
    }
    final_respond.append(result)

  return jsonify(final_respond)

if __name__ == '__main__':
    app.run(debug = False)