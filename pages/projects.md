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
      <li><a target="_blank" href="https://aclanthology.org/2021.naacl-main.303.pdf">
        "<i style="font-family:sans-serif">t-</i>WTWT: Asserting the Role of Targets for Detecting Stance in Tweets"</a>, Ayush Kaushal, Avirup Saha and Niloy Ganguly <br>
              <i>Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (<b>NAACL-HLT 2021</b>)</i><a style="float:right; color:#3491fe;" data-toggle="collapse" data-target="#biasstance"><u>More</u> </a>
      </li>
        <div id="biasstance" class="collapse" style="font-size:15px;margin:50px">
          The stance detection task aims at detecting the stance of a tweet or a text for a target. These targets can be named entities or free-form sentences (claims). Though the task involves reasoning of the tweet with respect to a target, we find that it is possible to achieve high accuracy on several publicly available Twitter stance detection datasets without looking at the target sentence. Specifically, a simple tweet classification model achieved human-level performance on the WT–WT dataset and more than two-third accuracy on various other datasets. We investigate the existence of biases in such datasets to find the potential spurious correlations of sentiment-stance relations and lexcal choice associated with the stance category. Furthermore, we propose a new large dataset free of such biases and demonstrate its aptness on the existing stance detection systems. Our empirical findings show much scope for research on the stance detection task and proposes several considerations for creating future stance detection datasets.
          <br> <br>
          {% include elements/button.html link="https://github.com/Ayushk4/bias-stance" text="Code" %} {% include elements/button.html link="https://github.com/Ayushk4/stance-dataset" text="Dataset" %} {% include elements/button.html link="https://aclanthology.org/2021.naacl-main.303.pdf" text="Pdf" %} {% include elements/button.html link="https://aclanthology.org/2021.naacl-main.303.bib" text="Cite" %} {% include elements/button.html link="https://docs.google.com/presentation/d/11kM4MJ4ct1GtdFuzko-Ou8wN5QxqhmL6hXG3WBrPevk/edit?usp=sharing" text="Slides" %} {% include elements/button.html link="https://drive.google.com/file/d/1L6BW887fOtZZ2d9jnB6Jl_Gqnu6LnLMX/view?usp=sharing" text="Poster" %}
        </div>
        <br>

    <li><a target="_blank" href="https://www.aclweb.org/anthology/2020.wnut-1.79.pdf">
              "Leveraging Event Specific and Chunk Span features to Extract COVID Events from tweets"</a>, Ayush Kaushal and Tejas Vaidhya <br>
              <i> <b><u>Oral Presentation</u></b> at the 6th Workshop on Noisy User-generated Text (W-NUT) at the 2020 Conference on Emperical Methods in Natural Language Processing (EMNLP)</i> <u><b>Shared Task Winners</b></u><a style="float:right; color:#3491fe;" data-toggle="collapse" data-target="#covid"><u>More</u> </a>
      </li>
        <div id="covid" class="collapse" style="font-size:15px;margin:50px">Twitter has acted as an important source of information during disasters and pandemic, especially during the times of COVID-19. In this paper, we describe our system entry for <i>WNUT 2020 Shared Task-3</i>. The task was aimed at automating the extraction of a variety of COVID-19 related events from Twitter, such as individuals who recently contracted the virus, someone with symptoms who were denied testing and believed remedies against the infection. The system consists of separate multi-task models for slot-filling subtasks and sentence-classification subtasks while leveraging the useful sentence-level information for the corresponding event. The system uses COVID-Twitter-Bert with attention-weighted pooling of candidate slot-chunk features to capture the useful information chunks. The system ranks <b>1st at the leader-board</b> with F1 of 0.6598, without using any ensembles or additional datasets. <br> <br>
          {% include elements/button.html link="https://github.com/Ayushk4/extract_covid_entity" text="Code" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.79.pdf" text="Pdf" %} {% include elements/button.html link="https://www.aclweb.org/anthology/2020.wnut-1.79.bib" text="Cite" %} {% include elements/button.html link="https://docs.google.com/presentation/d/13DDY6VSmrVPBddTjWb3rThYRFlRDE_9fi4iyBrhJev4/edit?usp=sharing" text="Slides" %} {% include elements/button.html link="https://github.com/noisy-text/noisy-text.github.io/blob/master/2020/posters/WNUT2020_91_poster%20-%20Tejas%20vaidhya.pdf" text="Poster" %}
      </div>
        <br>

  
      <li><a target="_blank" href="https://aclanthology.org/2021.semeval-1.46.pdf">
              "Multi-Staged Language Models for Extracting Measurements, their Attributes and Relations"</a>, Neel Karia*, Ayush Kaushal* and Faraaz Mallick* <br>
              <i> 15th International Workshop on Semantic Evaluation (SemEval'21) at ACL-IJCNLP'21</i> <u><b>Second Runner-up</b></u><a style="float:right; color:#3491fe;" data-toggle="collapse" data-target="#semeval21"><u>More</u> </a>
      </li>
        <div id="semeval21" class="collapse" style="font-size:15px;margin:50px">SemEval-2021 Task 8: MeasEval aims at improving the machine understanding of measurements in scientific texts through a set of entity and semantic relation extraction sub-tasks on identifying quantity spans along with various attributes and relationships. This paper describes our system, consisting of a three-stage pipeline, that leverages pre-trained language models to extract the quantity spans in the text, followed by intelligent templates to identify units and modifiers. Finally, it identifies the quantity attributes and their relations using language models boosted with a feature re-using hierarchical architecture and multi-task learning. Our submission significantly outperforms the baseline, with the best model from the post-evaluation phase delivering more than 100% increase on F1 (Overall) from the baseline. <br> <br>
          {% include elements/button.html link="https://github.com/Ayushk4/SE-T8" text="Code" %} {% include elements/button.html link="https://aclanthology.org/2021.semeval-1.46.pdf" text="Pdf" %} {% include elements/button.html link="https://aclanthology.org/2021.semeval-1.46.bib" text="Cite" %} {% include elements/button.html link="https://ayushk4.github.io/Coming-Soon" text="Slides" %}
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
              "Basic Tools for Tokenizing Natural Language in Julia."</a>, Ayush Kaushal, Lyndon White, Mike Innes, Rohit Kumar <br>
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


    <li><a target="_blank" href="https://drive.google.com/file/d/1iNqtbP9h9d6acqpS8cw-BwzAib2Ldf3C/view?usp=sharing">
              "Towards Target Aware Twitter Stance Detection."</a>, Ayush Kaushal<br>
              <i> Bachelor's Thesis, IIT Kharagpur</i> <a style="float:right;color:#3491fe" data-toggle="collapse" data-target="#bachelorsthesis"><u>More</u></a>
      </li>
        <div id="bachelorsthesis" class="collapse" style="font-size:15px;margin:50px">
        <!-- <div align="center">
            <img id="mobile-img" src="../images/Bio-BERT.png" width="50%" border="0" height="50%" alt=""><br>
            </div> -->
            In this project, we first study the role of the target entities in detecting stance and based on our findings move towards target aware stance detection systems. We mainly analyse the various publicly available stance detection datasets on tweets. In these datasets, the text is a tweet and targets are either fixed entities or naturally occurring free-form sentences. Empirical findings show that despite the task requiring significant amount of understanding of the target being considered, one can easily achieve impressive performance by doing simple target-agnostic classification over a tweet. Specifically, we observe that a simple tweet classification model achieved near-human upper bound performance on a large scale dataset (WT-WT). These classification models can also achieve more than two-third of accuracy on 6 other Twitter stance detection datasets. Then, an analysis of some of the datasets is carried out to explain the existence of such biases in such datasets. We find some spurious correlations between tweet sentiment and stance classes. These datasets additionally have a set of lexical choices associated with their respective stance category. Consequently, we propose novel methods to augment the var ious existing stance detection dataset to inhibit target oblivious models from performing well and evaluated the dataset’s usefulness on the stance detection baseline models. With these proper benchmarks, we propose and experiment with several target aware stance detection models and show that taking into consideration, the target aware cues, the models deliver state of the art performance. Finally, we create a leaderboard for the newly created datasets and make our code, datasets and pre-trained models publicly available.
            <br> <br>
            {% include elements/button.html link="https://drive.google.com/file/d/1iNqtbP9h9d6acqpS8cw-BwzAib2Ldf3C/view?usp=sharing" text="Pdf" %} {% include elements/button.html link="https://drive.google.com/open?id=1iNqtbP9h9d6acqpS8cw-BwzAib2Ldf3C&disco=AAAAO4n2YTs" text="Code" %} {% include elements/button.html link="https://docs.google.com/presentation/d/1gZChpzpNbAcRGG6dyYhkTXHRL-WTDAz2/edit?usp=sharing&ouid=104189619769587518485&rtpof=true&sd=true" text="Slides" %} {% include elements/button.html link="https://drive.google.com/drive/folders/1FmngtkX1AJR2IAT8SPeWQYtKXVrtc0Me?usp=sharing" text="MidTerm" %}
        </div>
        <br>



    <li><a target="_blank" href="https://live.juliacon.org/talk/Z8WWNV">
              "Natural Language Processing in Julia."</a>, Ayush Kaushal <br>
              <i> 30 min Talk: JuliaCon 2020 Conference</i> <a style="float:right;color:#3491fe" data-toggle="collapse" data-target="#juliacontalk"><u>More</u></a>
      </li>
        <div id="juliacontalk" class="collapse" style="font-size:15px;margin:50px">
          The JuliaText ecosystem provides various packages for working with human languages. In this talk, I showed the usage of these JuliaText packages with Flux.jl for Natural Language Processing (NLP) with a focus on deep learning-based approaches. The attendees will gain working knowledge about how to apply the package for NLP in Julia. The talk will encompass Tokenizers, Word Embeddings, Recurrent Neural Networks and Transformer based Language models.
          <br><br>
          {% include elements/button.html link="https://github.com/Ayushk4/JuliaCon20_Talk" text="Code" %} {% include elements/button.html link="https://live.juliacon.org/talk/Z8WWNV" text="Talk" %} {% include elements/button.html link="https://www.youtube.com/watch?v=hHCi8ojazqk" text="Video" %}

        </div>
        <br>
</ul>

<h2 style="margin:50px"> Other Selected Projects </h2>

{% include projects/index.html %}

