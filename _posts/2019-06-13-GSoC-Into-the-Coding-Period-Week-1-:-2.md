---
layout: post
title: "GSoC, Coding Period, Week 1 - 2"
date: 2019-06-13
comments: true
categories:
---
The Coding Period for Google Summer of Code commenced from 27th May.

I started by reading about various tagging schemes used for sequence labelling,
implemented these and function for converting between them. These have been added to [TextAnalysis.jl](https://github.com/JuliaText/TextAnalysis.jl).

Then, I worked on adding CoNLL Corpus to [CorpusLoaders.jl](https://github.com/JuliaText/CorpusLoaders.jl).
This, took longer than expected, as CorpusLoaders.jl had to be updated against the deprecations. As of now, CorpusLoaders.jl, works well on Julia 1.0.

A Tweet Tokenizer was needed by [@ComputerMaestro](https://github.com/ComputerMaestro) for adding sentiment datasets to CorpusLoaders.jl in their PR[#18](https://github.com/JuliaText/CorpusLoaders.jl/pull/18). I had been working on [adding a Tweet Tokenizer](https://github.com/JuliaText/WordTokenizers.jl/pull/13) in WorkTokenizers.jl for some time, which I continued working on in the Community Bonding Period. In these two weeks, I finally finished with it.

After this, I moved on to adding Linear Chain - Conditional Random Fields.
I started by reading about CRFs, HMMs, looked up at the existing implementations
of the same. This remained Work-in-Progress at the end of the second week.

## Tagging Schemes for Sequence Labelling

Tagging scheme is the way of encoding tags in sequence labelling tasks
like [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition), [Part of Speech Tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging), [Chunking](https://en.wikipedia.org/wiki/Shallow_parsing) etc.

Let us assume the following sentence for NER tagging task-
<br>
`The EU backs John Doe ’s proposal.`

Following are the NER tags assigned-
<br>
The `[EU]`<sub>`LOCATION`</sub>backs `[John Doe]`<sub>`PERSON`</sub>'s Proposal.

### <u> IO (Inside-Outside)</u>
The simplest possible tagging scheme would be marking a token either as inside or outside a tag. The `I-` prefix before a tag, indicates that tag is inside the chunk, and `O` is used for one not belonging to any chunk.
<br>
The<sub>`O`</sub> EU<sub>`I-Loc`</sub> backs<sub>`O`</sub> John<sub>`I-Per`</sub> Doe<sub>`I-Per`</sub> 's<sub>`O`</sub> Proposal<sub>`O`</sub>

### <u> BIO (Beginning-Inside-Outside) </u>
BIO differs from IO scheme by using a separate tag prefix `B-` for beginning of a multi-token tag chunk.
<br>
The<sub>`O`</sub> EU<sub>`I-Loc`</sub> backs<sub>`O`</sub> John<sub>`B-Per`</sub> Doe<sub>`I-Per`</sub> 's<sub>`O`</sub> Proposal<sub>`O`</sub>

`BIO2` is similar to BIO format, but uses the prefix `B-` for the beginning token, including  ones with single element.
<br>
The<sub>`O`</sub> EU<sub>`B-Loc`</sub> backs<sub>`O`</sub> John<sub>`B-Per`</sub> Doe<sub>`I-Per`</sub> 's<sub>`O`</sub> Proposal<sub>`O`</sub>

### <u> BIOES / IOBES </u>
Other Tagging Scheme include BIOES / IOBES, where 'E-' prefix denotes ending character in a tag sequence and 'S-' prefix denotes single element.
<br>
The<sub>`O`</sub> EU<sub>`S-Loc`</sub> backs<sub>`O`</sub> John<sub>`B-Per`</sub> Doe<sub>`E-Per`</sub> 's<sub>`O`</sub> Proposal<sub>`O`</sub>

This tagging scheme is most popular for NER Tagging due to its high accuracy <sup>([ref](https://www.aclweb.org/anthology/W09-1119))</sup>.

Other names for it are BMEWO and BILOU. The following table, describes the analogous letters in the three tagging schemes.
<style>
 table {
   border-collapse: collapse;
   margin-right:auto;
   /* margin-left:0px; */
   table-layout:fixed;
   max-width: 25%;
 }

 table, td, th {
   text-align: left;
   white-space: normal;
   max-width: 50%;
 }
</style>

| BIOES | B- | I- | O | E- | S- |
| BILOU | B- | I- | O | L- | U- |
| BMEWO | B- | M- | O | E- | W- |

-----------

TextAnalysis offers various tagging formats and their conversions-

---------- Example usage -----------

```julia
julia> using TextAnalysis

julia> tags = ["I-LOC", "O", "I-PER", "B-MISC", "I-MISC", "B-PER", "I-PER", "I-PER"]

julia> tag_scheme!(tags, "BIO1", "BIOES")

julia> tags
8-element Array{String,1}:
 "S-LOC"
 "O"
 "S-PER"
 "B-MISC"
 "E-MISC"
 "B-PER"
 "I-PER"
 "E-PER"
```

## CorpusLoaders.jl and CoNLL2003
CorpusLoaders.jl provides us with a loaders for various NLP corpora.
I worked on adding the support for CoNLL corpora in a generic sense
and CoNLL 2003 in particular.

One can access the various sets of CoNLL2003 data as follows-

    train = load(CoNLL(), "train") # training set
    test = load(CoNLL(), "test") # test set
    dev = load(CoNLL(), "dev") # dev set

Structure of each set is - `document, sentences, words, characters`.

To get the desired levels, `flatten_levels` function from [MultiResolutionIterators.jl](https://github.com/oxinabox/MultiResolutionIterators.jl) can be used.

---------- Example usage --------

Load the packages-

    using CorpusLoaders, MultiResolutionIterators

We can flatten_levels at the document level
to get a set of sentences of tagged words.

```julia
julia> dataset = flatten_levels(train, lvls(CoNLL, :document)) |> full_consolidate

julia> typeof(dataset)
Document{Array{Array{CorpusLoaders.NERTaggedWord,1},1},String}

julia> length(dataset) # Total number of sentences.
14041

julia> dataset[6]
33-element Array{CorpusLoaders.NERTaggedWord,1}:
 CorpusLoaders.NERTaggedWord("O", "O", "\"", "\"")
 CorpusLoaders.NERTaggedWord("O", "B-NP", "PRP", "We")
 CorpusLoaders.NERTaggedWord("O", "B-VP", "VBP", "do")
 CorpusLoaders.NERTaggedWord("O", "I-VP", "RB", "n't")
 CorpusLoaders.NERTaggedWord("O", "I-VP", "VB", "support")
 CorpusLoaders.NERTaggedWord("O", "B-NP", "DT", "any")
 CorpusLoaders.NERTaggedWord("O", "I-NP", "JJ", "such")
 CorpusLoaders.NERTaggedWord("O", "I-NP", "NN", "recommendation")
 CorpusLoaders.NERTaggedWord("O", "B-SBAR", "IN", "because")
 CorpusLoaders.NERTaggedWord("O", "B-NP", "PRP", "we")
 ⋮
 CorpusLoaders.NERTaggedWord("B-PER", "I-NP", "NNP", "Nikolaus")
 CorpusLoaders.NERTaggedWord("I-PER", "I-NP", "NNP", "van")
 CorpusLoaders.NERTaggedWord("I-PER", "I-NP", "FW", "der")
 CorpusLoaders.NERTaggedWord("I-PER", "I-NP", "NNP", "Pas")
 CorpusLoaders.NERTaggedWord("O", "B-VP", "VBD", "told")
 CorpusLoaders.NERTaggedWord("O", "B-NP", "DT", "a")
 CorpusLoaders.NERTaggedWord("O", "I-NP", "NN", "news")
 CorpusLoaders.NERTaggedWord("O", "I-NP", "NN", "briefing")
 CorpusLoaders.NERTaggedWord("O", "O", ".", ".")
```

Now the tags can be extracted using

    CorpusLoaders.named_entity(ner_tagged_word) 

Then could then be converted into desired tagging scheme-

```julia
julia> using TextAnalysis

julia> tags = CorpusLoaders.named_entity.(dataset[6])
33-element Array{String,1}:
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 ⋮
 "B-PER"
 "I-PER"
 "I-PER"
 "I-PER"
 "O"
 "O"
 "O"
 "O"
 "O"

julia> tag_scheme!(tags, "BIO2", "BIOES")

julia> tags
33-element Array{String,1}:
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 "O"
 ⋮
 "B-PER"
 "I-PER"
 "I-PER"
 "E-PER"
 "O"
 "O"
 "O"
 "O"
 "O"  
```

## Summarizing the work
- [Tagging Schemes and Conversion.](https://github.com/JuliaText/TextAnalysis.jl/pull/161)
- [Support for CoNLL Corpora](https://github.com/JuliaText/CorpusLoaders.jl/pull/20)
- [Deprecations and fixing levelname_mapping](https://github.com/JuliaText/CorpusLoaders.jl/pull/21)
- [Conditional Random Fields](https://github.com/JuliaText/TextAnalysis.jl/pull/162) (WIP)
- [Tweet Tokenizer](https://github.com/JuliaText/WordTokenizers.jl/pull/13)

### Other Contribs
- TextAnalysis.jl - bug fixes, docs, tests etc: [#150](https://github.com/JuliaText/TextAnalysis.jl/pull/150) \| [#151](https://github.com/JuliaText/TextAnalysis.jl/pull/151) \| [#154](https://github.com/JuliaText/TextAnalysis.jl/pull/154) \| [#155](https://github.com/JuliaText/TextAnalysis.jl/pull/155).

## References
- [Ratinov and Roth, survey](https://www.aclweb.org/anthology/W09-1119) 
- [LingPipe-blog](https://lingpipe-blog.com/2009/10/14/coding-chunkers-as-taggers-io-bio-bmewo-and-bmewo/)
- [Inside Outside Beginning](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging))
- [NLP Encoding Schemes](https://chameleonmetadata.com/Education/NLP-3/ref_nlp_encoding_schemes_list.php)
- [CoNLL 2003 Task](https://arxiv.org/abs/cs/0306050)