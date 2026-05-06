<!--

<table style="width: 100%; border-collapse: collapse; margin: auto;">
  <tbody>
    <tr>
      <td style="border: 0px"> <a href="/M2/main.md"><nobr><- Previous module</nobr></a> </td>
      <td style="width: 50%; border: 0px"> </td>
      <td style="border: 0px"> <a href="/SUMMARY.md"><nobr>GAPS Summary</nobr></a> </td>
      <td style="width: 50%; border: 0px"></td>
      <td style="border: 0px"> <a href="/M4/main.md"><nobr>Next module -></nobr></a> </td>
    </tr>
  </tbody>
</table>


-->

<div align="center"><nobr>

[← Previous module](/M2/main.md) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
[GAPS Summary](/SUMMARY.md) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
[Next module →](/M4/main.md)

</nobr></div>

---

![GAPS logo](../GAPS-logo.png)


# Module 3 - Preparing research artifacts

<!-- MendezEtAl2020 -->
The major challenge that keeps researchers from following all the open science practices described above is probably the difficulty and effort required when making everything openly available. All the practices constitute additional steps that researchers have to do in addition to the non-open research process. They might be motivated to do these additional steps to support the scientific process and higher visibility of open publications. Yet, this motivation has limits. Therefore, the ease of doing open science practices is essential. For this reason, this module address aspects of preparing and sharing research artifacts.

<!-- MendezEtAl2020 -->
A well-known challenge that might keep researchers from employing openness in their research is the area of conflict between anonymity and confidentiality on the one side and openness on the other. In open science, we ideally would like to make everything open that helps others to understand, verify, and build on our work. When we work with companies, however, they have an understandable interest to protect their intellectual property and reputation, often reflected in signed nondisclosure agreements. Therefore, we have to reduce the data that we can make open or anonymize the data that we have. This is, again, additional effort and a risk that we accidentally make something open that should be confidential. Similarly, when our studies involve humans, they have an interest in protecting their private data. In both cases, companies and individual humans, it is therefore imperative to publish any potentially sensitive data only with the explicit consent of the study participants. Only they themselves can decide what is sensitive and critical for them. In principle, this holds for any kind of publication and, hence, only needs to be extended to ask for consent for publishing the data as well.

<!-- MendezEtAl2020 - -->
In practice, not all research data can be made openly available, especially when dealing with sensitive or confidential information. In such cases, researchers often rely on a shadow repository that stores the original raw data under restricted access. Before sharing artifacts publicly, the data must be carefully filtered, anonymized, or transformed to ensure that no sensitive information is disclosed. This separation allows researchers to balance transparency with ethical and legal constraints.




## Data curation

The value of shared data depends on quality of its documentation. Simply placing a data set online somewhere, without any explanation of its content, structure, and origin, is of limited value. A critical aspect of Open Data is ensuring that research data are findable (in a certified repository) as well as clearly documented by meta-data and process documents. <!-- ZeeReich2018 -->

Research data should be prepared and curated in a way that facilitates understanding, reuse, and long-term accessibility. This includes selecting appropriate file formats, documenting the data thoroughly, and clearly defining how the data can be accessed. <!-- Survey2026 -->

Whenever possible, data should be provided in widely supported and open formats (e.g., CSV, JSON, or Markdown), which reduce technical barriers and improve interoperability. In addition to the data itself, artifacts should include sufficient contextual information to support interpretation, such as descriptions of the data structure, provenance, collection procedures, and any relevant ethical or legal considerations. <!-- Survey2026 -->

In cases where the full dataset cannot be made publicly available, researchers should still aim to maximize transparency. This can be achieved by sharing rich metadata that describes the dataset in detail, allowing others to understand its scope and characteristics before requesting access. When only metadata is shared, it is important to clearly explain how and under which conditions the full dataset can be accessed. <!-- Survey2026 -->

When working with sensitive or confidential data, it is often necessary to maintain a private repository containing the original raw data. In such cases, a filtered or anonymized version of the dataset can be prepared for public release. Researchers should clearly document the transformations applied to the data and explain how the shared version differs from the original dataset. <!-- Survey2026 -->

Finally, care must be taken to ensure that no shared data violates confidentiality agreements or ethical constraints. Established anonymization techniques should be applied where appropriate, and all decisions regarding data sharing should be aligned with consent agreements and legal requirements. <!-- Survey2026 -->

