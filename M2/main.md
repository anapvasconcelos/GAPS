<!--

<table style="width: 100%; border-collapse: collapse; margin: auto;">
  <tbody>
    <tr>
      <td style="border: 0px"> <a href="/M1/main.md"><nobr><- Previous module</nobr></a> </td>
      <td style="width: 50%; border: 0px"> </td>
      <td style="border: 0px"> <a href="/SUMMARY.md"><nobr>GAPS Summary</nobr></a> </td>
      <td style="width: 50%; border: 0px"></td>
      <td style="border: 0px"> <a href="/M3/main.md"><nobr>Next module -></nobr></a> </td>
    </tr>
  </tbody>
</table>

-->

<div align="center"><nobr>

[← Previous module](/M1/main.md) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
[GAPS Summary](/SUMMARY.md) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
[Next module →](/M3/main.md)

</nobr></div>

---

![GAPS logo](../GAPS-logo.png)

# Module 2 - Artifact-first mindset

## Learning objectives 

By the end of this module, participants will be able to:

- Understand the artifact-first mindset and how it differs from an artifact-last approach.
- Plan which artifacts to produce and share from the early stages of a study.
- Assess data sharing feasibility considering ethical, legal, and practical constraints.
- Organize data, code, and documentation to support reproducibility.
- Apply practices for continuous artifact maintenance throughout the project.
- Identify and avoid common pitfalls that hinder artifact reuse and reproducibility.

## The artifact-first mindset
<!-- Survey2026 -->

Decisions about where and how to publish artifacts should be made early in the research data management plan. Key questions include: what data and materials will be shared, how long they should be preserved, and under which access conditions. <!-- = SonjaEtAl2018 -->

In practice, openness is often treated as an afterthought, with artifacts prepared only at the end of the project. This module addresses this issue by integrating artifact creation and sharing throughout the entire research lifecycle. <!-- MendezEtAl2020 -->

Adopting an artifact-first mindset means treating artifacts as integral components of the research process, rather than a final packaging step.

### Plan artifacts during study design
- Define early which artifacts will be produced and shared.
- Integrate artifact creation into the research workflow from the beginning.
- Early planning helps avoid undocumented decisions and disorganized data later.


### Plan data sharing feasibility upfront
- Clarify whether data can be shared (e.g., ethical, legal, or consent constraints).
- Adapt data collection and consent procedures accordingly.
- Anticipate limitations, especially for qualitative or sensitive data.

In addition to assessing whether data can be shared, researchers should plan how data will be prepared:

- Choose open and widely supported formats.
- Define required metadata and documentation.
- Anticipate anonymization or transformation needs.

For sensitive data:
- Keep raw data in restricted repositories when needed.
- Share anonymized or filtered versions publicly.
- Clearly define access conditions.
- Document how shared data differs from the original.

Even when data cannot be fully shared, provide rich metadata and sufficient dataset descriptions to support understanding the structure, content, and context.


### Align data structure with the analysis plan
- Organize datasets to match the intended analysis workflows.
- Maintain consistency between raw data, processed data, and analytical procedures.

### Maintain artifacts continuously
- Update and refine artifacts throughout the project, not only at the end.
- Continuous maintenance supports incremental documentation, early error detection, and easier final packaging.

### Structure the project repository as the artifact
- Organize the project so that it can be directly shared as a replication package.
- Ensure that all necessary components (data, code, documentation) are consistently integrated.

### Treat artifacts as first-class research outputs
- Consider artifacts as valuable contributions, not just supporting materials.
- Ensure they are documented, licensed, and preserved accordingly.
- Share scripts, pipelines, and tools used in the research.
- Provide documentation, licensing, and instructions for reuse.

---


## Artifact-first vs. artifact-last

| Artifact-last approach | Artifact-first approach |
|----------------------|------------------------|
| Artifacts prepared at the end | Artifacts developed continuously |
| Data scattered across tools and folders | Structured and versioned data |
| Manual and undocumented steps | Scripted and traceable processes |
| High effort at submission time | Low effort at submission time |
| Limited reproducibility | Built-in reproducibility |


---


### Example: From artifact-last to artifact-first

