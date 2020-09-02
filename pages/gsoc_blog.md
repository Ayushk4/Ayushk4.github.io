---
layout: default
permalink: /2019/08/22/My-Journey-in-Google-Summer-of-Code-.html
weight: 1
---

Hi there! 👋,

Google Summer of Code 2019 is soon coming to an end.
In this post, I would like to give share my experience at this program by Google.

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 30%;
  height: 30%;
}
</style>

<img src="/assets/img/gsoc_logo.png" alt="Google Summer of Code">

## Acknowledgement

I would like to thank the **Google** team for giving me this fantastic opportunity to work with the latest research for Deep Learning and Natural Language Processing.
I would also like to thank my mentor **Dr. Lyndon White**, **Mr. Avik Sengupta** and fellow student GSoCer - **Manjunath Bhat**.

## <u> Summary of work done </u>

My project was on Practical Deep Learning models for sequence labelling tasks of Named Entity Recognition and Part of Speech that generalizes well and is fast enough to be used in practice.

Speed and performance comparison against other models.
<img id="two" src="/assets/img/ner_compare.png" alt="Performance Comparison against other NLP Libraries" width="500" height="500">

We have open sourced the [code](https://github.com/Ayushk4/NER) and developed an API based on the smaller model, making pretrained NER and POS models accessible in just two lines:

`>>> ner = NERTagger()` <br>
`>>> ner("Some sentence")` <br>

## Word Tokenizers

I also worked on a novel regex free approach for high-speed `WordTokenizers` package providing with statistical and (custom) rule-based tokenizers for multiple languages.
Following is a performance analysis comparing the Tokenizers of _Spacy, NLTK with our Tokenizers_.

<img id="tffwo" src="/assets/img/tknzrs_plot.png" alt="Performance of Our Tokenizers" width="500" height="500">