In case research data cannot be shared at all, due to privacy issues or legal requirements, it is typically still possible to at least share meta-data: information about the scope, structure, and content of the data set. In addition, researchers can share “process documents,” which outline how, when, and where the data were collected and processed. In both cases (meta-data and process documentation), transparency can be increased even when the research data themselves are not shared. <!-- ZeeReich2018 -->

Perhaps the strongest objection to Open Data sharing concerns issues of privacy protection. Safeguarding the identity and other valuable information of research participants is of utmost importance and takes priority over data sharing, but these are not mutually exclusive endeavors. Sharing data is not a binary decision, and there is a growing body of research around differential privacy that suggests a variegated approach to data sharing <!-- ZeeReich2018 -->

Even when a data set cannot be shared publicly in its entirety, it may be possible to share deidentified data or, as a minimum, information about the shape and structure of the data (i.e., meta-data). <!-- ZeeReich2018 -->

Even when a whole data set cannot be shared, subsets might be sharable to provide more insight into coding techniques or other analytic approaches. Privacy concerns should absolutely shape decisions about what researchers choose to share, and researchers should pay particular attention to implications for informed consent and data collection practices, but research into differential privacy shows that openness and privacy can be balanced in thoughtful ways. <!-- ZeeReich2018 -->


Many datasets containing participant-level private information can be shared once the dataset has been de-identified (Safe Harbor method) or a expert has determined that the dataset is not individually identifiable (Expert Determination method). <!-- SonjaEtAl2018 -->
However, some datasets cannot be safely de-identified and shared. Researchers can still improve the openness of research on such data by creating and sharing synthetic data. Synthetic data is similar in structure, content, and distribution to the real data and aims to attain "analytic validity": statistical analysis will return the same results for the synthetic data as the real data. <!-- SonjaEtAl2018 -->
As mentioned above, the ultimate goal of data sharing your research data is to make them maximally reusable. To that end, before sharing your data you should manage them according to best practice. This includes, i.a., documentation and the choice of open file formats and licenses. <!-- SonjaEtAl2018 -->



### Qualitative data

<!-- MendezEtAl2020 -->
Achieving replicability and reproducibility of qualitative studies is particularly challenging and many might argue that it is not possible at all. This renders, however, the disclosure of qualitative data not less important than the disclosure of quantitative data. Even if we cannot support reproducibility of qualitative studies in the nearer sense (if interpreting those terms literally), we can at least achieve transparency of the research and support researchers not involved in the study in understanding how the researchers carrying out the study have drawn their conclusions. Qualitative data is usually the most difficult to prepare for disclosure in a replication package, because it is most personal and most difficult to anonymize within legal and ethical constraints. A number is more abstract (and easier to open) than spoken words spoken (and transcribed) by individuals, e.g., during an interview. Ideally, we anonymize also qualitative data7 and publish it with the explicit consent of the participants. It is important to be open about it upfront to understand whether the participants will agree. When it is not possible to get the consent, it is even more important that at least the analysis material is shared. This is typically easier to share and may include a study protocol as well as the coding schema and coding rules used when coding qualitative data (e.g., as part of a Grounded Theory study). That way, reviewers and other researchers can at least check the trustworthiness of the analysis process and understand how the authors have drawn their conclusions.

<!-- MendezEtAl2020 -->
By anomymisation of qualitative data we refer to the removal of any information that allows to reveal the individuals' identities and/or otherwise sensitive not directly related to the study.


## Sensitive vs shareable data

Ethics are an integral part of a research project, from the conceptual stage of the research proposal to its completion. Many research funders and journals expect or require data sharing (i.e., making data available in a repository). However, especially when dealing with personal or sensitive data, there is often a tension between openness and data protection. <!-- = CESSDA -->

According to the Brazilian General Data Protection Law (LGPD - *Lei Geral de Proteção de Dados Pessoais* - Law No. 13,709/2018), personal data refers to any information related to an identified or identifiable natural person. Sensitive personal data includes information about racial or ethnic origin, religious beliefs, political opinions, trade union membership, health or sexual life, and genetic or biometric data when linked to an individual. These categories require special care when handling and sharing data.

Ethical review processes help researchers anticipate and address such concerns. Research Ethics Committees (RECs) play a key role in protecting participants' rights, safety, and well-being, ensuring that studies comply with applicable data protection regulations and ethical standards. <!-- CESSDA -->

