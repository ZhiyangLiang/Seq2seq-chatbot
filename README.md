<h1>Seq2seq-chatbot</h1>

<h2>Introduction</h2>
<p>这是一个基于Seq2seq算法实现的用python flask搭建的项目，用户能够在线与经过语料训练的机器人进行一些简单的对话。该项目支持手机端与PC端，所有的推理计算均在作者用于部署的轻量应用服务器中完成。</p>

<h2>Playground Online</h2>
<a target="_blank" href="https://paradox-11.com/">聊天机器人在线网站</a>

<h2>Deployment</h2>
<p>如果您想在自己的电脑上运行该项目或希望用自己的语料对模型进行训练，请参考下面的操作指南。</p>
<p>一、clone该项目的相关文件：</p>
<p>二、您可能需要安装torch zhon jieba flask，具体的安装命令可以参考网上的相关教程。</p>
<p>三、如果您想要更改训练语料，请先删除Mymodels文件夹中的.pt文件。</p>
<p>四、对训练语料进行个性化的处理后，请先执行execute.py文件，进行训练。</p>
<p>五、在训练过程中您可以实时观察loss的变化，训练完毕后再执行app.py文件即可成功运行该项目。</p>
<p>六、您可以在config文件夹中的seqseq.ini文件更改训练停止的最小loss值及一些训练相关的参数。</p>

```python
print("hello world")
```
