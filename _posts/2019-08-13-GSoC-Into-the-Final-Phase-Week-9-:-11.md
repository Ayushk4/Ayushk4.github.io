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
With this done, I proceeded with writing the API for Named Entity Tagging.

Before jumping into writing the API, I looked at various other similar APIs provided by [Metalhead](https://github.com/FluxML/Metalhead.jl) and [TextAnalysis](https://github.com/JuliaText/TextAnalysis.jl).
As a part of the API, downloading of the model weights needed to be taken care of. After discussing this with my mentors, [DataDeps](https://github.com/oxinabox/DataDeps.jl) was used for this, since it offered various advantages like handling download corruption, supporting re-download etc.

I added `DataDeps` to the Average Perceptron Tagger for downloading weights. Noticing that it lacked APIs for `Document` and `Corpus` types, I also added these.
Then, I proceeded to write the API supporting NER tagging over sentences as well as sequences of tokens. The API was later added to support various `Document` and `Corpus` types as provided by the `TextAnalysis` package.

After writing the API, I tested the NER API on various input and datasets, and the results were great. It gave 0.926, 0.89 f1 scores on dev and test sets of `CoNLL-2003` [(link)](https://github.com/Ayushk4/NER.jl/blob/master/valid/CoNLL.ipynb). The tests `Groningen Meaning Bank` 1.1.0 [(link)](https://github.com/Ayushk4/NER.jl/blob/master/valid/GMB.ipynb), gave an f1 of about 0.79. However, GMB Corpus, not being a gold standard one, had some ambiguities when compared to CoNLL. The results of `WikiGold` Corpus were decent with f1 of 0.712 [(link)](https://github.com/Ayushk4/NER.jl/blob/master/valid/WikiGold.ipynb), being much better than the ones by SpaCy or NLTK as per the results given in [this paper](https://www.aclweb.org/anthology/W16-2703).

[@thebhatman](https://github.com/thebhatman) and I also tried out some input sentences against the API. The notebook is available [here](https://github.com/Ayushk4/NER.jl/blob/master/valid/Random_sentences_tryouts.ipynb).
Here are some examples of the API in action -

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

The NER model, owing to the usage of CRFs, decodes globally hence tagging 'Manjunath Bhat' as an organisation in the above example, based on the contect. In the API, the character level features are also generated and used, thereby making the model perform well for out of vocabulary words.
However, much to my disappointment, the API doesn't label my name as a person in most sentences. 😞

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

Apart from the API, I also worked on `CorpusLoaders` package, contributing in the form of doc fixes, fixing CI tests and adding a Project.toml. While working on it, I learned more about `Documenter.jl` and the deploying of docs.

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
