"""Shared content for the design previews.

Every design renders from this one file, so the designs differ only in layout
and style. Facts come from the website brief (sections 3 to 6), the MegaTabICL
paper, and the current site. Anything not yet confirmed is marked TODO(owner).
"""

ME = "Ayush Kaushal"

PROFILE = {
    "name": "Ayush Kaushal",
    "pronouns": "he/him",
    "role": "PhD student, Université de Montréal and Mila",
    "lab": "CERC lab, advised by Irina Rish",
    "location": "Montreal",
    "tagline": "Efficient pretraining and scaling of foundation models that learn in context.",
}

# Paragraphs of the homepage bio (draft from the brief, with the MegaTabICL
# claims narrowed to stage 1 as the paper states them).
BIO = [
    "I'm a PhD student at Université de Montréal and Mila, advised by Irina Rish "
    "in the CERC lab. I work on making foundation-model pretraining cheap enough "
    "that its scaling behaviour can be measured, with a current focus on tabular "
    "foundation models that are meta-trained on synthetic priors and predict "
    "through in-context learning.",
    "My recent work, MegaTabICL, reproduces TabICLv2's stage-1 pretraining at "
    "3.86x lower cost on 4 H100s and trains a 1B-parameter model within the "
    "stage-1 compute of the original 28M run, which enabled a 24-model scaling "
    "study from 5M to 1B parameters. Earlier, I pretrained and studied ternary "
    "language models (Spectra, ICLR 2025 Spotlight; Spectra 1.1, ACL 2025), "
    "covering scaling laws and inference kernels.",
    "Before the PhD, I co-founded Nolano (2023 to 2026), did research at Google, "
    "and studied at UT Austin (MS) and IIT Kharagpur (B.Tech).",
]

COLLAB = (
    "I'm open to research collaborations, compute partnerships and funding around "
    "open tabular foundation models and efficient pretraining."
)

NOW = [
    ("MegaTabICL", "Presenting at the NeurIPS 2026 AXIOM workshop in Paris on Dec 13; "
                   "extending the scaling study past stage 1."),
    ("Interests", "Agents and automated research (no public work yet)."),
]

NEWS = [
    ("2026-12", "Dec 2026", "Presenting MegaTabICL at the NeurIPS 2026 AXIOM workshop, Paris (Dec 13)."),
    ("2026-09", "Sep 2026", "MegaTabICL accepted as a poster at NeurIPS 2026 AXIOM (on OpenReview since 29 Sept 2026)."),
    ("2025-08", "Aug 2025", "Started my PhD at Université de Montréal and Mila."),
    ("2025-07", "Jul 2025", "Spectra 1.1 published at ACL 2025."),
    ("2025-04", "Apr 2025", "Spectra presented as a Spotlight at ICLR 2025."),
]

# label, url (None = TODO(owner)), short handle
LINKS = [
    ("Google Scholar", None, "TODO(owner)"),
    ("GitHub", "https://github.com/ayushk4", "ayushk4"),
    ("OpenReview", "https://openreview.net/profile?id=~Ayush_Kaushal1", "~Ayush_Kaushal1"),
    ("Hugging Face", "https://huggingface.co/ayushk4", "ayushk4"),
    ("LinkedIn", "https://www.linkedin.com/in/ayushkaushal4/", "ayushkaushal4"),
    ("X", None, "TODO(owner)"),
]

THEMES = [
    ("pretraining", "Efficient pretraining and scaling"),
    ("inference", "Efficient inference and systems"),
    ("earlier", "Earlier work: understanding and evaluating language models"),
    ("opensource", "Open source"),
]

