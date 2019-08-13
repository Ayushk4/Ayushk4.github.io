---
layout: post
title: "GSoC, Into the Final Phase, Week 9 - 11."
date: 2019-08-13
comments: true
tags: [Google Summer of Code, GSoC, Deep Learning, Natural Language Processing, Machine Learning, Julia Language, JuliaText, Named Entity Recognition, Part of Speech Tagging]
categories:
---

At the end of the second phase,
the BiLSTM-CNN-CRF model gave good F1 score on Named Entity Recognition (NER).
With this done, I proceeded with the API for NER model.

Before jumping into writing the API, I looked at various other similar pre-trained Machine Learning models provided by [Metalhead](https://github.com/FluxML/Metalhead.jl) and [TextAnalysis](https://github.com/JuliaText/TextAnalysis.jl).
To manage the dependency of the API on model weights, after discussing with my mentors, [DataDeps](https://github.com/oxinabox/DataDeps.jl) was used since offered various advantages like handling download corruption, supporting re-download.

I switched the Average Perceptron Tagger of TextAnalysis to use `DataDeps` for downloading weights. And APIs were written for `Document` and `Corpus` types.
I then proceeded to write the API supporting NER tagging over sentences as well as sequences of tokens. The API was later added to support various `Document` and `Corpus` types as provided by the `TextAnalysis` package.

After writing the API, I tested the NER API on various input and datasets, and the results were great. It seemed to give 0.926, 0.89 f1 scores on dev and test sets of `CoNLL-2003` [(link)](https://github.com/Ayushk4/NER.jl/blob/master/valid/CoNLL.ipynb). The tests on inputs from `Groningen Meaning Bank` 1.1.0 [(link)](https://github.com/Ayushk4/NER.jl/blob/master/valid/GMB.ipynb), gave an f1 of about 0.79. However, GMB Corpus, not being a gold standard one, had some ambiguities when compared to CoNLL. The results of `WikiGold` Corpus were decent with f1 of 0.712 [(link)](https://github.com/Ayushk4/NER.jl/blob/master/valid/WikiGold.ipynb).
[@thebhatman](https://github.com/thebhatman) and I also tried out some input sentences against the API. The notebook is available [here](https://github.com/Ayushk4/NER.jl/blob/master/valid/Random_sentences_tryouts.ipynb).
Here are some examples -

```julia
julia> using TextAnalysis

julia> ner = NERTagger()
```

Now we can try the tagger on various inputs -

```julia

julia> ner("Lyndon White and Avik Sengupta affiliated with Julia Computing in Bangalore.")
12-element Array{String,1}:
 "PER"
 "PER"
 "O"
 "PER"
 "PER"
 "O"
 "O"
 "ORG"
 "ORG"
 "O"
 "LOC"
 "O"

julia> ner("Google, Yahoo and Mercari vs Manjunath Bhat.")
9-element Array{String,1}:
 "ORG"
 "O"
 "ORG"
 "O"
 "O"
 "O"
 "ORG"
 "ORG"
 "O"
```

The NER model, owing to the usage of CRFs, decodes globally. Since the character level features are also used to predict the tag, the model works well for out of vocabulary words.
However, it doesn't label my name as a person in certain sentences. 😞

```julia
julia> ner("Is my name Ayushk4 or Ayush?")
8-element Array{String,1}:
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"

```

Apart from NER, I made a few changes to `CorpusLoaders` package, in the form of fixing docs, changing CI tests and adding a Project.toml. While working on it, I learned more about `Documenter.jl` and the process of docs deploying.

The Sequence Labelling model was trained on [Part-of-Speech Tagging](https://github.com/Ayushk4/POS.jl)
Within a few epochs of training, it gave decent results.

### <u> Links to the work done in weeks 9 - 11 </u>

* [NER API](https://github.com/JuliaText/TextAnalysis.jl/pull/167)
* [Testing of NER API](https://github.com/Ayushk4/NER.jl/tree/master/valid)
* [Part of Speech Tagger](https://github.com/Ayushk4/POS.jl)

Other Contribs -

- [Fixing the Docs in CorpusLoaders](https://github.com/JuliaText/CorpusLoaders.jl/pull/26)
- [Improving the average perceptron POS Tagger](https://github.com/JuliaText/TextAnalysis.jl/pull/166)
- [Fixes in CorpusLoaders.jl](https://github.com/JuliaText/CorpusLoaders.jl/pull/25)