In practice, deciding what can be shared requires balancing transparency with the protection of sensitive information. Not all data collected during a study should be made publicly available. When data contain personal, confidential, or proprietary information, researchers should assess whether the data can be safely shared in full, partially shared, or only described through metadata.  <!-- Survey2026 -->

When full sharing is not possible, alternative strategies should be adopted. These include providing detailed metadata, sharing aggregated or transformed data, or offering controlled access under specific conditions. In such cases, it is essential to clearly document data availability, including how and under which conditions access can be granted. <!-- Survey2026 -->

A common approach is to separate the original raw data from the shareable version. The raw data can be maintained in a restricted repository, while a filtered or anonymized version is prepared for public release. Researchers should explicitly document the differences between these versions and justify any omissions or transformations applied to the data. <!-- Survey2026 -->



## Anonymization strategies

In practice, research participants may provide information that can lead to their identification, either directly or indirectly. This can happen because the data collection instrument encourages detailed responses, or unintentionally when participants reveal specific characteristics that distinguish them from others. Such details may include gender (e.g., being a woman in a predominantly male context), occupation (e.g., working in a small company), age (e.g., belonging to a rare age group), location, religion, or other attributes that, when combined, may enable re-identification.

Anonymization refers to the process of removing or transforming any information that could allow observations to be traced back to individuals. This process should not be treated as a final step performed only before publication, but rather as a systematic activity integrated throughout the research lifecycle. <!-- MendezEtAl2020 - ->

Before sharing data, researchers should assess which elements of the dataset may directly or indirectly identify participants or organizations. Personal data can be disclosed through two main types of identifiers. **Direct identifiers** (e.g., names, addresses, phone numbers) explicitly identify individuals. **Indirect identifiers** (e.g., occupation, age, location) may not identify someone on their own, but can do so when combined with other information. <!-- CESSDA -->

Based on this assessment, appropriate anonymization strategies should be applied. These may include removing identifiers, replacing them with pseudonyms, or generalizing and aggregating values to reduce the risk of re-identification. In some cases, the best way to protect privacy is to avoid collecting certain identifiable information in the first place.

It is important to distinguish anonymization from pseudonymization. Anonymization irreversibly removes any possibility of identifying individuals. In contrast, pseudonymization replaces identifying information with artificial identifiers, but allows re-identification if additional information is available and securely stored separately. For this reason, pseudonymized data should still be treated as sensitive.

In practice, anonymization often results in a shareable version of the dataset that differs from the original raw data. Maintaining a clear separation between these versions, keeping the original data securely stored and sharing only the anonymized version, helps balance transparency with ethical and legal constraints. This process should be carefully documented to ensure clarity about how the data were transformed.

Finally, anonymization may reduce the level of detail available in the data, which can impact its potential for reuse. Researchers should therefore aim to preserve as much analytical value as possible while ensuring that participants' confidentiality is not compromised.




### Sharing quantitative data
<!-- = CESSDA -->

Best practices for anonymizing quantitative data: <!-- = CESSDA -->

- This may involve removing or aggregating variables or reducing the precision or detailed textual meaning of a variable.
- Aggregate or reduce the precision of a variable such as age or place of residence. As a general rule, report the lowest level of geo-referencing that will not potentially breach respondent confidentiality.
- Generalise the meaning of a detailed text variable by replacing potentially disclosive free-text responses with more general text.
- Restrict the upper or lower ranges of a continuous variable to hide outliers if the values for certain individuals are unusual or atypical within the wider group researched.


<!-- <!-- MendezEtAl2020 Anonymising company names is often enough. For anonymising sensitive data of study participants, there are also established techniques (see, e.g., Saunders et al. 2015). -->



### Sharing qualitative data

Achieving replicability and reproducibility of qualitative studies is particularly challenging and many might argue that it is not possible at all. This renders, however, the disclosure of qualitative data not less important than the disclosure of quantitative data. Even if we cannot support reproducibility of qualitative studies in the nearer sense (if interpreting those terms literally), we can at least achieve transparency of the research and support researchers not involved in the study in understanding how the researchers carrying out the study have drawn their conclusions.  <!-- == MendezEtAl2020 -->

Qualitative data is usually the most difficult to prepare for disclosure in a replication package, because it is most personal and most difficult to anonymize within legal and ethical constraints. A number is more abstract (and easier to open) than spoken words spoken (and transcribed) by individuals, e.g., during an interview.  <!-- == MendezEtAl2020 -->

