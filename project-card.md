<!-- Use this template to record details on both the dataset and model (if necessary) for any data science projects at Cybera

For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1

Doc / guide: https://huggingface.co/docs/hub/model-cards 
-->

# Project Card for [project name]

<!-- Provide a quick summary of the project, it's purpose. -->

Dataset card required? [yes|no]
<!-- If not including dataset card, include justification here and remove dataset card section -->

Model card required? [yes|no]
<!-- If not including model card, include justification here and remove model card section -->

<!-- Begin dataset card section -->

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is and where it originated. -->

- **Curated by:**
- **Funded by [optional]:** 
- **Shared by [optional]:**
- **Language(s) (NLP):**
- **License:**

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:**
- **Paper [optional]:**
- **Demo [optional]:**

## Uses

<!-- Address questions around how the dataset is intended to be used, both in this project and in general. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. This is also the place to note and address any controversy surrounding the dataset that may have been in the enws. -->

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

## Dataset Creation

<!-- Much of the information here can be copied (with attribution and URLs) from the source repository -->

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

### Annotations [optional]

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. If no annotations, this section can be removed. -->

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. Names or organizations are both acceptable -->

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations, as well as any concerns about how the data might be biased and any efforts taken to mitigate it. -->

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations beyond those actions taken by the creators of the dataset (if external). -->

## Citation [optional]

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**


**APA:**


## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->


## More Information [optional]

<!-- Use this section to capture any information that you deem relevant that hasn't been included elsewhere, such as concerns with the dataset (or similar datasets) and efforts taken to ensure due diligence has been done on our end -->

<!-- This ends the dataset section -->

<!-- This starts the model card section -->

# Model Card
<!-- For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1

Doc / guide: https://huggingface.co/docs/hub/model-cards -->


## Model Details

<!-- Provide a quick summary of what the model is/does. -->

### Model Description

<!-- Provide a longer summary of what this model is. On most occasions, the model will have been developed elsewhere and this information can be copied (with attribution and URL where necessary) from the original source 

If using a model card alongside a dataset card, many of the redundant fields in this section can refer back to the relevant sections in the dataset card -->


- **Developed by:**
- **Funded by [optional]:**
- **Shared by [optional]:**
- **Model type:**
- **Language(s) (NLP):**
- **License:**
- **Finetuned from model [optional]:**

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:**
- **Paper [optional]:**
- **Demo [optional]:**

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. For concerns about the data used to generate the model, refer back to the datacard section -->

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

## How to Get Started with the Model

<!-- Many pre-existing models will have a 'Quickstart' or 'Get Started' guide that will contain code to download the model and run a quick demo. That can be copied into a code cell here -->

Use the code below to get started with the model.

## Training Details

<!-- If most or all of the information in this section is already described either elsewhere in this document or on the website of the original repository, sections can be quoted from it and linked to  -->

### Training Data

<!-- For entries in this section that have already been addressed by the corresponding fields in the dataset card, they can be referred to in text, with optional comment -->

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]

<!-- If the data was modified between its appearance in the original dataset and the model, note those changes here -->

#### Training Hyperparameters

- **Training regime:** <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

<!-- If the model is available in different sizes, note which one was used here -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

#### Summary

<!-- Summarize the model and its use -->

## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly

<!-- Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700 -->

- **Hardware Type:**
- **Hours used:**
- **Cloud Provider:**
- **Compute Region:**
- **Carbon Emitted:**

## Technical Specifications [optional]

<!-- Use this section to describe the model (to the best of the available knowledge) -->

### Model Architecture and Objective

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

**APA:**

## More Information [optional]

<!-- Any additional information not covered in the previous sections -->

<!-- This ends the model card section -->

## Project Card Authors

<!-- Author of the dataset card (from Cybera) and/or author(s) if much of the information was copied from pre-existing cards -->

## Project Card Contact

<!-- Unless otherwise specificed, this could simply be datascience@cybera.ca -->