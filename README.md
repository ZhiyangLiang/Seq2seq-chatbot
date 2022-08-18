<h1>Seq2seq-chatbot</h1>

<h2>Introduction</h2>
<p>This is a project based on the Seq2seq algorithm implementation that enables users to conduct some simple conversations online with a corpus-trained chatbot. The project supports both mobile and PC side, and all inference calculations are done in a lightweight application server used by the author for deployment.</p>

<h2>Playground Online</h2>
<a target="_blank" href="https://paradox-11.com/">paradox-11.com</a>

<h2>Deployment</h2>
<p>If you want to run the project on your own computer or want to train the model with your own corpus, please refer to the following instructions.</p>
<p>1、Clone documents for the project：</p>
```
git clone git@github.com:paradox-11/Seq2seq-chatbot.git
```
<p>2、Download the required open source frameworks and packages</p>

<p>3、If you want to change the training corpus, please delete the .pt file in the Mymodels folder first.</p>
<p>4、After personalizing the training corpus, please execute the execute.py file for training.</p>
<p>5、You can observe the change of loss in real time during the training process, and then execute the app.py file after the training is finished to run the project successfully.</p>
<p>6、You can change the minimum loss value for training stops and some training related parameters in the seqseq.ini file in the config folder.</p>

<h2>Reference</h2>
<p>Ilya Sutskever, Oriol Vinyals and Quoc V. Le.Sequence to Sequence Learning with Neural Networks.In NIPS, 2014.</p>

```cpp
print("111")
```
