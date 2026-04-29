<table style="width: 100%; border-collapse: collapse; margin: auto;">
  <tbody>
    <tr>
      <td style="border: 0px"> <nobr><- Previous module</nobr> </td>
      <td style="width: 50%; border: 0px"> </td>
      <td style="border: 0px"> <a href="/SUMMARY.md"><nobr>GAPS Summary</nobr></a> </td>
      <td style="width: 50%; border: 0px"></td>
      <td style="border: 0px"> <a href="/M2/main.md"><nobr>Next module -></nobr></a> </td>
    </tr>
  </tbody>
</table>

---

# Module 1 - Foundations of research artifacts


## Learning objectives

By the end of this module, participants will be able to:

- Explain what research artifacts are and why they are essential in empirical research.
- Identify and distinguish different types of research artifacts and their roles in the research process.
- Recognize key characteristics of good research artifacts, including usability, reproducibility, and reusability.
- Describe the artifact life cycle and apply it to organize, document, and share research artifacts.


---

Before discussing research artifacts, it is important to first understand the broader context in which they emerge. Artifacts are not an isolated concept; they emerge as a response to limitations in how research has traditionally been conducted and communicated. In this sense, Open Science provides the conceptual foundation that motivates the creation, sharing, and reuse of research artifacts. By understanding Open Science principles, it becomes clearer why artifacts play a central role in improving transparency, reproducibility, and reuse in empirical research.

## Open Science
<!-- ZeeReich2018 -- > <!-- MendezEtAl2020 -->

The credibility and verifiability of empirical studies in Software Engineering depend strongly on transparency regarding complex artifacts, such as datasets, tools, and experimental setups. Historically, scientific communication was constrained by print-based publication models, which imposed strict limits on space and high dissemination costs. This scenario often led researchers to present summarized methodological descriptions that mask the inherent complexity of the research process, such as intermediate decisions, discarded analyses, or changes in study design.

Today, the global spread of networked technologies has removed these physical barriers, allowing scientific communication to move beyond the static paper and include the sharing of the entire research cycle. In this context, Open Science should not be viewed as a set of universal prescriptions, but as an invitation for researchers to be explicit and honest about their practices. It emerges as a set of practices designed to increase the transparency of evidentiary reasoning and access to research across key stages of the research process.

It is important to note that openness in science is not a binary toggle, but rather a continuum. The transition toward more transparent practices can be gradual and must account for contextual constraints, such as ethical considerations, participant privacy, or the sensitivity of proprietary software data. Ultimately, this movement seeks to improve the quality of scientific dialogue by addressing chronic issues like publication bias and replication failures through increased visibility of the entire research process.


### What is Open Science?
<!-- UNESCO2021 - -> <!-- FOSTER2018 - -> <!-- ZeeReich2018 - ->  <!-- MendezEtAl2020 -- > <!-- SonjaEtAl2018 -->

- A set of practices that make the research process and its underlying reasoning more transparent.
- It makes scientific knowledge, data, methods, and processes openly available so that others can access, reuse, and build upon them.
- It promotes collaboration across researchers and society.
- It supports validation, reproducibility, and broader impact of research.
- Open Science also involves advocacy efforts to promote openness, influence policies, and engage stakeholders across the research ecosystem.

Scientific progress depends on research that is reliable, verifiable, and reusable. In this sense, transparency, credibility, and reproducibility are essential foundations for building robust knowledge, particularly in an evolving field such as Software Engineering. Open Science provides the foundation to support these goals.


### Core Open Science practices

![Open Science elements](/M1/images/FIG-open-science-elements.png) <!-- GallagherEtAl2020 -->

Open Science is commonly operationalized through a set of complementary practices:

#### Open Access

<!-- MendezEtAl2020 -- > <!-- GallagherEtAl2020 -->

**What is it**:
- Scientific publications are made freely available on the public Internet without financial, legal, or technical barriers, allowing anyone to read, download, copy, reuse, distribute, print, search, or link to the full texts of publications for any lawful purpose.

**Why it matters**:
- Open Access increases the visibility and dissemination of research, accelerates knowledge transfer, and reduces inequalities by allowing researchers worldwide to access scientific results regardless of institutional resources.