# Publications. "authors" keeps order as published; a trailing * marks equal
# contribution where the current site shows it.
PUBS = [
    {
        "id": "megatabicl", "year": 2026,
        "title": "MegaTabICL: Efficient Scaling of Tabular Foundation Model Pretraining",
        "authors": ["Ayush Kaushal", "Daria Yasafova", "Irina Rish"],
        "abbr": "NeurIPS 2026 W", "venue": "NeurIPS 2026 Workshop AXIOM: Foundations of Efficient Deep Learning",
        "note": "Poster", "selected": True, "themes": ["pretraining"],
        "links": [("OpenReview", "https://openreview.net/forum?id=WfamdVi3VV"),
                  ("PDF", "https://openreview.net/pdf?id=WfamdVi3VV"),
                  ("Code", None), ("Project", "megatabicl")],
        "abstract": (
            "Pretraining frontier Tabular Foundation Models (TFMs) such as TabICLv2 is expensive: "
            "a single 28M-parameter run costs 24.5 H100-days. This limits systematic study of their "
            "scaling behavior, architecture and synthetic priors. We find this cost stems from adopting "
            "standard pretraining practices from other modalities, whose assumptions do not hold for the "
            "TFM pretraining workload. Three mismatches stand out: heavy-tailed prior-generation compute, "
            "heterogeneous input shapes across micro-batches, and computational load concentrated in "
            "low-parameter components. We propose MegaTabICL, which exactly reproduces the TabICLv2 "
            "pretraining recipe while resolving these mismatches, together with a stabilized BF16 "
            "pretraining recipe. Focusing on stage 1, which accounts for over 80% of total pretraining "
            "cost, MegaTabICL and the BF16 recipe reproduce the reference 28M-parameter run using 4 H100s "
            "at 3.86x lower cost, and train a 1B-parameter model in less compute than that reference run "
            "required. As an initial demonstration, we pretrain 24 models spanning 5M to 1B parameters "
            "across six compute budgets. We find the compute-optimal parameter count grows with the "
            "training budget, already reaching 0.2B at TabICLv2's own stage-1 budget, since pretraining "
            "cost grows only sublinearly with parameter count. We open-source the MegaTabICL framework."),
    },
    {
        "id": "spectra11", "year": 2025,
        "title": "Scaling Laws and Efficient Inference for Ternary Language Models",
        "authors": ["Tejas Vaidhya", "Ayush Kaushal", "Vineet Jain", "Francis Couture-Harpin",
                    "Prashant Shishodia", "Majid Behbahani", "Yuriy Nevmyvaka", "Irina Rish"],
        "abbr": "ACL 2025", "venue": "ACL 2025 (Long Papers)", "note": None,
        "selected": True, "themes": ["pretraining", "inference"],
        "links": [("ACL Anthology", "https://aclanthology.org/2025.acl-long.1294/"),
                  ("PDF", "https://aclanthology.org/2025.acl-long.1294.pdf"),
                  ("arXiv", "https://arxiv.org/abs/2506.23025"),
                  ("Models", None), ("Kernels", None)],
        "abstract": None,
    },
    {
        "id": "spectra", "year": 2025,
        "title": "Spectra: Surprising Effectiveness of Pretraining Ternary Language Models at Scale",
        "authors": ["Ayush Kaushal*", "Tejas Vaidhya*", "Arnab Kumar Mondal", "Tejas Pandey",
                    "Aaryan Bhagat", "Irina Rish"],
        "abbr": "ICLR 2025", "venue": "ICLR 2025", "note": "Spotlight",
        "selected": True, "themes": ["pretraining"],
        "links": [("OpenReview", "https://openreview.net/forum?id=TJo6aQb7mK"),
                  ("PDF", "https://openreview.net/pdf?id=TJo6aQb7mK"),
                  ("arXiv", "https://arxiv.org/abs/2407.12327"),
                  ("Models", "https://huggingface.co/SpectraSuite")],
        "abstract": (
            "Rapid advancements in GPU computational power has outpaced memory capacity and bandwidth "
            "growth, creating bottlenecks in Large Language Model (LLM) inference. Post-training "
            "quantization is the leading method for addressing memory-related bottlenecks in LLM "
            "inference, but it suffers from significant performance degradation below 4-bit precision. "
            "This paper addresses these challenges by investigating the pretraining of low-bitwidth "
            "models specifically Ternary Language Models (TriLMs) as an alternative to traditional "
            "floating-point models (FloatLMs) and their post-training quantized versions (QuantLMs). We "
            "present Spectra LLM suite, the first open suite of LLMs spanning multiple bit-widths, "
            "including FloatLMs, QuantLMs, and TriLMs, ranging from 99M to 3.9B parameters trained on "
            "300B tokens. Our comprehensive evaluation demonstrates that TriLMs offer superior scaling "
            "behavior in terms of model size (in bits). Surprisingly, at scales exceeding one billion "
            "parameters, TriLMs consistently outperform their QuantLM and FloatLM counterparts for a "
            "given bit size across various benchmarks. Notably, the 3.9B parameter TriLM matches the "
            "performance of the FloatLM 3.9B across all benchmarks, despite having fewer bits than "
            "FloatLM 830M."),
    },
    {
        "id": "trilm", "year": 2024,
        "title": "TriLM vs FloatLM: Ternary LLMs are more Performant than Quantized FP16 LLMs",
        "authors": ["Ayush Kaushal", "Tejas Vaidhya", "Tejas Pandey", "Aaryan Bhagat", "Irina Rish"],
        "abbr": "ICML 2024 W", "venue": "ICML 2024 Workshop on Foundation Models in the Wild", "note": None,
        "selected": False, "themes": ["pretraining"],
        "links": [("OpenReview", "https://openreview.net/forum?id=gvaDL9omKU"),
                  ("PDF", "https://openreview.net/pdf?id=gvaDL9omKU"),
                  ("Models", "https://huggingface.co/SpectraSuite")],
        "abstract": None,
    },
    {
        "id": "lord", "year": 2024,
        "title": "LoRD: Low-Rank Decomposition of Monolingual Code LLMs for One-Shot Compression",
        "authors": ["Ayush Kaushal*", "Tejas Vaidhya*", "Irina Rish"],
        "abbr": "ICML 2024 W", "venue": "ICML 2024 Workshop on Foundation Models in the Wild", "note": None,
        "selected": False, "themes": ["pretraining"],
        "links": [("OpenReview", "https://openreview.net/forum?id=br49PQvuMp"),
                  ("PDF", "https://openreview.net/pdf?id=br49PQvuMp"),
                  ("arXiv", "https://arxiv.org/abs/2309.14021")],
        "abstract": (
            "We propose using low-rank matrix decomposition (LoRD), which splits a large matrix into a "
            "product of two smaller matrices, to compress neural network models and thereby enhance "
            "inference speed. Unlike quantization, LoRD maintains fully differentiable, trainable "
            "parameters and leverages efficient floating-point operations. We investigate its advantages "
            "for compressing Large Language Models (LLMs) for monolingual code generation, demonstrating "
            "that linear layer ranks can be reduced by up to 39.58% with less than a 1% increase in "
            "perplexity. Specifically, we use LoRD to compress the StarCoder 16B model to 13.2B "
            "parameters with no performance drop and to 12.3B parameters with minimal performance drop "
            "in the HumanEval Pass@1 score, all within 10 minutes on a single A100 GPU."),
    },
    {
        "id": "streaming", "year": 2023,
        "title": "Efficient Encoders for Streaming Sequence Tagging",
        "authors": ["Ayush Kaushal", "Aditya Gupta", "Shyam Upadhyay", "Manaal Faruqui"],
        "abbr": "EACL 2023", "venue": "EACL 2023", "note": None,
        "selected": True, "themes": ["inference"],
        "links": [("ACL Anthology", "https://aclanthology.org/2023.eacl-main.31/"),
                  ("PDF", "https://aclanthology.org/2023.eacl-main.31.pdf"),
                  ("BibTeX", "https://aclanthology.org/2023.eacl-main.31.bib")],
        "abstract": None,
    },
    {
        "id": "tokens", "year": 2022,
        "title": "What do tokens know about their characters and how do they know it?",
        "authors": ["Ayush Kaushal", "Kyle Mahowald"],
        "abbr": "NAACL 2022", "venue": "NAACL 2022", "note": None,
        "selected": False, "themes": ["earlier"],
        "links": [("PDF", "https://aclanthology.org/2022.naacl-main.179.pdf"),
                  ("Code", "https://github.com/ayushk4/character-probing-pytorch"),
                  ("arXiv", "https://arxiv.org/abs/2206.02608"),
                  ("BibTeX", "https://aclanthology.org/2022.naacl-main.179.bib")],
        "abstract": (
            "Pre-trained language models (PLMs) that use subword tokenization schemes can succeed at a "
            "variety of language tasks that require character-level information, despite lacking "
            "explicit access to the character composition of tokens. Here, studying a range of models "
            "(e.g., GPT-J, BERT, RoBERTa, GloVe), we probe what word pieces encode about character-level "
            "information by training classifiers to predict the presence or absence of a particular "
            "alphabetical character in a token, based on its embedding. We find that these models "
            "robustly encode character-level information and, in general, larger models perform better "
            "at the task."),
    },
    {
        "id": "indeprop", "year": 2022,
        "title": "INDEPROP: Information-Preserving De-propagandization of News Articles (Student Abstract)",
        "authors": ["Aaryan Bhagat*", "Faraaz Mallick*", "Neel Karia*", "Ayush Kaushal*"],
        "abbr": "AAAI 2022", "venue": "AAAI 2022 (Student Abstract)", "note": None,
        "selected": False, "themes": ["earlier"],
        "links": [("Paper", "https://ojs.aaai.org/index.php/AAAI/article/view/21594")],
        "abstract": None,
    },
    {
        "id": "causal", "year": 2021,
        "title": "Causal Direction in Data Matters: Implications of Causal and Anticausal Learning in NLP",
        "authors": ["Zhijing Jin", "Julius von Kügelgen", "Jingwei Ni", "Tejas Vaidhya", "Ayush Kaushal",
                    "Mrinmaya Sachan", "Bernhard Schölkopf"],
        "abbr": "EMNLP 2021", "venue": "EMNLP 2021", "note": None,
        "selected": False, "themes": ["earlier"],
        "links": [("PDF", "https://aclanthology.org/2021.emnlp-main.748.pdf"),
                  ("BibTeX", "https://aclanthology.org/2021.emnlp-main.748.bib")],
        "abstract": None,
    },
    {
        "id": "twtwt", "year": 2021,
        "title": "tWT–WT: Asserting the Role of Targets for Detecting Stance in Tweets",
        "authors": ["Ayush Kaushal", "Avirup Saha", "Niloy Ganguly"],
        "abbr": "NAACL 2021", "venue": "NAACL 2021", "note": None,
        "selected": False, "themes": ["earlier"],
        "links": [("PDF", "https://aclanthology.org/2021.naacl-main.303.pdf"),
                  ("Code", "https://github.com/Ayushk4/bias-stance"),
                  ("BibTeX", "https://aclanthology.org/2021.naacl-main.303.bib")],
        "abstract": None,
    },
    {
        "id": "semeval", "year": 2021,
        "title": "Multi-Staged Language Models for Extracting Measurements, their Attributes and Relations",
        "authors": ["Neel Karia*", "Ayush Kaushal*", "Faraaz Mallick*"],
        "abbr": "SemEval 2021", "venue": "SemEval 2021 at ACL-IJCNLP 2021", "note": None,
        "selected": False, "themes": ["earlier"],
        "links": [("PDF", "https://aclanthology.org/2021.semeval-1.46.pdf"),
                  ("Code", "https://github.com/Ayushk4/SE-T8")],
        "abstract": None,
    },
    {
        "id": "covid", "year": 2020,
        "title": "Leveraging Event Specific and Chunk Span features to Extract COVID Events from tweets",
        "authors": ["Ayush Kaushal", "Tejas Vaidhya"],
        "abbr": "W-NUT 2020", "venue": "W-NUT 2020 at EMNLP 2020", "note": "Oral, 1st on shared task",
        "selected": False, "themes": ["earlier"],
        "links": [("PDF", "https://aclanthology.org/2020.wnut-1.79.pdf"),
                  ("Code", "https://github.com/Ayushk4/extract_covid_entity")],
        "abstract": None,
    },
    {
        "id": "joss", "year": 2020,
        "title": "Basic Tools for Tokenizing Natural Language in Julia",
        "authors": ["Ayush Kaushal", "Lyndon White", "Mike Innes", "Rohit Kumar"],
        "abbr": "JOSS 2020", "venue": "Journal of Open Source Software, 2020", "note": None,
        "selected": False, "themes": ["opensource"],
        "links": [("Paper", "https://doi.org/10.21105/joss.01956"),
                  ("Code", "https://github.com/JuliaText/WordTokenizers.jl")],
        "abstract": None,
    },
    {
        "id": "juliacon", "year": 2020,
        "title": "Natural Language Processing in Julia",
        "authors": ["Ayush Kaushal"],
        "abbr": "JuliaCon 2020", "venue": "JuliaCon 2020, talk (30 min)", "note": None,
        "selected": False, "themes": ["opensource"],
        "links": [("Video", "https://www.youtube.com/watch?v=hHCi8ojazqk"),
                  ("Code", "https://github.com/Ayushk4/JuliaCon20_Talk")],
        "abstract": None,
    },
]

