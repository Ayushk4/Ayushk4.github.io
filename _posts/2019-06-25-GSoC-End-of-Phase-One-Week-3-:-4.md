---
layout: post
title: "GSoC, End of Phase One, Week 3 - 4."
date: 2019-06-25
comments: true
tags: [Google Summer of Code, GSoC, Deep Learning, Natural Language Processing, Machine Learning]
categories:
---
Phase One of Google Summer of Code concluded on 24th June.
In the last two weeks, I mainly worked on the following three things:

* Conditional Random Fields using Flux

* Faster Preprocessing Functions in TextAnalysis.jl

* Fixing toktok Tokenizer and WordTokenizers.jl support for Julia 1.1

### <u> Conditional Random Fields </u>

Conditional Random Fields (CRF) are discriminative models used for sequence modelling. I started with CRFs at the end of week 2, by reading and understanding the model. After going through the Flux code for various layers, I moved on to implementing it. Next, I studied in detail - the `Viterbi Algorithm`, a dynamic programming algorithm used to label a sequence with the most probable tag sequence. Implemented it and repeated the same for the `CRF_loss` function using the `forward algorithm`.

Conditional Random Fields was pretty new to me and it took a lot more effort and time than anticipated. Finally, by the end of week 4, I managed to get it running. This is being added to TextAnalysis.jl. ([#162](https://github.com/JuliaText/TextAnalysis.jl/pull/162))

### <u> Faster PreProcessing in TextAnalysis </u>

There are various issues with the current document and Corpus preprocessing functions in TextAnalysis.jl. Owing to the usage of Regex, it was slow. PCRE was also limiting the number of stopwords and additional words/tokens that could be removed, also failing for tokens with Regex-like punctuations.

In WordTokenizers.jl, we have been using a `TokenBuffer` instead of `Regex` for faster tokenization. I started with a similar approach for preprocessing Documents in TextAnalysis.jl and sent a [PR](https://github.com/JuliaText/TextAnalysis.jl/pull/163) for the same.

The first implementation turned the input text into a readable stream of `Char`.
As this stream was read, it flushed out the preprocessed characters in a separate buffer. It performed nearly at the same speed as the existing one.

The second implementation involved traversing a single stream and modifying it. This implementation was faster and used less memory than the previous one.

### <u> Fixing Toktok and WordTokenizers.jl support for 1.1 </u>

The default tokenizer for WordTokenizers.jl - `toktok` was failing on wikitext103 Corpus for Julia 1.1 and 1.0.

Meanwhile, [another issue](https://github.com/JuliaText/WordTokenizers.jl/issues/28) was raised where a tokenized sentence began with final periods, instead of having the final periods coming at the last.

A patch ([#29](https://github.com/JuliaText/WordTokenizers.jl/pull/29)) was sent fixing both the issues and updating the test set. However, one of the new tests seemed to fail exclusively for Julia 1.1 due to a [small difference](https://github.com/JuliaText/WordTokenizers.jl/pull/29#issuecomment-504311770) b/w the two versions. It was fixed, and WordTokenizers.jl updated for Julia 1.1.

## Summarizing work done

### <u> Week 3 and 4 </u>

* [Conditional Random Fields](https://github.com/JuliaText/TextAnalysis.jl/pull/163)
* [Faster PreProcess](https://github.com/JuliaText/TextAnalysis.jl/pull/163)
* [Fixing TokTok.jl & support for Julia 1.1](https://github.com/JuliaText/WordTokenizers.jl/pull/29)

Throughout the GSoC - Phase One so far,

* Improvements to TextAnalysis.jl, bug fixes, docs, tests.
* Tagging Schemes Added
* CorpusLoaders supports CoNLL corpora.
* Tweet Tokenizer added
* WordTokenizers.jl and CorpusLoaders.jl supports Julia 1.1 & Julia 1.0
* Conditional Random Fields added
* Faster Preprocessing in TextAnalysis.jl

## What's ahead
NER and POS models will have CorpusLoaders.jl, WordTokenizers.jl and TextAnalysis.jl as dependencies. The model will also require CRFs.

With all these dependencies met. I move on to NER Tagging. In the coming three weeks, I will work on the training of the Bi-LSTM-CNN-CRF model for NER tagging, writing an API for the same and testing on a variety of datasets. After this, I move onto the same for POS tagging.