**Examples in practice**: 
- Publishing papers in open-access venues.
- Depositing preprints in repositories (e.g., arXiv).
- Providing author-accepted manuscripts in institutional repositories.

**Relation to research artifacts**:
- Open Access ensures that the paper describing the artifact is available, enabling others to understand its context, usage, and contributions.

---

#### Open Data
<!-- MendezEtAl2020 -- > <!-- ZeeReich2018 -- > <!-- GallagherEtAl2020 -->

**What it is**:
- Data produced during research are made available for access and reuse, typically through public repositories.
- Openness can come in various forms and at different degrees, depending on ethical and legal constraints.
- It includes all data collected or generated during the research, as well as supporting materials, whether quantitative or qualitative.

**Why it matters**:
- Open Data enables validation of results, supports reproducibility, and allows secondary analyses.
- It increases the value of data, which are often costly to collect, and improves the quality of peer review by allowing inspection of underlying evidence.

**Examples in practice**:
- Publishing datasets in repositories (e.g., Zenodo, Figshare).
- Sharing replication packages with raw, processed, and derived data, supporting materials, such as texts, interview transcripts, log data, diaries, and any other materials that were used or produced in a study.
- Providing metadata and data documentation.

**Relation to research artifacts**:
- Open Data corresponds directly to data artifacts, which are central for reproducibility, validation, and reuse.

---

#### Open Resources
<!-- UNESCO2021 -- > <!-- GallagherEtAl2020 -- > <!-- SonjaEtAl2018 -->

**What it is**:
- Teaching, learning and research materials in any medium (digital or otherwise) released under an open license that allow no-cost access, use, adaptation and redistribution by others with no or limited restrictions.

**Why it matters**:
- Supports learning, lowers barriers to entry, and broadens access to scientific knowledge.
- Open resources are often built upon research findings, helping disseminate and translate research into reusable educational materials.

**Examples in practice**:
- Sharing tutorials, lecture slides, and teaching materials.
- Publishing guidelines, checklists, and documentation.
- Providing reusable study materials.

**Relation to research artifacts**:
- Open Resources correspond to documentation and communication artifacts, which improve usability, understanding, and learning.
- They support reuse and adaptation, enabling others to build upon and extend research outputs.

---

#### Open Source (Open Research Software)
<!-- UNESCO2021 -- > <!-- GallagherEtAl2020 -- > <!-- SonjaEtAl2018 -->

**What it is**:
- Open research software refers to software used in research (e.g., for analysis, simulation, or visualization) or developed as a research output, whose source code is made publicly available.
- It is shared in a user-friendly, human- and machine-readable, and modifiable format, under an open license that allows others to use, study, modify, and redistribute it.

**Why it matters**:
- Open Source in research enables transparency in computational processes, supports reproducibility, and allows others to inspect, reuse, and extend research software.

**Examples in practice**:
- Publishing code on GitHub with an open license.
- Sharing analysis scripts and pipelines.
- Providing executable implementations of algorithms.

**Relation to research artifacts**:
- Open Source corresponds to implementation artifacts, enabling execution and reproduction of results.

 ---

#### Open Peer Review
<!-- MendezEtAl2020 -- > <!-- GallagherEtAl2020 -- > <!-- SonjaEtAl2018 -->

**What it is**:
- Open Peer Review is an umbrella term for practices that aim to increase transparency in the peer review process.
  - It may include open identities (authors and reviewers know each other), open reports (reviews are publicly available), and other forms of interaction and participation.
  -  Nowadays, there is yet no commonly accepted and clear definition nor an agreed schema. <!--There is no single universally accepted definition.-->

**Why it matters**:
- Open Peer Review increases transparency and accountability, improves the quality of feedback, and allows broader scrutiny of research, data, and methods.

**Examples in practice**:
- Publishing review reports alongside papers.
- Open discussion between authors and reviewers.
- Community-driven or post-publication review.

**Relation to research artifacts**:
- Open Peer Review increases transparency and enables greater scrutiny of data and methods, which in turn reinforces the need for sharing research artifacts to support verification and reproducibility.

