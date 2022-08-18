<h1>Seq2seq-chatbot</h1>

<h2>Introduction</h2>
<p>This is a project based on the Seq2seq model[1] implementation that enables users to conduct some simple conversations online with a corpus-trained chatbot. The project supports both mobile and PC side, and all inference calculations are done in a lightweight application server used by the author for deployment.</p>

<h2>Online</h2>
<a target="_blank" href="https://paradox-11.com/">paradox-11.com</a>

<h2>Model</h2>
<p>Seq2seq is a network of Encoder-Decoder structures, whose input and output are both a sequence. In Encoder, the sequence is converted into a fixed-length vector, and then that vector is converted into the sequence output we want by Decoder.</p>

<h2>Packages</h2>
<h3>jieba</h3>
<p>The jieba library is a library for Chinese word splitting, which can split complete sentences into multiple fragments based on lexicality, enabling the model to learn fragmented semantics to eventually understand complete sentences, and also reducing the amount of vocabulary that needs to be encoded during the training process.</p>
<h3>zhon</h3>
<p>The role of the zhon library here is to remove the interference of common Chinese symbols in the sentences to improve the training effect of the model.</p>

<h2>Deployment</h2>
<p>If you want to run the project on your own computer or want to train the model with your own corpus, please refer to the following instructions.</p>
<p>1、Clone documents for the project：</p>

```
git clone git@github.com:paradox-11/Seq2seq-chatbot.git
```
<p>2、Download the required open source frameworks and packages</p>

```
pip install torch==1.11.0
pip install flask==2.0.2
pip install jieba==0.42.1
pip install zhon==1.1.5
```
<p>3、If you want to change the training corpus, please delete the .pt file in the Mymodels folder first.</p>
<p>4、After personalizing the training corpus, please execute the execute.py file for training.</p>
<p>5、You can observe the change of loss in real time during the training process, and then execute the app.py file after the training is finished to run the project successfully.</p>
<p>6、You can change the minimum loss value for training stops and some training related parameters in the seqseq.ini file in the config folder.</p>

<h2>Reference</h2>
<p>[1]:Ilya Sutskever, Oriol Vinyals and Quoc V. Le.Sequence to Sequence Learning with Neural Networks.In NIPS, 2014.</p>
