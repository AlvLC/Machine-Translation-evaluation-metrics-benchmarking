# Machine-Translation-evaluation-metrics-benchmarking

This repository is the product of a Master's thesis for the "Master in Fundamental Principles of Data Science" (UB), supervised by [Jordi Vitrià](https://algorismes.github.io/). The thesis will be available soon as a [PDF](link-to-pdf) and the slides [presentation slides](link-to-slides) will also be provided.

This thesis endeavors to cast a spotlight on the evolution and applicability of machine
translation (MT) evaluation metrics and models, mainly contrasting statistical
methods against the more contemporary neural-based ones, where we also give
special attention to the exciting modern Large Language Models (LLMs). MT, a significant
area in Natural Language Processing (NLP), has seen a vast metamorphosis
over the years, bringing into focus the critical need for thorough exploration of these
evolving systems.

Our research is anchored on the Digital Corpus of the European Parliament
(DCEP), a complex and multilingual corpus that makes it an ideal testbed to benchmark
MT models given its comprehensive and diversified linguistic data. Through
the use of this extensive corpus, we aim to present a comprehensive benchmarking
of various selected MT models, encapsulating not just their evolution but also their
performance dynamics across different tasks and contexts.
A vital facet of our study includes evaluating the relevance and reliability of various
MT metrics, such as the old BLEU, METEOR, CHRF, along with newer neural-based
metrics which promise to capture semantics more effectively. We aim to uncover
the inherent strengths and limitations of these metrics, consequently guiding
the choice of appropriate metrics for specific MT contexts for future practitioners
and researchers.

In this repository, you can find a collection of Jupyter/Colab/Databricks notebooks, as well as some simple python scripts, which intend to evaluate a number of selected translation models with several interesting metrics. For this benchmarking process, a [preprocessing step of our Corpus](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/DCEP_PROCESSING/README2.md) is required to get all the alligned pairs of source and reference sentences needed to perform our tasks. Once done, you can find all the relevant code in the following, in order to translate, process, evaluate and plot the results of these models and metrics. For further analysis and documentation, review the [project](link-to-pdf) when available and feel free to [contact me](https://github.com/AlvLC).

## Translations

1. [Colab Notebook with the implementation of flan-t5-base](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/colab_FLAN-T5_translation.ipynb)
2. [Jupyter Notebook with the implementation of gpt-3.5-turbo (ChatGPT)](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/gpt-35-turbo_translation.ipynb)
3. [Databricks Notebook with the implementation of the Azure Cognitive Services Translator](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/databricks_azure_translation.ipynb)

## Postprocessing of txt files

1. [Jupyter Notebook with the postprocessing of flan-t5-base outputs (hypothesis and references)](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/postprocess_flant5.ipynb)
2. [Jupyter Notebook with the postprocessing of gpt-3.5-turbo outputs (hypothesis and references)](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/postprocess_gpt_dict.ipynb)
3. [Jupyter Notebook with the postprocessing of Azure CST outputs (hypothesis and references)](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/postprocess_azure.ipynb)

## Metrics implementations and models evaluation
1. [Colab Notebook with the evaluation of flan-t5-base outputs with a series of implementations of our selected metrics](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/colab_flant5_metrics_evaluations.ipynb)
2. [Colab Notebook with the evaluation of gpt-3.5-turbo outputs with a series of implementations of our selected metrics](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/colab_gpt_metrics_evaluations.ipynb)
3. [Colab Notebook with the evaluation of Azure CST outputs with a series of implementations of our selected metrics](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/colab_azure_metrics_evaluations.ipynb)

## Plots
1. [Jupyter Notebook with the final plots and comparisons](https://github.com/AlvLC/Machine-Translation-evaluation-metrics-benchmarking/blob/main/plots.ipynb)