---

#### Open Methods
<!-- GallagherEtAl2020 -->

**What it is**:
- Research methods, protocols, and procedures are explicitly documented and shared, enabling others to understand and reproduce the research process.

**Why it matters**:
- Open Methods improve transparency, reduce ambiguity in research design, and support replication by making methodological decisions explicit.

**Examples in practice**:
- Sharing study protocols and experimental designs.
- Providing data collection instruments (e.g., surveys, interview scripts).
- Documenting analysis procedures and decisions.

**Relation to research artifacts**:
- Open Methods correspond to methodological artifacts, which are essential for replication and understanding how results were produced.

---

#### FAIR Principles
<!-- MendezEtAl2020 -- > <!-- SonjaEtAl2018 -- > <!-- WilkonsonEtAl2018 -->

**What it is**:
- A set of guiding principles designed to ensure that digital research objects are <u>**F**</u>indable, <u>**A**</u>ccessible, <u>**I**</u>nteroperable, and <u>**R**</u>eusable.

  - **Findable**: They are assigned persistent identifiers, described with rich metadata, and indexed in searchable resources.
    <!--
    - F1. (Meta)data are assigned a globally unique and persistent identifier.
    - F2. Data are described with rich metadata (defined by R1).
    - F3. Metadata clearly and explicitly include the identifier of the data they describe.
    - F4. (Meta)data are registered or indexed in a searchable resource.-->
    
  - **Accessible**: They are retrievable via open, standardized protocols with defined access conditions, and metadata remain accessible even if the data are no longer available.
    <!--
    - A1. (Meta)data are retrievable by their identifier using a standardised communications protocol.
      - A1.1 The protocol is open, free, and universally implementable.
      - A1.2 The protocol allows for an authentication and authorisation procedure, where necessary.
    - A2. Metadata are accessible, even when the data are no longer available.-->
    
  - **Interoperable**: They use shared vocabularies, formal languages, and include links to related data for integration.
    <!--
    - I1. (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.
    - I2. (Meta)data use vocabularies that follow FAIR principles.
    - I3. (Meta)data include qualified references to other (meta)data.-->
    
  - **Reusable**: They are well-described with relevant attributes, include clear usage licenses and provenance, and comply with community standards.
    <!--
    - R1. (Meta)data are richly described with a plurality of accurate and relevant attributes.
      - R1.1. (Meta)data are released with a clear and accessible data usage license.
      - R1.2. (Meta)data are associated with detailed provenance.
      - R1.3. (Meta)data meet domain-relevant community standards.-->

![FAIR Principles](/M1/images/FIG-FAIR-IDS.png)

**Why it matters**:
- FAIR principles provide a structured way to improve the quality and reusability of research objects, ensuring that they can be discovered, accessed, integrated, and reused by both humans and machines.
- Making data open does not guarantee reuse. Data must also follow FAIR principles.
  

**Examples in practice**:
- Assigning persistent identifiers (e.g., DOIs).
- Providing rich metadata and documentation.
- Using standard formats and vocabularies.
- Including licenses and provenance information.

**Relation to research artifacts**:
- FAIR principles define the quality attributes of good artifacts, guiding how all types of artifacts should be structured, documented, and shared.


<!--
![FAIR Principles](/M1/images/FIG-FAIR-principles.png) <!-- WilkonsonEtAl2018 -- > <!-- ChatGPT -->

---

### Practice Open Science sounds like extra work, right?
<!-- FOSTER2018 -->

Practising Open Science may require additional effort, but it brings important benefits.

> **For research:**
- Improves transparency and reproducibility.
- Facilitates validation and reuse of results.
- Accelerates knowledge generation.
- Helps to ensure that all researchers have a level playing field, regardless of their location or economic situation.

> **For society:**
- Increases the return on publicly funded research.
- Expands access to scientific knowledge.

> **For researchers:**

- Increases visibility and potential impact of their work.
- Creates additional citable outputs (e.g., datasets, code).
- Fosters new collaborations and research opportunities.

---

While these benefits highlight why Open Science is valuable, they are rooted in a broader set of values (e.g., quality, equity, collective benefit, and inclusiveness) and principles (e.g., transparency, collaboration, and accountability) that guide Open Science practices. The figure below summarizes these guiding elements.

![Open Science values and principles](/M1/images/FIG-open-science-values-principles.png) <!-- UNESCO2021 -->


To make Open Science practical, researchers rely on research artifacts. These artifacts, such as datasets, code, protocols, and documentation, make it possible to share not only the results of a study, but also the process through which those results were produced. As a result, artifacts are essential for enabling transparency, reproducibility, and reuse in empirical research.

Artifacts are the concrete mechanism through which Open Science becomes actionable in practice, translating abstract principles into tangible and reusable research outputs.

Adoption of open practices may require awareness and cultural change within research communities.



## Research Artifacts

In the context of Open Science, sharing only the paper is not enough to fully communicate a study. To make research transparent, reproducible, and reusable, it is necessary to also share the materials that support it. These materials are known as research artifacts.


**What is a research artifact?**

- A research artifact is any external material associated with a research report (e.g., paper).
- It helps others understand, verify, reproduce, or reuse the study. 
- These artifacts are made available via a link within the research report.


**Why do artifacts matter?**

- Research artifacts are essential because they make research transparent and verifiable, allowing others to understand and validate how results were produced.
- They support reproducibility and replicability, enabling studies to be re-executed under the same or similar conditions.
- Artifacts promote reusability and cumulative science, allowing future work to build upon, extend, and compare existing results.

<!--
Research artifacts are essential because they support three fundamental goals:

- **Transparency and verifiability**:    
Making the research process visible and enabling independent validation of results.

- **Reproducibility and replicability**:    
Allowing others to obtain the same results or re-execute the study under similar conditions.

- **Reusability and cumulative science**:   
  Enabling future research to build upon, extend, and compare existing work.
-->


**Formal definition**

More formally, a research artifact can be defined as a digital object generated as a result of the research itself or created by the authors to be used as part of the research, being essential for the associated paper. <!-- ACM2020 TimperleyEtAl2021 -->



## Types of research artifacts

Once we understand what artifacts are, the next step is to understand the different roles they play. They can be grouped into categories based on what they represent and how they contribute to the study.

These categories are not strict or exhaustive, and a single artifact may fit into more than one category. <!-- MenziesEtAl2018 -->


**Overview of artifact types**

1. Conceptual and scientific artifacts
2. Methodological artifacts
3. Data artifacts
4. Implementation artifacts
5. Documentation and communication artifacts
6. Reproducibility and infrastructure artifacts
7. Research outputs as artifacts

Together, these categories reflect the full research lifecycle, from problem definition to execution, communication, and reuse.

Once we understand what artifacts are, the next step is to understand the different roles they play.

The table below presents the definition and role of each artifact category. Rather than memorizing categories, it is more important to understand that artifacts cover the entire research process. The categories below serve as a guide to help you recognize their roles.

Each category reflects a different aspect of the research process, from planning to execution and dissemination.


| Artifact type | Definition | Role |
|---------------|------------|------|
| **1. Conceptual and scientific artifacts** | Artifacts that define, guide, or interpret the research. | Frame the research problem and contribute to scientific knowledge. |
| **2. Methodological artifacts** | Artifacts that describe how the research is conducted. | Enable understanding and replication of the research design. |
| **3. Data artifacts** | Artifacts related to the data used or produced. | Support empirical analysis and validation of results. |
| **4. Implementation artifacts** | Artifacts that operationalize the research. | Enable execution and reproduction of results. |
| **5. Documentation and communication artifacts** | Artifacts that explain how to understand and use the work. | Improve usability, accessibility, and learning. |
| **6. Reproducibility and infrastructure artifacts** | Artifacts that support execution across environments. | Ensure reproducibility and facilitate reuse. |
| **7. Research outputs as artifacts** | Artifacts that are traditionally seen as outputs but can also be reused. | Connect the artifact ecosystem to the published work. |

---


The table below shows examples of the types of research artifacts of each category.


| Artifact type | Examples of artifacts |
|---------------|-----------------------|
| **1. Conceptual and scientific artifacts** | - Motivational or challenge statements<br> - Hypotheses<br> - Baseline results<br> - New findings and results<br> - Negative results<br> - Future work directions<br> - Annotated or structured bibliographies<br> |
| **2. Methodological artifacts** | - Study instruments (e.g., surveys, interview scripts)<br> - Study protocols <br> - Sampling procedures<br> - Statistical tests and analysis rationale<br> - Checklists for study design<br> - Patterns (best practices)<br> - Anti-patterns (common pitfalls) |
| **3. Data artifacts** | - Raw datasets<br> - Processed datasets<br> - Derived datasets<br> - Data documentation |
| **4. Implementation artifacts** | - Analysis or visualization scripts<br> - Programs implementing algorithms<br> - Executable models<br> - Pipelines and workflows |
| **5. Documentation and communication artifacts** | - README files<br> - Execution guides<br> - Tutorials and educational materials<br> - Commentary on scripts or analysis<br> - Informative visualizations <br> - Figures and tables used in the paper |
| **6. Reproducibility and infrastructure artifacts** | - Configuration and dependency files<br> - Build scripts<br> - Containerization setups (e.g., Docker)<br> - Virtual machines or pre-configured environments<br> - Delivery tools for automated execution |
| **7. Research outputs as artifacts** | - The paper manuscript (which describes the study and references the associated artifacts) <br> - Supplementary materials |



## Key characteristics of good research artifacts

Instead of thinking in terms of a fixed checklist, it is more useful to understand good artifacts as those that enable understanding, execution, and reuse.

These qualities can be grouped into three complementary dimensions:


> **Usability** (Can others understand and use it?)

Good artifacts should be:

- **Well-documented**: clearly explain structure, purpose, and usage.
- **Self-contained**: include all necessary components and dependencies or clearly specify them.
- **Consistent**: aligned with the paper and its claims.

**Why it matters**: Without usability, even available artifacts are rarely reused.


> **Reproducibility** (Can others run and verify it?)

Good artifacts should be:

- **Executable**: runnable with reasonable effort.
- **Automated**: support end-to-end execution with minimal manual intervention.
- **Verifiable**: allow independent validation of results.

**Why it matters**: Reproducibility is not just about sharing code, it is about enabling execution.



> **Reusability** (Can others build upon it?)

Good artifacts should be:

- **Legally compliant**: include clear licenses and respect ethical constraints.
- **Preserved**: stored in reliable repositories with long-term access.

- **FAIR-aligned**: follow principles such as *Findable*, *Accessible*, *Interoperable*, and *Reusable*.
  
**Why it matters**: Reusability is what turns artifacts into long-term scientific contributions.



## Common pitfalls and good practices in research artifacts

Even when artifacts are shared, they often fail in practice. Typical issues include:

**Poor practices**

- “Code available upon request”.
- Missing preprocessing steps.
- Hard-coded paths or parameters.
- Undocumented setup or execution.
- Broken or temporary links.
- Results that cannot be reproduced.

These issues are not rare, they are among the most common reasons why shared artifacts fail in practice.

**Good practices**

Well-prepared artifacts typically:

- Provide clear documentation (README, instructions).
- Include all dependencies and versions.
- Allow execution from scratch.
- Enable regeneration of results (tables/figures).
- Maintain consistency between artifact outputs and the paper.
- Include quick-start examples or test cases.
- Explicitly state limitations or non-shared components.

A good artifact should be understandable and usable on its own, without requiring deep interpretation of the paper.

In practice, achieving these qualities depends on how artifacts are created, documented, and shared over time. This process can be understood through the artifact life cycle.



## Artifact life cycle
<!-- Montgomery2024 -->

Research artifacts should not be treated as a final step of the research process. Instead, they should evolve alongside the study, from its early stages to publication and beyond.

Thinking in terms of a life cycle helps ensure that artifacts are not only created, but also properly prepared for sharing, reuse, and long-term preservation.

A practical way to structure this process is through the following stages:

> **1. Collect**

**What to do**:
- Gather all materials produced or used during the research.
- Collection should happen continuously, not only at the end of the project.

**Examples**:
- Data.
- Code.
- Scripts.
- Protocols.
- Any supporting resources.

**Why it matters**: Missing or incomplete materials are one of the main barriers to reproducibility.



> **2. Document**

**What to do**:
- Clearly describe the artifact and its contents, so others can understand and use them.

**Examples**:
- Purpose and scope.
- Structure and organization.
- Authorship and contributions.
- Relation to the paper.
- Execution instructions (when applicable).

**Why it matters**: An undocumented artifact is effectively unusable.



> **3. License**

**What to do**:
- Define how others can use, modify, and share the artifact.

**Examples**:
- Use appropriate open licenses for:
  - Code (e.g., MIT, Apache)
  - Data (e.g., CC-BY)

**Why it matters**: Without a clear license, reuse is legally uncertain.



> **4. Archive**

**What to do**:
- Store artifacts in reliable repositories that support:
  - Long-term preservation.
  - Persistent identifiers (e.g., DOI).
  - Versioning.

**Why it matters**: Personal websites and temporary links are not reliable for long-term access.



> **5. Share**

**What to do**:
- Make artifacts visible and accessible to the research community.
- Link the artifacts directly in the paper.
- Use other dissemination channels.

**Why it matters**: Artifacts only contribute to science if others can find and access them.


---

**Continuous process**

Although presented as stages, this process is iterative. Artifacts are refined over time, especially after feedback, reuse, or replication attempts.


![Artifact life cycle](/M1/images/FIG-artifact-life-cycle.png) <!-- Montgomery2024 --> <!-- Gemini2026 -->





## Practical example

This example is based on a real research artifact developed in a study analyzing the evolution of artifact calling (i.e., how venues encourage or require artifact sharing) and artifact sharing practices in papers published at ICSE and FSE over a decade.

The artifact supports a full empirical study and enables the reproduction of all reported results.

Artifacts in this project include:

- **Curated dataset of collected papers**
(e.g., list of ICSE and FSE papers with identifiers, titles, and publication years)

- **Processed dataset**
(e.g., structured dataset with extracted variables such as artifact links, availability status, badges, and derived metrics)

- **Extracted data from conference websites**
(e.g., calls for papers, artifact evaluation policies, and historical changes over time)

- **Data extraction protocol**
(e.g., procedures used to collect and classify data from papers and websites)

- **Classification schemes** 
(e.g., artifact availability categories, platform types, disclosure statements)

- **Analysis scripts**
(e.g., R scripts that automatically generate all figures and tables reported in the paper)

- **Results and visualizations**
(e.g., timelines, distributions, and statistical analyses such as correlations)

- **Reproducibility package**
(e.g., organized folder structure with scripts, data, and outputs, enabling one-command execution)

- **Documentation**
(e.g., README files describing the dataset, scripts, and step-by-step reproduction instructions)

This example illustrates how the concepts presented in this module come together in practice and how different types of artifacts (data, code, documentation, and infrastructure) are combined to support transparency, reproducibility, and reuse in empirical research.

---

## References

This module builds on a shared set of references used throughout the GAPS material, including guidelines, standards, and research studies on Open Science and research artifacts.

To avoid redundancy and ensure consistency across modules, all references are centralized in the following document: [GAPS References](/references.md).

Contents in this module were adapted and synthesized from these sources.

---

## Table of Contents

- [Module 1 - Foundations of research artifacts](#module-1---foundations-of-research-artifacts)
  - [Learning objectives](#learning-objectives)
  - [Open Science](#open-science)
    - [Core Open Science practices](#core-open-science-practices)
    - [Practice Open Science sounds like extra work, right?](#practice-open-science-sounds-like-extra-work-right)
  - [Research Artifacts](#research-artifacts)
  - [Types of research artifacts](#types-of-research-artifacts)
  - [Key characteristics of good research artifacts](#key-characteristics-of-good-research-artifacts)
  - [Common pitfalls and good practices in research artifacts](#common-pitfalls-and-good-practices-in-research-artifacts)
  - [Artifact life cycle](#artifact-life-cycle)
  - [Practical example](#practical-example)
  - [References](#references)
  - [Table of Contents](#table-of-contents)

---