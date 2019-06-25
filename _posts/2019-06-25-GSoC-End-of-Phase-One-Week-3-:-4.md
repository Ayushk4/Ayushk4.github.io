---
layout: post
title: "GSoC, End of Phase One, Week 3 - 4"
date: 2019-06-25
comments: true
categories:
---
Phase One of Google Summer of Code concluded on 24th June.
In the last two weeks, I mainly worked on three things:

* Conditional Random Fields using Flux

* Faster Preprocessing Functions in TextAnalysis.jl

* Fixing toktok Tokenizer and updating WordTokenizers.jl to Julia 1.1

### <u> Conditional Random Fields </u>

Conditional Random Fields (CRF) are models used for sequence modelling.
Linear Chain - CRFs will be used as a part of the Bi-LSTM-CNN-CRF model for building APIs for  Named Entity Recognition (NER) and Part of Speech (POS) Tagging

I started with CRFs at the end of week 2, by reading and understanding the model.
After understanding how a Linear Chain - CRF works, I went for implementing it.
I studied in detail - the `Viterbi Algorithm`, a dynamic programming algorithm
used to label with the most probable tag sequence.
Implemented it and repeated the same for the `CRF_loss` function using the `forward algorithm`.

Conditional Random Fields was pretty new to me and
took a lot more effort and time than anticipated.
Finally, by the end of week 4, I managed to get it up and running.
This is being added to TextAnalysis.jl ([#162](https://github.com/JuliaText/TextAnalysis.jl/pull/162))

### <u> Faster PreProcessing in TextAnalysis </u>

There are various issues with the current document and Corpus preprocessing functions in TextAnalysis.jl.
Owing to the usage of Regex, it was slow.
The number of stopwords and additional words to be removed were restricted by the maximum character limit of PCRE.
It also fails for removing tokens with Regex-like punctuations.

In WordTokenizers.jl, we have been using a `TokenBuffer` instead of `Regex` for faster tokenization.
I started with a similar approach for preprocessing Documents in TextAnalysis.jl and sent a [PR](https://github.com/JuliaText/TextAnalysis.jl/pull/163) for the same.

The first implementation turned the input text, into a readable stream of `Char`.
As this stream was read this, it flushed out the preprocessed it a separate buffer.
This implementation had the same speed as the existing functions.

The second implementation involved one stream which was modified while it was read.
This was faster and used less memory than the previous one.

### <u> Fixing Toktok and WordTokenizers.jl support for 1.1 </u>

The default tokenizer for WordTokenizers.jl -
`toktok` was failing for wikitext103 Corpus for Julia 1.1.
It also failed on Julia 1.0, due to similar, but slightly different reasons.

Meanwhile, [another issue](https://github.com/JuliaText/WordTokenizers.jl/issues/28) was also raised where it the tokenized sentence began with final periods, instead of coming at the last full stop.

A patch ([#29](https://github.com/JuliaText/WordTokenizers.jl/pull/29)) was sent fixing both the above issues and updating the testset.
However one of the new tests still seemed to fail for Julia 1.1 due to a [small difference](https://github.com/JuliaText/WordTokenizers.jl/pull/29#issuecomment-504311770) b/w the 2 versions. This was then updated for Julia 1.1.

## Summarizing work done

### <u> Week 3 and 4 </u>

- [Conditional Random Fields](https://github.com/JuliaText/TextAnalysis.jl/pull/163)
- [Faster PreProcess](https://github.com/JuliaText/TextAnalysis.jl/pull/163)
- [Fixing TokTok.jl & support for Julia 1.1](https://github.com/JuliaText/WordTokenizers.jl/pull/29)

Over the course of the GSoC - Phase One so far,

- Improvements to TextAnalysis.jl, bug fixes, docs, tests.
- Tagging Schemes Added
- CorpusLoaders supports CoNLL corpora.
- Tweet Tokenizer added
- WordTokenizers.jl and CorpusLoaders.jl supports Julia 1.1 & Julia 1.0
- Conditional Random Fields added
- Faster Preprocessing in TextAnalysis.jl

## What's ahead
The API for NER and POS, will have CorpusLoaders.jl, WordTokenizers.jl and TextAnalysis.jl as dependencies.
CRF will be required for the model, which now is working.
In the coming 3 weeks, I will work on training of the Bi-LSTM-CNN-CRF model for NER tagging,
writing an API for the same and test it on variety of datasets.
After, this, I move onto the same for POS tagging.