PROJECTS_OSS = [
    {
        "id": "llama-int4", "year": 2023, "title": "llama-int4-quant",
        "abbr": "Mar 2023",
        "text": ("Ran 4-bit LLaMA-7B on a MacBook CPU by adding the LLaMA architecture to ggml's "
                 "experimental 4-bit branch. Working on March 9, about a day before llama.cpp's first "
                 "release. I then archived it so development would consolidate in llama.cpp."),
        "links": [("Code", "https://github.com/NolanoOrg/llama-int4-quant")],
        "themes": ["inference", "opensource"],
    },
    {
        "id": "gsoc", "year": 2019, "title": "JuliaText packages, Google Summer of Code 2019",
        "abbr": "GSoC 2019",
        "text": "Tokenizers and NLP tooling for Julia; later mentored for GSoC, GCI and KWoC.",
        "links": [("Write-up", "/2019/08/22/My-Journey-in-Google-Summer-of-Code.html")],
        "themes": ["opensource"],
    },
]

# ---------------------------------------------------------------- MegaTabICL

MTI = {
    "title": "MegaTabICL: Efficient Scaling of Tabular Foundation Model Pretraining",
    "authors": ["Ayush Kaushal", "Daria Yasafova", "Irina Rish"],
    "venue": "NeurIPS 2026 Workshop AXIOM: Foundations of Efficient Deep Learning",
    "note": "Poster, non-archival",
    "published": "29 Sept 2026",
    "presenting": "Paris, Dec 13 2026",
    "openreview": "https://openreview.net/forum?id=WfamdVi3VV",
    "pdf": "https://openreview.net/pdf?id=WfamdVi3VV",
    "code": None,
    "tldr": ("We characterize the TFM pretraining workload to build MegaTabICL, an exact 3.86x-cheaper "
             "implementation of TabICLv2 pretraining, and use it for a first billion-parameter scaling "
             "study showing the compute-optimal parameter count growing with budget."),
    "headline": [
        ("3.86x", "lower stage-1 cost", "Reference 28M run on 4xH100: 20.96 to 5.43 H100-days."),
        ("17.35", "H100-days for 1B params", "Full 500K-step stage 1, 37x Base, below the 28M reference."),
        ("0.2B", "compute-optimal size", "At TabICLv2's own stage-1 budget, 7x its size."),
        ("24", "models, 5M to 1B", "Six budgets, one non-repeating table sequence, 27.5 H100-days in total."),
    ],
    "mismatches": [
        ("Heavy-tailed prior generation",
         "Tables are generated on CPU with median 218 ms and p99 2893 ms; 37% of attempts are rejected, "
         "using 36% of sampler time. MegaTabICL keeps several batches in generation so the slowest table "
         "no longer stalls a step."),
        ("Heterogeneous input shapes",
         "Rows and columns vary by orders of magnitude per table, which breaks compiled graphs. "
         "Shape-independent dynamic compilation, shape-agnostic attention kernels and a cost model for "
         "balancing micro-batches across ranks."),
        ("Compute in low-parameter layers",
         "The column embedder and row interactor hold under 5% of parameters but over half of step time. "
         "78% of tensors hold 2.5% of parameters, so a grouped optimizer step goes from 158.9 ms to 14.2 ms."),
    ],
    "limitations": "Stage 1 only, one seed per size, and budgets in H100-days on this implementation rather than FLOPs.",
}

