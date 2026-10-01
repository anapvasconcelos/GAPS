# Module 1 - Foundations

Research in Software Engineering depends on more than well-written papers. For results to be trusted and built upon, other researchers must be able to access and reproduce the underlying materials. Research artifacts emerged to complement traditional, paper-based communication and make the research process more visible, verifiable, and reusable.

Before discussing artifacts in detail, it is important to understand the broader context in which they emerge. Open Science is the movement that motivates their creation, sharing, and reuse. Understanding these foundations is essential to grasp why artifacts play a central role in improving transparency and reproducibility, before engaging with the practical aspects covered in subsequent modules.

This lifecycle provides an overview of the practices developed throughout the subsequent modules.

## 1.1. Learning objectives

By the end of this module, you will be able to:

- Explain the relationship between Open Science and research artifacts.
- Distinguish the main types and roles of research artifacts in Software Engineering research.
- Explain how research artifacts support transparency, reproducibility, and reuse.
- Distinguish execution-oriented and transparency-oriented artifacts.
- Describe the main stages of the research artifact life cycle.
- Identify the characteristics that make an artifact usable, reproducible, and reusable.

## 1.2. Open Science
<!-- Source: ZeeReich2018 - - MendezEtAl2020 - - BeyerWinter2025 -->

The credibility and verifiability of empirical studies in Software Engineering depend strongly on transparency regarding complex artifacts, such as datasets, tools, and experimental setups. Historically, scientific communication was constrained by print-based publication models, which imposed strict limits on space and high dissemination costs. This often led researchers to present summarized methodological descriptions that mask the inherent complexity of the research process, such as intermediate decisions, discarded analyses, or changes in study design. <!-- Source: ZeeReich2018 -->

Today, networked technologies have removed these physical barriers, allowing scientific communication to move beyond the static paper and encompass the sharing of the entire research cycle. In this context, Open Science is not a set of universal prescriptions, but an invitation to be explicit and honest about research practices, a set of practices designed to increase the transparency of evidentiary reasoning and access to research across key stages of the research process.

The transition toward more transparent practices has been gradual and must account for contextual constraints, such as ethical considerations, participant privacy, or the sensitivity of proprietary software data. Ultimately, this movement seeks to improve the quality of scientific dialogue by addressing chronic issues like publication bias and replication failures through increased visibility of the entire research process.

In Software Engineering, these concerns contributed to the emergence of initiatives aimed at improving transparency, reproducibility, and long-term accessibility of research artifacts. One important example is the adoption of artifact evaluation processes by major conferences, encouraging authors to share datasets, tools, scripts, and other materials that support published findings. The Software Engineering community was among the early adopters of these practices. One of the earliest examples occurred at ESEC/FSE 2011, where research artifacts supporting published results were voluntarily submitted for peer review.

### 1.2.1. What is Open Science?
<!-- Source: UNESCO2021 - - FOSTER2018 - - ZeeReich2018 - - MendezEtAl2020 - - BezjakEtAl2018 -->

Open Science is a set of practices that make the research process and its underlying reasoning more transparent. It makes scientific knowledge, data, methods, and processes openly available so that others can access, reuse, and build upon them. More specifically, Open Science:

- Promotes collaboration across researchers and society.
- Supports validation, reproducibility, and broader impact of research.
- Involves advocacy efforts to promote openness, influence policies, and engage stakeholders across the research ecosystem.

Scientific progress depends on research that is reliable, verifiable, and reusable. Transparency, credibility, and reproducibility are essential foundations for building robust knowledge, particularly in an evolving field such as Software Engineering.

### 1.2.2. Open Science practices

Open Science encompasses a broad and evolving ecosystem of practices, principles, infrastructures, and policies. Since this ecosystem is extensive, this module focuses on the subset of practices most directly connected to research artifacts and reproducibility in empirical Software Engineering research.

#### 1.2.2.1. Open Access
<!-- Source: MendezEtAl2020 - - GallagherEtAl2020 - - DamascenoStruber2021 -->

Scientific publications are made freely available on the public internet without financial, legal, or technical barriers, allowing anyone to read, download, copy, reuse, distribute, and link to full texts of publications for any lawful purpose.

- **Why it matters:** Open Access increases the visibility and dissemination of research, accelerates knowledge transfer, and reduces inequalities by allowing researchers worldwide to access scientific results regardless of institutional resources.

- **Relation to research artifacts:** Open Access ensures that the paper describing the artifact is available, enabling others to understand its context, usage, and contributions.

- **Examples in practice:** 
  - Publishing papers in open-access venues.
  - Depositing preprints in repositories (e.g., arXiv).
  - Providing author-accepted manuscripts in institutional repositories.

#### 1.2.2.2. Open Data
<!-- Source: MendezEtAl2020 - - ZeeReich2018 - - GallagherEtAl2020 - - DamascenoStruber2021 -->

Data produced during research are made available for access and reuse, typically through public repositories. It includes all data collected or generated during the research, as well as supporting materials. Openness can come in various forms and at different degrees, depending on ethical and legal constraints.

- **Why it matters:** Open Data enables validation of results, supports reproducibility, and allows secondary analyses. It increases the value of data (often costly to collect) and improves the quality of peer review by allowing inspection of underlying evidence.

- **Relation to research artifacts:** Open Data corresponds directly to data artifacts, which are central for reproducibility, validation, and reuse.

- **Examples in practice:**
  - Publishing datasets in repositories (e.g., Zenodo, Figshare).
  - Sharing replication packages with raw, processed, and derived data, including texts, interview transcripts, log data, and diaries.
  - Providing metadata and data documentation.

#### 1.2.2.3. Open Resources
<!-- Source: UNESCO2021 - - GallagherEtAl2020 - - BezjakEtAl2018 -->

Teaching, learning, and research materials in any medium, released under an open license that allows no-cost access, use, adaptation, and redistribution by others with no or limited restrictions.

- **Why it matters:** Open resources support learning, lower barriers to entry, and broaden access to scientific knowledge.

- **Relation to research artifacts:** Open Resources correspond to documentation and communication artifacts, which improve usability, understanding, and learning, supporting reuse and adaptation.

- **Examples in practice:**
  - Sharing tutorials, lecture slides, and teaching materials.
  - Publishing guidelines, checklists, and documentation.
  - Providing reusable study materials.

#### 1.2.2.4. Open Source (including open research software)
<!-- Source: UNESCO2021 - - GallagherEtAl2020 - - BezjakEtAl2018 -->

Open research software refers to software developed to be used in research (for analysis, simulation, or visualization) or developed as a research output, whose source code is made publicly available. It is shared in a user-friendly, human- and machine-readable, and modifiable format, under an open license that allows others to use, study, modify, and redistribute it.

- **Why it matters:** Open Source in research enables transparency in computational processes, supports reproducibility, and allows others to inspect, reuse, and extend research software.

- **Relation to research artifacts:** Open Source corresponds to implementation artifacts, enabling execution and reproduction of results.

- **Examples in practice:**
  - Publishing code on GitHub with an open license.
  - Sharing analysis scripts and pipelines.
  - Providing executable implementations of algorithms.

#### 1.2.2.5. Open Peer Review
<!-- Source: MendezEtAl2020 - - GallagherEtAl2020 - - BezjakEtAl2018 -->

Open Peer Review is an umbrella term for practices that aim to increase transparency in the peer review process. It may include open identities (authors and reviewers know each other), open reports (reviews are publicly available), and other forms of interaction and participation. There is yet no commonly accepted and clear definition nor an agreed schema. <!-- Source: BezjakEtAl2018 -->

- **Why it matters:** Open Peer Review increases transparency and accountability, improves the quality of feedback, and allows broader scrutiny of research, data, and methods. <!-- Source: MendezEtAl2020 -->

- **Relation to research artifacts:** Open Peer Review increases scientific rigor through increased scrutiny of data and methods. It reinforces the need for sharing research artifacts to support verification and reproducibility. <!-- Source: GallagherEtAl2020 -->

**Examples in practice:**
- Publishing review reports alongside papers.
- Open discussion between authors and reviewers.
- Community-driven or post-publication review.

#### 1.2.2.6. Open Methods
<!-- Source: GallagherEtAl2020 -->

Research methods, protocols, and procedures are explicitly documented and shared, enabling others to understand and reproduce the research process.

- **Why it matters:** Open Methods improve transparency, reduce ambiguity in research design, and support replication by making methodological decisions explicit.

- **Relation to research artifacts:** Open Methods correspond to methodological artifacts, which are essential for replication and understanding how results were produced.

- **Examples in practice:**
  - Sharing study protocols and experimental designs.
  - Providing data collection instruments (e.g., surveys, interview scripts).
  - Documenting analysis procedures and decisions.

#### 1.2.2.7. FAIR principles
<!-- Source: MendezEtAl2020 - - BezjakEtAl2018 - - WilkonsonEtAl2018 -->

A set of guiding principles designed to ensure that digital research objects are <u>**F**</u>indable, <u>**A**</u>ccessible, <u>**I**</u>nteroperable, and <u>**R**</u>eusable.

- **Why it matters:** FAIR principles provide a structured way to improve the quality and reusability of research objects, ensuring they can be discovered, accessed, integrated, and reused by both humans and machines. Making data open does not guarantee reuse, so data must also follow FAIR principles.

- **Relation to research artifacts:** FAIR principles define the quality attributes of good artifacts, guiding how all types of artifacts should be structured, documented, and shared.

Openness alone is not sufficient. FAIR principles complement Open Science by focusing on the conditions that make research artifacts discoverable, accessible, interoperable, and reusable for both humans and machines.  <!-- Source: WilkinsonEtAl2016 -->

##### 1.2.2.7.1. FINDABLE
<!-- Source: WilkinsonEtAl2016 - - DamascenoStruber2021 -->

Artifacts are assigned persistent identifiers, described with rich metadata, and indexed in searchable resources.

<!-- Source: WilkinsonEtAl2016 - - DamascenoStruber2021 - - ZeeReich2018 -->
| Principle | Description |
|---|---|
| F1. Globally unique and persistent identifier (PID) | Artifacts should have stable and unique identifiers that allow them to be reliably referenced, cited, and located over time. |
| F2. Rich metadata | Artifacts should include detailed metadata describing their content, purpose, authorship, structure, context, and usage. |
| F3. Metadata include the PID of the described object | Metadata should explicitly reference the identifier of the artifact they describe. |
| F4. Registered or indexed in searchable resources | Artifacts and their metadata should be deposited in repositories or platforms where they can be searched, discovered, and accessed by others. |

Persistent identifiers (PIDs) are typically resolvable through stable web links, allowing artifacts to remain locatable even if their storage location changes. DOI is the PID standard most widely adopted by archival repositories and supported across scholarly indexing infrastructures (e.g., Crossref, Scopus). Other PIDs also exist (e.g., Handle, ARK, SWHIDs).

##### 1.2.2.7.2. ACCESSIBLE
<!-- Source: WilkinsonEtAl2016 -->

Artifacts are retrievable via open, standardized protocols with defined access conditions, and metadata remain accessible even if the artifact itself is no longer available.

| Principle | Description |
|---|---|
| A1. Retrievable via PID using a standardized protocol | Artifacts should be accessible through stable and standardized mechanisms (e.g., HTTPS, APIs) using their identifiers. |
| A1.1. Open, free, and universally implementable protocols | Access protocols should rely on open and widely supported technologies that do not require proprietary tools. |
| A1.2. Authentication and authorization when necessary | When artifacts cannot be fully public, access mechanisms should still support controlled and well-defined authorization procedures. |
| A2. Metadata remain accessible even if the artifact is no longer available | Even if the artifact becomes unavailable, its metadata should remain accessible so others can still understand its existence and context. |

##### 1.2.2.7.3. INTEROPERABLE
<!-- Source: WilkinsonEtAl2016 -->

Artifacts use shared vocabularies, formal languages, and include links to related data for integration.

| Principle | Description |
|---|---|
| I1. Formal, accessible, shared, and broadly applicable representation languages | Artifacts should use standardized and broadly supported formats. |
| I2. Vocabularies that follow FAIR principles | Artifacts and metadata should adopt shared vocabularies or terminologies that are themselves well-documented and reusable. |
| I3. Qualified references to related objects | Artifacts should explicitly indicate how they relate to other datasets, scripts, papers, or research outputs. | 

##### 1.2.2.7.4. REUSABLE
<!-- Source: WilkinsonEtAl2016 -->

Artifacts are well-described with relevant attributes, include clear usage licenses and provenance, and comply with community standards.

<!-- Source: WilkinsonEtAl2016 - - DamascenoStruber2021 -->
| Principle | Description |
|---|---|
| R1. Richly described with accurate and relevant attributes | Artifacts should provide sufficient detail about their content, context, assumptions, limitations, and intended use. |
| R1.1. Clear and accessible usage license | Artifacts should include explicit licensing information specifying how others may use, modify, and redistribute them. |
| R1.2. Detailed provenance | Artifacts should document their origin, history, processing steps, versions, and responsible contributors. |
| R1.3. Domain-relevant community standards | Artifacts should follow conventions, formats, and best practices commonly adopted within the relevant research community. |

### 1.2.3. Why practice Open Science?
<!-- Source: FOSTER2018 -->

Practising Open Science may require additional effort, but it brings important benefits at multiple levels:

| Level | Benefits |
|---|---|
| For research | - Supports transparency, validation, and reproducibility.<br>- Facilitates the reuse of results.<br>- Accelerates knowledge generation. |
| For society | - Expands access to scientific knowledge regardless of geographic or economic constraints.<br>- Increases the return on publicly funded research. |
| For you | - Increases visibility and potential impact of your work.<br>- Creates additional citable outputs (e.g., datasets, code).<br>- Fosters new collaborations and research opportunities. |

To make Open Science practical, researchers rely on **research artifacts**, the concrete mechanism through which Open Science becomes actionable, translating abstract principles into tangible and reusable research outputs.

## 1.3. Research artifacts

In the context of Open Science, sharing only the paper is not enough to fully communicate a study. To make research transparent, reproducible, and reusable, you also need to share the materials that support it.

### 1.3.1. What is a research artifact?

A research artifact is any external material associated with a research report (e.g., a paper) that helps others understand, verify, reproduce, or reuse the study. These artifacts are made available via a link within the research report. More formally, a research artifact is a digital object generated as a result of the research itself or created by the authors to be used as part of the research, being essential for the associated paper. <!-- Source: ACM2020 - - TimperleyEtAl2021 -->

### 1.3.2. Why do artifacts matter?

- They make research **transparent and verifiable**, allowing others to understand and validate how results were produced.
- They support **reproducibility and replicability**, enabling studies to be re-executed under the same or similar conditions.
- They promote **reusability and cumulative science**, allowing future work to build upon, extend, and compare existing results.

## 1.4. Types of research artifacts

Artifacts can be grouped into categories based on what they represent and how they contribute to the study. These categories are not strict or exhaustive, and a single artifact may fit into more than one category. Together, they reflect the full research lifecycle, from problem definition to execution, communication, and reuse. <!-- Source: MenziesEtAl2018 -->

<!-- Source: MenziesEtAl2018 -->
| Artifact type | Definition | Role |
|---|---|---|
| 1. Conceptual and scientific artifacts | Artifacts that define, guide, or interpret the research. | Frame the research problem and contribute to scientific knowledge. |
| 2. Methodological artifacts | Artifacts that describe how the research is conducted. | Enable understanding and replication of the research design. |
| 3. Data artifacts | Artifacts related to the data used or produced. | Support empirical analysis and validation of results. |
| 4. Implementation artifacts | Artifacts that operationalize the research. | Enable execution and reproduction of results. |
| 5. Documentation and communication artifacts | Artifacts that explain how to understand and use the work. | Improve usability, accessibility, and learning. |
| 6. Reproducibility and infrastructure artifacts | Artifacts that support execution across environments. | Ensure reproducibility and facilitate reuse. |
| 7. Research outputs as artifacts | Artifacts traditionally seen as outputs that can also be reused. | Connect the artifact ecosystem to the published work. |

Examples by category: <!-- Source: MenziesEtAl2018 - - DamascenoStruber2021 -->

| Artifact type | Examples |
|---|---|
| 1. Conceptual and scientific | - Motivational or challenge statements<br> - Hypotheses<br> - Baseline results<br> - New findings<br> - Negative results<br> - Future work directions<br> - Annotated or structured bibliographies<br> |
| 2. Methodological | - Study instruments (e.g., surveys, interview scripts)<br> - Study protocols <br> - Sampling procedures<br> - Statistical tests and analysis rationale<br> - Checklists for study design<br> - Patterns (best practices)<br> - Anti-patterns (common pitfalls) |
| 3. Data | - Raw datasets<br> - Processed datasets<br> - Derived datasets<br> - Data documentation |
| 4. Implementation | - Analysis or visualization scripts<br> - Programs implementing algorithms<br> - Executable models<br> - Pipelines and workflows |
| 5. Documentation and communication | - README files<br> - Execution guides<br> - Tutorials and educational materials<br> - Commentary on scripts or analysis<br> - Informative visualizations <br> - Figures and tables used in the paper |
| 6. Reproducibility and infrastructure | - Configuration and dependency files<br> - Build scripts<br> - Containerization setups (e.g., Docker)<br> - Virtual machines or pre-configured environments<br> - Delivery tools for automated execution |
| 7. Research outputs | - The paper manuscript<br> - Supplementary materials <br> - Figures and tables |