Instead of:

- Collecting data manually and storing it in spreadsheets.
- Running analysis through manual steps.
- Reconstructing the workflow at the end.

An artifact-first approach would:

- Use scripts to collect and store data in structured formats.
- Version control all intermediate steps.
- Automatically generate results (tables and figures).
- Maintain documentation throughout the process.

At the end of the project, the artifact is already close to a publishable package, requiring minimal additional effort.

---



## Why the artifact-first mindset matters

Without an artifact-first approach, many research projects face recurring problems:

- Data becomes disorganized or partially lost.
- Key decisions are not documented.
- Results cannot be reproduced, even by the original authors.
- Preparing artifacts at the end becomes time-consuming and error-prone.

In contrast, an artifact-first mindset:

- Reduces rework at the end of the project.
- Improves traceability of decisions and results.
- Makes reproducibility a natural outcome of the workflow.
- Facilitates collaboration and onboarding of new team members.


---



## Common pitfalls in artifact-first practices

Even when researchers aim to adopt better practices, some common mistakes persist:

- Treating artifacts as a final task instead of a continuous process.
- Mixing raw and processed data.
- Relying on manual steps that are not documented.
- Using proprietary or non-reproducible tools without alternatives.
- Failing to track versions of data and scripts.

Avoiding these pitfalls is essential to make artifacts reusable and reproducible.


---


## What artifacts should be collected
<!-- Montgomery2024 -->

When adopting an artifact-first mindset, researchers should think early about which materials will be part of the final artifact package.

This decision directly affects how reproducible and reusable the study will be.

To guide this process, artifact content can be grouped into three main categories:


> **Open Data**

All data that contributed to the scientific claims made in your paper.

- **Raw data**: Data that is used to generate or support claims in your scientific work. This data is typically untouched by the analysis, often even before cleaning, since cleaning may introduce bias. 
 
- **Derived Data**: Data that is created as a result of your scientific analysis (automatically or manually). This includes models trained through machine learning algorithms and data created as a result of qualitative methods, such as coding tables, schemas, etc.

- **Protocols and study design artifacts**: Data pertaining to the planning, execution, and adjustment of your scientific work. This includes logs of decisions taken by participating scientists, protocols given to study participants, rationale for change requests, discussion notes, etc.

- **Figures, Tables, and Extended Findings**: Data used to generate figures and tables, as well as the original PNGs, PDFs, and LaTeX used to generate them in your paper. It also includes the generated figures and tables itself.


> **Open Material** and **Open Source**

All material that contributed to the scientific claims made in your paper. Future researchers need these materials and tools to replicate, verify, and improve on your work.

- **Data Collection Scripts**: Scripts used to collect your research data. E.g., a custom web scraper, a script to iteratively access an API, an HTML-to-SQL data-writing script.

- **Data Transformation Scripts**: Scripts used to transform data in unique ways. E.g., static analysis, machine learning, image recognition, generative AI.

- **Analysis Scripts**: Scripts used to analyze your final output data. Whether data from surveys, observations, or output vectors of a machine learner, it is likely that you used scripts to interpret and produce results (tables and figures) from that data.

- **Software Tools**: Software tools used in your research. E.g., a custom survey tool, a new IDE, a Jira or GitLab plugin, etc.



> **Open Access**

Future users should be able to find and access the associated paper. You should include a permanent DOI link to your Open Access paper in the README.md, as well as the permanent DOI to the published version.


- **Manuscript**: The paper itself (linked via DOI).


The openness of research also depends on sharing materials beyond data.<!-- SonjaEtAl2018 -->

**Protocols**: A protocol describes a formal or official record of scientific experimental observations in a structured format. <!-- SonjaEtAl2018 -->

**Notebooks, containers, software, and hardware**: Reproducible analysis is aided by the use of literate programming, container technology, and virtualization. In addition to sharing your code and data, also share your Jupyter notebooks, Docker images, or other analysis materials or software dependencies.  <!-- SonjaEtAl2018 -->

