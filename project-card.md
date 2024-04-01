<!-- Use this template to record details on both the dataset and model (if necessary) for any data science projects at Cybera

For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1

Doc / guide: https://huggingface.co/docs/hub/model-cards 
-->

# Project Card for Ookla / StatCan Analysis

<!-- Provide a quick summary of the project, it's purpose. -->

Dataset card required? [yes]
<!-- If not including dataset card, include justification here and remove dataset card section -->

Model card required? [no]
<!-- If not including model card, include justification here and remove model card section -->

This repository holds only the data to do comparisons between the Ookla dataset (provided) and the [Statistics Canada National Broadband Internet Service Availability Map](https://ised-isde.canada.ca/app/scr/sittibc/web/bbmap?lang=eng#!/map). Other than wrangling the data and combining it in different ways, no machine learning model (and certainly no _advanced_ model) is used.

<!-- Begin dataset card section -->

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is and where it originated. -->

- **Curated by:** [Cybera, Inc](https://www.cybera.ca/)
- **Funded by [optional]:** [Ookla](https://www.ookla.com/ookla-for-good/open-data)
- **Shared by [optional]:** [Cybera Data Science team](https://www.cybera.ca/data-science/)
- **Language(s) (NLP):** English (w/ French province and territory names)
- **License:** CC BY-NC-SA 4.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** https://registry.opendata.aws/speedtest-global-performance/
- **Paper [optional]:** N/A
- **Demo [optional]:** [Tutorials available on Github](https://github.com/teamookla/ookla-open-data?tab=readme-ov-file#tutorials)

## Uses

<!-- Address questions around how the dataset is intended to be used, both in this project and in general. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

Ookla makes this dataset available to the public in the service of open data, focusing on fixed broadband and mobile network connectivity and performance. For Cybera's use case, of special interest is the use of this dataset in relation to the [Canadian Radio-television and Telecommunications Commission's](https://crtc.gc.ca/eng/internet/internet.htm) goal of 50/10 Mbps connectivity across Canada.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. This is also the place to note and address any controversy surrounding the dataset that may have been in the enws. -->

There are significant and valid questions about how the data is collected, and the need for careful statistical analysis. Any conclusions drawn should make readers aware of the underlying method of sampling and how to communicate findings.

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

## Project Card Authors

<!-- Author of the dataset card (from Cybera) and/or author(s) if much of the information was copied from pre-existing cards -->

## Project Card Contact

<!-- Unless otherwise specificed, this could simply be datascience@cybera.ca -->