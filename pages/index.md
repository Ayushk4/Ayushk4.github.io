---
layout: default
permalink: /
---
{% include landing.html %}
<h2 style="margin-left:50px;margin-bottom:20px;margin-right:0px;margin-top:0px"><b>About Me</b></h2>
<div style="font-size:20px;margin-left:50px;">
Hi There! :wave:
<br><br>
I am an aspiring researcher in the areas of Machine Learning and its applications to Natural Language Processing, Multimodal Learning and Social Computing. My Bachelor Thesis is under the guidance of <a href="https://scholar.google.com/citations?user=hCbFmUUAAAAJ&hl=en">Prof. Niloy Ganguly</a> at CNeRG Lab, IIT Kharagpur.
<br><br>
I am currently researching on Multimodal Learning at SHI Labs, University of Oregon. I previously have interned at IBM Research Labs, and Google Summer of Code in the domains of Deep Learning and Natural Language Procesing. Years ago, as a college freshman and sophomore, I developed various <a href="softwares/">open source packages</a>.
<br>
</div>


<br>


<h4 style="text-indent:-0.0em;font-weight:bold;font-size:25px;margin-left:50px;margin-bottom:20px;margin-right:0px;margin-top:0px">News!</h4>

<ul style="font-size:19.6px;margin-left:45px">
<li> <b>March 2021:</b> 1 first-author paper accepted at NAACL-HLT 2021.</li>
<li> <b>January 2021:</b> Our submission to <a href="https://competitions.codalab.org/competitions/25770">SemEval 2021-8 SubTask-2</a> stood runner up.</li>
<li> <b>November 2020:</b> <a href="https://arxiv.org/abs/2012.10052">1 Oral</a> and <a href="https://arxiv.org/abs/2012.11145">1 poster</a> at EMNLP 2020, W-NUT Workshop and won its <a herf="http://noisy-text.github.io/2020/extract_covid19_event-shared_task.html">Shared Task 3</a>.</li>
<li> <b>August 2020:</b> I was selected to attend <a href="https://sites.google.com/view/aisummerschool2020">Google AI Research</a> School 2020 for Natural Language Understanding Track.</li>
<li> <b>May 2020:</b> I will be giving a <a href="https://pretalx.com/juliacon2020/talk/Z8WWNV/">talk at JuliaCon</a> Conference 2020 on NLP packages I developed during Google SoC'19.</li>
<!-- - **May 2020:** I am a project mentor at <a href="https://summerofcode.withgoogle.com/projects/#5015442659213312">Google Summer of Code</a> for the project - Albert and statistical language models. -->
<li> <b>February 2020:</b> Mentored students in <a href="https://codein.withgoogle.com/archive/"> Google Code In</a>, 2019. 3 of my students were selected as 6 finalists!</li>
<li> <b>January 2020:</b> 1 <a href="https://www.theoj.org/joss-papers/joss.01956/10.21105.joss.01956.pdf">Paper</a> accepted at Journal of Open Source Software for the work during Google's - SoC  last year.</li>
<li> <b>December 2019:</b> Awarded <a href="https://github.com/Ayushk4/Resume/blob/master/certificates%20and%20related%20documents/Mitacs_Research_Scholarship.pdf">Globalink Research Scholarship</a> by MITACS and Indo-Canada Shastri.</li>
<li> <b>August 2019:</b> Had a wonderful summer at <a href="https://summerofcode.withgoogle.com/archive/2019/projects/4945754462879744/">Google Summer of Code</a>, researching on Deep neural networks for sequence labelling and developing NLP research packages. </li>

</ul>

<!-- ## Publications and Talks -->


<!-- <div class="row">
#{% include about/timeline.html title="Research Experience" source=site.data.education-timeline %}
</div >
*details of the projects can be found* [here](research/)

 -->



<h2 style="margin-left:50px;margin-bottom:20px;margin-right:0px;margin-top:50px"> Publications and Talks </h2>

<ul style="font-size:20px;margin-left:50px">
    <li><a target="_blank" href="https://www.aclweb.org/anthology/2020.wnut-1.79.pdf">
              "Leveraging Event Specific and Chunk Span features to Extract COVID Events from tweets"</a>, Ayush Kaushal and Tejas Vaidhya <br>
              <i> <b><u>Oral Presentation</u></b> at the 6th Workshop on Noisy User-generated Text (W-NUT) at the 2020 Conference on Emperical Methods in Natural Language Processing (EMNLP)</i> <u><b>Shared Task Winners</b></u><a style="float:right; color:#3491fe;" data-toggle="collapse" data-target="#covid"><u>More</u> </a>
      </li>
        <div id="covid" class="collapse" style="font-size:15px;margin:50px">Twitter has acted as an important source of information during disasters and pandemic, especially during the times of COVID-19. In this paper, we describe our system entry for <i>WNUT 2020 Shared Task-3</i>. The task was aimed at automating the extraction of a variety of COVID-19 related events from Twitter, such as individuals who recently contracted the virus, someone with symptoms who were denied testing and believed remedies against the infection. The system consists of separate multi-task models for slot-filling subtasks and sentence-classification subtasks while leveraging the useful sentence-level information for the corresponding event. The system uses COVID-Twitter-Bert with attention-weighted pooling of candidate slot-chunk features to capture the useful information chunks. The system ranks <b>1st at the leader-board</b> with F1 of 0.6598, without using any ensembles or additional datasets. <br> <br>
          {% include elements/button.html link="https://github.com/Ayushk4/extract_covid_entity" text="Code" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.79.pdf" text="Pdf" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.79.bib" text="Cite" %} {% include elements/button.html link="https://docs.google.com/presentation/d/13DDY6VSmrVPBddTjWb3rThYRFlRDE_9fi4iyBrhJev4/edit?usp=sharing" text="Slides" %} {% include elements/button.html link="https://github.com/noisy-text/noisy-text.github.io/blob/master/2020/posters/WNUT2020_91_poster%20-%20Tejas%20vaidhya.pdf" text="Poster" %}
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
            {% include elements/button.html link="https://github.com/tejasvaidhyadev/W-NUT_2020" text="Code" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.34.pdf" text="Pdf" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.34.bib" text="Cite" %} {% include elements/button.html link="https://github.com/noisy-text/noisy-text.github.io/blob/master/2020/posters/WNUT2020_92_poster%20-%20Tejas%20vaidhya.pdf" text="Poster" %}
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
            {% include elements/button.html link="https://github.com/JuliaText/WordTokenizers.jl" text="Code" %} {% include elements/button.html link="https://www.theoj.org/joss-papers/joss.01956/10.21105.joss.01956.pdf" text="Pdf" %} {% include elements/button.html link="https://zenodo.org/record/3663390/export/hx" text="Cite" %}
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
          {% include elements/button.html link="../research/#Coming-Soon" text="Pdf"%}
        </div>

</ul>

<h2 style="margin-left:40px;margin-bottom:0px;margin-top:50px"> Other Selected Projects </h2>

{% include projects/index.html %}


<h3 style="margin-left:25px;margin-bottom:0px;margin-top:50px"> Contact</h3>
<div style="margin-left:30px">
<i>Email: username at gmail dot com ; where username = ayushk4</i><br>

<br>
<br>

<div align="center" style="font-size: 80%">
	<i></i><br>
</div>