# Table 1: ablation, one technique removed at a time (Base, median s/step)
ABLATION = [
    ("MegaTabICL, 1 GPU", 0.75, None, True),
    ("no dynamic shape handling", 2.45, 3.3, False),
    ("no BF16 recipe", 1.45, 1.9, False),
    ("no grouped optimizer", 0.90, 1.2, False),
    ("no prior generation pipelining", 1.70, 2.3, False),
    ("MegaTabICL, 4 GPU", 0.22, None, True),
    ("no balancing/sharding", 0.24, 1.1, False),
]

# Table 2: architecture
ARCH = {
    "cols": ["Tiny", "Base", "Medium", "Large"],
    "rows": [
        ("Embedding dim d", ["64", "128", "128", "256"]),
        ("ICL blocks", ["8", "12", "18", "24"]),
        ("d_icl", ["256", "512", "1024", "2048"]),
        ("Parameters", ["4.7M", "27.6M", "194.2M", "1027.5M"]),
    ],
}

# Table 4: speed and memory (stage 1, 500K-step projection)
# model, gpus, median s/step, mean s/step, wall days, H100-days, speedup, eff, peak GiB
SPEED = [
    ("Tiny 4.7M", 1, 0.4118, 0.4191, 2.42, 2.42, 1.00, 1.00, 3.0),
    ("Tiny 4.7M", 2, 0.2380, 0.2434, 1.41, 2.82, 1.73, 0.86, 3.0),
    ("Tiny 4.7M", 4, 0.1279, 0.1361, 0.79, 3.15, 3.22, 0.81, 3.0),
    ("Base 27.6M", 1, 0.7611, 0.7734, 4.48, 4.48, 1.00, 1.00, 9.8),
    ("Base 27.6M", 2, 0.4281, 0.4411, 2.55, 5.11, 1.78, 0.89, 10.3),
    ("Base 27.6M", 4, 0.2225, 0.2347, 1.36, 5.43, 3.42, 0.85, 10.2),
    ("Medium 194.2M", 1, 0.9954, 1.0150, 5.87, 5.87, 1.00, 1.00, 15.4),
    ("Medium 194.2M", 2, 0.5690, 0.5904, 3.42, 6.83, 1.75, 0.88, 16.6),
    ("Medium 194.2M", 4, 0.2955, 0.3116, 1.80, 7.21, 3.37, 0.84, 16.5),
    ("Large 1027.5M", 1, 2.5006, 2.5066, 14.51, 14.51, 1.00, 1.00, 50.1),
    ("Large 1027.5M", 2, 1.4083, 1.4135, 8.18, 16.36, 1.78, 0.89, 56.3),
    ("Large 1027.5M", 4, 0.7285, 0.7496, 4.34, 17.35, 3.43, 0.86, 55.3),
    ("Reference TabICLv2, Base", 1, 2.1712, 2.1669, 12.54, 12.54, 1.00, 1.00, 19.3),
    ("Reference TabICLv2, Base", 2, 1.3643, 1.3555, 7.84, 15.69, 1.59, 0.80, 19.5),
    ("Reference TabICLv2, Base", 4, 0.9009, 0.9054, 5.24, 20.96, 2.41, 0.60, 19.3),
]

