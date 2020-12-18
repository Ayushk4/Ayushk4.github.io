---
layout: default
title: Research
permalink: /research/
weight: 1
/*remote_projects: 
  - git-for-wizards
  - arduino-visitor-counter */
---


<br>
<h2 style="margin:50px"> Publications and Talks </h2>

<ul style="font-size:20px;margin:50px">
    <li><a target="_blank" href="https://www.aclweb.org/anthology/2020.wnut-1.79.pdf">
              "Leveraging Event Specific and Chunk Span features to Extract COVID Events from tweets"</a>, Ayush Kaushal and Tejas Vaidhya <br>
              <i> <b><u>Oral Presentation</u></b> at the 6th Workshop on Noisy User-generated Text (W-NUT) at the 2020 Conference on Emperical Methods in Natural Language Processing (EMNLP)</i> <u><b>Shared Task Winners</b></u><a style="float:right; color:#3491fe;" data-toggle="collapse" data-target="#covid"><u>More</u> </a>
      </li>
        <div id="covid" class="collapse" style="font-size:15px;margin:50px">Twitter has acted as an important source of information during disasters and pandemic, especially during the times of COVID-19. In this paper, we describe our system entry for <i>WNUT 2020 Shared Task-3</i>. The task was aimed at automating the extraction of a variety of COVID-19 related events from Twitter, such as individuals who recently contracted the virus, someone with symptoms who were denied testing and believed remedies against the infection. The system consists of separate multi-task models for slot-filling subtasks and sentence-classification subtasks while leveraging the useful sentence-level information for the corresponding event. The system uses COVID-Twitter-Bert with attention-weighted pooling of candidate slot-chunk features to capture the useful information chunks. The system ranks <b>1st at the leader-board</b> with F1 of 0.6598, without using any ensembles or additional datasets. <br> <br>
          {% include elements/button.html link="https://github.com/Ayushk4/extract_covid_entity" text="Code" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.79.pdf" text="Pdf" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.79.bib" text="Bib" %} {% include elements/button.html link="https://github.com" text="Slides" %} {% include elements/button.html link="https://github.com" text="Poster" %}
      </div>
        <br>


    <li><a target="_blank" href="https://www.aclweb.org/anthology/2020.wnut-1.34.pdf">
              "Domain specific BERT representation for Named Entity Recognition of lab protocol."</a>, Tejas Vaidhya and Ayush Kaushal <br>
              <i> Proceedings of the 6th Workshop on Noisy User-generated Text (W-NUT) at the 2020 Conference on Emperical Methods in Natural Language Processing (EMNLP) </i> <a style="float:right;color:#3491fe" data-toggle="collapse" data-target="#wetlab"><u>More</u></a>
      </li>
        <div id="wetlab" class="collapse" style="font-size:15px;margin:50px">
        <!-- <br>
        <div align="center">
            <img id="mobile-img" src="../images/Bio-BERT.png" width="50%" border="0" height="50%" alt=""><br>
            </div> -->
            Supervised models trained to predict properties from representations, have been achieving high accuracy on a variety of tasks. For instance, the BERT family seems to work exceptionally well on the downstream task from NER tagging to the range of other linguistic tasks. But the vocabulary used in the medical field contains a lot of different tokens used only in the medical industry such as the name of different diseases, devices, organisms, medicines, etc. that makes it difficult for traditional BERT model to create contextualized embedding. In this paper, we are going to illustrate the System for Named Entity Tagging based on Bio-Bert. Experimental results show that our model gives substantial improvements over the baseline and stood the fourth runner up in terms of F1 score, and first runner up in terms of Recall among 13 teams with just 2.21 F1 score behind the best one.
            <br> <br>
            {% include elements/button.html link="https://github.com/tejasvaidhyadev/W-NUT_2020" text="Code" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.34.pdf" text="Pdf" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.34.bib" text="Bib" %} {% include elements/button.html link="https://github.com" text="Poster" %}
        </div>
        <br>


    <li><a target="_blank" href="https://www.theoj.org/joss-papers/joss.01956/10.21105.joss.01956.pdf">
              "Basic Tools for Tokenizing Natural Language in Julia."</a>, Ayush Kaushal, Lyndon White, Mike Innes and Rohit Kumar <br>
              <i> The Journal of Open Source Software (JOSS) 2020</i> <a style="float:right;color:#3491fe" data-toggle="collapse" data-target="#joss2020"><u>More</u></a>
      </li>
        <div id="joss2020" class="collapse" style="font-size:15px;margin:50px">
        <!-- <div align="center">
            <img id="mobile-img" src="../images/Bio-BERT.png" width="50%" border="0" height="50%" alt=""><br>
            </div> -->
            WordTokenizers.jl is a tool to help users of the Julia programming language work with natural language. WordTokenizers.jl provides a flexible API for defining fast tokenizers and sentence segmentors. Using this API several standard tokenizers and sentence segmenters have been implemented, allowing researchers and practitioners to focus on the higher details of their NLP tasks. WordTokenizers.jl uses a TokenBuffer API and its various lexers for fast word tokenization. TokenBuffer turns the string into a readable stream. A desired set of TokenBuffer lexers are used to read characters from the stream and flush out into an array of tokens. The package provides the following tokenizers made using this API. WordTokenizers.jl is currently being used by packages like TextAnalysis.jl, Transformers.jl and CorpusLoaders.jl for tokenizing text.
            <br> <br>
            {% include elements/button.html link="https://github.com/JuliaText/WordTokenizers.jl" text="Code" %} {% include elements/button.html link="https://www.theoj.org/joss-papers/joss.01956/10.21105.joss.01956.pdf" text="Pdf" %} {% include elements/button.html link="https://zenodo.org/record/3663390/export/hx" text="Bib" %}
        </div>
        <br>



    <li><a target="_blank" href="https://live.juliacon.org/talk/Z8WWNV">
              "Natural Language Processing in Julia."</a>, Ayush Kaushal <br>
              <i> Full Talk: JuliaCon 2020 Conference</i> <a style="float:right;color:#3491fe" data-toggle="collapse" data-target="#juliacontalk"><u>More</u></a>
      </li>
        <div id="juliacontalk" class="collapse" style="font-size:15px;margin:50px">
          The JuliaText ecosystem provides various packages for working with human languages. In this talk, I showed the usage of these JuliaText packages with Flux.jl for Natural Language Processing (NLP) with a focus on deep learning-based approaches. The attendees will gain working knowledge about how to apply the package for NLP in Julia. The talk will encompass Tokenizers, Word Embeddings, Recurrent Neural Networks and Transformer based Language models.
          <br><br>
          {% include elements/button.html link="https://github.com/Ayushk4/JuliaCon20_Talk" text="Code" %} {% include elements/button.html link="https://live.juliacon.org/talk/Z8WWNV" text="Talk" %} {% include elements/button.html link="https://www.youtube.com/watch?v=hHCi8ojazqk" text="Video" %}

        </div>
        <br>

    <li><a target="_blank" href="https://drive.google.com/file/d/1czsvXBNTUgN9S5I44JOYoghNwbeajOGF/view?usp=sharing">
              "Stance Detection is not Classification: Increasing the Role of Target Entities for Detecting Stance"</a>, Ayush Kaushal, Avirup Saha and Niloy Ganguly <br>
              <i>Under Review</i><a style="float:right; color:#3491fe;" data-toggle="collapse" data-target="#biasstance"><u>More</u> </a>
      </li>
        <div id="biasstance" class="collapse" style="font-size:15px;margin:50px">
          The stance detection task aims at detecting the stance of a tweet or a text with respect to a target. These targets can be named entities or free-form sentences (claims). Though the task by nature involves reasoning of the tweet with respect to a target, we find that it is possible to achieve high accuracy on several publicly available Twitter stance detection datasets without looking at the target sentence. Specifically, a simple tweet classification model achieved human-level performance on the WT-WT dataset and more than two-third accuracy on a variety of other datasets. We carry out an investigation into the existence of biases in such datasets to find the potential spurious correlations of sentiment-stance relations and lexical choice associated with stance category. Furthermore, we propose a new bias-free dataset, the largest of its kind with 100k+ tweet-target pairs and evaluate its usefulness using the existing stance detection systems. Our results show much scope for research on stance detection systems.
          <br> <br>
          {% include elements/button.html link="https://drive.google.com/file/d/1czsvXBNTUgN9S5I44JOYoghNwbeajOGF/view?usp=sharing" text="Pdf"%}
        </div>
        <br>
