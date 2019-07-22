---
layout: post
title: "GSoC, End of Phase Two, Week 7 - 8."
date: 2019-07-21
comments: true
tags: [Google Summer of Code, GSoC, Deep Learning, Natural Language Processing, Machine Learning, Conditional Random Fields, CRF]
categories:
---
Phase Two of Google Summer of Code comes to an end today.
The last two weeks of GSoC were full of fun and learning various stuff.

* Sequence Labelling model on Named Entity Recognition task

* Re-Structuring Conditional Random Fields

* BM-25, Co-occurrence Matrix, LSA, ROUGE-N in TextAnalysis.jl.

### <u> Named Entity Recognition </u>

The Sequence Labelling models previously implemented were debugged
and trained for `Named Entity Recognition` Task.
Even though the models seem to run perfectly well on `CPUs`,
a lot of bugs were faced while training it on a `GPU`.
Having not much prior experience in GPU programming,
I used this opportunity to get myself familiarized with working on GPUs.
I got to learn the usage of packages like
[CuArrays.jl](https://github.com/JuliaGPU/CuArrays.jl) and
[CUDAnative.jl](https://github.com/JuliaGPU/CUDAnative.jl).

After training the model, it gave somewhat promising results within the first couple epochs of training. But with more epochs of training, the result diverged which could possibly be due to not using rate decay in optimiser.

### <u> Conditional Random Fields </u>

While training the Model on NER, the loss resulted to infinity at times.
This problem was narrowed down to the previously written CRF.
The previous implementations were replaced with much more stable implementations.
`CRF` was re-structured, with corresponding `Viterbi decode` and `forward algorithm` being changed accordingly.
The `forward algorithm`, used in the loss function
was then shifted to a more stable log space implementation.
The support for GPU was also added for the CRF loss function.
While trained the model on NER,
the layer managed to learn the rules of BIOES labelling within first couple of epochs.([TextAnalysis/#162](https://github.com/JuliaText/TextAnalysis.jl/pull/162))

### <u> BM-25, Co-occurrence Matrix, LSA, ROUGE-N </u>

Having not much prior knowledge about these, I started with reading about each of these.
Then, I added [Okapi BM-25](https://en.wikipedia.org/wiki/Okapi_BM25) and Word Co-occurrence matrix,
referring to the implementation in [StringAnalysis.jl](https://github.com/zgornel/StringAnalysis.jl),
writing as per the APIs in [TextAnalysis.jl](https://github.com/JuliaText/TextAnalysis.jl).
Next, I improved the [ROUGE-N](https://en.wikipedia.org/wiki/ROUGE_(metric)) score
implementation in terms of speed, memory, providing multilingual support.
Then, I fixed the [Latent Semantic Analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis) model and added Tests, docs for all these.

## Summarizing work done

### <u> Week 7 and 8 </u>

* [Named Entity Recognition](https://github.com/Ayushk4/NER.jl)
* [Conditional Random Fields](https://github.com/JuliaText/TextAnalysis.jl/pull/163)
* [BM-25, Co-occurrence Matrix, LSA, ROUGE-N](https://github.com/JuliaText/TextAnalysis.jl/pull/165)

Throughout the GSoC phase 2 so far,

* Implementing Sequence Labelling Models
* Various fixes in TextAnalysis.jl
* Fixes/Updates in DataDeps.jl, WordTokenizers.jl
* Restructure Conditional Random Fields
* Sequence Labelling Model on NER task.

## What's ahead

With the models working and all the dependencies met,
the work that remains for the next five weeks is writing the API for Named Entity Recognition (NER) and testing it. The model also needs to be trained for it.
Then the same procedure will be duplicated for Part of Speech (POS) Tagging,
using the same sequence labelling model.
