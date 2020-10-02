---
layout: default
permalink: /2019/08/22/My-Journey-in-Google-Summer-of-Code.html
weight: 1
---


### Check out my [project page at Google's GSoC website](https://summerofcode.withgoogle.com/archive/2019/projects/4945754462879744/)


Hi there! 👋,

I had a wonderful time working at Google Summer of Code 2019 this summer. 

Here, I would like to give share some of my work done. I will giving a talk on the NLP packages I worked on, at the [JuliaCon 2020 Conference](https://live.juliacon.org/talk/Z8WWNV).

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 30%;
  height: 30%;
}
</style>
<img src="../../../images/gsoc_logo.png" alt="Google Summer of Code">

## Acknowledgement

I would like to thank the **Google** team for giving me this fantastic opportunity to work with the latest research for Deep Learning and Natural Language Processing.
I would also like to thank my mentor **Dr. Lyndon White**, **Mr. Avik Sengupta** and fellow student GSoCer - **Manjunath Bhat**.

## <u> Summary of work done </u>

1. Deep Learning based neural sequence labelling models.

2. High speed word tokenizers in [WordTokenizers package](https://github.com/JuliaText/WordTokenizers.jl).

3. A julia package for [text analysis](https://github.com/JuliaText/TextAnalysis.jl).

4. A bunch of [corpus loaders](https://github.com/JuliaText/CorpusLoaders.jl).

   

   Following I discuss about some of the works. 

## Ner and Pos Taggers

My project was on Practical Deep Learning models for sequence labelling tasks of Named Entity Recognition and Part of Speech that generalizes well and is fast enough to be used in practice.

Speed and performance comparison against other models.
<img id="two" src="../../../images/ner_compare.png" alt="Performance Comparison against other NLP Libraries" style="width:1000px;">

We have open sourced the [code](https://github.com/Ayushk4/NER) and developed an API based on the smaller model, making pretrained NER and POS models accessible in just two lines:

`>>> ner = NERTagger()` <br>
`>>> ner("Some sentence")` <br>

similary for POS. The POS tagger performs 0.902 F1 on CoNLL-2003.

## Word Tokenizers

I also worked on a novel regex free approach for high-speed `WordTokenizers` package providing with statistical and (custom) rule-based tokenizers for multiple languages.


Following is a performance analysis comparing the Tokenizers of _Spacy, NLTK with our Tokenizers_.

<img id="tffwo" src="../../../images/tknzrs_plot.png" alt="Performance of Our Tokenizers" style="width:500px;">

This work has been published at [the Journal of Open Source Software](https://www.theoj.org/joss-papers/joss.01956/10.21105.joss.01956.pdf).

<iframe src="https://www.theoj.org/joss-papers/joss.01956/10.21105.joss.01956.pdf" width="100%" height="750px">


