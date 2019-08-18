---
layout: post
title: "My Journal in Google Summer of Code, 2019"
date: 2019-08-20
tags: [Google Summer of Code, GSoC]
comments: true
categories:
---

Hello reader,
with this Google Summer of Code, 2019.

# Summary of work done.

1. Models
- POS
- https://github.com/JuliaText/TextAnalysis.jl/pull/167
- https://github.com/JuliaText/TextAnalysis.jl/pull/162
2. TextAnalysis.jl

- https://github.com/JuliaText/TextAnalysis.jl/pull/166
- https://github.com/JuliaText/TextAnalysis.jl/pull/165

- https://github.com/JuliaText/TextAnalysis.jl/pull/161
- https://github.com/JuliaText/TextAnalysis.jl/pull/159
- https://github.com/JuliaText/TextAnalysis.jl/pull/155
- https://github.com/JuliaText/TextAnalysis.jl/pull/154
- https://github.com/JuliaText/TextAnalysis.jl/pull/151
- https://github.com/JuliaText/TextAnalysis.jl/pull/150
3. WordTokenizers.jl

- https://github.com/JuliaText/WordTokenizers.jl/pull/33
- https://github.com/JuliaText/WordTokenizers.jl/pull/13
- https://github.com/JuliaText/WordTokenizers.jl/pull/29

4. CorpusLoaders.jl

- https://github.com/JuliaText/CorpusLoaders.jl/pull/20
- https://github.com/JuliaText/CorpusLoaders.jl/pull/21
- https://github.com/JuliaText/CorpusLoaders.jl/pull/26
- https://github.com/JuliaText/CorpusLoaders.jl/pull/28
- https://github.com/JuliaText/CorpusLoaders.jl/pull/30

Though my proposal was about writing APIs for NER and POS,
the first few weeks was mainly about working on various packages in JuliaText ecosystem and related packages that these API would be dependent on.
The documentation and tests were done for each patch as new features or APIs were written.

Links to repos-

- NER.jl
- WordTokenizers.jl_analyse
- POS.jl

# Overview and my experience and what I learned

including why I went for this org.

From jekyll site, GPU, Metaprogramming and various other things about Julia language.

# What's ahead
Maitenance
APIs for training ones own NER and POS model.
Improving performance and APIs for tagging over specific domains like TweetNER, BioNER.
JuliaText might be a good option.

# Why should you consider contributing to Julia packages

My 2 cents on why you should consider contributing to Julia packages in specific
Great Learning op, no strong prerequisite.

- Writing packages is easier than ever.

- Excellent Community

# Acknowledgement

Firstly, I would like to thank Google for organizing Google Summer of Code
that gave me this amazing opportunity to work with Open Source Community.
I would also like to thank JuliaLang for selecting me to work on this project.

I am grateful to my mentors
[@oxinabox (Lyndon White)](https://github.com/oxinabox)
and [@aviks (Avik Sengupta)](https://github.com/aviks)
for guiding me through my project.
Finally, I would also like to thanks various fellow students
[@thebhatman](https://github.com/thebhatman),
[@ComputerMaestro](https://github.com/ComputerMaestro),
[@shreyas-kowshik](https://github.com/shreyas-kowshik)
as well the amazing JuliaLang Community for helping me whenever I got stuck
and making the GSoC journey fun.

# Links to Past GSoC Blogs

- [Week 9 - 11:](https://ayushk4.github.io/2019/08/13/GSoC-Into-the-Final-Phase-Week-9-11.html)
- [Week 7 - 8:](https://ayushk4.github.io/2019/07/21/GSoC-End-of-Phase-Two-Week-7-8.html)
- [Week 5 - 6:](https://ayushk4.github.io/2019/07/12/GSoC-Models-for-Sequence-Labeling-Week-5-6.html)
- [Week 3 - 4:](https://ayushk4.github.io/2019/06/25/GSoC-End-of-Phase-One-Week-3-4.html)
- [Week 2 - 1:](https://ayushk4.github.io/2019/06/13/GSoC-Into-the-Coding-Period-Week-1-2.html)
