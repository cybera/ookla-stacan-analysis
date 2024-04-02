<!-- Use this template to record details on both the dataset and model (if necessary) for any data science projects at Cybera

For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1

Doc / guide: https://huggingface.co/docs/hub/model-cards 
-->

# Project Card for Ookla / StatCan Analysis

<!-- Provide a quick summary of the project, it's purpose. -->

The repository here contains the code necessary to setup an environment and download the data to investigate internet speed data across Canada. Though the code has been written by Cybera data scientists, the data itself comes from [Ookla](https://www.ookla.com/), who make internet speed test data available for anyone interested in investigating, as well as [Statistics Canada (StatsCan)](https://www.statcan.gc.ca/en/start), who maintain datasets on numerous topics related to Canada. The Ookla dataset provides information about internet speed and access, where the StatsCan data provides context in the form of data about populations, drawn from census data (2016).

##### Note: it is not uncommon for links to StatsCan pages to rot over time. Curators of this repository endeavour to keep this information current, but no guarantees can be given.

Once the datasets are downloaded they are aggregated and visualized to make analysis more meaningful. Though the data is necessarily transformed as part of this process, references in this document refer to the raw data and may not be able to be perfectly extrapolated to the combined data. To that end, the Project Card here largely reflects the information available on the Ookla and StatsCan websites, and references specific sections where nrecessary.

Dataset card required? [yes]
<!-- If not including dataset card, include justification here and remove dataset card section -->

Model card required? [no]
<!-- If not including model card, include justification here and remove model card section -->

This repository holds only the data to do aggregations between the Ookla dataset and the StatsCan census data, similar to the [Statistics Canada National Broadband Internet Service Availability Map](https://ised-isde.canada.ca/app/scr/sittibc/web/bbmap?lang=eng#!/map). Other than wrangling the data and combining it in different ways, no machine learning model (and certainly no _advanced_ model) is used.

<!-- Begin dataset card section -->

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is and where it originated. -->

- **Curated by:** [Cybera, Inc](https://www.cybera.ca/)
- **Funded by [optional]:** [Ookla](https://www.ookla.com/ookla-for-good/open-data); [StatsCanada](https://www.statcan.gc.ca/en/about/statcan?MM=1)
- **Shared by [optional]:** [Cybera Data Science team](https://www.cybera.ca/data-science/)
- **Language(s) (NLP):** English (w/ French province and territory names)
- **License:** CC BY-NC-SA 4.0

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

#### Ookla
- **Repository:** https://registry.opendata.aws/speedtest-global-performance/
- **Paper [optional]:** N/A
- **Demo [optional]:** [Tutorials available on Github](https://github.com/teamookla/ookla-open-data?tab=readme-ov-file#tutorials)

#### StatsCan
- **Repository:** https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2016-eng.cfm
- **Paper [optional]:** N/A
- **Demo [optional]:** N/A

## Uses

<!-- Address questions around how the dataset is intended to be used, both in this project and in general. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

Ookla makes this dataset available to the public in the service of open data, focusing on fixed broadband and mobile network connectivity and performance. For Cybera's use case, of special interest is the use of this dataset in relation to the [Canadian Radio-television and Telecommunications Commission's](https://crtc.gc.ca/eng/internet/internet.htm) goal of 50/10 Mbps connectivity across Canada.

StatsCan makes significant amounts of data available through their website, with no suggestion of how the data is to be used, other than suggestions on limitations. For our purposes, the goal is to compare against Ookla data by adding information about demographics and regions.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. This is also the place to note and address any controversy surrounding the dataset that may have been in the enws. -->

There are significant and valid questions about how the data is collected, and the need for careful statistical analysis. Any conclusions drawn should make readers aware of the underlying method of sampling and how to communicate findings.

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->


#### Ookla
The Ookla dataset is organized into folders representing quarters (Q1-Q4) from 2019 through latest full quarter (Q4 2023 as of writing), each folder containing a single zip file with four files inside.

Four different raw filetypes are present within the zip (.dbf, .prj, .shp, .shx), all geo datatypes that can be reconstructed to form maps with the below fields (and more in newer updates of the dataset):
- `quadkey`: Identifier for the tile used to map the data, and where the remaining fields pertain to
- `avg_d_kbps`: Average download speed in kbps
- `avg_u_kbps`: Average upload speed in kbps
- `avg_lat_ms`: Average latency in ms
- `tests`: Number of tests conducted per tile
- `devices`: Number of unique devices on which tests were conducted

More information on attributes [here](https://github.com/teamookla/ookla-open-data?tab=readme-ov-file#tile-attributes) or file formats [here](https://github.com/teamookla/ookla-open-data?tab=readme-ov-file#data-formats)

#### StatsCan
Similar to Ookla, StatsCan data contains the same four filetypes needed to reconstruct maps, but with census information instead of internet performance. Also included in the StatsCan zip file data is a technical PDF with more details on the features, and a more in-depth [data dictionary](https://www12.statcan.gc.ca/census-recensement/2016/ref/dict/index-eng.cfm) is provided online to search any terms necessary.

## Dataset Creation

<!-- Much of the information here can be copied (with attribution and URLs) from the source repository -->

Information availale from [Ookla Github](https://github.com/teamookla/ookla-open-data?tab=readme-ov-file#about), or [StatsCan](https://www12.statcan.gc.ca/census-recensement/2016/ref/index-eng.cfm) regarding census data

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

Rationale from [Ookla for Good](https://www.ookla.com/ookla-for-good).

[Census data](https://en.wikipedia.org/wiki/Census_in_Canada) is collected by the Canadian government via StatsCan every five years, and results are slowly released up to two years following the year of collection. Demographic and population statistics are only some of vast amounts of data collected from the census.

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

Ookla ata was collected from devices conducting speed tests at https://www.speedtest.net/.

StatsCan data is derived from survey responses from Canadians (or their families) from past years.

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

Ookla data is collected and aggregated monthly, as per Ookla's notes [here](https://github.com/teamookla/ookla-open-data?tab=readme-ov-file#update-cadence). Data will routinely be updated to remain in compliance with privacy legislation from different areas of the world, such as GDPR, so fidelity cannot be guaranteed if accessing at different times.

StatsCan data is collected every five years, and released two years following (i.e. data from the 2016 census is released as late as 2018). The data is anonymized and aggregated so as to remove any personal identifiable information (PII).

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

The data is collected from any user who utilizes Ookla's speed test website (as mentioned above in [Source Data](#source-data)); census data is collected by StatsCan

### Annotations [optional]

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. If no annotations, this section can be removed. -->

N/A

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

N/A

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. Names or organizations are both acceptable -->

N/A

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

Though the Ookla information here is collected from individuals who visit the speed test website, the fields contained in this dataset pertain to internet speeds and geographic data only, which cannot on their own be attached to any single individual. As the data is aggregated in tiles, which are as large as 610x610m at the equator (as per [Github](https://github.com/teamookla/ookla-open-data?tab=readme-ov-file#tiles)), no personally identifiable geographic information is present either.

The subset of census data used from StatsCan contains well-established geographic boundaries and count data of those regions. No PII is present.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations, as well as any concerns about how the data might be biased and any efforts taken to mitigate it. -->

Though there are no biases and risks as they pertain to the people on which this data is collected, there are arguments to be made that the method of collection may introduce a sampling bias. For example, it's rare for people who are not experiencing performance issues with their internet service to seek speed tests, nor should it be expected that a certain level of internet speed is guaranteed anywhere. Any analysis of these issues should be aware of the limitations of generalizing findings.

Census data has a much higher confidence in how its collected, as it's arguably the most important data that StatsCan collects. More information on the Canada census can be found on the StatsCan page [here](https://www.statcan.gc.ca/en/census/census-engagement/about).

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations beyond those actions taken by the creators of the dataset (if external). -->

Any statistical analysis should be aware of sampling bias, the disparity of speeds even within the same tile, and these concerns should be clearly stated alongside reported findings.

## Citation [optional]

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

See [citation card](CITATION.cff) or widget for Cybera citation.

Ookla citation:
```
Speedtest® by Ookla® Global Fixed and Mobile Network Performance Maps was accessed on 1 April, 2024 from AWS. Based on Cybera, Inc's analysis of Speedtest® by Ookla® Global Fixed and Mobile Network Performance Maps for Q1 2019 to Q4 2023. Ookla trademarks used under license and reprinted with permission.

StatsCan:
Statistics Canada. (2019). 2016 Census - Boundary files. https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2016-eng.cfm
```

**BibTeX:**

```
@software{Cybera_Ookla_Open_Data_2024,
author = {{Cybera, Inc}},
license = {CC-BY-NC-SA-4.0},
month = apr,
title = {{Ookla Open Data and Statistics Canada Internet Analysis}},
url = {https://github.com/cybera/ookla-statcan-analysis},
year = {2024}
}
```

**APA:**

Cybera, Inc. (2024). Ookla Open Data and Statistics Canada Internet Analysis [Computer software]. https://github.com/cybera/ookla-statcan-analysis

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->

N/A


## More Information [optional]

<!-- Use this section to capture any information that you deem relevant that hasn't been included elsewhere, such as concerns with the dataset (or similar datasets) and efforts taken to ensure due diligence has been done on our end -->

<!-- This ends the dataset section -->

N/A

## Project Card Authors

<!-- Author of the dataset card (from Cybera) and/or author(s) if much of the information was copied from pre-existing cards -->

Jordan Swanson (Cybera, Inc)

## Project Card Contact

<!-- Unless otherwise specificed, this could simply be datascience@cybera.ca -->

For more information on project cards and other efforts to improve transparency and responsibility surrounding artificial intelligence and data, check out our [Wiki page](https://wiki.cybera.ca/display/DS/Artificial+Intelligence+and+Data+Resources)

Contact Cybera at datascience@cybera.ca