# Table 6: TALENT-Tiny classification subset (28 datasets), 24 sweep checkpoints
# size, iters (K), H100-days, acc, auc, f1
SWEEP = [
    ("Tiny", 10, 0.06, 0.7983, 0.8764, 0.6583), ("Tiny", 20, 0.12, 0.7937, 0.8784, 0.6574),
    ("Tiny", 35, 0.22, 0.7937, 0.8767, 0.6576), ("Tiny", 50, 0.31, 0.7980, 0.8775, 0.6598),
    ("Tiny", 100, 0.63, 0.8015, 0.8804, 0.6664), ("Tiny", 200, 1.26, 0.8005, 0.8792, 0.6675),
    ("Base", 10, 0.11, 0.7971, 0.8762, 0.6579), ("Base", 20, 0.22, 0.8010, 0.8821, 0.6640),
    ("Base", 35, 0.38, 0.8026, 0.8866, 0.6636), ("Base", 50, 0.54, 0.8099, 0.8876, 0.6765),
    ("Base", 100, 1.09, 0.8083, 0.8875, 0.6709), ("Base", 200, 2.17, 0.8054, 0.8872, 0.6728),
    ("Medium", 10, 0.14, 0.8018, 0.8825, 0.6546), ("Medium", 20, 0.28, 0.8007, 0.8838, 0.6621),
    ("Medium", 35, 0.50, 0.8083, 0.8903, 0.6698), ("Medium", 50, 0.72, 0.8072, 0.8910, 0.6715),
    ("Medium", 100, 1.44, 0.8173, 0.8946, 0.6797), ("Medium", 200, 2.88, 0.8183, 0.8951, 0.6853),
    ("Large", 10, 0.35, 0.8010, 0.8802, 0.6546), ("Large", 20, 0.70, 0.8058, 0.8887, 0.6694),
    ("Large", 35, 1.22, 0.8110, 0.8914, 0.6736), ("Large", 50, 1.74, 0.8069, 0.8921, 0.6672),
    ("Large", 100, 3.47, 0.8150, 0.8942, 0.6828), ("Large", 200, 6.94, 0.8193, 0.8966, 0.6811),
]
SWEEP_REF = ("Official TabICLv2 (500K steps + stages 2 and 3)", 24.5, 0.8238, 0.8990, 0.6998)
SIZES = [("Tiny", "4.7M"), ("Base", "27.6M"), ("Medium", "194.2M"), ("Large", "1.03B")]