</ul>


<!-- ## Publications
<ul>
<li> <b>Leveraging Event Specific and Chunk Span information to Extract COVID Events from Tweets</b><br>
    <b>Ayush Kaushal</b> and Tejas Vaidhya<br>
	<b><u>Oral Presentation</u></b> <i>EMNLP 2020 Noisy User Generated Text Workshop</i> <a href="https://www.aclweb.org/anthology/2020.wnut-1.79">[paper]</a> <a href="https://github.com/Ayushk4/extract_covid_entity">[code]</a> </li>
<li> <b>Domain specific BERT representation for Named Entity Recognition of lab protocol</b><br>
    Tejas Vaidhya and <b>Ayush Kaushal</b><br>
   To appear <i>EMNLP 2020 Noisy User-generated Text Workshop</i> <a href="https://www.aclweb.org/anthology/2020.wnut-1.34">[paper]</a> <a href="https://github.com/tejasvaidhyadev/NER_Lab_Protocols">[code]</a> </li>
<li> <b>Basic Tools for Tokenizing Natural Language in Julia</b><br>
    <b>Ayush Kaushal</b>, Lyndon White, Mike Innes, Rohit Kumar,<br>
    <i>Journal of Open Source Software, 2020 </i></li>
<li> <b>Talk on Natural Language Processing in Julia</b><br>
    <b>Ayush Kaushal</b><br>
    <i>JuliaCon 2020 Conference</i></li>
</ul> -->

<br>

Following are the research projects I have worked on.

{% include projects/index.html %}

