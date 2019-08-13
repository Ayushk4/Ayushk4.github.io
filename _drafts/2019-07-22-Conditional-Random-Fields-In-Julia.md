---
layout: post
title: "Conditional Random Fields in Julia"
date: 2019-07-26
tags: [Machine Learning, Deep Learning, Conditional Random Fields, Linear Chain Conditional Random Fields, CRF, Natural Language Processing, Viterbi Decode, Forward Algorithm, Flux]
comments: true
categories:
---

Table of Contents

1. Conditional Random Fields
2. Decoding CRFs - Viterbi Algorithm
3. CRF Loss function
4. Implementing a Linear Chain CRF layer
5. Neural Networks with CRF Layer in Julia
6. References

# Conditional Random Fields

I will be mainly restricting to Linear Chain Conditional Random Fields in this blog.

# Decoding CRFs - Viterbi Algorithm

Takes exponential time, so use viterbi algorithm

# CRF Loss function

Use forward algorithm

# Implementing a Linear Chain CRF layer

The score functions similar to the ones in https://arxiv.org/abs/1603.01354.

# Neural Networks with CRF Layer in Julia

# References

These are the main references I used for CRFs.
https://www.lewuathe.com/machine%20learning/crf/conditional-random-field.html
https://blog.echen.me/2012/01/03/introduction-to-conditional-random-fields/
https://pytorch.org/tutorials/beginner/nlp/advanced_tutorial.html
https://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf
http://www.cs.columbia.edu/~mcollins/crf.pdf

I also referred to https://arxiv.org/pdf/1603.01354.pdf and 