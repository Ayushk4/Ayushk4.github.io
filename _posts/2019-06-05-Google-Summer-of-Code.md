---
layout: post
title: "Summer of Code with Julia"
date: 2019-06-05
tags: [Google Summer of Code, GSoC]
comments: true
categories:
---

I am happy to share the news that my proposal got accepted in Google Summer of Code, 2019 under **The JuliaLang organization**. I will be working this summer on implementing and testing APIs for Named Entity Recognition and Part of Speech Tagging under the Flux projects. 

Here is a list of the major things I will be working on-

- Linear Chain Conditional Random Fields (CRF):
- Named Entity Recognition:
- Part of Speech Tagging:

The model that will be implemented for NER and POS tagging will be a Neural Network using Bi-LSTM-CNN-CRFs as follows-


Character Representation Layer using CNNs        |  Bi-LSTM-CRF layer with Word Embeddings and Character Representation Input
:-------------------------:|:-------------------------:
![Character Representation](../../../images/2019/Char-rep.png)  |  ![Bi-LSTM CRF layer.](../../../images/2019/LSTM-CRF-layer.png){:class="img-responsive"}

The details of the Model is described in this paper by [Xuezhe Ma and Eduard Hovy](https://arxiv.org/pdf/1603.01354.pdf)
