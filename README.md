<h1>Seq2seq-chatbot</h1>

<h2>Introduction</h2>
<p>这是一个基于Seq2seq算法实现的用python flask搭建的项目，用户能够在线与经过语料训练的机器人进行一些简单的对话。该项目支持手机端与PC端，所有的推理计算均在作者用于部署的轻量应用服务器中完成。</p>

<h2>Playground Online</h2>
<a target="_blank" href="https://paradox-11.com/">聊天机器人在线网站</a>

<h2>Deployment</h2>
<p>If you want to run the project on your own computer or want to train the model with your own corpus, please refer to the following instructions.</p>
<p>1、Clone documents for the project：</p>

<p>2、Download the required open source frameworks and packages</p>
<p>3、If you want to change the training corpus, please delete the .pt file in the Mymodels folder first.</p>
<p>4、After personalizing the training corpus, please execute the execute.py file for training.</p>
<p>5、You can observe the change of loss in real time during the training process, and then execute the app.py file after the training is finished to run the project successfully.</p>
<p>6、You can change the minimum loss value for training stops and some training related parameters in the seqseq.ini file in the config folder.</p>
