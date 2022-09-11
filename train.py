# -*- coding:utf-8 -*-
import os
import sys
import time
import torch
import model
from config import getConfig
import io
from torch import optim
from zhon.hanzi import punctuation
import re
import jieba

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
gConfig = {}
gConfig = getConfig.get_config()
units = gConfig['layer_size']
BATCH_SIZE = gConfig['batch_size']
EOS_token = 1
SOS_token = 0
MAX_LENGTH = gConfig['max_length']
def preprocess_sentence(w):
    c = w[:1]
    if c != "E":
        w = re.sub(r"[%s]+" % punctuation, "", w)
        w = w[2:]
        w = " ".join(jieba.cut(w))
    w ='start '+ w + ' end'
    return w

def create_dataset(path, num_examples):
    lines = io.open(path, encoding='UTF-8').read().strip().split('\n')
    pairs = [[preprocess_sentence(w)for w in l.split('\t')] for l in lines[:num_examples]]
    input_lang = Lang("ask")
    output_lang = Lang("ans")
    cnt = 0
    for pair in pairs:
        if cnt % 3 == 0:
            cnt += 1
            continue
        elif cnt % 3 == 1:
            input_lang.addSentence(pair[0])
            
        elif cnt % 3 == 2:
            output_lang.addSentence(pair[0])
        cnt += 1

    return input_lang, output_lang, pairs

def max_length(tensor):
    return max(len(t) for t in tensor)
class Lang:
    def __init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2count = {}
        self.index2word = {0: "start", 1: "end"}
        self.n_words = 2

    def addSentence(self, sentence):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1


def indexesFromSentence(lang, sentence):
    lang.addSentence(sentence)
    for word in sentence.split(' '):
        if word not in lang.word2index:
            return -1
    return [lang.word2index[word] for word in sentence.split(' ')]

def tensorFromSentence(lang, sentence):

    indexes = indexesFromSentence(lang, sentence)
    if indexes == -1:
        return -1
    indexes.append(EOS_token)

    return torch.tensor(indexes, dtype=torch.long, device=device).view(-1, 1)


def read_data(path, num_examples):
    input_tensors = []
    target_tensors = []
    input_lang, target_lang, pairs = create_dataset(path, num_examples)
    for i in range(num_examples-1):
        if i % 3 == 0:
            continue
        elif i % 3 == 1:
            input_tensor_mid = tensorFromSentence(input_lang, pairs[i][0])
            input_tensors.append(input_tensor_mid)
        elif i % 3 == 2:
            target_tensor_mid = tensorFromSentence(target_lang, pairs[i][0])
            target_tensors.append(target_tensor_mid)
    return input_tensors, input_lang, target_tensors, target_lang
input_tensor, input_lang, target_tensor, target_lang= read_data(gConfig['seq_data'], gConfig['max_train_data_size'])
hidden_size = 256
def train():
    print("Preparing data in %s" % gConfig['train_data'])
    steps_per_epoch = len(input_tensor) // gConfig['batch_size']
    checkpoint_dir = gConfig['model_data']
    checkpoint_prefix = checkpoint_dir + "/pt"
    start_time = time.time()
    encoder = model.Encoder(input_lang.n_words, hidden_size).to(device)
    decoder = model.AttentionDencoder(hidden_size, target_lang.n_words, dropout_p=0.1).to(device)
    if os.path.exists(checkpoint_prefix):
        checkpoint = torch.load(checkpoint_prefix, map_location='cpu')
        encoder.load_state_dict(checkpoint['modelA_state_dict'], strict=False)
        decoder.load_state_dict(checkpoint['modelB_state_dict'], strict=False)
    max_data = gConfig['max_train_data_size']
    total_loss = 0
    step_loss = 1
    current_steps = 0
    while step_loss > gConfig['min_loss']:
        start_time_epoch = time.time()
        for i in range(1, (max_data//BATCH_SIZE)):
            if i > 5545:
                break
            inp = input_tensor[(i-1)*BATCH_SIZE:i*BATCH_SIZE]
            targ = target_tensor[(i-1)*BATCH_SIZE:i*BATCH_SIZE]
            batch_loss = model.train_step(inp, targ, encoder, decoder, optim.SGD(encoder.parameters(), lr=0.001), optim.SGD(decoder.parameters(), lr=0.01))
            total_loss += batch_loss
            print('训练总步数:{} 最新每步loss {:.5f}'.format(i, batch_loss))
        step_time_epoch = (time.time() - start_time_epoch) / steps_per_epoch
        step_loss = total_loss / steps_per_epoch
        current_steps += steps_per_epoch
        step_time_total = (time.time() - start_time) / current_steps
        print('训练总步数: {} 每步耗时: {}  最新每步耗时: {} 最新每步loss {:.5f}'.format(current_steps, step_time_total, step_time_epoch,
                                                                      batch_loss))
        torch.save({'modelA_state_dict': encoder.state_dict(),
                     'modelB_state_dict': decoder.state_dict()}, checkpoint_prefix)
        sys.stdout.flush()

def predict(sentence):
    max_length_tar = MAX_LENGTH
    encoder = model.Encoder(3894, hidden_size).to(device)
    decoder = model.AttentionDencoder(hidden_size, target_lang.n_words, dropout_p=0.1).to(device)
    checkpoint_dir = gConfig['model_data']
    checkpoint_prefix = checkpoint_dir + "/pt"
    checkpoint = torch.load(checkpoint_prefix, map_location='cpu')
    encoder.load_state_dict(checkpoint['modelA_state_dict'], strict=False)
    decoder.load_state_dict(checkpoint['modelB_state_dict'], strict=False)
    input_tensor = tensorFromSentence(input_lang, sentence)

    input_length = input_tensor.size()[0]
    result = ''
    max_length=MAX_LENGTH
    encoder_hidden = encoder.initHidden()
    encoder_outputs = torch.zeros(max_length, encoder.hidden_size, device=device)
    for ei in range(input_length):
        encoder_output, encoder_hidden = encoder(input_tensor[ei], encoder_hidden)
        encoder_outputs[ei] += encoder_output[0, 0]

    dec_input = torch.tensor([[SOS_token]], device=device)

    dec_hidden = encoder_hidden
    for t in range(max_length_tar):
        predictions, dec_hidden, decoder_attentions = decoder(dec_input, dec_hidden, encoder_outputs)
        predicted_id, topi = predictions.data.topk(1)

        if topi.item() == EOS_token:
            result += '<EOS>'
            break
        else:
            result += target_lang.index2word[topi.item()]
            result += ' '
        dec_input = topi.squeeze().detach()
    return result


if __name__ == '__main__':
    if len(sys.argv) - 1:
        gConfig = getConfig.get_config(sys.argv[1])
    else:
        gConfig = getConfig.get_config()
    print('\n>> Mode : %s\n' %(gConfig['mode']))

    if gConfig['mode'] == 'train':
        train()
