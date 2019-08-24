---
layout: post
title: "My Journey in Google Summer of Code, 2019"
date: 2019-08-22
tags: [Google Summer of Code, GSoC]
comments: true
categories:
---

Hello there,

Google Summer of Code 2019 is soon coming to an end.
In this post, I would like to summarize my work done so far and discuss what's ahead.

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 30%;
  height: 30%;
}
</style>

<img src="../../../images/2019/gsoc.png" alt="Google Summer of Code">

# <u> Summary of work done </u>

Over the past few months,
I worked towards developing and improving [WordTokenizers.jl](https://github.com/JuliaText/WordTokenizers.jl),
[TextAnalysis.jl](https://github.com/JuliaText/TextAnalysis.jl), [CorpusLoaders.jl](https://github.com/JuliaText/CorpusLoaders.jl) along with adding `Conditional Random Fields`
as well as building APIs for `Named Entity Recognition` and `Part of Speech Tagging`.

Here is a listing of the major PRs I made during the summer.
Most are merged, some are yet to be merged.
We discuss only an overview of the major works done on each domain, leaving out bug fixes and small patches.

1. Sequence Labelling
- [Part of Speech Tagger](https://github.com/JuliaText/TextAnalysis.jl/pull/169)
- [Named Entity Recognition API](https://github.com/JuliaText/TextAnalysis.jl/pull/167)
- [Conditional Random Fields](https://github.com/JuliaText/TextAnalysis.jl/pull/162)

2. TextAnalysis.jl
- [Updates to Avg Perceptron Tagger](https://github.com/JuliaText/TextAnalysis.jl/pull/166)
- [ROUGE-N, LSA, porting BM-25 and Word Cooccurrence matrix](https://github.com/JuliaText/TextAnalysis.jl/pull/165)
- [Tagging Schemes Conversion APIs](https://github.com/JuliaText/TextAnalysis.jl/pull/161)
- [Documentation / Docstrings revamp](https://github.com/JuliaText/TextAnalysis.jl/pull/150)

3. WordTokenizers.jl
- [Tweet Tokenizer and Lexers for TokenBuffer API](https://github.com/JuliaText/WordTokenizers.jl/pull/13)
- [Fix toktok tokenizer](https://github.com/JuliaText/WordTokenizers.jl/pull/29)
- [Handle Final Periods in tok-tok tokenizer](https://github.com/JuliaText/WordTokenizers.jl/pull/33)

4. CorpusLoaders.jl
- [Support for CoNLL 2003 Corpora](https://github.com/JuliaText/CorpusLoaders.jl/pull/20)
- [Address deprecations and other fixes](https://github.com/JuliaText/CorpusLoaders.jl/pull/21)
- [Enabling support for WikiGold Corpus](https://github.com/JuliaText/CorpusLoaders.jl/pull/28)
- [Adding CoNLL 2000](https://github.com/JuliaText/CorpusLoaders.jl/pull/30)

The following repositories were also created during GSoC'19 -

- [WordTokenizers.jl_analyse](https://github.com/Ayushk4/WordTokenizers.jl_analyse): Made while analysing tweet tokenizer. Also compares the speed of tokenizers in WordTokenizers.jl against other libraries.
- [NER.jl](https://github.com/Ayushk4/NER.jl): Contains sequence labelling models implemented and performance of NER API on various datasets.
- [POS.jl](https://github.com/Ayushk4/POS.jl): POS model and performance of POS API on various datasets.

<style>
  body{
    font-size: 20px;
  }
  ul{
    margin-left:50px;
  }
  ol{
    margin-left:20px;
  }
  #two{
    height: 50%;
    width: 50%;
  }
</style>

## Sequence Labelling Models

JuliaText now provides with APIs for Part of Speech Tagging and Named Entity Recognition.
These APIs and CRF currently are being kept in [TextAnalysis.jl](https://github.com/JuliaText/TextAnalysis.jl).

- Here is a table comparing the NER API performance. The accuracy and F1 scores are much better being a neural based tagger. However, it takes upto thrice the time to tag compared to SpaCy. Since the other NER Taggers, don't have a specific NER tag for `MISC`, it hasn't been considered for F1 score. (Here, P = Precision, R = Recall and NER API is the API written)

<img id="two" src="../../../images/2019/ner_compare.png" alt="Performance Comparison against other NLP Libraries" width="500" height="500">

- **Conditional Random Fields** have proven to be better at modelling sequential data than Hidden Markov Models
since the labelling is done globally rather than independently at each state.
Linear Chain - Conditional Random Fields was implemented and now works well over flux layers.

A `BiLSTM-CNN-CRF model` was implemented for sequence labelling tasks of
Named Entity Recognition and Part of Speech Tagging.
It was a neural model that used `fine-tuned GloVe Word Embeddings` and `Character level representation` as input and  decoded using `Linear Chain - Conditional Random Fields`.
A big part of the time I spent on this went into taking care of batches.
Since one minibatch consisted of various input sentences made up of words and their one-hot matrix of characters, leading to multiple levels of iterations.

After re-implementing Conditional Random Fields layer twice and a lot debugging,
an accuracy of about 90% was finally achieved on CoNLL compared to the claimed ~91%.
It was also tested on various other datasets [(link)](https://github.com/Ayushk4/NER.jl/tree/master/valid).
Here are some input sentences ran by **@bhatman** and me on the NER API.
<iframe src="../../../misc_assets/2019/NER_NB.html" width="80%" height="500">
</iframe>

The Linear Chain - Conditional Random Fields has also been tested and
can now be used with Flux layers.

A part of speech tagger was also implemented and an API for made for the same.
The POS API the obtained accuracy of ~91% on CoNLL 2003 against the claimed 97.5% accuracy. [(link)](https://github.com/Ayushk4/POS.jl/tree/master/valid)
It remains to be investigated upon and improved.



## WordTokenizers.jl

`WordTokenizers.jl` is a package providing with tokenizers for working with natural languages.
I had been working on a **Tweet Tokenizer** since January.
After a re-write, this was finally finished in June.
While working the tweet tokenizer _various lexers_ were written for working with `TokenBuffer` API.
As of now, the package lets the users build their custom tokenizers
using the TokenBuffer API and its several lexer functions.

[Here](https://github.com/Ayushk4/WordTokenizers.jl_analyse/blob/master/speed/Speed_wordtokenizers.jl_spacy_nltk.ipynb) is a performance analysis comparing the Tokenizers of _Spacy, NLTK and WordTokenizers_ in Julia.
The package performs much better while also providing a lot more tokenizers as well as means to create custom tokenizers.

<img id="two" src="../../../images/2019/tknzrs_plot.png" alt="Performance of Tokenizers in WordTokenizers.jl" width="500" height="500">

## TextAnalysis.jl

Just as the name suggests, `TextAnalysis.jl` provides with the tools for text analysis.
I managed to improve the codebase by adding docstrings to the codebase,
and improving documentation fixing the various bugs encountered on the way.
Code for Average Perceptron Part of Speech Tagger was changed to using DataDeps.jl for managing data dependency, and various APIs were written for all the `Document` types offered by TextAnalysis.jl.

New features included **Conversion between Tagging Schemes**, **Latent Semantic Analysis**,
porting of **BM-25**, **Word Co-occurrence matrix** and speeding up **ROUGE-N**.
I also started to work on a faster Pre Processing API using an approach similar to the `TokenBuffer`,
used by WordTokenizers.jl. This, however, remains Work-in-Progress.

## CorpusLoaders.jl

`CorpusLoaders.jl` provides with loaders for various text Corpora,
with lazy loading and using `DataDeps.jl` for managing data dependency.
The several corpora that I used while testing the NER and POS APIs like
**CoNLL 2000**, **CoNLL 2003** and **WikiGold** were added to CorpusLoaders.jl.
The package also needed multiple issues to be addressed,
such as deploying of docs, Fixing CI tests.
These were taken care of one by one.

# <u> What's ahead </u>

The work got deviated a little from my original proposal to solely writing APIs for
Named Entity Recognition and Part of Speech Tagging.
But, I believe it was for the betterment of the ecosystem.

While a lot has been achieved, the ending of GSoC also serves as a beginning in many ways.
Here are some of the things I would like to work on soon.

- Writing APIs for further training the NER and POS models with one's own dataset.
- Smaller models for NER and testing in domains of TweetNER and BioNER.
- Improving the performance of POS API.
- Testing CRFs over BERT for Named Entity Recognition.
- Faster pre-processing in TextAnalysis.
- Checking and fixing for the performance bottlenecks in Tweet Tokenizer and TokenBuffer lexers.

I would also like to work on other ecosystems of Flux, DiffEq and JuliaGPU in the near future.

# <u> Why consider contributing to Julia packages </u>

Working on open-source packages provides excellent opportunities to learn.
Here are my two cents on why you should consider contributing to Julia packages.

### <u> Writing packages is simpler than ever </u>

Writing packages or code that require high performance, like a new layer in Deep Learning is difficult in high-level dynamic typed languages like Python.
To get speed, the packages and layers have to be written in C or C++.
However in Julia, you can write the packages and libraries in Julia itself, without compromising on speed.
This makes maintaining packages a lot less outrageous.

### <u> Diverse and Excellent Community </u>

Owing to the fact that Julia lets easy writing of packages,
multiple ecosystems in various domains have grown.
People from various domains are involved with the development of these packages.
You can also reach us out for help or julia package/libraries related discussions ( or gripes 😉 ) in the respective channels or _#helpdesk_ on the slack workspace  ([Invitation link](https://slackinvite.julialang.org/)) or discourse.

# <u> Acknowledgement </u>

Firstly, I would like to thank **Google** and **JuliaLang** for giving me this fantastic opportunity to work on Open Source this summer.
I am grateful to my mentors
**@oxinabox (Lyndon White)** and **@aviks (Avik Sengupta)**
for guiding me through my project.
I would also like to thanks fellow Summer of Code students
**@thebhatman**, **@ComputerMaestro**, **@shreyas-kowshik**
as well the fantastic **JuliaLang Community** for helping me whenever I got stuck
and making the GSoC journey fun. 😄

--------------------

To sum up, the summer was full of learning new things,
some about writing good software, some about writing better Julia code.
My knowledge also deepened about various topics in Deep Learning, Natural Language Processing, among few to name.
I also used GSoC as an excuse to learn Jekyll 😉 and built this minimalistic blog-site for myself.
Looking back, it feels that these past four months passed way too quickly.
I still remember anticipating for proposal acceptance results like it was yesterday.

However, there was a repercussion of doing GSoC with _The Julia Language_.
I am now very much dependent on the JuliaLang slack's slackbot for reminders of sorts 😛.

Here are some more detailed blogs for the work done in each week.
You might wanna take a look at these -

- [Week 9 - 11](https://ayushk4.github.io/2019/08/13/GSoC-Into-the-Final-Phase-Week-9-11.html)
- [Week 7 - 8](https://ayushk4.github.io/2019/07/21/GSoC-End-of-Phase-Two-Week-7-8.html)
- [Week 5 - 6](https://ayushk4.github.io/2019/07/12/GSoC-Models-for-Sequence-Labeling-Week-5-6.html)
- [Week 3 - 4](https://ayushk4.github.io/2019/06/25/GSoC-End-of-Phase-One-Week-3-4.html)
- [Week 2 - 1](https://ayushk4.github.io/2019/06/13/GSoC-Into-the-Coding-Period-Week-1-2.html)
- [Week 0](https://ayushk4.github.io/2019/06/05/Google-Summer-of-Code.html)