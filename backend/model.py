import torch.nn as nn
import config
bertoutput_size = 768

class MTRefine(nn.Module):
  def __init__(self,bert,mer_size, men_size):
    super(MTRefine, self).__init__()

    self.word_embeddings = bert

    self.fMer=nn.Linear(config.bertoutput_size,mer_size)
    self.fMen=nn.Linear(config.bertoutput_size,men_size)

  def forward(self,x, input_mask, segment_test):

    x = self.word_embeddings(x.long(),attention_mask=input_mask.long(), token_type_ids=segment_test.long() )[0] 
    
    y1 = self.fMer(x) 
    y2 = self.fMen(x)           

    return y1,y2