Research artifacts can range from simple non-executable materials, such as datasets, documentation, and study protocols, to fully executable artifacts, including software systems, automated pipelines, and reproducible environments. Even relatively small artifacts (such as the data used to generate figures or the scripts used in the analysis) can significantly improve transparency beyond what is possible in the paper alone. What matters most is that the artifact is relevant to the study and contributes meaningfully to understanding, verification, reproducibility, or reuse. <!-- Source: ICSE2026 - - MenziesEtAl2018 -->

### 1.4.1. Packaging research artifacts

Research artifacts may require different packaging approaches depending on their nature and how they are intended to be used. Two broad approaches can be distinguished:

- **Simple package:** for non-executable artifacts such as documents, datasets, protocols, or files accessible with common tools. <!-- Source: Survey2026 - - ICSA2025 -->

- **Installation package:** for software systems, tools, scripts, or executable workflows that require installation and execution in a specific environment. <!-- Source: Survey2026 - - NDSS2026 - - DamascenoStruber2021 -->

### 1.4.2. Execution-oriented vs. transparency-oriented artifacts
 <!-- Source: SEFM2024 -->

Research artifacts can also be understood according to how they support verification, reuse, and reproducibility:

- **Execution-oriented artifacts** are primarily designed to support computational reproduction (running software, reproducing analyses, regenerating results, or recreating experimental workflows).
  - Examples: executable scripts, pipelines, notebooks, containers, virtual machines, and automated workflows.
- **Transparency-oriented artifacts** primarily support inspection, interpretation, and understanding. These artifacts may not be directly executable, but they remain essential for explaining the study design, documenting decisions, clarifying procedures, and enabling critical assessment of the research.
  - Examples: study protocols, interview guides, coding manuals, documentation, figures, and methodological descriptions.

Many artifacts combine both roles. For example, notebooks may simultaneously document and execute analyses, while datasets may support inspection alone or become executable when integrated into automated pipelines.

Non-executable artifacts are still valuable research artifacts. Transparency, documentation, and contextualization are fundamental components of reproducible and reusable research.

| Artifact example | Primary role |
|---|---|
| README | Transparency-oriented |
| Survey instrument | Transparency-oriented |
| Interview protocol | Transparency-oriented |
| Dataset | Transparency-oriented or execution-oriented |
| Analysis script | Execution-oriented |
| Jupyter notebook | Both |
| Docker container | Execution-oriented |
| Paper figures | Transparency-oriented |
| Reproduction pipeline | Execution-oriented |

## 1.5. Artifact life cycle

Research artifacts evolve throughout the research process, from early planning and development to publication, reuse, and long-term preservation. Thinking in terms of a life cycle helps ensure that artifacts are not only created, but also properly prepared, shared, and maintained. <!-- Source: Montgomery2024 -->

<!-- Source: Montgomery2024 -->
| Stage | What to do | Why it matters |
|---|---|---|
| 1. Collect | Gather all materials produced or used during the research (continuously, not only at the end). Includes data, code, scripts, protocols, and supporting resources. | Missing or incomplete materials are one of the main barriers to reproducibility. |
| 2. Document | Clearly describe the artifact: purpose, scope, organization, authorship, relation to the paper, and execution instructions when applicable. | An undocumented artifact is effectively unusable. |
| 3. License | Define how others can use, modify, and share the artifact. Use appropriate open licenses (e.g., MIT or Apache for code; CC BY for data). | Without a clear license, reuse is legally uncertain. |
| 4. Archive | Store artifacts in reliable repositories that support long-term preservation, persistent identifiers, and versioning. | Personal websites and temporary links are not reliable for long-term access. |
| 5. Share | Make artifacts visible and accessible to the research community. Link them directly in the paper. | Artifacts only contribute to science if others can find and access them. |

The practical guidance for each of these stages (how to prepare, document, ensure reproducibility, publish, and maintain artifacts) is covered in the subsequent modules.

## 1.6. Key characteristics of good research artifacts

Good artifacts are not required to be perfect or exhaustive to be valuable. What matters most is that the artifact is relevant to the study and contributes meaningfully to understanding, verifying, or extending the research. These qualities can be understood through three complementary dimensions. <!-- Source: ICSE2026 -->

### 1.6.1. Usability - *Can others understand and use it?*

Good artifacts should be understandable and usable without requiring extensive interpretation from the paper authors.

<!-- Source: Survey2026 - - DamascenoStruber2021 -->
- **Well-documented.** Clearly describe purpose, structure, organization, dependencies, execution process, and expected outputs.
  - README files, execution instructions, metadata, inline comments in scripts.
- **Self-contained.** Include all necessary components, or clearly specify external dependencies and how to obtain them.
  - Datasets, scripts, configuration files, dependency versions, environment specifications.
- **Consistent.** Remain aligned with the paper and its claims, figures, tables, and execution procedures.

### 1.6.2. Reproducibility - *Can others run and verify it?*

Good artifacts should allow others to independently execute the research workflow and verify how results were produced.

<!-- Source: Survey2026 - - DamascenoStruber2021 -->
- **Executable.** Run with reasonable effort using the provided instructions and environment specifications.
  - Avoid undocumented manual setup, hidden dependencies, or excessive configuration effort.
- **Automated.** Minimize manual intervention whenever possible. Automation reduces human error and improves consistency.
  - Automated pipelines, preprocessing scripts, and automatic regeneration of figures and tables.
- **Verifiable.** Allow others to independently inspect and validate the research process and its outputs.
  - Provide access to intermediate outputs, analytical procedures, and generated results.

### 1.6.3. Reusability - *Can others build upon it?*

Well-prepared artifacts may support uses beyond the original study. This includes secondary analyses, benchmarking, teaching, comparative studies, or integration into future research workflows. <!-- Source: BeyerWinter2025 -->

<!-- Source: Survey2026 - - DamascenoStruber2021 -->
- **Legally compliant.** Include clear licensing and respect ethical, legal, and privacy constraints.
  - This includes software licenses, data usage permissions, consent restrictions, third-party dependency compliance.
- **Preserved.** Store in reliable repositories with long-term access.
  - Temporary or personal hosting solutions may become unavailable over time.
- **FAIR-aligned.** Follow FAIR principles so they can be found, accessed, integrated, and reused.
  - This includes rich metadata, standardized formats, searchable repositories, explicit relationships between artifacts.

-----

# Module 2 - Planning and artifact organization

Open Science requires effort beyond simply uploading files. Data, scripts, figures, and other materials often need organization, documentation, cleaning, and anonymization before they can be meaningfully shared. Careful planning from the start of the project is essential to streamline this process and maximize its efficacy. <!-- Source: MendezEtAl2020 - - ZeeReich2018 - - Survey2026 -->

## 2.1. Learning objectives

By the end of this module, you will be able to:

- Integrate artifact preparation into the research process from its early stages.
- Organize research materials into a structure that supports sharing, reproducibility, and reuse.
- Select appropriate file formats for different types of research materials.
- Separate raw, processed, and derived data while preserving data provenance and traceability.
- Apply consistent naming and repository organization practices.
- Plan for data sharing constraints, including ethical, legal, licensing, consent, and privacy considerations.
- Align artifact organization and contents with the associated publication.
- Anticipate reuse requirements when making early decisions about artifact structure and resources.

## 2.2. Artifact-oriented workflow

Two approaches can be distinguished in how researchers integrate artifacts into their research workflow. An artifact-last workflow treats artifact preparation primarily as a final step, whereas an artifact-oriented workflow considers artifacts throughout the research process, from the early stages of the study. <!-- Source: R1-suggestion -->

Treat artifact preparation as an ongoing activity, not a final packaging step. <!-- Source: MendezEtAl2020 - - Survey2026 - - ACMSIGPLAN -->

<!-- Source: Survey2026 -->
| Artifact-last workflow | Artifact-oriented workflow |
|---|---|
| Artifacts prepared only near submission | Artifacts developed continuously throughout the project |
| Data scattered across tools and folders | Structured and versioned data |
| Intermediate files overwritten or lost | Intermediate steps version-controlled |
| Key decisions undocumented | Decisions and results traceable |
| Manual, undocumented steps | Scripted and traceable processes |
| Collect data manually and store in spreadsheets | Use scripts to collect and store data in structured formats |
| Reconstruct workflow at the end | Maintain documentation throughout the process |
| Run analyses through manual steps | Automatically generate results, figures, and tables |
| High effort at submission time | Lower, incremental effort at submission time |
| Limited reproducibility, even by original authors | Reproducibility integrated into the workflow |
| Collaboration harder due to missing context | Shared workflows facilitate collaboration and onboarding |

In an artifact-oriented workflow, the final package is often already close to publication quality by the end of the project, requiring minimal additional preparation. <!-- Source: Survey2026 -->

### 2.2.1. Planning early

Early planning helps researchers: <!-- Source: ACMSIGPLAN - - Survey2026 - - SEFM2024 -->

- Improve repository organization from the start.
- Reduce rework at the end of the project.
- Improve traceability of decisions and results.
- Preserve version history and avoid losing intermediate outputs.
- Facilitate inspection, validation, extension, and comparison across studies.
- Anticipate ethical, legal, institutional, and consent-related constraints for data sharing.

Support from co-authors also makes the process smoother. <!-- Source: Survey2026 -->

Even when full sharing is not possible, plan appropriate documentation, metadata, anonymization strategies, and access conditions throughout the research process. <!-- Source: Survey2026 --> <!-- SaundersKitzingerKitzinger2015 -->

Structure your project so that it can be directly shared as a replication package. Integrate all necessary components (data, code, documentation) consistently from the beginning. <!-- Source: ACMSIGPLAN - - Survey2026 - - SEFM2024 -->

Without an artifact-oriented approach, data may become disorganized or partially lost, important decisions may remain undocumented, and results may become difficult to reproduce, even by the original authors. <!-- Source: ACMSIGPLAN - - Survey2026 - - SEFM2024 -->

