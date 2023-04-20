
import torch
from transformers import AutoTokenizer, AutoModel
import config
import model
import pickle

tokenizer = AutoTokenizer.from_pretrained(config.PATH_BERT)
bert      = AutoModel.from_pretrained(config.PATH_BERT)

#load data for create model
filehandler = open(config.PATH_PICKLE +r'/data_create_model.pickle' ,'rb')
data_create_model = pickle.load(filehandler)

#create model
mer_size = data_create_model['mer_size']
men_size = data_create_model['men_size']
mTRefine =  model.MTRefine(bert, mer_size,men_size)
mTRefine.load_state_dict(torch.load(config.PATH_MODEL + r'/model.pth', map_location=torch.device('cpu')))
mTRefine.eval()


#load data for test
#filehandler = open(config.PATH_PICKLE +r'/data_for_test_mer_cdr.pickle' ,'rb')
#data_for_test_mer_cdr = pickle.load(filehandler)

#load data for creating model
#filehandler = open(config.PATH_PICKLE +r'/data_for_create_model.pickle' ,'rb')
#data_for_create_model = pickle.load(filehandler)

#mer_size = data_for_create_model['mer_size']
#men_size = data_for_create_model['men_size']

#mTRefine =  model.MTRefine(bert, mer_size,men_size)
#mTRefine.load_state_dict(torch.load(config.PATH_MODEL + r'/mt_refine_bcdr.pth'))
#mTRefine.eval()
#shared_bert =mTRefine.word_embeddings

#mTFineTuneMerCDR= model.MTFineTuneMer(shared_bert, mer_size)
#mTFineTuneMerCDR.load_state_dict(torch.load(config.PATH_MODEL + r'/mt_finetune_bcdr.pth'))
#mTFineTuneMerCDR.eval()


#for name in mTFineTuneMerCDR.parameters():
#    print(name)