Researchers may be reluctant to share their data because they are afraid that others will reuse them before they have extracted the maximum usage from them, or that others might not fully understand the data and therefore misuse them. <!-- SonjaEtAl2018 --> 
They may publish their data to make them findable with metadata, but set an embargo period on the data to make sure that they can publish their own paper(s) first. <!-- SonjaEtAl2018 -->



## Minimum quality expectations

Once artifacts are defined, their quality directly affects transparency, reproducibility, and reuse.

### File formats and long-term accessibility
<!-- SonjaEtAl2018 -->

To ensure long-term accessibility and reuse, researchers should prefer open and well-documented file formats.

- Avoid proprietary or patent-encumbered formats when possible.
- Prefer formats based on open standards.
- Avoid unnecessary compression and encryption for archived materials, as they may hinder direct access and reuse.

Examples of recommended formats include:

- **Text**: TXT, ODT, PDF/A, XML.
- **Tabular data**: CSV, TSV.
- **Images**: TIFF, PNG, JPG 2000, SVG, WebP.
- **Audio**: WAV, FLAC, OPUS.
- **Video**: MPEG2, VP8, VP9, AV1, Motion JPG 2000 (MJ2).
- **Binary hierarchical data** (structured data): HDF5.

While formats such as CSV and TSV are preferred for reproducibility and long-term accessibility, spreadsheet formats (e.g., XLSX) remain widely used for human inspection and exploratory analysis.

When appropriate, consider providing both:
- a **machine-friendly version** (e.g., CSV) for reproducibility and automation, and
- a **human-friendly version** (e.g., XLSX) for readability and manual inspection.

However, XLSX files should not be used as the sole representation of tabular data.

In some cases, proprietary formats cannot be avoided. When this happens, consider providing additional documentation or alternative representations when possible.

Also, check whether your target repository defines preferred formats for submission.



## Design principles for reproducibility

Prefer script-based and version-controllable tools (e.g., R, Python) over point-and-click software (e.g., SPSS when used without syntax) or programs producing binary files (e.g., Excel). Scripted workflows improve transparency, reproducibility, and version control. <!-- MendezEtAl2020 -->

---

## Key takeaway

An artifact-first mindset shifts artifact creation from a final obligation to a continuous research practice.

By planning, organizing, and maintaining artifacts throughout the project, researchers reduce effort at publication time while significantly improving reproducibility, transparency, and reuse.

---

## References

This module builds on a shared set of references used throughout the GAPS material, including guidelines, standards, and research studies on Open Science and research artifacts.

To avoid redundancy and ensure consistency across modules, all references are centralized in the following document: [GAPS References](/references.md).

Contents in this module were adapted and synthesized from these sources.

---


## Table of contents

- [Module 2 - Artifact-first mindset](#module-2---artifact-first-mindset)
  - [Learning objectives](#learning-objectives)
  - [The artifact-first mindset](#the-artifact-first-mindset)
    - [Plan artifacts during study design](#plan-artifacts-during-study-design)
    - [Plan data sharing feasibility upfront](#plan-data-sharing-feasibility-upfront)
    - [Align data structure with the analysis plan](#align-data-structure-with-the-analysis-plan)
    - [Maintain artifacts continuously](#maintain-artifacts-continuously)
    - [Structure the project repository as the artifact](#structure-the-project-repository-as-the-artifact)
    - [Treat artifacts as first-class research outputs](#treat-artifacts-as-first-class-research-outputs)
  - [Artifact-first vs. artifact-last](#artifact-first-vs-artifact-last)
    - [Example: From artifact-last to artifact-first](#example-from-artifact-last-to-artifact-first)
  - [Why the artifact-first mindset matters](#why-the-artifact-first-mindset-matters)
  - [Common pitfalls in artifact-first practices](#common-pitfalls-in-artifact-first-practices)
  - [What artifacts should be collected](#what-artifacts-should-be-collected)
  - [Minimum quality expectations](#minimum-quality-expectations)
    - [File formats and long-term accessibility](#file-formats-and-long-term-accessibility)
  - [Design principles for reproducibility](#design-principles-for-reproducibility)
  - [Key takeaway](#key-takeaway)
  - [References](#references)
  - [Table of contents](#table-of-contents)

---