When the research involves sensitive or restricted data, ethical and legal considerations should also be anticipated at this stage. See [Module 5](#module-5---data-privacy-and-ethics) for guidance.

### 2.2.2. Planning for reuse

Well-prepared artifacts may support uses beyond the original study. This includes secondary analyses, benchmarking, teaching, comparative studies, or integration into future research workflows. <!-- Source: BeyerWinter2025 -->

Reusability is not an afterthought, it depends on decisions made early in the project: <!-- Source: Survey2026 - - BeyerWinter2025 - - DamascenoStruber2021 -->
- Consider licensing conditions that allow reuse, modification, and redistribution.
- Prefer open-source implementations and resources that others can access independently. <!-- Source: Survey2026 -->
- Structure code as modular components whenever possible. <!-- Source: Survey2026 -->
- Structure and document datasets with potential reuse beyond the original study in mind. <!-- Source: Survey2026 -->
- Use public benchmarks and datasets that others can also access and run independently. <!-- Source: Survey2026 -->
- Avoid relying on unstable external resources. When external datasets, APIs, or repositories are required, consider their versioning and long-term availability.

For guidance on documenting an artifact for reuse, including the Reusability Guide and extension scenarios, see [Module 9](#module-9---reusability-and-extension).

## 2.3. File formats

### 2.3.1. Choosing file formats early

Decide on file formats at the start of the project. Changing formats near the end may require time-consuming conversions or recreation of important files. <!-- Source: BeyerWinter2025 - - Survey2026 -->

Prefer open, widely supported, and well-documented formats. Avoid proprietary or tool-specific formats whenever suitable alternatives exist. <!-- Source: BezjakEtAl2018 - - Survey2026 - - BeyerWinter2025 - - ETAPS2025 - - DamascenoStruber2021 -->

### 2.3.2. Considering format suitability

When possible, prefer formats that are standard within the relevant research community and have stable, open-source readers available. <!-- Source: ETAPS2025 - - BezjakEtAl2018 - - Survey2026 - - DamascenoStruber2021 - - BeyerWinter2025 - - BarowyEtAl2023 -->

For common content types, the following formats can be considered:

<!-- Source: ETAPS2025 - - BezjakEtAl2018 - - Survey2026 - - DamascenoStruber2021 - - BeyerWinter2025 - - BarowyEtAl2023 -->
| Content type | Recommended formats |
|---|---|
| Text and documentation | TXT, Markdown (MD), ODT, PDF/A, XML, HTML |
| Tabular data | CSV, TSV, JSON |
| Data interchange | JSON, XML, YAML |
| Databases | SQLite, CSV dumps |
| Images | TIFF, PNG, JPG, SVG |
| Audio | WAV, FLAC, OPUS |
| Video | MPEG2, VP8, VP9, AV1, Motion JPEG 2000 (MJ2) |
| Virtual Machine (VM) | OVA, OVF |
| Compressed archives | ZIP, TAR.GZ, TBZ2 |

Additional format guidelines: <!-- Source: ETAPS2025 - - BezjakEtAl2018 - - Survey2026 - - MendezEtAl2020 - - DamascenoStruber2021 - - Padhye2019 -->

- Avoid Excel-only formats, binary spreadsheets, proprietary database exports, and proprietary word processor, binary, or compression formats when suitable open alternatives are available. <!-- Source: MendezEtAl2020 - - DamascenoStruber2021 -->
- Prefer CSV or Markdown over LaTeX source for tables. <!-- Source: Padhye2019 -->
- Prefer machine-readable formats for automated and reproducible workflows. <!-- Source: MendezEtAl2020 -->
- When both human- and machine-readable representations are valuable, provide both. Avoid spreadsheet formats as the sole representation of research data.However, you can provide CSV for automation and spreadsheet formats for manual inspection. <!-- Source: MendezEtAl2020 -->

For guidance on file formats and long-term preservation, see [Module 8](#module-8---preservation-versioning-and-maintenance).

## 2.4. Repository organization

The repository structure should capture the essence of the research process, making it clear how the study was conducted and how results were produced. <!-- Source: MendezEtAl2020 - - Survey2026 - - DamascenoStruber2021 -->

Discuss and align the repository structure with collaborators early in the project to reduce inconsistencies and facilitate artifact preparation later. <!-- Source: Survey2026 -->

### 2.4.1. Folder structure

The folder structure should reflect the research workflow. <!-- Source: MendezEtAl2020 - - Survey2026 - - DamascenoStruber2021 -->

This structure should later be documented for external users so that they can navigate the artifact and understand the role of its components. See [Module 3](#module-3---documentation), section 3.4, for guidance on documenting the repository structure.

#### 2.4.1.1. Separating raw and processed data

Never manipulate original data files directly. Always generate derived files through scripts, stored in separate directories. <!-- Source: MendezEtAl2020 -->

- Keep original data in a dedicated folder (e.g., `data-raw/`). <!-- Source: MendezEtAl2020 -->
- Store cleaned/transformed data in a separate folder (e.g., `data-clean/`). <!-- Source: MendezEtAl2020 -->
- Store cleaning scripts alongside the cleaned data to make the transformation reproducible. <!-- Source: MendezEtAl2020 -->

Mixing raw and processed data in the same folders risks accidentally overwriting files, losing intermediate results, or making data transformations untraceable. <!-- Source: MendezEtAl2020 -->

#### 2.4.1.2. Naming conventions

Good naming conventions improve readability and reduce ambiguity, especially in collaborative or long-running studies. <!-- Source: MendezEtAl2020 - - Survey2026 -->

The critical practice is to **align file and folder names with the terminology used in the paper**. Variable names, dataset labels, script names, and output files should map directly to the experimental setup and results described in the publication. <!-- Source: Survey2026 - - USENIXSec2026 - - DamascenoStruber2021 -->

<!-- Source: MendezEtAl2020 -->
| Descriptive names ✅ | Generic names ❌ |
| --- | --- |
| - `clean_survey_data.csv` <br> - `generate_figures.py` <br> - `rq1_results.csv` <br> - `interview_protocol.md` | - `final.csv` <br> - `script2.py` <br> - `new_results.xlsx` <br> - `misc_notes.txt` |

Consistency matters more than any particular naming style. Avoid inconsistent abbreviations, duplicated patterns, or filenames that depend on personal interpretation. <!-- Source: USENIXSec2026 - - Survey2026 -->

## 2.5. Data curation

Data curation focuses on preserving the quality, traceability, and integrity of data throughout the research process. Researchers should keep track of how data are collected, transformed, filtered, and organized so that these decisions remain traceable when the artifact is prepared for sharing. <!-- Source: ZeeReich2018 - - Survey2026 -->

The resulting information should later be documented for external users as part of the artifact documentation. See [Module 3](#module-3---documentation), section 3.5.2, for guidance on documenting datasets.

### 2.5.1. Tracking data collection and transformation

Throughout the research process, keep track of how data are collected, transformed, filtered, and organized. <!-- Source: ETAPS2025 - - DamascenoStruber2021 - - ZeeReich2018 - - Survey2026 -->

Record the decisions and procedures that affect the resulting data, including: <!-- Source: ETAPS2025 - - DamascenoStruber2021 - - ZeeReich2018 -->

- How the data were collected.
- Preprocessing and cleaning procedures.
- Inclusion and exclusion criteria.
- Transformations and filtering applied to the data.
- The organization of original and derived data.

Preserve sufficient information to trace how the data used in analyses or reported results were derived from the original data. <!-- Source: MendezEtAl2020 - - Survey2026 -->

For data involving human participants or other sensitive information, identify anonymization, ethical, legal, or licensing constraints during the research process rather than addressing them only when preparing the artifact for sharing. See [Module 5](#module-5---data-privacy-and-ethics) for detailed guidance.

### 2.5.2. Identifying data sharing constraints

Identify early whether the data can be shared and what restrictions may apply. Consider ethical, legal, contractual, licensing, consent, and privacy constraints throughout the research process. <!-- Source: ZeeReich2018 - - Survey2026 -->

When full public sharing is not possible, plan early for the documentation and access conditions that will be needed when the artifact is prepared for sharing. <!-- Source: Survey2026 -->

See [Module 5](#module-5---data-privacy-and-ethics) for strategies for handling sensitive or restricted data and [Module 3](#module-3---documentation), section 3.7, for guidance on documenting non-shared components and controlled access.

-----

# Module 3 - Documentation

Good documentation is one of the most important factors in artifact adoption. Without it, even well-structured and technically sound artifacts may remain unusable. Research artifacts are not only technical deliverables, they are communication mechanisms. Well-documented artifacts help others understand the study design, execution workflow, assumptions, limitations, and expected outputs without requiring direct contact with the authors. <!-- Source: WilsonEtAl2017 - - Survey2026 - - DamascenoStruber2021 -->

In practice, documentation is often treated as an afterthought. This results in incomplete instructions, missing context, and artifacts that are difficult or impossible to reuse. Preparing documentation incrementally throughout the research process, starting with a brief explanatory comment at the beginning of each script, significantly reduces this problem. <!-- Source: WilsonEtAl2017 - - Survey2026 -->

## 3.1. Learning objectives

By the end of this module, you will be able to:

- Explain the role of documentation in making research artifacts usable, reproducible, and reusable.
- Distinguish operational, structural, and scientific documentation.
- Write documentation that enables users to install, execute, navigate, and understand an artifact.
- Document requirements, execution steps, expected outputs, execution time, resources, parameters, and error recovery procedures.
- Document the structure and purpose of artifact components.
- Connect artifact components and outputs to the methods, results, and claims reported in the publication.
- Document artifact scope, limitations, unsupported claims, and non-shared components transparently.
- Structure a README as an effective entry point to the artifact.

## 3.2. Levels of artifact documentation

Good artifact documentation operates at three complementary levels. All three are necessary, because an artifact that is well-organized but lacks execution instructions is unusable; one with step-by-step instructions but no connection to the paper cannot be independently validated; one that reproduces results but provides no structural overview is difficult to inspect and extend. <!-- Source: Survey2026 -->

| Level | Purpose | Key questions answered |
|---|---|---|
| Operational | Explains how to install, execute, and validate the artifact. | - How do I run this?<br> - What do I need?<br> - What output should I expect? |
| Structural | Describes how the artifact is organized. | - Where is everything?<br> - What does each folder and file contain? |
| Scientific | Explains how the artifact connects to the research and the paper. | - Which claims does this support?<br> - How do outputs relate to the paper? |

## 3.3. Operational documentation

Write operational documentation clearly enough that someone with reasonable technical knowledge can install and execute the artifact, understand the expected behavior and outputs, and identify common execution problems without background knowledge about the study. <!-- Source: Survey2026 -->

### 3.3.1. Assumed background and requirements

State the expected technical background of the user at the beginning. Document the requirements needed to use the artifact, including: <!-- Source: Survey2026 - - ICSE2026 - - ETAPS2025 - - DamascenoStruber2021 -->

- Operating system and hardware requirements.
- Software dependencies and their versions.
- Estimated execution time and storage requirements.
- Any credentials, access permissions, or software licenses required.

See [Module 4](#module-4---environments-dependencies-and-automation) for guidance on specifying and isolating execution environments.

Avoid overstating platform support. Clearly state which platforms have been tested and avoid claiming compatibility that has not been verified. Document hardware architecture assumptions (e.g., x86, ARM) explicitly. Architecture incompatibilities may prevent reproduction even when all software dependencies are available. <!-- Source: Survey2026 - - ETAPS2025 -->

If the artifact requires specialized hardware, provide instructions for how users can gain access to those resources. <!-- Source: Survey2026 - - ETAPS2025 -->

### 3.3.2. Step-by-step execution instructions

Provide complete, step-by-step instructions for: <!-- Source: Survey2026 - - DamascenoStruber2021 -->

- Obtaining and unpacking the artifact.
- Preparing the environment and installing dependencies.
- Executing experiments or analyses.
- Interpreting and locating outputs.
- Extending or uninstalling the artifact, when applicable.

Tailor the instructions to the type of artifact. For example: <!-- Source: ETAPS2025 - - DamascenoStruber2021 -->

- Data artifacts should emphasize provenance, context, ethical and legal conditions, and storage requirements.
- Software artifacts should explain how to use the tool and reproduce the relevant paper results.; and
- Proof artifacts should explain how their components relate to the formalisms presented in the paper. 

All commands must be listed explicitly and formatted for copy-paste into a terminal. For each command, specify: <!-- Source: Survey2026 - - Padhye2019 -->

- Which directory to run it from.
- What output files it generates and where they are located.
- Whether it creates new directories, accesses the internet, or uses significant disk space.
- What output to expect if execution is successful.

Write the documentation as if you are a stranger to your own work. Do not assume users share your context, tools, or environment. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

### 3.3.3. Execution time and resource expectations

Document the time and resources required to use the artifact:

- Document how long each major step takes on the reference hardware and indicate the main resource requirements. <!-- Source: Survey2026 - - ICSA2025 - - DamascenoStruber2021 -->
- Provide approximate execution times for the main steps. <!-- Source: Survey2026 - - DamascenoStruber2021 - - Padhye2019 -->
- Indicate relevant CPU, GPU, memory, storage, or other resource requirements. <!-- Source: Survey2026 - - USENIXSec2026 - - DamascenoStruber2021 -->

An overview of the expected duration can help users plan the execution. For example: <!-- Source: Padhye2019 -->

```
## Overview

* Getting started    (10 human-minutes + 5 compute-minutes)
* Build              (2 human-minutes + 1 compute-hour)
* Run experiments    (5 human-minutes + 3 compute-hours)
* Validate results   (30 human-minutes + 5 compute-minutes)
* Reuse guide        (20 human-minutes)
```

When execution involves substantial waiting time, indicate this clearly so users can distinguish expected behavior from failures. Progress messages or estimated duration for each execution step can further reduce uncertainty during reproduction attempts. <!-- Source: BarowyEtAl2023 - - DamascenoStruber2021 - - Survey2026 -->

If the artifact takes a very long time to run fully, consider providing alternatives that allow users to verify or partially reproduce the results with less time or fewer resources:

- A shorter representative subset that allows users to verify core functionality first. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- Alternative configurations that run with fewer resources and still produce results that approximate those in the paper. <!-- Source: Padhye2019 -->
- Reduced input datasets or pre-computed intermediate results. <!-- Source: Survey2026 - - Padhye2019 -->
- Alternative procedures to run partial reproduction.  <!-- Source: Survey2026 -->
- A screencast as an alternative. <!-- Source: Survey2026 -->

Individual steps should not take longer than 8–12 hours to execute. <!-- Source: Survey2026 -->

When approximate or partial execution is provided, include pre-computed outputs from the full experiments alongside approximate results, in the same format. This allows reviewers to compare the two and build confidence that the full run would be consistent with the paper. <!-- Source: Padhye2019 -->

### 3.3.4. Documenting parameters and configurations

Document everything that could significantly affect results: <!-- Source: ACMSIGPLAN - - Survey2026 - - DamascenoStruber2021 -->

- Parameter values and default settings.
- Software and dependency versions.
- Hardware specifications used in the original experiments.
- Execution configurations: thread counts, memory limits, random seeds, training configurations, workload sizes, cache sizes.

When artifacts involve training, tuning, calibration, or iterative design decisions, clearly distinguish data used during development from data used for evaluation. <!-- Source: ACMSIGPLAN -->

If the artifact performs potentially risky operations (privileged execution, network access, large file creation, sensitive data handling), flag these clearly at the top of the README, before the installation instructions. For each command, clarify whether it: <!-- Source: WOOT2025 - - Survey2026 - - Padhye2019 -->
- Creates or modifies files.
- Accesses the internet.
- Uses significant disk space.
- Requires elevated permissions.

### 3.3.5. Error recovery

- Document expected failures and known tool limitations explicitly. If the artifact produces specific error messages or warnings that are expected and safe to ignore, state this clearly. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- Help users identify failing steps quickly. <!-- Source: Padhye2019 -->
  - Cascading errors, where one undocumented failure causes later steps to fail silently, are among the most frustrating experiences for artifact users. <!-- Source: Padhye2019 -->

- Troubleshooting. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
  - Include common installation and runtime errors with solutions.
  - Known issues and limitations.
  - Frequently asked questions
  - A link to a GitHub Issues page or support forum, when available.

Being transparent about problems is more helpful than presenting the artifact as flawless. Users appreciate knowing upfront if something has only been tested on specific machines or has known edge cases. <!-- Source: Survey2026 -->

## 3.4. Structural documentation

Structural documentation translates the repository organization set up in [Module 2](#module-2---planning-and-artifact-organization) into clear explanations for external users. It makes it possible for them to navigate the repository efficiently without having to read the entire paper first. <!-- Source: Survey2026 -->

### 3.4.1. Folder structure

Document the repository structure inside the artifact itself. It is especially important in large repositories with datasets, scripts, intermediate files, and generated outputs. <!-- Source: MendezEtAl2020 - - Survey2026 - - DamascenoStruber2021 -->

A documentation block describing the folder structure should appear in the main README. Example: <!-- Source: MendezEtAl2020 - - Survey2026 - - DamascenoStruber2021 -->

```
project/
├── data-raw/         ## Original, unmodified collected data
├── data-clean/       ## Processed datasets derived from raw data
├── scripts/          ## Data collection, cleaning, and analysis scripts
├── figures/          ## Generated plots and visualizations
├── docs/             ## Supplementary documentation and protocols
└── README.md         ## Repository overview and usage instructions
```

For each directory, describe: <!-- Source: Survey2026 - - ETAPS2025 -->
- Its purpose and the types of files it contains.
- The purpose of each major directory and the role of key files within it.
  - Whether its contents are essential or auxiliary.
  - Which files are required to execute or reproduce the artifact.
- Where raw and processed data are stored.
- Where scripts, execution entry points, and generated results are located.
  - The relationships between scripts and outputs.

Provide a table of contents or navigation index in the README when the repository is large or complex. <!-- Source: Survey2026 -->

See [Module 2](#module-2---planning-and-artifact-organization), section 2.4, for guidance on how to structure and name folders.

### 3.4.2. In-folder documentation

For complex projects, place additional documentation files within specific folders rather than concentrating all explanations in the root README. A brief description of data organization inside the `data-raw/` or `data-clean/` folder, or usage notes inside the `scripts/` folder, reduces the cognitive load required to navigate the artifact and helps users locate relevant context close to the files it describes. <!-- Source: ETAPS2025 - - Survey2026 - - DamascenoStruber2021 -->

### 3.4.3. Naming conventions

The guidance for creating naming conventions is covered in [Module 2](#module-2---planning-and-artifact-organization), section 2.4.1.2. From a documentation perspective, the key complement is: when terminology changed between artifact development and paper submission - for example, if a concept was renamed after the analysis was complete - include a brief explanation of old versus new terminology in the README, before the execution instructions. This helps users map the paper's language to the files they are working with. <!-- Source: Survey2026 - - MendezEtAl2020 - - DamascenoStruber2021 -->

### 3.4.4. Distinguishing essential from auxiliary components

Clearly distinguish which components are required for execution or reproduction and which are supplementary or optional. Explicit labeling helps users prioritize attention and troubleshoot more effectively. <!-- Source: Survey2026 - - ETAPS2025 -->

## 3.5. Scientific documentation

Scientific documentation explains how the artifact connects to the research study and the published paper, allowing reviewers and future researchers to understand which claims are supported, how outputs were produced, and how results relate to the paper. <!-- Source: Survey2026 -->

### 3.5.1. Artifact purpose statement

Begin with a clear explanation of what the artifact is, what it does, and how it supports the paper. Go beyond "this is a replication package of..." and explain why the artifact matters and what it enables. <!-- Source: ICSE2026 - - Survey2026 -->

The purpose statement should: <!-- Source: Survey2026 -->

- Briefly describe the study goal and the role of the artifact.
- List the main components included.
- Briefly explain how the artifact supports the study and its reported results.
- Explain why certain claims may not be supported, if applicable.

### 3.5.2. Data description

When the artifact includes datasets, document the information external users need to understand and reuse the data. Document: <!-- Source: Survey2026 - - ETAPS2025 - - DamascenoStruber2021 - - MODELS2025 -->

- The meaning of each variable, feature, or field.
- How the data were collected and why.
- Preprocessing and cleaning procedures.
- Inclusion and exclusion criteria.
- Storage requirements.
- Any restrictions that affect how the data can be interpreted or reused.

For technical datasets, provide precise documentation of each data field, including variable names, metrics, units, and file structures. <!-- Source: MODELS2025 -->

For non-executable artifacts, such as interview guides, protocols, codebooks, or qualitative datasets, also explain how the materials can be interpreted and reused by other researchers or practitioners. <!-- Source: RE2026 - - Survey2026 -->

For ethical, privacy, and legal considerations affecting data sharing, see [Module 5](#module-5---data-privacy-and-ethics).

### 3.5.3. Mapping outputs to paper results

Do not ask users to run scripts without explaining what to expect. Provide an explicit mapping between artifact outputs and paper results. <!-- Source: Padhye2019 - - DamascenoStruber2021 -->

For each relevant output, specify: <!-- Source: Survey2026 -->

- Which figure, table, subsection, or claim in the paper it corresponds to.
- Where the output file is located within the repository.
- How to interpret the output relative to the paper.
- How long it takes to generate.

The mapping should allow users to identify which artifact components and execution steps support each reported result.

When practical, include archived expected outputs in a separate directory for comparison during execution and evaluation. Keep these reference outputs separate from generated outputs so that they are not overwritten during testing. <!-- Source: Padhye2019 - - Survey2026 -->

A simple mapping table is often the clearest approach: <!-- Source: Rapoport -->

| Paper element | Location in the paper | Artifact file      |
|---------------|-----------------------|--------------------|
| Figure 3      | Section 4             | `scripts/fig3.py`  |
| RQ2 analysis  | Section 5             | `analysis/stats.R` |
| Survey data   | Page 7                | `data/survey.csv`  |

The paper should remain understandable without requiring readers to inspect the artifact. Artifact documentation complements the paper by supporting execution, inspection, and reuse. It should not serve as a container for unrelated scientific content. <!-- Source: IPDPS26 -->

### 3.5.4. Handling comparative evaluations

When the artifact includes comparisons against other systems: <!-- Source: ACMSIGPLAN - - Survey2026 -->

- Include a version of each compared system and instructions for reproducing the comparison numbers used in the paper.
- If a compared tool crashes on a subset of inputs, note this explicitly as expected behavior.
- Clearly document experimental conditions for all compared systems: configurations, optimization levels, datasets, and preprocessing steps.
- Document any differences in configurations, hardware, or datasets between compared systems. 

## 3.6. How to write an effective README

The README is the primary entry point for anyone working with the artifact. It should be clear, complete, and honest, allowing users to understand what the artifact does, how to use it, and what to expect without needing to contact the authors. <!-- Source: ZimmermannEtAl2023 - - Survey2026 -->

Include operational details that may seem trivial to the original authors but are essential for external users. <!-- Source: ETAPS2025 - - Survey2026 -->

### 3.6.1. Recommended README sections

A good README file should have: <!-- Source: Survey2026 - - RE2026 - - DamascenoStruber2021 - - ICSE2026 - - ETAPS2025 -->

| README section | Description | Where to read more about | Importance |
| --- | --- | --- | --- |
| Summary of artifacts | A brief description of what the artifact contains: datasets, scripts, models, results, or any combination. This is not the same as the paper abstract - it describes the artifact itself, not the research it supports. | - | Essential |
| Operational documentation pointer | A short statement directing the reader to the operational documentation: system requirements, setup steps, execution instructions, expected execution time, and troubleshooting. If the artifact is small enough, this content may be embedded directly in the README rather than placed in a separate file. | section 3.3 | Essential |
| Structural documentation pointer | A short statement directing the reader to the structural documentation, including the repository map and the purpose of each directory and file. | section 3.4 | Essential |
| Scientific documentation pointer | A short statement directing the reader to the scientific documentation, explaining how the artifact connects to the claims, methods, and figures in the paper. | section 3.5 | Essential |
| Potential risks | Any known risks that users should be aware of before executing the artifact: high resource consumption, external service calls, modification of system state, or irreversible operations. | section 3.3.4 | Context-dependent |
| Reusability guide | A brief note on how the artifact can be reused beyond the original study: which components are general-purpose, what would need to change for a different dataset or context, and what the artifact was explicitly not designed to support. | section 9.2 | Context-dependent |
| Licenses | The license governing use and redistribution of the artifact. If different components carry different licenses, list each separately. | section 7.6 | Essential |
| Citation | How to cite the artifact. If a CITATION.cff file is present, the README should point to it. If not, provide the recommended citation inline. | section 7.7.2 and 7.7.3 | Essential |
| Authors and contact | The names of the people responsible for the artifact and a contact address for questions, bug reports, or collaboration requests. | section 7.7.2 | Essential |

Include access to the accepted paper, either as a PDF within the artifact repository or as a link to a preprint in an archival repository (e.g., arXiv).

## 3.7. Documenting limitations and non-shared components

Transparency about what the artifact does not include is as important as describing what it does. Missing or unexplained omissions erode trust and make independent validation harder. <!-- Source: Survey2026 - - IPDPS26 -->

### 3.7.1. Scope and unsupported claims

An artifact does not need to support every claim in the paper, but unsupported claims must be clearly justified. For each claim in the paper: <!-- Source: Survey2026 - - Padhye2019 -->

- State whether it is supported by the artifact.
- For supported claims, explain how the artifact provides that support.
- For unsupported claims, explain why they are omitted (e.g., proprietary data, specialized hardware, ethical constraints, excessive computation time).

Explicitly listing all claims helps distinguish bugs that invalidate the paper's results from bugs that are simply a normal part of the software engineering process. <!-- Source: Survey2026 -->

Claims about reproducibility, applicability, automation, scalability, or platform support should reflect the actual conditions under which the artifact was evaluated. Overly broad claims are problematic when based on a limited subset. <!-- Source: ACMSIGPLAN -->

When using simplified experiments or toy examples, the documentation should clarify how the provided evaluation relates to real-world scenarios when the artifact claims benefits for realistic applications. <!-- Source: ACMSIGPLAN -->

### 3.7.2. Non-shared components

When components cannot be disclosed due to legal, contractual, ethical, or proprietary restrictions, document this explicitly rather than leaving it implicit. <!-- Source: IPDPS26 - - Survey2026 -->

Examples of disclosure statements: <!-- Source: IPDPS26 -->

- *"Source code not available due to proprietary restrictions."*
- *"Dataset cannot be publicly shared due to licensing constraints."*
- *"Raw interview transcripts are not included due to participant privacy. The coding schema and study protocol are provided instead."*

When possible, provide intermediate analysis artifacts that help explain how conclusions were derived from the available data and procedures.

When the paper has no artifacts at all, explain in the paper itself why no artifact is provided, given the broad range of materials that can constitute an artifact. <!-- Source: IPDPS26 - - Survey2026 -->

Providing partial transparency is always more useful than providing no documentation at all. <!-- Source: IPDPS26 - - BeyerWinter2025 -->

For strategies for sharing restricted or sensitive data, see [Module 5](#module-5---data-privacy-and-ethics), section 5.4.

### 3.7.3. Disclosure statement

Include a concise disclosure statement in the artifact documentation covering information that may affect the interpretation, use, evaluation, or transparency of the artifact. <!-- Source: Survey2026 -->

The disclosure statement should address, when applicable:

- Conflicts of interest or funding sources relevant to the artifact.
- Limitations or constraints of the artifact.
- Ethical considerations, such as data handling conditions or consent agreements.
- Components or materials that are not included in the shared artifact and the reasons for their exclusion.

The disclosure statement is distinct from the [Data Availability Statement (DAS)](#78-data-availability-statements-das) in the paper. The former provides transparency about the artifact, while the latter declares the availability and access conditions of the materials supporting the study.

### 3.7.4. Impact of anonymization on interpretability

When data have been anonymized before sharing, document the impact on the data's interpretability. Explain how anonymization may reduce clarity or completeness, and indicate any limitations this introduces for reproduction or reuse. <!-- Source: SaundersKitzingerKitzinger2015 - - Survey2026 -->

See [Module 5](#module-5---data-privacy-and-ethics) for anonymization strategies and methods.

### 3.7.5. Contextual variability in empirical studies

In studies involving human participants, exact reproducibility may not be achievable. Artifacts should: <!-- Source: Survey2026 - - DamascenoStruber2021 -->

- Document the experimental context clearly.
- Support replication of procedures rather than exact results.
- Explain how results may vary across different contexts or participant populations.

### 3.7.6. Controlled data access

When data cannot be made fully public but can be made available under controlled conditions, document: <!-- Source: Survey2026 -->

- The nature of the access restriction.
- The conditions under which access may be granted.
- How users can request access.
- Any relevant governance or approval requirements.

See [Module 5](#module-5---data-privacy-and-ethics) for strategies for sharing restricted data and [Module 7](#module-7---publishing-licensing-and-citation) for repository and publication considerations.

## 3.8. Complementary documentation

Beyond the README, additional forms of documentation can significantly improve artifact usability. <!-- Source: Survey2026 -->

**Inline comments and code documentation.** Comment scripts and code, especially at complex or non-obvious steps. When a paper introduces specific algorithms, heuristics, or implementation strategies, explicitly indicate where these components are implemented in the source code. <!-- Source: BarowyEtAl2023 - - Survey2026 - - DamascenoStruber2021 -->

**Literate programming and notebooks.** R Markdown and Jupyter notebooks, for instance, combine executable code with explanatory text, making the connection between analysis steps and results visible in a single document. <!-- Source: Survey2026 -->

**Tutorials and demonstration videos.** Consider providing a short demonstration video or screencast to illustrate how the artifact works and highlight its main features. Tutorial-style videos are particularly useful when: <!-- Source: ASE2025 - - Survey2026 - - DamascenoStruber2021 -->

- The installation or execution workflow is involved.
- The artifact includes a graphical interface.
- Understanding outputs requires context that is difficult to convey in text alone.

**Additional visual materials.** Architectural diagrams, screenshots, and annotated figures help users understand the artifact structure, expected outputs, and system components. <!-- Source: Survey2026 -->

**Documenting differences from the paper.** Any relevant differences between the artifact and the published paper should be documented explicitly. Examples include: <!-- Source: BarowyEtAl2023 - - Padhye2019 -->

- Bug fixes introduced after submission.
- Updated or modified scripts.
- Datasets modified to remove confidential information.
- Reduced workloads provided for reproducibility purposes.
- Changes in terminology.


When terminology differs between the artifact and the paper, include a brief explanation of old versus new terminology in the README. <!-- Source: Padhye2019 -->

### 3.8.1. Changelogs

When the artifact has multiple released versions, maintain a changelog documenting relevant changes and their potential effects on reproducibility, execution, or reuse. See [Module 8](#module-8---preservation-versioning-and-maintenance), section 8.3.5, for guidance on maintaining changelogs.

-----

# Module 4 - Environments, dependencies, and automation

Publicly sharing code and data alone is often insufficient. Missing environment information, undocumented workflows, manual processing steps, and unclear links between artifacts and publications may still prevent others from validating or extending the research. <!-- Source: Survey2026 - - ACMSIGPLAN -->

The table below summarizes key dimensions of artifact reproducibility and illustrates how artifacts evolve from limited usability to fully reproducible and durable research assets. <!-- Source: SiddiqEtAl2025 -->

<!-- Source: SiddiqEtAl2025 -- - DamascenoStruber2021 -->
| Dimension | Limited artifact | Operational artifact | Durable artifact |
|---|---|---|---|
| Accessibility | No or fragmented artifacts; links missing, private, or ephemeral. | Artifacts hosted but with fragile links (personal cloud, ad-hoc URLs); partial coverage of code, data, and models. | Artifacts versioned and persistently hosted (e.g., PID, archival repository) with clear mapping to experiments. |
| Environment specification | Missing or incomplete environment requirements. | Basic installation steps documented, but incomplete dependency lists and implicit platform assumptions. | Complete, machine-readable environment specification (e.g., lockfiles, container specs) covering OS, libraries, and hardware. |
| Versioning rigor | Floating or unspecified versions. | Some versions documented (e.g., major library versions) but not consistently pinned. | Pinned versions at all hierarchy levels (datasets, models, frameworks, OS), with change logs or manifests. |
| Execution fidelity | No runnable scripts; only high-level prose or pseudo-code. | Pipelines runnable with manual effort (e.g., several shell commands, manual downloads, ad hoc scripts). | End-to-end, automated pipelines or containers that recreate results from scratch with minimal manual steps. |
| Legal openness | Licenses absent, incompatible, or ambiguous. | Some components licensed, but coverage incomplete. | Explicit, compatible licenses for all artifacts required to reproduce results. |

Reproducibility is not a single property. It is a combination of dimensions that determine how easily others can understand, execute, verify, and build upon your work. <!-- Source: Survey2026 - - ACMSIGPLAN -->

## 4.1. Learning objectives

By the end of this module, you will be able to:

- Specify software and hardware dependencies precisely enough to support reproducible execution.
- Configure reproducible and isolated execution environments.
- Select appropriate environment isolation mechanisms according to the artifact and its execution requirements.
- Replace undocumented manual procedures with scripted and automated workflows.
- Automate the generation of research outputs, including figures and tables.
- Structure workflows for modular and incremental execution.
- Apply version control practices that preserve the history and reproducibility of artifact development.
- Identify common environment and workflow practices that can undermine reproducibility.

## 4.2. Reproducible environments

Reproducing results manually is error-prone, difficult to verify, and hard to maintain. Automation makes workflows traceable, repeatable, and independently executable. <!-- Source: Survey2026 -->

Artifacts may become difficult or impossible to execute when environment information is missing. Even when datasets, scripts, and documentation are publicly available, differences in operating systems, software versions, libraries, hardware configurations, or system settings may prevent workflows from executing correctly. <!-- Source: Survey2026 -->

Many reproducibility problems emerge because artifacts implicitly depend on local machine configurations that are never documented. Common examples include missing dependency versions, OS-specific behavior, incompatible libraries, unavailable system tools, or hardcoded environment settings. As a result, workflows that function correctly for the original authors may fail when executed by others on different machines. <!-- Source: Survey2026 -->

Always document the execution environment used to develop and test the artifact: <!-- Source: Survey2026 - - DamascenoStruber2021 -->

- Operating system and kernel version.
- Hardware requirements (performance, storage, or non-commodity peripherals).
- All software dependencies and their exact versions.
- Experiment-specific tools, libraries, or frameworks.
- Any deviation from standard environments, with justification.

Many reproducibility failures stem not from missing scripts or data, but from undocumented or inconsistent execution environments. <!-- Source: Survey2026 -->

### 4.2.1. Dependency specification

Include a dependency specification file in the repository. These files preserve dependency versions, simplify environment reconstruction, and reduce inconsistencies across systems. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

All required dependencies must be explicitly specified with pinned versions. Specify exact versions of all libraries, tools, and dependencies. Incomplete or implicit dependency specifications are one of the most common causes of reproduction failures. <!-- Source: BeyerWinter2025 - - Survey2026 - - DamascenoStruber2021 -->

Remove unused dependencies and installable packages before release to reduce setup complexity and avoid unnecessary installation failures. <!-- Source: Survey2026 -->

### 4.2.2. Environment isolation and portability

Virtual environments, containers, or virtual machines can isolate dependencies and simplify environment setup. Containers may also improve portability by distributing workflows together with the required execution environment. The goal is not to eliminate all setup complexity, but to make the execution environment reproducible across systems. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

- Artifacts should be as **self-contained** as possible. Avoid relying on external services, undocumented configurations, or transient resources. <!-- Source: ETAPS2025 - - ZimmermannEtAl2023 - - Survey2026 -->
- **Avoid runtime downloads** from external services. APIs, remote databases, and third-party repositories may not be available during execution. Include required data and dependencies within the artifact package whenever possible. <!-- Source: ETAPS2025 - - ZimmermannEtAl2023 - - Survey2026 -->
- **Archive critical dependencies.** When external resources are essential, archive or mirror them alongside the artifact. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- **Use isolated environments.** Containers or virtual machines encapsulate dependencies and reduce the impact of changes in the host system. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- Prefer **open-source tools** when suitable alternatives are available, as they allow users to inspect and reproduce the execution environment without depending on proprietary software. <!-- Source: Survey2026 - - ETAPS2025 -->
  - If proprietary tools are unavoidable, identify them as explicit dependencies and indicate how users can obtain and use them. <!-- Source: Survey2026 - - ETAPS2025 -->
- Prefer **open and widely supported formats** for archives, datasets, and documents (e.g., ZIP, TAR.GZ, CSV, JSON, PDF). Community-standard formats reduce maintenance effort and improve interoperability and reuse. <!-- Source: ETAPS2025 -->
- Account for **architecture-specific requirements** (e.g., ARM vs. x86, GPU dependencies, OS constraints) when designing the execution environment. <!-- Source: BeyerWinter2025 - - DamascenoStruber2021 -->
- **Avoid hardcoded paths.** Use repository-relative paths to improve portability. <!-- Source: Survey2026 -->

### 4.2.3. Containers and virtual machines

A pre-built container or VM image is preferable to setup scripts alone. Use virtual machines for stronger isolation that includes the OS. Pre-built images eliminate reliance on external dependencies during the configuration step. <!-- Source: PLDI2025 - - DamascenoStruber2021 -->

- Software artifacts should ideally be contained within a VM or container that includes all dependencies, reducing the likelihood of artifact decay over time. <!-- Source: ZimmermannEtAl2023 -->
- When using Docker, ensure what you distribute is **fully self-contained**. A base container that installs dependencies at runtime reduces artifact size but increases reliance on external systems that may eventually become unavailable. <!-- Source: ZimmermannEtAl2023 - - Survey2026 -->
- Non-software artifacts (e.g., datasets) should be distributed as a single archive. <!-- Source: ZimmermannEtAl2023 -->
  - A container is not necessary for non-executable materials. <!-- Source: ZimmermannEtAl2023 -->
- Ship VMs in a portable format (OVA or OVF). <!-- Source: BarowyEtAl2023 -->
- Always provide the Dockerfile, provisioning scripts, or initialization scripts used to create the environment, not only the pre-built image. <!-- Source: NDSS2026 -->
- Document the internal organization of containers and VMs: where source code, datasets, scripts, generated outputs, and documentation are located. <!-- Source: BarowyEtAl2023 -->

Simple usability improvements help significantly. For example, a terminal already opened in the main artifact directory, or shortcut scripts for common tasks. <!-- Source: BarowyEtAl2023 -->

For lighter-weight isolation, language-level virtual environments are a practical alternative for many types of artifacts. <!-- Source: MendezEtAl2020 -->

### 4.2.4. Virtualized vs. bare-metal execution

Some performance-related experiments may not reproduce accurately in virtualized environments. When this is the case:

- Identify whether virtualization affects the validity of the experiment. <!-- Source: BarowyEtAl2023 -->
- Use bare-metal execution when required by the experimental setup. <!-- Source: BarowyEtAl2023 - - DamascenoStruber2021 -->
- When specialized hardware is required, ensure that the execution environment provides access to the necessary resources. <!-- Source: NDSS2026 - - Survey2026 -->

### 4.2.5. Ease of use

Provide a lightweight execution path that allows users to verify that the artifact is functioning before committing to a full experiment. <!-- Source: Survey2026 -->

- Provide small representative inputs for quick execution when the complete experiment is computationally expensive. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- Divide complex workflows into independently executable parts when appropriate, so users can run and inspect individual stages without executing the entire experiment. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- Automate lengthy setup procedures using scripts, containers, or virtual environments. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

## 4.3. Scripts and workflow automation

Manual, undocumented workflows reduce reproducibility. Scripts make research processes traceable, repeatable, and easier to maintain. <!-- Source: MendezEtAl2020 - - Survey2026 -->

### 4.3.1. Prefer scripted workflows

- Use script-based, version-controllable tools (e.g., R, Python) over point-and-click software (e.g., SPSS without syntax) or binary project files (e.g., Excel). <!-- Source: MendezEtAl2020 - - DamascenoStruber2021 -->
- Automate data preprocessing so that cleaned or derived datasets can be regenerated from the original inputs without manual intervention. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- Store scripts together with the artifact. <!-- Source: MendezEtAl2020 - - DamascenoStruber2021 -->
- Avoid workflow assumptions that depend on local or machine-specific configurations. <!-- Source: Survey2026 -->

### 4.3.2. End-to-end automation

Whenever possible, make the complete workflow, from raw inputs to final outputs, executable through a single command or a minimal sequence of steps. <!-- Source: Survey2026 -->

- Automate build, evaluation, and visualization pipelines. <!-- Source: Survey2026 -->
- Use parameterized scripts with command-line flags so users can customize execution without modifying source code. <!-- Source: Survey2026 -->
- Provide installation or setup scripts when multiple manual configuration steps would otherwise be required. <!-- Source: SEFM2024 -->

### 4.3.3. Modular and incremental execution

For complex or long-running workflows, provide modular and interruptible scripts that allow individual steps to be executed independently. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

- Allow pausing and resuming execution.
- Support running on small input subsets.
- Include **smoke tests** and quick validation steps that confirm core functionality without running the full experiment.
- Provide modular scripts for individual steps of complex or long-running tasks.

If the artifact runs for more than a few minutes, explain how to run it on smaller inputs and how long the full run is expected to take. <!-- Source: PLDI2025 -->

Make workflow steps idempotent whenever possible, so that re-running the same command should produce the same result regardless of how many times it is executed. <!-- Source: Padhye2019 -->

### 4.3.4. Automated figure and table generation

Generate figures, tables, and statistical summaries automatically from data and scripts rather than editing them manually or requiring manual inspection of log files and comparison with the corresponding paper elements. Manual steps can introduce inconsistencies between the artifact and the published results. <!-- Source: BarowyEtAl2023 - - Survey2026 - - DamascenoStruber2021 - - Padhye2019 -->

- Provide scripts to automatically regenerate the tables and figures presented in the paper. <!-- Source: Survey2026 - - DamascenoStruber2021 - - BarowyEtAl2023 -->
- Generate outputs directly from the experimental results used to produce the corresponding paper elements. <!-- Source: Survey2026 - - DamascenoStruber2021 - - BarowyEtAl2023 -->
- Keep the generated data and visualizations consistent with the formats and organization used in the paper. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

### 4.3.5. Workflow orchestration

Explicitly define how outputs depend on inputs. Tools such as GNU Make allow researchers to document which commands generate which outputs and how files depend on one another. <!-- Source: Survey2026 - - MendezEtAl2020 -->

A Makefile describes:

- **Targets:** what needs to be produced.
- **Dependencies:** which files the target depends on.
- **Commands:** the instructions executed to generate or update the target.

```
target: dependency1 ... dependencyN
    command_to_generate_the_target
```

In the example below, the cleaned dataset `clean_data.csv` is generated from the raw datasets using the cleaning script. The figure `rq1_plot.png` is then generated from the cleaned dataset using the figure-generation script.

<!-- Source: MendezEtAl2020 -->
```makefile
## data/clean_data.csv depends on raw data and the cleaning script
data/clean_data.csv: data/raw/messy_data1.xlsx data/raw/messy_data2.csv scripts/clean_data.R
    Rscript scripts/clean_data.R

## figures depend on clean data and the figure generation script
figures/rq1_plot.png: data/clean_data.csv scripts/generate_figures.R
    Rscript scripts/generate_figures.R
```

If a dependency changes, Make automatically reruns the corresponding command to regenerate affected outputs. This helps keep derived datasets, figures, and results synchronized with their inputs while reducing manual effort and the risk of inconsistencies.

For more details, consult the [GNU Make manual](https://devdocs.io/gnu_make/).

## 4.4. Version control practices

Version control systems preserve the history of decisions, scripts, data transformations, and workflow changes throughout the project. <!-- Source: WilsonEtAl2017 - - DamascenoStruber2021 - - Survey2026 - - USENIXSec2026 -->

In practice, researchers work on local copies of their files and record changes in the repository whenever they want to create a permanent version or share progress. When multiple contributors edit the same files, the system detects overlapping changes and requires conflicts to be resolved before integrating contributions. <!-- Source: WilsonEtAl2017 -->

Without version control, it becomes difficult to track modifications, recover previous states, or understand how results were produced over time. <!-- Source: Survey2026 -->

### 4.4.1. What version control enables

- Tracks the history of changes automatically, without manual file naming conventions or separate logs. <!-- Source: WilsonEtAl2017 -->
- Stores only differences between versions rather than full copies, making the process efficient even for large projects. <!-- Source: WilsonEtAl2017 -->
- Supports distributed collaboration by allowing multiple contributors to work simultaneously. <!-- Source: WilsonEtAl2017 -->
- Provides an accurate record of what actually changed. <!-- Source: WilsonEtAl2017 -->

### 4.4.2. What to version control

Version control works best with **plain text files** such as source code, scripts, and documentation. Binary files (e.g., compiled executables, PDFs, Word documents) cannot be inspected in detail between versions, limiting the usefulness of version tracking for those formats. <!-- Source: WilsonEtAl2017 -->

Guidelines: <!-- Source: WilsonEtAl2017 - - Survey2026 -->

- **Raw data** typically does not require version control, as it should remain unchanged.
- **Intermediate data and results** can be excluded if they can be regenerated from the original data and scripts.
- **Small datasets and result files** may still be versioned when this supports collaboration and comparison across different workflow versions.

When code and data have different characteristics or distribution requirements, they may be maintained under separate version control or distribution strategies. <!-- Source: WilsonEtAl2017 - - Survey2026 -->

For guidance on artifact versioning with persistent identifiers, see [Module 8](#module-8---preservation-versioning-and-maintenance), section 8.3.

## 4.5. Common pitfalls

<!-- Source: BeyerWinter2025 - - Survey2026 -->
- Relying on undocumented manual steps that only work on the original development machine.
- Using proprietary or non-reproducible tools without documenting alternatives.
- Failing to track versions of data, scripts, and dependencies.
- Uploading compressed archives that cannot be extracted on different operating systems.
- Releasing artifacts with hardcoded machine-specific paths.
- Overstating platform support for environments tested on only one machine.
- Leaving expected warnings or error messages unexplained.
- Not testing the artifact on a clean machine before sharing.
- Releasing partial artifacts that do not support the main claims of the paper.

-----

# Module 5 - Data, privacy, and ethics

Research involving human participants often generates data that cannot be freely shared without careful consideration of legal obligations, ethical commitments, and participant rights. Ethical and legal constraints do not necessarily prevent data sharing, but they often influence how data can be shared. This module addresses those considerations and provides practical strategies for sharing data responsibly. <!-- Source: ZeeReich2018 - - Survey2026 - - DamascenoStruber2021 -->

Privacy protection and data sharing are not mutually exclusive. Carefully evaluate what can be safely shared, partially shared, transformed, anonymized, or described through metadata only. <!-- Source: ZeeReich2018 - - Survey2026 - - CESSDA -->

## 5.1. Learning objectives

By the end of this module, you will be able to:

- Identify ethical, legal, privacy, consent, and licensing conditions that affect research data sharing.
- Distinguish personal, sensitive, confidential, and other data requiring special handling.
- Identify direct and indirect identifiers and assess their potential identification risks.
- Select appropriate anonymization strategies for quantitative and qualitative data.
- Apply anonymization iteratively while considering its effects on data interpretation and analytical value.
- Select appropriate strategies for sharing data that cannot be made fully public.
- Document access restrictions and the conditions under which restricted data may be accessed.

## 5.2. Legal and ethical considerations

Sharing research artifacts involving human participants requires attention to legal and ethical obligations that extend beyond the data collection phase. Researchers must evaluate whether participants consented to data sharing, whether applicable regulations permit redistribution, and whether ethical commitments made at the time of collection are honored at the time of publication.

### 5.2.1. Personal and sensitive data

According to the Brazilian General Data Protection Law (LGPD - *Lei Geral de Proteção de Dados Pessoais*, Law No. 13,709/2018), personal data refers to any information related to an identified or identifiable natural person. Sensitive personal data includes racial or ethnic origin, religious beliefs, political opinions, trade union membership, health information, sexual life, and genetic or biometric data. These categories require special care during collection, storage, processing, and sharing. <!-- Source: LGPD -->

Research Ethics Committees help researchers anticipate and address such concerns. Explicit consent is required, so researchers must obtain explicit permission from participants before publishing any data, clearly communicating what will be shared and how it will be used. Anonymization alone is not sufficient without proper consent agreements in place. <!-- Source: CESSDA - - Survey2026 -->

Ethical and legal constraints do not necessarily prevent data sharing, because sharing data is not a binary decision, but they often influence how data can be shared. Depending on the context, researchers may apply different levels of anonymization, filtering, access restriction, or confidentiality protection. <!-- Source: ZeeReich2018 - - Survey2026 - - DamascenoStruber2021 -->

### 5.2.2. Confidentiality and anonymity

- **Confidentiality** refers to protecting information from disclosure beyond the authorized research team. <!-- Source: SaundersKitzingerKitzinger2015 -->
- **Anonymity** is one form of confidentiality, specifically focused on preventing the identification of participants. <!-- Source: SaundersKitzingerKitzinger2015 -->
- In qualitative research, confidentiality may also require withholding parts of the data itself. <!-- Source: SaundersKitzingerKitzinger2015 -->
  - Some information may remain too sensitive or identifying to share safely, even after anonymization. <!-- Source: SaundersKitzingerKitzinger2015 -->

### 5.2.3. Ethical considerations at publication time

Before releasing an artifact publicly, revisit consent agreements and ethical constraints established during the research design phase. <!-- Source: SaundersKitzingerKitzinger2015 - - Survey2026 -->

- Obtain explicit permission from participants before publishing any data. <!-- Source: Survey2026 -->
- Clearly communicate what will be shared and how it will be used. <!-- Source: Survey2026 -->
- Do not assume that anonymization alone is sufficient without proper consent agreements. <!-- Source: Survey2026 -->
- Recognize that anonymization risks may evolve: even carefully anonymized data may become re-identifiable as participants publicly share related stories or social media content after publication. <!-- Source: SaundersKitzingerKitzinger2015 -->

Consent procedures may offer participants different levels of permission for data sharing, and the terms agreed upon at the time of data collection determine what can be released and under which conditions. Verify which level applies before selecting a sharing strategy. Typical levels include: <!-- Source: SaundersKitzingerKitzinger2015 -->

- Restricting access to the research team only.
- Allowing controlled reuse for research purposes.
- Permitting archival in designated repositories.
- Authorizing public dissemination of specific excerpts or media.

## 5.3. Anonymization strategies

Anonymization is an iterative process integrated throughout the research lifecycle, not a one-time task performed before submission. <!-- Source: MendezEtAl2020 - - SaundersKitzingerKitzinger2015 -->

In qualitative research especially, anonymization should be understood as a continuum. The goal is to reduce identification risk as much as reasonably possible while preserving the usefulness and analytical value of the data. <!-- Source: SaundersKitzingerKitzinger2015 -->

### 5.3.1. Types of identifiers

Before sharing data, assess which elements may directly or indirectly identify participants or organizations: <!-- Source: CESSDA -->

<!-- Source: CESSDA -->
| Type | Definition | Examples |
|---|---|---|
| Direct identifiers | Uniquely identify an individual | Full name, passport number, email address, photograph |
| Strong indirect identifiers | Can identify someone when combined with other data | Phone number, date of birth, employer name |
| Indirect identifiers | May contribute to identification in combination with other attributes | Age, city, occupation, education level |

### 5.3.2. Anonymization methods

<!-- Source: CESSDA - - Survey2026 -->
| Method | Description |
|---|---|
| Remove | Delete the information entirely |
| Change | Replace with a pseudonym or generic descriptor |
| Categorize | Generalize or group values (e.g., age ranges instead of exact age, regional reference instead of city name) |

Important distinction: <!-- Source: CESSDA -->
- **Anonymization** irreversibly removes any possibility of identifying individuals. 
- **Pseudonymization** replaces identifying information with artificial identifiers but allows re-identification if additional information is available. Pseudonymized data should still be treated as sensitive.

### 5.3.3. Identifier classification and recommended actions

<!-- Source: CESSDA - - FSD -->
| Identifier | Direct | Strong indirect | Indirect | Recommended action |
|---|:---:|:---:|:---:|---|
| Personal ID (passport, CPF, RG) | ✓ | | | Remove |
| Full name | ✓ | | | Remove / Change |
| Email address | ✓ | ✓ | | Remove |
| Home address | ✓ | | | Remove |
| Phone number | | ✓ | | Remove |
| Postal code | | | ✓ | Remove / Categorize |
| City | | | ✓ | Categorize |
| State | | | ✓ | Categorize |
| Audio recording (voice) | ✓ | | | Remove |
| Video recording | ✓ | | | Remove |
| Photograph | ✓ | | | Remove |
| Date / year of birth | | ✓ | | Categorize |
| Age | | | ✓ | Categorize |
| Gender | | | ✓ | - |
| Marital status | | | ✓ | - |
| Occupation | | X | ✓ | Categorize |
| Employer / workplace | | X | ✓ | Categorize |
| Education level | | | ✓ | Categorize |
| Field of education | | | ✓ | - |
| Nationality | | | ✓ | Categorize |
| Vehicle registration number | | ✓ | | Remove |
| Web page address | | X | ✓ | Remove |
| Student ID / registration number | | ✓ | | Remove |
| IP address | | ✓ | | Remove |
| Health-related information* | | X | ✓ | Categorize / Remove |
| Ethnic group | | X | ✓ | Categorize / Remove |
| Criminal or punishment history | | | ✓ | Categorize / Remove |
| Political or religious allegiance | | | ✓ | Categorize |
| Trade union membership | | | ✓ | Categorize |
| Sexual orientation | | | ✓ | Remove |

**X** *indicates the identifier may behave as a strong indirect identifier depending on context (e.g., rare populations, combination with other attributes).* <!-- Source: CESSDA - - FSD -->

### 5.3.4. Key practices

- Replacing names is usually **only the first step** - also evaluate indirect identifiers and combinations of attributes that together could enable re-identification. <!-- Source: SaundersKitzingerKitzinger2015 -->
- Replace identifiers with **pseudonyms or generic descriptors** - use bracket notation to clearly mark anonymized passages: `[a senior developer]`, `[a software company in Brazil]`. <!-- Source: CESSDA -->
- Maintain an **anonymization log** (de-anonymization key) of all replacements, aggregations, and removals - stored securely and separately from the anonymized data files. <!-- Source: CESSDA -->
- Use "search and replace" carefully to avoid unintended changes or missed misspellings. <!-- Source: CESSDA -->
- Apply pseudonyms and replacements **consistently** across the research team and across publications. <!-- Source: CESSDA -->
- Plan anonymization **at the time of transcription or initial write-up**, not only before submission. <!-- Source: CESSDA -->
- Beware of **over-anonymization**: removing too many contextual details may reduce the interpretability and analytical value of qualitative data. <!-- Source: SaundersKitzingerKitzinger2015 -->
- Be aware of **contextual identification risks**: in small populations, specialized institutions, or tightly connected communities, participants may remain identifiable even after names are removed, through uncommon experiences, institutional affiliations, or combinations of attributes. <!-- Source: SaundersKitzingerKitzinger2015 -->
- Recognize that anonymization may disproportionately obscure the experiences of minority or underrepresented participant groups, since uncommon characteristics increase identification risk. <!-- Source: SaundersKitzingerKitzinger2015 -->

Different stages of a project may require different levels of anonymization: <!-- Source: SaundersKitzingerKitzinger2015 -->
- An initial step may support internal sharing within the research team.
- Later steps may prepare excerpts or datasets for publication or archival.
- Public release typically requires stricter anonymization than internal collaborative use.

### 5.3.5. Identification risks

Identification risks may come from different audiences: <!-- Source: SaundersKitzingerKitzinger2015 -->

- **Internal identification risk:** participants or people within the studied community recognize individuals through shared experiences or contextual details.
- **External identification risk:** outside audiences identify participants through publicly available information, media coverage, legal documents, or online content.

Researchers should evaluate both forms of risk when preparing qualitative data for sharing. <!-- Source: SaundersKitzingerKitzinger2015 -->

### 5.3.6. Anonymizing quantitative data

- Remove or aggregate variables that directly identify individuals. <!-- Source: CESSDA -->
- Reduce the precision of variables such as age or place of residence. As a general rule, report the lowest level of geo-referencing that will not potentially breach respondent confidentiality. <!-- Source: CESSDA -->
- Generalize the meaning of detailed free-text variables by replacing potentially disclosive responses with more general descriptions. <!-- Source: CESSDA -->
- Restrict the upper or lower ranges of continuous variables to hide outliers or atypical values. <!-- Source: CESSDA -->

### 5.3.7. Anonymizing qualitative data

Qualitative data is usually the most difficult to prepare for disclosure. It is personal and hard to anonymize within legal and ethical constraints. <!-- Source: MendezEtAl2020 - - Survey2026 -->

Preparing qualitative data for sharing may require extensive manual review. Plan sufficient time and resources for: <!-- Source: SaundersKitzingerKitzinger2015 -->

- Removing direct identifiers.
- Evaluating indirect identification risks.
- Revising and checking excerpts.
- Preparing different sharing versions (e.g., internal version vs. public version).

Even when full anonymization is not possible, at minimum share the study protocol and coding schemas and coding rules used in the analysis. This allows reviewers and other researchers to assess the trustworthiness of the analysis process and understand how conclusions were drawn. <!-- Source: MendezEtAl2020 - - Survey2026 -->

Audio and video artifacts may expose identifiable features such as voice, facial appearance, gestures, or environmental context. Discuss these risks with participants and consider whether voice alteration, image masking, selective editing, or restricted access are necessary before sharing. <!-- Source: SaundersKitzingerKitzinger2015 -->

Some excerpts may require stronger anonymization than others. Researchers may choose to: <!-- Source: SaundersKitzingerKitzinger2015 -->
- Isolate sensitive excerpts.
- Avoid linking excerpts from the same participant.
- Apply different pseudonyms for the same person across different publications or documents.
- Reduce cross-referencing between publications.

### 5.3.8. Example: Anonymizing an interview transcript

Study background: A study investigating how software developers adopt new tools in their daily work. An interview was conducted with a senior developer from a mid-sized company in Brazil. <!-- Source: CESSDA -->

<!-- Source: CESSDA -->
| Original transcript | Anonymized version |
|---|---|
| *"I'm Vando Azevedo, I work as a senior developer at Tech Solutions here in Recife. We started using CodeFlow around March this year."* | *"I'm [a senior developer], working at [a software company] in [a large city in Brazil]. We started using [a code review tool] earlier this year."* |
| *"Barbara, one of our junior developers, found it difficult to adapt."* | *"[A junior developer] found it difficult to adapt."* |
| *"Our manager, Carol, organized some internal workshops. Our team is about eight people."* | *"[The team manager] organized some internal workshops. Our team is [a small team]."* |

What was anonymized:

<!-- Source: CESSDA -->
| Information | Identifier type | Action |
|---|---|---|
| Full name (Vando Azevedo) | Direct identifier | Removed |
| Company name (Tech Solutions) | Strong indirect identifier | Generalized |
| City (Recife) | Indirect identifier | Generalized |
| Tool name (CodeFlow) | Context-dependent | Generalized (optional) |
| Colleagues' names (Barbara, Carol) | Direct identifiers | Removed |
| Team size (8 people) | Indirect identifier | Coarsened |

Anonymization is not only about removing names. It involves identifying and handling combinations of information that could make individuals identifiable, even indirectly. <!-- Source: CESSDA -->

The UK Data Archive provides a [Text Anonymization Helper Tool](https://ukdataservice.ac.uk/app/uploads/md5_94fc0c2a25f3a75396059826a23b8224_textanonymisationhelpertool.zip), an MS Word macro add-on for aiding anonymization of qualitative data. <!-- Source: CESSDA -->

## 5.4. Sharing strategies for restricted data

### 5.4.1. Sharing strategies overview

Different strategies may be adopted depending on the sensitivity of the data: <!-- Source: Survey2026 - - BezjakEtAl2018 - - ZeeReich2018 -->

<!-- Source: Survey2026 - - BezjakEtAl2018 - - ZeeReich2018 -->
| Strategy | When to use |
|---|---|
| Share complete dataset | No restrictions apply |
| Share anonymized or filtered version | Sensitive identifiers present |
| Share only subsets | Parts of the dataset are shareable even when the full dataset is not |
| Controlled or restricted access | NDA or legal restrictions |
| Aggregated or transformed data | Individual-level data cannot be shared |
| Synthetic dataset | Full anonymization is not feasible |
| Metadata and process documentation only | Dataset cannot be shared at all |

A common practice is to maintain the original raw data in a **restricted (shadow) repository** while preparing a separate shareable version for public release. Ensure that the shared version preserves sufficient information to understand which privacy-preserving transformations were applied and how they affect the data. <!-- Source: Survey2026 -->

See [Module 3](#module-3---documentation), section 3.7, for guidance on documenting non-shared components and their limitations.

Many datasets containing participant-level private information can be shared once de-identified or once a qualified expert has determined that the dataset does not allow individual identification. Consult your Research Ethics Board or Institutional Review Board to learn which approaches are applicable in your context. <!-- Source: BezjakEtAl2018 -->

When a dataset cannot be safely de-identified, researchers can create and share **synthetic data**. This data is similar in structure, content, and distribution to the real data, designed so that statistical analyses return the same results. <!-- Source: BezjakEtAl2018 - - ICSA2025 - - Survey2026 -->

> If confidentiality issues prevent public sharing, include a clear statement of the motivations in the `README.md`. Some venues accept private or password-protected access links when public release is not possible. <!-- Source: RE2026 - - ICSA2025 - - Survey2026 -->

### 5.4.2. Shadow repositories

When original raw data cannot be made publicly available, a shadow repository approach can help balance transparency with ethical and legal constraints. <!-- Source: MendezEtAl2020 - - Survey2026 -->

A **shadow repository** is a restricted-access repository storing the original, non-anonymized data and materials, kept private and not shared publicly. In parallel, a **public repository** hosts the shareable version of the artifact, typically including anonymized, filtered, or transformed data along with relevant documentation.

When using a shadow repository: <!-- Source: Survey2026 - - IPDPS26 -->

- Clearly distinguish the restricted original data (raw) from the publicly shareable version.
- Apply and preserve the privacy-preserving transformations required for public release.
- Document which transformations were applied to the shared data and explain why elements were removed or modified.

### 5.4.3. Preserving analytical value

Privacy-preserving transformations may reduce the completeness or interpretability of shared data. When choosing a sharing strategy, balance the reduction of identification risk with the preservation of the analytical value needed to understand, assess, or reuse the research. <!-- Source: SaundersKitzingerKitzinger2015 - - Survey2026 -->

When privacy constraints prevent sharing the original data, consider whether anonymized, filtered, aggregated, or synthetic alternatives can preserve sufficient information for independent assessment of the study. <!-- Source: ICSA2025 - - Survey2026 -->

-----

# Module 6 - Validation and pre-release preparation

Producing a working artifact in your own development environment is not the same as producing one that others can independently use. Authors often test artifacts only on their own machines, where implicit dependencies and configuration steps are already in place. External validation reveals problems that would otherwise only be discovered by reviewers or future users.

This module covers the steps needed to verify that an artifact is ready to be shared: validating it under realistic conditions, documenting result variability and known limitations, cleaning and curating its contents, and running a final pre-release checklist.

## 6.1. Learning objectives

By the end of this module, you will be able to:

- Validate an artifact in an environment independent from its development environment.
- Verify that the artifact is complete and behaves as documented.
- Check whether the artifact supports the results and claims it is intended to reproduce.
- Identify and document expected result variability and deviations from reported results.
- Distinguish expected variability from failures that require correction or explanation.
- Inspect the final artifact for inconsistencies, unnecessary materials, and unresolved limitations.
- Apply a pre-release checklist to prepare an artifact for sharing.

## 6.2. Why validation matters

Reproducible artifacts should allow external users to understand, execute, and validate the reported results without relying on undocumented knowledge from the original authors. <!-- Source: BeyerWinter2025 - - Survey2026 -->

For results to be independently verifiable, the artifact must provide sufficient context for others to understand how conclusions were derived, configure the environment correctly, and interpret the outputs they produce. <!-- Source: ACMSIGPLAN - - DamascenoStruber2021 -->

Validation is the testing counterpart to documentation: where [Module 3](#module-3---documentation) defines what must be written and claimed about the artifact, this module defines how to verify that those claims actually hold.

Three core validation questions should guide the process:

- **Does the artifact support the paper?** Verify that the workflows, datasets, scripts, and outputs produce the claims, figures, or tables they are intended to support. <!-- Source: BeyerWinter2025 - - DamascenoStruber2021 -->
- **Can an external user execute it independently?** Verify that a user can retrieve, install, execute, and understand the artifact without relying on undocumented knowledge from the authors. <!-- Source: BeyerWinter2025 -->
- **Are the reported results and limitations supported?** Verify that the artifact produces the expected results under the documented conditions and that known variability or limitations are consistent with what is reported. <!-- Source: ACMSIGPLAN -->

Before validation begins, verify that the artifact is internally consistent with the paper it supports:
- Align variable names, metrics, units, and outputs with those used in the paper. <!-- Source: Survey2026 -->
- Guarantee that the artifact directly reflects the experimental setup described in the paper. <!-- Source: Survey2026 -->

## 6.3. Validating the artifact

Validate the artifact under realistic conditions that simulate how external users will interact with it, not just in your own development environment. This is one of the most commonly overlooked steps in artifact preparation. <!-- Source: Survey2026 -->

Authors often test artifacts only on their own machines, where implicit dependencies and configuration steps are already in place. External validation reveals problems that would otherwise only be discovered by reviewers or future users. <!-- Source: Survey2026 -->

### 6.3.1. Validation steps

<!-- Source: RE2026 - - Padhye2019 - - BeyerWinter2025 -->
| Validation step | What to do |
|---|---|
| Full rerun from scratch | Execute the entire workflow from raw inputs to final outputs without manual intervention. |
| Follow your own documentation | Read and execute the instructions exactly as written, without relying on prior knowledge of the project. |
| Test in a clean environment | Run on a machine where no prior setup exists to reveal implicit dependencies. |
| Test on multiple platforms | Identify platform-specific issues across operating systems or hardware configurations. |
| External tester | Ask a colleague or student not involved in the artifact to execute it and report problems. Iterate until no major issues remain. |
| Automated tests | Run unit tests, sanity-check scripts, or automated checks on individual components. |
| Verify archived outputs | Ensure that expected outputs stored for comparison have not been modified during testing. |
| Test compressed packages | Verify that archives can be extracted correctly on different operating systems. Avoid absolute paths or platform-specific compression tools. |
| Test copy-paste commands | Execute each command from the README exactly as written. |

For guidance on specifying dependencies and preparing reproducible execution environments, see [Module 4](#module-4---environments-dependencies-and-automation).

Validation should not be limited to checking whether the artifact runs successfully. Verify that its actual behavior matches what the documentation claims, including expected inputs, outputs, execution steps, resource requirements, supported platforms, and known limitations. <!-- Source: Survey2026 - - ACMSIGPLAN -->

If the full reproduction takes too long to execute during validation, verify that the provided reduced workflow or representative input produces the expected behavior and outputs. <!-- Source: RE2026 - - ICSA2025 -->

Vet the artifact on a clean machine to confirm it can be set up within a reasonable time frame before submitting. <!-- Source: ICSE2026 -->

### 6.3.2. File integrity and completeness

File integrity verification covers two complementary checks: confirming that downloaded files are intact, and confirming that all components required to run the artifact are present and functional.

Provide **checksums** (e.g., SHA-256 hashes) for important files or compressed packages so users can verify the integrity of downloaded materials. This is particularly important for large datasets, pre-built binaries, or VM images. <!-- Source: AdarEtAl2017 -->

Before release, verify the artifact for any setup problems that may prevent proper use, such as corrupted, or missing files, VMs that do not start, or immediate crashes on the simplest example input. Verify that code artifacts execute correctly after being **downloaded**, not only after local development. <!-- Source: ICSA2025 - - Survey2026 -->

## 6.4. Documenting result variability and limitations

Exact reproduction is not always achievable. Transparently documenting expected variability and justifiable deviations is more valuable than overstating reproducibility claims. <!-- Source: ACMSIGPLAN - - Survey2026 -->

### 6.4.1. Expected result variability

For experiments involving nondeterministic behavior or performance variability, document: <!-- Source: ACMSIGPLAN -->

- The number of executions performed.
- Whether warm-up phases were used.
- How measurements were aggregated.
- How variability was analyzed.
- What level of variation is considered acceptable (replication tolerance).

Include measures of variability (e.g., standard deviation, confidence intervals, ranges across repeated executions) rather than only central tendency measures. <!-- Source: ACMSIGPLAN -->

Provide **archived expected outputs** in a separate folder so users can compare their results against a reference without accidentally overwriting it. <!-- Source: Survey2026 -->

### 6.4.2. Interpreting deviations

Validation does not always require exact numerical reproduction. When results may legitimately differ from those reported in the paper, verify that the deviation is expected, documented, and consistent with the study design. <!-- Source: Survey2026 - - ACMSIGPLAN - - DamascenoStruber2021 -->

<!-- Source: Survey2026 - - Padhye2019 - - DamascenoStruber2021 -->
| Situation | What to verify |
|---|---|
| Results are performance data and hardware-dependent. | Verify that reproduced results show the expected high-level trends under the documented conditions, even when exact values differ. |
| Evaluation takes a very long time. | Verify that the reduced or representative evaluation demonstrates the expected core behavior. |
| Evaluation requires specialized hardware. | Verify that the artifact documentation identifies the required hardware and that the workflow can be executed when those resources are available. |
| Benchmark code is proprietary or licensed. | Verify that the evaluation uses the benchmarks or alternatives described in the artifact documentation. |
| Experiments run for multiple days. | Verify that the provided partial reproduction or reduced workflow produces the expected intermediate or final results. |

Known deviations from results presented in the paper should be explicitly outlined. This includes cases where a table or figure is not produced, or where reproduced results differ from those in the paper. <!-- Source: RE2026 -->

### 6.4.3. Reproducibility in qualitative studies

Exact reproduction may not be possible in qualitative studies because results may depend on participants, context, and interpretation. Validation should therefore focus on whether the documented procedures, analytical process, and contextual information can be independently inspected and followed. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

Verify that the artifact provides sufficient evidence for others to assess how the analysis was conducted and to repeat the research procedures under comparable conditions.

## 6.5. Final artifact inspection

Before release, inspect the artifact as an external user would. The purpose of this final inspection is not to repeat the preparation steps described in previous modules, but to verify that the resulting artifact is complete, consistent, and ready to be shared. <!-- Source: Survey2026 -->

Verify that: <!-- Source: BeyerWinter2025 - - Survey2026 - - AdarEtAl2017 - - SEFM2024 - - DamascenoStruber2021 -->

- **All materials are available in English.** If the associated paper is written in English, ensure that the artifact materials are also available in English. <!-- Source: Survey2026 -->
- **All required components are present.** Confirm that the files, data, scripts, configurations, and other materials required for the documented reproduction workflow are included and functional. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- **The artifact is consistent with the paper.** Confirm that variable names, metrics, units, outputs, experimental conditions, figures, tables, and supported claims are consistent with the publication. <!-- Source: Survey2026 -->
- **The artifact is consistent with its documentation.** Execute the documented workflow as an external user would and confirm that the instructions, commands, expected outputs, resource requirements, and supported platforms correspond to the actual artifact (see [Module 3](#module-3---documentation) for guidance on documenting the artifact). <!-- Source: Survey2026 -->
- **The artifact contains no unnecessary internal materials.** Check for temporary files, backups, obsolete versions, internal comments, TODOs, unused scripts, dead code, or other materials that do not contribute to the shared artifact. <!-- Source: Survey2026 -->
- **Sensitive and restricted materials are appropriately handled.** Confirm that sensitive information, credentials, personal data, and proprietary materials have been removed, anonymized, or appropriately restricted. See [Module 5](#module-5---data-privacy-and-ethics) for guidance on privacy and anonymization. <!-- Source: Survey2026 -->
- **Links and references work as expected.** Verify hyperlinks, cross-references, embedded assets, and references to external resources.
- **Known limitations and deviations are documented.** Confirm that differences from the reported results, unsupported claims, known constraints, and relevant exclusions are clearly explained. <!-- Source: Survey2026 -->
- **Access conditions are correctly configured.** Confirm that intended users can retrieve and use the artifact under the documented access conditions. <!-- Source: Survey2026 -->
- **The archive can be extracted successfully.** Test that the packaged artifact can be extracted correctly on the operating systems that the artifact is intended to support. <!-- Source: BeyerWinter2025 -->
- **The repository presentation is correct.** When supported by the repository, perform a preview upload to verify how the artifact page and its metadata will appear before making the artifact public. <!-- Source: Survey2026 -->

Do not release an artifact with known missing components that are necessary to reproduce its supported claims. If a component cannot be included, verify that its omission is clearly documented and justified. <!-- Source: Survey2026 -->

-----

# Module 7 - Publishing, licensing, and citation

<!-- Source: Survey2026 - - MendezEtAl2020 - - Montgomery2024 -->
Preparing an artifact for your own use is not the same as preparing it for others. Publishing requires assembling all components (data, code, documentation, licenses, and metadata) into a coherent, self-contained bundle that others can retrieve, install, and use independently. Without proper archival and citation practices, even well-prepared artifacts may disappear over time, preventing others from verifying, reusing, or building upon your work.

A good published artifact is self-explanatory without requiring access to the paper, and allows users to reproduce at least one key result, understand how results were generated, and extend or adapt the work for new purposes. <!-- Source: Survey2026 -->

## 7.1. Learning objectives

By the end of this module, you will be able to:

- Select an appropriate repository for publishing and preserving a research artifact.
- Prepare an artifact package for publication and long-term access.
- Apply FAIR principles when publishing research artifacts.
- Select and apply appropriate licenses to different types of artifact components.
- Identify licensing compatibility and usage constraints that affect artifact publication and reuse.
- Assign persistent identifiers and preserve version-specific artifact references.
- Provide appropriate citation metadata for research artifacts.
- Cite research artifacts consistently in publications.
- Prepare a Data Availability Statement that accurately describes the availability and access conditions of research materials.

## 7.2. Repository selection

Selecting an appropriate archival repository is one of the most consequential decisions in the publishing process. Not all platforms designed for code sharing or collaboration are suitable for long-term archival.

### 7.2.1. Repository selection criteria

When selecting a repository, verify that it supports: <!-- Source: AdarEtAl2017 - - Montgomery2024 - - JORS - - DamascenoStruber2021 - - ConfPub - - ICSE2026 - - MODELS2025 -->

| Characteristic | Description | Importance |
| --- | --- | --- |
| Dedicated, immutable PIDs | The repository automatically generates persistent identifiers (e.g., DOI, Handle, ARK, SWHIDs) that do not change, with a separate PID for each version. | Essential |
| Immutable releases | Once published, content cannot be silently modified or changed after release. |  Essential |
| Long-term preservation | The hosting organization must commit to maintaining access and URLs for the foreseeable future by a declared long-term preservation policy. | Essential |
| Publicly accessible online | No registration required for access. |  Essential |
| Versioning | Ability to publish new versions while maintaining access to all previous versions. |  Essential |
| Metadata support for discoverability | Support for structured metadata (title, authors, keywords, description, license) that enables indexing by aggregators and search engines. | Recommended |
| Integration with development platforms | e.g., GitHub-to-Zenodo. | Optional |

Prefer repositories that allow anonymous access and do not require user registration, manual approval, or restrictive access controls to download the artifact. <!-- Source: Survey2026 -->

Choosing the right archival platform is critical for long-term accessibility and citability. <!-- Source: Montgomery2024 - - Survey2026 -->

### 7.2.2. Archival platform options

Platforms not suitable as the sole archival repository: <!-- Source: Montgomery2024 - - MendezEtAl2020 - - Survey2026 -->

| Platform | Why it fails as an archive |
| --- | --- |
| GitHub, GitLab, Hugging Face | Repositories can be renamed, modified, or deleted over time. Not designed for immutable, long-term archival. |
| Institutional and research group websites | Frequently restructured. Links break when staff leave. |
| Employee web pages | Taken offline when the employee leaves. |
| Google Drive, Dropbox, OneDrive | Designed for backup/sync, not archival. URLs can be changed or deleted at any time. |
| ResearchGate, Academia.edu | Not archival platforms. Content is volatile and not guaranteed to persist. |

These platforms remain useful during development and collaboration, but must be complemented with dedicated archival repositories at publication time. <!-- Source: Montgomery2024 -->

<!-- Source: Montgomery2024 - - Graziotin2019 - - DamascenoStruber2021 - - Survey2026 -->
| Repository | Scope | PID | Versioning | Platform integration | Key characteristics |
|:---:|:---:|:---:|:---:|:---:|---|
| Zenodo | General-purpose artifacts | DOI | Native | GitHub | Free, nonprofit repository operated by CERN and OpenAIRE. Supports DOI reservation before publication and concept DOIs for versioned artifacts. |
| OSF | Research projects and associated artifacts | DOI/ARK | Native | GitHub, Dropbox, Google Drive, etc. | Supports project organization, preregistration, collaboration, and artifact sharing, while also serving as an archival repository. |
| FigShare | General-purpose artifacts | DOI | Native | GitHub | Commercial platform with preservation support through CLOCKSS. |
| Dryad | Research datasets | DOI | Native | - | Curated repository specialized in datasets. Fees may apply. |
| Software Heritage | Source code | SWHID | Git-based | GitHub, GitLab | Archives public source code from platforms such as GitHub and GitLab. Preservation is based on the version-control history rather than direct artifact deposits. |

The directory [re3data.org](https://www.re3data.org/) can help identify additional suitable repositories for specific disciplines or data types. <!-- Source: BezjakEtAl2018 -->

Development and distribution platforms such as GitHub, GitLab, and Hugging Face may remain useful alongside the archival repository. The version associated with the publication should be deposited in an archival repository that provides persistent identification and long-term preservation. <!-- Source: Survey2026 -->

Large-scale components, such as trained neural-network weights or very large datasets, may exceed the storage limits of traditional archival repositories. In such cases, a distribution platform such as Hugging Face may be used for active access, while a version-specific snapshot, metadata record, or companion package is preserved in an archival repository to provide a persistent identifier and support long-term preservation.

No single repository is ideal for every artifact type. Repository selection should consider the nature of the artifact, community practices, storage requirements, and long-term preservation needs.

### 7.2.3. Recommended publication workflow

<!-- Source: Survey2026 - - ICSE2026 - - MODELS2025 - - DamascenoStruber2021 -->

1. **Develop and organize the artifact** using an appropriate development or collaboration platform.
2. **Archive the publication version** in a repository that provides persistent identification and long-term preservation.
3. **Cite the archived artifact** in the paper using its persistent identifier.

When both a development platform and an archival repository are used, provide links to both so users can distinguish the actively maintained version from the archived version. <!-- Source: MODELS2025 -->

Supplementary material published on personal or project webpages does not receive a PID and may become inaccessible over time. When supplementary material is intended for long-term accessibility, archive it as part of the research artifact. <!-- Source: ConfPub -->

## 7.3. Applying FAIR principles at publication

Before publishing the artifact, verify that the selected repository and publication metadata support the FAIR characteristics introduced in [Module 1](#module-1---foundations). <!-- Source: Survey2026 -->

- **Findable**: provide a persistent identifier, descriptive metadata, and searchable repository information. <!-- Source: Survey2026 -->

- **Accessible**: ensure that the artifact and its metadata can be retrieved under clearly defined access conditions. <!-- Source: Survey2026 -->

- **Interoperable (I)**: provide artifacts and metadata in formats that can be processed by commonly available tools. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

- **Reusable (R)**: provide sufficient documentation, licensing information, and provenance for others to understand and reuse the artifact. <!-- Source: Survey2026 -->

## 7.4. Anonymizing artifacts for review

The review model adopted by the venue determines whether the artifact must be anonymized during submission.

| Review model | Description | Artifact implications |
|---|---|---|
| Open review | Authors and reviewers know each other's identities. | The artifact does not need to hide the authors' identities. |
| Single-anonymous | Reviewers know authors' identities, but not vice versa. | The artifact does not need to hide the authors' identities, but reviewer anonymity needs to be protected. |
| Double-anonymous | Neither authors nor reviewers know each other's identities. | The artifact needs to be anonymized to prevent the authors' identities from being revealed, and reviewer anonymity needs to be protected. |

For double-anonymous review, verify whether the artifact could reveal the authors' identities through its files, repository, or associated metadata. The following aspects should be checked: <!-- Source: Survey2026 - - Graziotin2019 -->

- Remove author names from all project files, scripts, and documentation. <!-- Source: Survey2026 -->

- Remove metadata that may reveal authorship from project files (e.g., file properties, commit history, author fields in configuration files). <!-- Source: Survey2026 -->

- Remove identifying information from repository titles, descriptions, screenshots, and other repository metadata. <!-- Source: Survey2026 - - Graziotin2019 -->

When necessary, use a separate or temporarily anonymized repository for artifact submission so that the public development repository does not reveal author identities during double-anonymous review. Several approaches can be used to provide an anonymized artifact during review, depending on the repository and submission mechanism: <!-- Source: Survey2026 -->

- **Separate anonymized repository:** create a new, identity-free repository for submission.

- **Platform-supported temporary anonymization:** some repositories (e.g., FigShare) support private sharing links before public release.

- **Anonymous Docker repositories:** for containerized artifacts.

- **Anonymous GitHub:** a tool that creates an anonymized mirror of a GitHub repository.

During double-anonymous review, also check whether repository configurations or external services may expose identifying information through access logs, analytics tools, or tracking mechanisms. <!-- Source: ETAPS2025 -->

### 7.4.1. Finalizing the artifact after review

Once the review process is complete, restore the identifying information that was removed for anonymous review, including the authors' identities and the information linking the artifact to the paper. The final artifact should clearly identify its authors and establish its relationship with the published paper.

If the artifact undergoes a separate artifact evaluation, the transition to the final, de-anonymized version should occur after the artifact evaluation is completed. Otherwise, it should occur after the paper review process. The final paper should link to the final published version of the artifact rather than to the anonymized version used during review.

## 7.5. Preparing the artifact package

### 7.5.1. Assembling the publication package

At publication time, assemble the final artifact package from the components prepared and validated in the previous modules. The package should contain the materials necessary to support the documented reproduction and reuse scenarios, together with the metadata, license, and citation information required for publication. <!-- Source: Survey2026 - - ICSE2026 - - DamascenoStruber2021 -->

Artifacts do not need to be complete to be valuable, they simply need to be relevant to the study and add value beyond the paper. Even the data behind a single figure can improve transparency significantly. <!-- Source: ICSE2026 -->

Use [Module 6](#module-6---validation-and-pre-release-preparation) to verify that the package is complete and internally consistent before publication.

### 7.5.2. File formats for publication

Use the file-format guidance in [Module 2](#module-2---planning-and-artifact-organization) when preparing the artifact. At publication time, verify that reusable data and results are available in formats that users can inspect and process without requiring proprietary software whenever possible. <!-- Source: Survey2026 - - BeyerWinter2025 - - ETAPS2025 -->

### 7.5.3. Preparing the archive for publication

Before publishing, verify that the package is prepared in a format supported by the selected repository and that the uploaded artifact corresponds to the validated version. When the repository provides a preview or draft mode, use it to inspect the final publication record before making it public. <!-- Source: Survey2026 -->

### 7.5.4. Package types

The appropriate packaging format depends on the nature of the artifact:

- **Simple package:** for non-executable artifacts such as documents, datasets, protocols, or files accessible with common tools (e.g., PDF viewers, spreadsheet software). These artifacts can typically be distributed as compressed archives (e.g., ZIP or TAR.GZ) without requiring complex installation procedures. <!-- Source: Survey2026 - - ICSA2025 -->

- **Installation package:** for software systems, tools, scripts, or executable workflows. These packages should include the code, dependencies, configuration instructions, and example data required for installation and execution. When artifacts depend on complex or specialized environments, consider providing containers or virtual machines to simplify setup and improve reproducibility. <!-- Source: Survey2026 - - NDSS2026 - - DamascenoStruber2021 -->

## 7.6. Choosing a license

Without a license, others are not legally permitted to reuse, modify, or redistribute your artifact, even if it is publicly accessible. Licensing should be considered early in the project, not only at publication time. <!-- Source: Survey2026 -->

### 7.6.1. Distinguishing software from non-software artifacts

- **Software licenses**: for code, scripts, tools, and executable artifacts.
- **Content licenses**: for datasets, documentation, protocols, reports, and other non-software materials.

Be careful not to use the wrong license type (e.g., applying MIT to a dataset).

### 7.6.2. Selecting an appropriate license

**For non-software artifacts (data, documentation, protocols):**

<!-- Source: CC -->
| License | Key characteristic |
|---|---|
| CC0 | Public domain dedication; maximizes reuse with no restrictions. Suitable for datasets and metadata. |
| CC BY | Requires attribution; good default for most research artifacts. |
| CC BY-SA | Attribution and share-alike; derivatives must use the same license. |
| CC BY-NC / CC BY-ND | Restrict commercial use or derivatives; avoid when reproducibility and reuse are goals. |

Use CC0 or CC BY whenever reuse and reproducibility are primary goals. Avoid restrictive variants (NC, ND) that may hinder adoption and integration with other artifacts. <!-- Source: Survey2026 - - CC -->

For more details: [Creative Commons licenses](https://creativecommons.org/cc-licenses/)

**For software artifacts:**

<!-- Source: Choose -->
| License | Type | Key characteristic |
|---|---|---|
| MIT | Permissive | Simple, minimal restrictions; broad reuse allowed. |
| Apache 2.0 | Permissive | Includes patent protection; good for research software. |
| GPL v3 | Copyleft | Requires derivatives to remain open-source. |

Permissive licenses (MIT or Apache 2.0) are recommended unless you explicitly want to enforce that derivatives remain open. For more details: [Choose an Open Source License](https://choosealicense.com/licenses/) <!-- Source: Survey2026 - - Choose -->

**Quick decision guide:**

| Artifact type | Recommended license |
|---|---|
| Code and scripts | MIT or Apache 2.0 |
| Datasets | CC0 or CC BY |
| Documentation | CC BY |
| Mixed artifacts | Apply the appropriate license to each component |

### 7.6.3. Checking compatibility and constraints

Before finalizing the license: <!-- Source: Survey2026 -->

- **Ownership:** verify that you have the right to license the artifact. Institutional policies, funder requirements, and employer agreements may impose restrictions.
- **Dependencies:** verify compatibility with the licenses of any third-party tools, libraries, or datasets included in the artifact.
- **Publication venue:** some conferences and journals have specific licensing requirements.
- **Sensitive data:** licensing does not override ethical or legal restrictions on data sharing.
- **Industry artifacts:** artifacts from industry settings may require legal review before sharing. <!-- Source: Survey2026 -->

### 7.6.4. Applying the license correctly

<!-- Source: Survey2026 - - ZimmermannEtAl2023 -->
- Include a `LICENSE` file in the repository root.
- If the artifact includes components with different licenses (e.g., code under MIT and data under CC BY), clearly state which license applies to each component.
- Include a copyright notice identifying the rights holder.
- For third-party materials, include required notices and verify that redistribution is permitted.

## 7.7. Persistent identifiers and citation metadata

### 7.7.1. PIDs and immutability at publication

Use the PID, not a URL, when citing the artifact in the paper. URLs break, PIDs are stable. <!-- Source: AdarEtAl2017 -->

Key practices at publication time: <!-- Source: AdarEtAl2017 - - SEFM2024 -->

- Assign a PID to the artifact when archiving it.
- Verify that all files are intact and not corrupted after packaging. Add a checksum (e.g., SHA-256 hash) to the artifact metadata for additional integrity verification.
- Ensure the PID appears in both the text and the metadata of the associated paper.

On Zenodo, a DOI can be reserved before the final publication of the artifact, allowing you to include it in the paper before the camera-ready deadline. <!-- Source: RE2026 -->

### 7.7.2. CITATION.cff and AUTHORS file

Include a `CITATION.cff` file in the repository root. That is, a plain-text, human- and machine-readable file that specifies how the artifact should be cited. It allows citation managers and platforms (e.g., GitHub, Zenodo) to generate correct citations automatically. <!-- Source: RE2026 - - Survey2026 - - DamascenoStruber2021 -->

A `.cff` file can be created at the [CFF initializer website](https://citation-file-format.github.io/cff-initializer-javascript/#/).

Include also an `AUTHORS` file listing all contributors with affiliations and contact information. Note that institutional email addresses may not remain valid long-term. Consider providing additional means of contact. <!-- Source: MontgomeryEtAl2024 - - DamascenoStruber2021 - - Survey2026 -->

Artifacts should include self-descriptive metadata covering at minimum: <!-- Source: AdarEtAl2017 - - DamascenoStruber2021 -->

- Title
- Authors
- Version
- License
- Dependencies
- Execution requirements
- Related publication
- Keywords

### 7.7.3. Citing the artifact in the paper

Cite the artifact the same way you would cite other scholarly references, using the PID, and place it in a dedicated Data Availability Statement. <!-- Source: ConfPub -->

Example citation entry (Zenodo): <!-- Source: ConfPub - - DamascenoStruber2021 -->

```bibtex
@Misc{VasconcelosMadeiralSoares2026-artifacts,
  author       = {Ana Paula Vasconcelos and Fernanda Madeiral and Sergio Soares},
  title        = {Research Artifacts of "GAPS: A guide for better artifact
                  preparation and sharing"},
  howpublished = {Zenodo},
  year         = {2026},
  doi          = {10.5281/zenodo.03091985},
  version      = {final}
}
```

Always use the PID for the specific version used to produce the results in the paper. <!-- Source: ConfPub - - Survey2026 -->

## 7.8. Data Availability Statements (DAS)

A Data Availability Statement (DAS) explains which data and materials supported the study, whether they are openly available or restricted, and how other researchers can access them. It should appear as a dedicated section in the paper, typically before the references. <!-- Source: Researchdata - - ConfPub -->

The [Disclosure statement](advisor-GAPS.md#373-disclosure-statement) in the README is distinct from the Data Availability Statement in the paper. The former provides transparency about the artifact, the latter declares the availability and access conditions of the materials supporting the study.

A good DAS should: <!-- Source: Researchdata -->

- Identify which datasets, scripts, and materials support the results.
- State where the data are stored, with PID or persistent URL.
- Explain how access can be obtained.
- Describe any restrictions on sharing.
- Avoid vague statements such as "data available upon request".
  - Provide concrete access instructions instead.

### 7.8.1. DAS examples for common scenarios

<!-- Source: Researchdata -->
| Scenario | Example DAS |
|---|---|
| Artifacts publicly available | The research artifacts supporting this study are available at [PID URL]. |
| Privately shared during review, to be released after acceptance | Manuscript reviewers can preview the artifacts at [PRIVATE URL]. After acceptance, artifacts will be released at [PID URL]. |
| Data with privacy restrictions | The dataset contains information that could compromise participant privacy and cannot be made openly available. Metadata and access request instructions are available at [PID URL]. |
| Restricted artifacts available upon request | Some artifacts cannot be shared openly due to [legal / ethical / confidentiality] restrictions. Access may be requested from [CONTACT / INSTITUTION], subject to applicable restrictions. |
| Artifacts available within the paper | Artifacts supporting the findings of this study are available within the paper and/or its supplementary materials. |
| No artifacts were generated | No research artifacts or datasets were generated during this study. |

Different journals, conferences, and publishers may have specific DAS requirements. Always verify venue-specific policies before submission. <!-- Source: Researchdata -->

## 7.9. Publishing visibility

Publishing is not the final step. Making the artifact visible increases its impact and encourages reuse. <!-- Source: Survey2026 -->

In addition to linking the artifact in the paper: <!-- Source: Survey2026 -->

- Share the PID in talks, social media, and academic mailing lists.
- Ensure the artifact is accessible independently of publisher paywalls.
- Provide sufficient documentation within the artifact so that users without full paper access can still understand and reuse it.

Public releases may be difficult or impossible to fully reverse once an artifact has been distributed and archived. Verify the contents, access conditions, anonymization, and licensing before publication. <!-- Source: Graziotin2019 - - Survey2026 -->

-----

# Module 8 - Preservation, versioning, and maintenance

Publishing an artifact is not the end of the process. Artifacts frequently become unusable within months of publication, due to dependency decay, deprecated libraries, broken links, unavailable services, or undocumented environment assumptions. Long-term usability requires active attention to preservation, environment isolation, dependency management, and stable archival practices. Sustainability also supports the cumulative nature of science: when artifacts remain usable, future researchers can reproduce earlier results, compare their work against prior baselines, and build incrementally upon existing research. <!-- Source: BeyerWinter2025 - - Survey2026 -->

## 8.1. Learning objectives

By the end of this module, you will be able to:

- Identify factors that can cause research artifacts to become unavailable or difficult to reproduce over time.
- Apply preservation practices that reduce artifact decay.
- Manage artifact versions while preserving traceability and reproducibility.
- Distinguish development versions from published versions.
- Maintain the immutability of published artifact versions.
- Document changes between artifact versions using explicit versioning and changelogs.
- Maintain dependencies and documentation after publication.
- Respond to issues and document maintenance activities that may affect reproducibility or reuse.

## 8.2. Artifact decay: causes and prevention

Artifact decay (sometimes called *bit rot*) refers to the gradual degradation of an artifact's usability over time, even when no changes are made to the artifact itself. Most decay is predictable and preventable. <!-- Source: BeyerWinter2025 - - Survey2026 -->

| Cause | Description |
|---|---|
| Dependency decay | Libraries, packages, or tools used by the artifact are updated, deprecated, or removed. |
| Broken links | External datasets, APIs, or services referenced by the artifact become unavailable. |
| Undocumented environment assumptions | The artifact silently depends on specific OS versions, hardware configurations, or system settings that are no longer available. |
| Platform incompatibility | The artifact was only tested on a specific platform and fails on newer or different systems. |
| Expired credentials or access | APIs, private repositories, or institutional services required by the artifact become inaccessible. |
| Format obsolescence | Data or outputs were stored in proprietary or tool-specific formats no longer supported. |

Preventing artifact decay requires decisions made during preparation and publication, followed by continued monitoring after release. The practices introduced in earlier modules, such as dependency isolation, durable file formats, archival repositories, and explicit documentation, contribute to long-term preservation. <!-- Source: Survey2026 - - BeyerWinter2025 -->

In this module, the focus is on identifying what may deteriorate after publication and on maintaining the artifact when such changes occur.

### 8.2.1. Avoiding dependencies on development platforms

Long-term preservation requires the archived artifact to remain obtainable independently of the continued availability of the authors' development or distribution accounts. The archival artifact should remain the authoritative source for reproducing the published results. <!-- Source: Survey2026 -->

- If a development repository is also provided, clearly distinguish it from the archived version used for reproduction.
- The continued availability of an authors' development account or repository should not be a prerequisite for obtaining the published artifact.

See [Module 7](#module-7---publishing-licensing-and-citation) for guidance on selecting archival repositories and publishing the artifact.

## 8.3. Versioning and changelogs

### 8.3.1. Artifact versioning and persistent identifiers

Archival platforms such as Zenodo and FigShare support different identifiers for versioned artifacts. A version-specific PID identifies a single, fixed version, while a concept PID can provide a stable reference to the artifact across versions. <!-- Source: USENIXSec2026 - - AdarEtAl2017 -->

Each new version of the artifact should result in a new version-specific PID. This preserves the relationship between a published study and the exact artifact version associated with it, while allowing the artifact to evolve independently after publication. <!-- Source: AdarEtAl2017 - - USENIXSec2026 -->

Provide a hash or commit identifier alongside the PID when appropriate to further identify the exact artifact contents. <!-- Source: Survey2026 - - ConfPub -->

Update the preprint and artifact with the PID provided by the publisher once it becomes available. <!-- Source: Survey2026 -->

### 8.3.2. Why post-publication versioning matters

Artifacts evolve after publication. Bugs are discovered, dependencies break, documentation is improved, and new use cases emerge. Maintaining clear version records helps users understand what changed, when, and why, and allows them to distinguish the version associated with the original publication from later versions. <!-- Source: Graziotin2019 - - Survey2026 -->

### 8.3.3. Managing versions after publication

After publication, changes that affect a released artifact should be incorporated into a new version rather than applied to the published version. This includes corrections, dependency or environment changes, and changes to the artifact that affect its execution, results, or reuse. Document the changes in the changelog and, when they affect reproducibility or execution, update the relevant documentation and instructions accordingly. <!-- Source: Survey2026 - - ConfPub - - DamascenoStruber2021 -->

When a new version is released, preserve the relationship with the previous version so that users can identify which version was associated with the original publication and which changes were introduced later.

### 8.3.4. Version tagging

Each released version should correspond to a clear, explicit version tag. A useful tagging scheme produces predictable and self-explanatory identifiers that help distinguish releases throughout the artifact lifecycle. <!-- Source: ConfPub - - DamascenoStruber2021 -->

Example tagging schema for an artifact associated with a paper published at a venue called FSEV (Fictional Software Engineering Venue) in 2026: <!-- Source: ConfPub -->

```
FSEV-2026-submission          ## version accompanying the submitted paper
FSEV-2026-camera-ready        ## version accompanying the final version of the paper
FSEV-2026-AEC-submission      ## version submitted to artifact evaluation
FSEV-2026-AEC-revision        ## version after kick-the-tires feedback
FSEV-2026-AEC-final           ## version after addressing reviewer comments
```

When using Zenodo, you can reserve a DOI in advance so it can be included in the paper before the submission. <!-- Source: RE2026 -->

It is useful to separate a fixed archival artifact used for reproducibility (e.g., Zenodo) from an actively maintained development repository intended for continued updates and reuse (e.g., GitHub). <!-- Source: ConfPub -->

### 8.3.5. Changelog
<!-- Source: Survey2026 - - DamascenoStruber2021 -->

A changelog documents what changed between versions and helps users quickly understand whether an update affects their use of the artifact.

A changelog should: <!-- Source: Survey2026 -  - DamascenoStruber2021 -->

- List changes by version, in reverse chronological order (newest first).
- For each version, note the date and a description of changes.
- Distinguish between changes that affect reproducibility (e.g., bug fixes that change outputs) and those that do not (e.g., documentation improvements).

Example changelog structure:

```
## [2.0.0] - 2026-10-29
### Changed
- Updated Python dependency from 3.9 to 3.11.
- Replaced deprecated matplotlib API calls.

## [1.1.0] - 2025-09-03
### Fixed
- Corrected data cleaning script that produced incorrect output for edge cases.
### Added
- Minimal working example for quick validation.

## [1.0.0] - 2025-02-02
- Initial release accompanying the paper submission.
```

### 8.3.6. Immutability of published versions

Once an artifact version is associated with a publication, its contents must remain immutable. Instead of modifying a released version, create a new versioned release. <!-- Source: AdarEtAl2017 - - ConfPub - - Survey2026 - - DamascenoStruber2021 -->

## 8.4. Active maintenance after publication

Sustainability involves actively supporting users who interact with the artifact after publication, not only preventing decay. <!-- Source: Survey2026 -->

To maintain usability over time: <!-- Source: Survey2026 - - DamascenoStruber2021 -->

- **Monitor and respond to issues.** A responsive GitHub Issues page or discussion forum helps users report problems, and creates a public record of known issues and resolutions for future users. <!-- Source: Survey2026 - - DamascenoStruber2021 -->
- **Update dependencies when feasible.** When dependencies release breaking changes or security updates, updating the artifact preserves its usability. <!-- Source: Survey2026 -->
- **Document known issues and expected failures.** If certain problems are known but unresolved, document them explicitly in the README. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

### 8.4.1. Keeping documentation current

After each release, verify that the artifact documentation remains consistent with the current version. In particular, update documentation when changes affect: <!-- Source: Survey2026 -->

- Execution instructions or commands.
- Software dependencies or system requirements.
- Expected outputs or artifact behavior.
- Known issues or limitations.
- Links or external resources required for use.

Changes that affect reproducibility, execution, or reuse should also be recorded in the changelog. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

See [Module 3](#module-3---documentation) for guidance on artifact documentation.

-----

# Module 9 - Reusability and extension

Well-prepared artifacts are not only reproducible, they are also extensible. Supporting reuse beyond the original study increases the long-term scientific impact of the work. <!-- Source: Survey2026 - - BeyerWinter2025 -->

## 9.1. Learning objectives

By the end of this module, you will be able to:

- Identify which components of an artifact are intended for reuse beyond the original study.
- Document how reusable components can be adapted to new inputs, datasets, or configurations.
- Identify limitations that may constrain artifact reuse or extension.
- Describe plausible scenarios for extending an artifact beyond its original use.
- Prepare a Reusability Guide that communicates how others can reuse and extend the artifact.

## 9.2. Designing for reusability

The early planning decisions that support extensibility, including open licensing, modular code structure, stable dependencies, and source code availability, are addressed in [Module 2](#module-2---planning-and-artifact-organization), section 2.2.2. This section focuses on what to document and make explicit within the artifact so that other researchers can actually extend it.

<!-- Source: Survey2026 - - DamascenoStruber2021 -->
- **Document how to adapt to new inputs.** Explain which parameters, datasets, or configurations need to change for the artifact to be applied to a new study.
- **Explicitly identify which parts are reusable.** Not all parts of an artifact need to be designed for reuse. What matters is being explicit about which parts are reusable and which are not.

## 9.3. Reusability guide

A Reusability Guide is a dedicated section of the artifact's documentation (typically in the README or a separate file) written for researchers who want to reuse or build on the artifact rather than simply reproduce its original results. <!-- Source: Survey2026 - - DamascenoStruber2021 -->

A Reusability Guide should cover:
- **Which parts can be reused.** Identify which components are intended for reuse and which exist only to reproduce the paper results.
- **How to adapt.** Explain how to adapt the artifact to new inputs, datasets, or configurations.
- **Known limitations.** Describe constraints on how far the artifact can be adapted or repurposed.
- **Extension scenarios.** Describe example scenarios of how the artifact could be extended. Providing a worked example of an extension is a plus.

-----

# Module 10 - Artifact evaluation and submission
<!-- Source: RE2026 - - ACMSIGMOBILE - - BeyerWinter2025 -->

Artifact evaluation is a process in which reviewers assess research artifacts according to criteria defined by the evaluation program. These criteria may address aspects such as availability, documentation, functionality, reproducibility, or reusability, and their scope varies across venues and evaluation programs.

Understanding how artifact evaluation works and what reviewers may be asked to assess helps researchers prepare for the process without assuming a particular evaluation model or set of criteria.

## 10.1. Learning objectives

By the end of this module, you will be able to:

- Explain the purpose and scope of artifact evaluation.
- Identify the criteria and requirements defined by a specific artifact evaluation program.
- Prepare an artifact and its documentation according to the requirements of the target venue.
- Verify artifact accessibility, documentation, functionality, and reproducibility before submission.
- Prepare an artifact for anonymous evaluation when required.
- Anticipate common evaluation issues and address them before submission.
- Respond to evaluation feedback by documenting and applying appropriate changes to the artifact.

## 10.2. Accessing artifacts during review

Artifact anonymization requirements may differ from paper anonymization requirements. Always verify the specific policies of the target venue regarding artifact visibility, URLs, repository identities, and reviewer anonymity before preparing the submission. <!-- Source: SPLASH2024-CfA -->

The review model adopted by the venue determines whether the artifact must be anonymized during submission and whether reviewer anonymity must be protected. When single-anonymous review is required reviewer anonymity must be protected. When double-anonymous review is required, authors should also anonymize information that could reveal their identity through the artifact, its repository, or associated metadata and reviewer anonymity must be protected. See [Section 7.4](#74-anonymizing-artifacts-for-review) for guidance on artifact anonymization of authors'identities.

Artifact evaluation may require reviewers to access artifacts under conditions that protect their anonymity. The access mechanism should therefore allow reviewers to inspect the artifact without requiring them to disclose their identity or create an account that identifies them to the authors. <!-- Source: AdarEtAl2017 - - ICSA2025 -->

When reviewer anonymity must be protected, consider the following aspects:

- **No reviewer login:** whenever possible, the artifact should be accessible without requiring reviewers to create or use an account that identifies them. <!-- Source: ICSA2025 -->

- **Controlled access when necessary:** if the artifact cannot be made publicly accessible during review, a private or password-protected link may be used. When credentials are necessary, access can be provided to reviewers through credentials or tokens that do not require reviewers to disclose their identities. <!-- Source: AdarEtAl2017 - - ICSA2025 -->

- **No tracking or identifying data collection:** the repository, hosting service, or artifact itself should not expose reviewers through access logs, analytics, tracking mechanisms, or other services that collect identifying information. <!-- Source: ETAPS2025 -->

- **No unnecessary registration or personal information:** access should not require reviewers to provide personal information that could identify them to the authors. <!-- Source: ICSA2025 -->

- **Access throughout the evaluation period:** if the artifact depends on a live web instance or online service, it should remain available throughout the review period. <!-- Source: NDSS2026 -->

The specific access mechanism depends on the venue's review policy and the artifact's technical requirements. Always verify the instructions provided by the venue before submitting the artifact.

## 10.3. Artifact badge systems

Some artifact evaluation programs use badges or similar labels to communicate aspects of artifact availability, functionality, reproducibility, or reusability. The names, meanings, and requirements of these badges vary across venues and evaluation programs. <!-- Source: MODELS2025 - - ICSE2026 -->

The following categories illustrate concepts that may appear in artifact evaluation programs. The specific requirements for receiving each badge vary across venues and evaluation programs. <!-- Source: ACM2020 - - MODELS2025 - - ICSE2026 - - ICSA2025 - - DamascenoStruber2021 -->

| Badge | What it means |
|---|---|
| Available | The artifact is publicly available in a durable, accessible archival repository with a PID. This generally requires a persistent repository, a stable access link, and a PID. |
| Functional | The artifact has been inspected and found to be documented, consistent, complete, and exercisable. This generally requires sufficient documentation, all relevant components, consistency with the paper, and an executable or otherwise exercisable artifact. |
| Reusable | The artifact is carefully documented and structured to facilitate reuse and repurposing beyond the original paper. This generally requires clear documentation, a well-structured artifact, and adherence to relevant community norms and standards. |
| Reproduced | The main results of the paper have been independently reproduced by a third party using the artifact. |

Some evaluation programs allow functionality to be assessed even when the artifact cannot be made publicly available. For example, an artifact based on industry data subject to strict non-disclosure agreements may be accessible only upon request. <!-- Source: MODELS2025 -->

Regardless of the targeted badge, authors should focus on the quality of the artifact itself rather than on obtaining a particular badge. <!-- Source: MODELS2025 - - ICSE2026 -->

## 10.4. What reviewers typically check

Artifact evaluation may begin with basic checks of operability before moving to a deeper assessment of consistency, completeness, and reusability. The exact sequence and criteria vary across evaluation programs.

### 10.4.1. Initial checks

Before substantive evaluation begins, reviewers verify basic operability. Common problems that block evaluation: <!-- Source: ICSA2025 -->

- Corrupted or missing files.
- Broken or inaccessible links.
- Invalid credentials or expired access tokens.
- Environments that do not start (e.g., VM fails to boot, container crashes).
- Scripts that immediately fail on the simplest example input.

### 10.4.2. Deeper evaluation criteria

After confirming basic operability, reviewers may consider whether: <!-- Source: ICSA2025 - - BeyerWinter2025 -->

- The artifact can be executed and produces results consistent with the paper claims.
- The documentation and structure allow understanding and reuse.
- The artifacts relevant to the paper are available and accessible.
- The artifact can be understood and evaluated without requiring direct interaction with the authors.

## 10.5. Preparing for artifact evaluation

Artifact evaluation is typically conducted under practical constraints, including limited reviewer time, available computational resources, and the time available to complete the evaluation. When preparing an artifact for evaluation, consider these constraints and make the evaluation path as clear and feasible as possible. <!-- Source: Padhye2019 - - ACMSIGMOBILE - - ICSE2026 - - Survey2026 - - SEFM2024 -->

The artifact documentation should make clear: <!-- Source: Padhye2019 - - ACMSIGMOBILE - - ICSE2026 - - Survey2026 - - SEFM2024 -->

- What reviewers need to do to access and execute the artifact.
- What resources and approximate time are required.
- What results or behaviors reviewers should expect.
- Which parts of the evaluation can be performed using reduced configurations, when applicable.

When full execution is impractical because of time or resource constraints, an evaluation may use a reduced configuration or other form of approximate reproduction. The relationship between the reduced configuration and the full experiment should be made explicit so that reviewers can understand what is being evaluated and what differences should be expected. <!-- Source: Padhye2019 -->

Detailed guidance on documentation, execution instructions, resource requirements, and failure recovery is provided in [Module 3](#module-3---documentation) and [Module 4](#module-4---environments-dependencies-and-automation).

## 10.6. Artifact versioning during review

An artifact may be updated during the evaluation process in response to reviewer feedback or to correct problems identified during evaluation. When changes are made, the version being evaluated and any subsequent version should remain clearly distinguishable so that reviewers and authors can identify which artifact version was assessed.

Consider using a concept PID when submitting. It always points to the latest version, eliminating the need to update the link as revisions are made. Once evaluation is complete, switch to a version-specific PID in the camera-ready paper to ensure readers access the exact version associated with the publication. <!-- Source: USENIXSec2026 - - BeyerWinter2025 - - WOOT2025 -->

See [Module 8](#module-8---preservation-versioning-and-maintenance) for guidance on artifact versioning and persistent identifiers.

## 10.7. Clarification period and reviewer interaction

Artifact evaluation typically includes a clarification or rebuttal period during which authors can respond to reviewer concerns. During a clarification period, authors may respond to reviewer questions, clarify reported problems, provide additional information, or submit corrections when permitted by the evaluation process.  <!-- Source: ICSE2026 -->

During this period: <!-- Source: Survey2026 - - Padhye2019 -->

- **Clearly acknowledge problems or limitations.** If something is not working as expected, state this explicitly.

- **Clarify the impact of identified issues.** Distinguish issues that affect the paper's results from minor problems or expected limitations.

- **Provide fixes or updated instructions when feasible.** When changes affect the artifact, create a new version rather than silently modifying the version under evaluation.

#  Complementary Resources

The GAPS complementary resources provide practical resources to support the preparation, documentation, evaluation, and sharing of research artifacts. These resources complement the instructional modules and can be used by researchers, educators, and students according to their needs.

## GAPS Advisor

An interactive advisor that provides context-aware guidance based on the GAPS recommendations and checklist. Rather than presenting the recommendations sequentially, the Advisor identifies requirements relevant to the researcher's artifact and current situation.

[Access the GAPS Advisor](https://notebook.google.com/notebook/17518b1f-e320-48be-a9c2-0edee13c6737)

## Researcher-facing Self-check

A concise checklist to help researchers assess the readiness of their artifacts before sharing or submission.

[Access the Researcher-facing Self-check](https://github.com/anapvasconcelos/GAPS/blob/main/materials/researcher-facing-self-check.md)

## README Template

A ready-to-use template for documenting and communicating a research artifact. It provides a suggested structure covering key aspects of artifact documentation and can be adapted to different artifact types and contexts.

[Access the README Template](https://github.com/anapvasconcelos/GAPS/blob/main/materials/template-README.md)

## GAPS References

A collection of the references that support the recommendations and practices presented throughout GAPS. It provides the literature and guidelines used as the basis for the development of the material.

[Access the GAPS References](https://github.com/anapvasconcelos/GAPS/blob/main/materials/references.md)