Ideally, we anonymize also qualitative data and publish it with the explicit consent of the participants. It is important to be open about it upfront to understand whether the participants will agree. Especially for qualitative data, it might often not be the case that we get the consent. Then, it is even more important that at least the analysis material is shared. This is typically easier to share and may include a study protocol as well as the coding schema and coding rules used when coding qualitative data (e.g., as part of a Grounded Theory study). That way, reviewers and other researchers can at least check the trustworthiness of the analysis process and understand how the authors have drawn their conclusions. <!-- == MendezEtAl2020 -->

7 By anomymisation of qualitative data we refer to the removal of any information that allows to reveal the individuals’ identities and/or otherwise sensitive not directly related to the study.
<!-- == MendezEtAl2020 -->

Many datasets containing participant-level private information can be shared once the dataset has been de-identified (Safe Harbor method) or a expert has determined that the dataset is not individually identifiable (Expert Determination method). Consult with your Research Ethics Board / Institutional Review Board to learn how to do this with your data.  <!-- = SonjaEtAl2018 -->



Best practices for anonymizing qualitative data: <!-- = CESSDA -->

- Using pseudonyms or generic descriptors to edit identifying information, rather than blanking-out that information.
- Plan anonymization at the time of transcription or initial write-up, (longitudinal studies may be an exception if relationships between waves of interviews need special attention for harmonised editing).
- Use pseudonyms or replacements that are consistent throughout the research team and the project. For example, using the same pseudonyms in publications and follow-up research;
- Use "search and replace" techniques carefully so that unintended changes are not made, and misspelt words are not missed.
- Identify replacements in text clearly, for example with `[brackets]` or using XML tags such as `<seg>word to be anonymized</seg>`.
- Create an anonymization log (also known as a de-anonymization key) of all replacements, aggregations or removals made and store such a log securely and separately from the anonymized data files.




### Examples of anomymization methods 
 <!-- = CESSDA -->

Identifiers are classified as:
- **Direct identifiers**: uniquely identify an individual.
- **Strong indirect identifiers**: can identify someone when combined with other data.
- **Indirect identifiers**: may contribute to identification in combination with other attributes.

The anonymization methods include:
- **Remove**: delete the information.
- **Change**: replace with pseudonyms.
- **Categorise**: generalise or group values (e.g., age ranges instead of exact age).

 <!-- = CESSDA - -> <!-- FSD -->
| Identifier type | Direct identifier | Strong indirect identifier | Indirect identifier | Anonymization method |
| --- | :---: | :---: | :---: | :---: |
| Personal identification number (e.g., Passport number, RG, CPF) | x   |     |     | Remove |
| Full name | x   |     |     | Remove/Change |
| Email address | x   | x   |     | Remove |
| Address       | x   |     |      | Remove |
| Phone number |     | x   |     | Remove |
| Postal code (CEP) |     |     | x   | Remove/Categorise |
| City |     |     | x   | Categorise |
| State |     |     | x   | Categorise |
| Audio recording (voice) | x   |     |     | Remove |
| Video recording displaying person(s) | x   |     |     | Remove |
| Photograph of person(s) | x   |     |     | Remove |
| Data/Year of birth |     | x   |     | Categorise |
| Age |     |     | x   | Categorise |
| Gender |     |     | x   |     |
| Marital status |     |     | x   |     |
| Household composition |     |     | x   | Categorise |
| Occupation |     | (x) | x   | Categorise |
| Employment status |     |     | x   |     |
| Workplace/Employer |     | (x) | x   | Categorise |
| Education level |     |     | x   | Categorise |
| Field of education |     |     | x   |     |
| Nationality |     |     | x   | Categorise |
| Vehicle registration number |     | x   |     | Remove |
| Title of publication |     | x   |     | Categorise |
| Web page address |     | (x) | x   | Remove |
| Student ID / Registration number |     | x   |     | Remove |
| Bank account number |     | x   |     | Remove |
| IP address |     | x   |     | Remove |
| Health-related information \* |     | (x) | x   | Categorise/Remove |
| Ethnic group \* |     | (x) | x   | Categorise/Remove |
| Criminal or punishment history \* |     |     | x   | Categorise/Remove |
| Political or religious allegiance \* |     |     | x   | Categorise |
| Union membership \* |     |     | x   | Categorise |
| Social benefits / welfare \* |     |     | x   | Categorise/Remove |
| Sexual orientation \* |     |     | x   | Remove |


Note: Values marked as (x) indicate that the identifier may behave as a strong indirect identifier depending on the context (e.g., rarity, combination with other attributes, or population size).


This table is adapted from international guidelines and tailored to common research contexts in Brazil, particularly in Software Engineering empirical studies.



- **Anonymization tool**: The UK Data Archive (n.d.) has developed a [Text anonymization helper tool](https://ukdataservice.ac.uk/app/uploads/md5_94fc0c2a25f3a75396059826a23b8224_textanonymisationhelpertool.zip) (downloads in a .zip file). It is an add-on MS Word macro for aiding anonymization of qualitative data. Instructions on how to install the tool are with inclued in the zip file.

#### Example: Anonymizing an interview transcript
<!-- based on CESSDA -->

Follow the steps to identify direct and indirect identifiers and decide how to anonymize them.

##### Study background

The study investigates how software developers adopt new tools in their daily work.

An interview was conducted with a senior developer from a mid-sized company in Brazil who recently led the adoption of a new code review tool in their team.

**Transcript symbols**:
- INT: Interviewer
- RESP: Respondent

<!--
**Transcript**

INT: Could you describe your experience adopting the new tool in your team?

RESP: Sure. I’m Vando Azevedo, I work as a senior developer at Tech Solutions here in Recife. We started using CodeFlow around March this year.

INT: And how did the team react?

RESP: At first, people resisted a bit. For example, Barbara, one of our junior developers, found it difficult to adapt. But after a few weeks, things improved.

INT: Did the company provide any support?

RESP: Yes, our manager, Carol, organized some internal workshops. Also, since our team is relatively small, about eight people, it was easier to align everyone.


##### Step 3. Example of anonymization

Below is an example of how direct and indirect identifiers can be handled.

**Anonymized version**

INT: Could you describe your experience adopting the new tool in your team?

RESP: Sure. I’m [a senior developer], working at [a software company] in [a large city in Brazil]. We started using [a code review tool] earlier this year.

INT: And how did the team react?

RESP: At first, people resisted a bit. For example, [a junior developer] found it difficult to adapt. But after a few weeks, things improved.

INT: Did the company provide any support?

RESP: Yes, [the team manager] organized some internal workshops. Also, since our team is relatively small, about [a small team], it was easier to align everyone. -->


| Transcript | Anonymized version |
| :--------- | :----------------- |
| INT: Could you describe your experience adopting the new tool in your team? <br><br> RESP: Sure. I’m Vando Azevedo, I work as a senior developer at Tech Solutions here in Recife. We started using CodeFlow around March this year.<br><br> INT: And how did the team react?<br><br> RESP: At first, people resisted a bit. For example, Barbara, one of our junior developers, found it difficult to adapt. But after a few weeks, things improved.<br><br> INT: Did the company provide any support?<br><br> RESP: Yes, our manager, Carol, organized some internal workshops. Also, since our team is relatively small, about eight people, it was easier to align everyone. | INT: Could you describe your experience adopting the new tool in your team? <br><br> RESP: Sure. I’m [a senior developer], working at [a software company] in [a large city in Brazil]. We started using [a code review tool] earlier this year. <br><br> INT: And how did the team react? <br><br> RESP: At first, people resisted a bit. For example, [a junior developer] found it difficult to adapt. But after a few weeks, things improved. <br><br> INT: Did the company provide any support? <br><br> RESP: Yes, [the team manager] organized some internal workshops. Also, since our team is relatively small, about [a small team], it was easier to align everyone. |

---


##### What was anonymized?

| Identifier type | Category of the identifier | Anonymization method |
| --- | :---: | :---: |
| Full name (Vando Azevedo) | direct identifier |  removed |
| Company name (Tech Solutions) |  strong indirect identifier |  generalized |
| City (Recife) |  indirect identifier |  generalized |
| Tool name (CodeFlow) |  - | generalized (optional, context-dependent) |
| Colleagues' names (Barbara, Carol) |  direct identifiers | removed |
| Team size (8 people) |  indirect identifier |  coarsened  | 


**Key takeaway**

Anonymization is not only about removing names. It involves identifying and handling combinations of information that could make individuals identifiable, even indirectly.






AKIIIII - 

https://www.fsd.tuni.fi/en/services/data-management-guidelines/

https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005510&type=printable

https://docs.google.com/document/d/1KuTSECSYHXZmZX15GDjyD65pJ90eRMhHVEZ-1trsw30/edit?tab=t.0#heading=h.7au7sa260d14 - https://github.com/OpenScienceMOOC




## Archival requirements for Open Science

<!-- Montgomery2024 -->
**What is important when archiving?**

**Hosted Online for Public Access**: Artifacts are hosted online for anyone to access via the internet. E.g., not an intranet or offline solution. Additionally, there is no need for registration to access the artifacts.

**Dedicated DOIs and Immutable Data**: Digital Object Identifiers (DOIs) are automatically created for artifacts, and both the DOIs and data they point to are immutable. Artifacts can be updated, but each version must be maintained with their own DOI.

- Add the DOI of your artifact to your paper.
  - The online service you used to archive your artifact (e.g., Zenodo) will automatically generate a DOI for your artifact.
  - Note that these services generate a DOI for the entire artifact, auto-resolving to the most recent version, and they also often generate additional DOIs, one for each version of your updated artifact. It is recommended using the former for reference in your paper.


**Long-Term Maintainability**: The organization hosting the URL plans to maintain it for the foreseeable future. For this, you must check the mission statement of the hosting organization.
- These archiving services allow you to update your artifact by adding new versions, while maintaining the old versions as well.
- Use this power wisely and responsibly. Upload updated versions when you notice issues with the existing ones.

**So, where can I archive my artifacts?**: In principle, any organization that fulfill the above requirements can be used for archiving artifacts. In reality, there are currently only a few known organizations that satisfy these requirements: ✅ ArXiv for papers ✅ Zenodo for data ⚠️ FigShare for data. FigShare is a “for profit” commercial organisation, which may affect long-term maintainability.


<!-- Elman and Kapiszewski (2014) wrote an informative guide to sharing qualitative data, which we recommend to qualitative researchers. 

-->


Here are some notable services that DO NOT satisfy the above requirements:

- **Institutional Websites, Employee Web Pages, and Research Group Websites**: Institutions update their websites over time, and do not maintain access to resources and URLs. Employee web pages are taken offline when the employee leaves. Similar problems exist for research group websites.

Institutional websites can conform to the three “archiving requirements for Open Science” as described above, in which case you could use them. However, this is usually not the case, and not worth the nuanced investigation you would have to make. Other options are much better.


- **Cloud-Storage Providers**: These storage providers, such as Dropbox, Google Drive, OneDrive, and iCloud, are solutions for backing up and/or syncing data, not archiving data. For example, individuals can change the data and URLs at any time.
  
- **GitHub, GitLab, and other Social Git/Code Platforms**: These services offer features for social product development, which conflict with the requirements for Open Science artifact archival. For example, they allow repositories to be deleted and renamed.

GitHub (and platforms like it) are important for Open Source Software, as they offer a suite of features designed to foster an open and collaborative environment. Some of these features, however, are in direct conflict with Open Science principles. The solution: use both! There are step-by-step guides to automatically archive GitHub project releases to [Zenodo](https://guides.github.com/activities/citable-code/) and [FigShare](https://knowledge.figshare.com/articles/item/how-to-connect-figshare-with-your-github-account).



---

## References

This module builds on a shared set of references used throughout the GAPS material, including guidelines, standards, and research studies on Open Science and research artifacts.

To avoid redundancy and ensure consistency across modules, all references are centralized in the following document: [GAPS References](/references.md).

Contents in this module were adapted and synthesized from these sources.

---

## Table of Contents


- [Module 3 - Preparing research artifacts](#module-3---preparing-research-artifacts)
  - [Data curation](#data-curation)
    - [Qualitative data](#qualitative-data)
  - [Sensitive vs shareable data](#sensitive-vs-shareable-data)
  - [Anonymization strategies](#anonymization-strategies)
    - [Sharing quantitative data](#sharing-quantitative-data)
    - [Sharing qualitative data](#sharing-qualitative-data)
    - [Examples of anomymization methods](#examples-of-anomymization-methods)
      - [Example: Anonymizing an interview transcript](#example-anonymizing-an-interview-transcript)
        - [Study background](#study-background)
        - [What was anonymized?](#what-was-anonymized)
  - [Archival requirements for Open Science](#archival-requirements-for-open-science)
  - [References](#references)
  - [Table of Contents](#table-of-contents)


---