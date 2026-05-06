<table style="width: 100%; border-collapse: collapse; margin: auto;">
  <tbody>
    <tr>
      <td style="border: 0px"> <a href="/M5/main.md"><nobr><- Previous module</nobr></a> </td>
      <td style="width: 50%; border: 0px"> </td>
      <td style="border: 0px"> <a href="/SUMMARY.md"><nobr>GAPS Summary</nobr></a> </td>
      <td style="width: 50%; border: 0px"></td>
      <td style="border: 0px"> <a href="/M7/main.md"><nobr>Next module -></nobr></a> </td>
    </tr>
  </tbody>
</table>

---

![GAPS logo](..\GAPS-logo.png)


# Module 6 - Packaging and sharing artifacts

## Where to publish artifacts

A common mistake when sharing research artifacts is to publish them on personal or institutional websites. While this approach is simple and provides a URL, it does not guarantee long-term availability. Websites change, links break, and content may disappear over time. <!-- MendezEtAl2020 -->

For this reason, for archival purposes avoid using:

- **Personal or institutional websites:** content may be removed or updated without notice.
- **Cloud storage**: designed for storage, not archival; content can be modified or deleted (e.g., Google Drive, Dropbox).
- **Code hosting platforms**: support development, but do not guarantee long-term preservation, as they allow deletion or renaming (e.g., GitHub, GitLab).

These platforms can still be useful during development. However, for publication, they should be complemented with archival repositories.

When selecting a repository, consider:

- Whether it provides a persistent identifier (PID).
- Whether it supports versioning.
- Whether it ensures long-term preservation.
- Whether it allows public access without restrictions.

Repositories such as Zenodo, Figshare, Dataverse, and Dryad provide these important guarantees.

Directories such as [re3data](https://www.re3data.org/) can help identify suitable repositories. <!-- SonjaEtAl2018 -->

A common and recommended approach is:

1. Develop on GitHub.
2. Archive a release on Zenodo/Figshare.
3. Cite the DOI.


## How to publish artifacts

A well-organized artifact is essential for enabling reuse and reproducibility.

Adopt an artifact-first mindset: from the beginning of the study, organize all materials within a clear and consistent structure.

Key principles
- Keep all files inside a single root folder.
- Separate raw data from processed data.
- Organize files according to research stages (e.g., collection, processing, analysis).
- Use clear and consistent naming conventions.

Example structure:

**FIG - Folder structure example.**
```
artifact/
├── 01-data-collection/
│   ├── raw-data/
│   ├── sources/
│   └── data-collection-scripts/
├── 02-data-processing/
│   ├── processed-data/
│   └── data-processing-scripts/
├── 03-analysis/
│   ├── tex-files/
│   ├── analysis-scripts/
│   └── intermediate-results/
├── 04-results/
│   ├── expected-outputs/
│   └── outputs/
├── CITATION.cff
├── LICENSE-CCBY40
├── LICENSE-MIT
└── README.md
```

A good structure should:

- Reflect the steps of the study.
- Make navigation intuitive.
- Clearly indicate the purpose of each file.

In addition, documentation should explain:

- What each folder contains.
- How components relate to each other.
- Which files are required to reproduce results.




### Shadow repositories

In many research projects, especially those involving sensitive, confidential, or proprietary data, it is not possible to make the original raw data publicly available. In such cases, researchers can adopt the use of a *shadow repository*.

A shadow repository is a restricted-access repository that stores the original, non-anonymized data. This repository is kept private and is not shared publicly, ensuring that sensitive information remains protected.

In parallel, a separate public repository is created to host the shareable version of the artifact. This version typically includes anonymized, filtered, or transformed data, along with documentation and materials necessary for understanding and reproducing the study.

Maintaining this separation allows researchers to balance transparency with ethical and legal constraints. It also supports good data management practices by preserving the integrity of the original data while enabling controlled sharing of research artifacts.

When using shadow repositories, it is important to clearly document the relationship between the private and public versions of the data, including what transformations were applied and why certain elements were removed or modified.


## What to publish
<!-- Survey2026 -->

**What to include**

Artifacts should contain everything necessary to understand and reproduce the study:

- Raw data (when possible).
- Processed data.
- Scripts and code (e.g., to collect, transform, and analyze data).
- Study protocols and materials.
- Tools and configurations.

**What to omit**

Remove unnecessary content that increases complexity without adding value:

- Old versions of files.
- Temporary or backup files.
- Unused scripts or data.


**Format matters**

- Separate reusable results (e.g., tables, data behind figures) into text-format files.
- Artifacts should be shared in reusable formats.
  - Avoid sharing data only inside PDFs.
  - Prefer formats that are easy to read, parse, and reuse, such as CSV, JSON, YAML, XML, or HDF5.


### Transparency for restricted or processed data
<!-- Survey2026 -->

In some cases, data cannot be fully shared due to legal, ethical, or privacy constraints. Even in these situations, artifacts should remain as transparent as possible. To achieve this:

- Clearly indicate whether data is original (raw) or processed.
- Rich metadata and detailed dataset descriptions should be included to ensure that others can understand the structure, content, and context of the data (specially when data cannot be openly shared).
- Document all transformations (e.g., anonymization, filtering, aggregating).
- Explain differences between original and shared data.
- Provide instructions for requesting access, when applicable.

Additionally:

- Keep raw data unchanged when possible.
- Perform transformations through scripts.
- Store processed data separately.


### Preparing the artifact package for distribution
<!-- Survey2026 -->

Artifacts should be distributed as self-contained packages.

A well-prepared artifact should include:
- Code and scripts.
- Data (raw and processed, when possible).
- Sample outputs.
- Documentation (README, instructions).

It allows users to:
- Reproduce at least one result from the paper.
- Understand how results were generated.
- Extend or adapt the work.

#### Key principles

- **Self-containment**: All necessary components should be included or clearly specified.

- **Minimal external dependencies**: Avoid requiring downloads during execution. If unavoidable, document them explicitly.

- **Ease of execution**: Reduce setup effort as much as possible.


#### Execution environments

To improve reproducibility, artifacts may include:

- Containerized environments (e.g., Docker).
- Virtual machines.
- Pre-configured environments.

These help ensure consistent execution across systems.


#### Versioning

Each published artifact should correspond to a specific version of the study.

Use:

- Tagged releases.
- Archived versions.

This ensures that others can access exactly the same artifact used in the paper.


### Documentation completeness
<!-- Survey2026 -->

Documentation is as important as code and data. Artifacts must include sufficient documentation to enable independent use, execution, and evaluation, covering three levels:

**Operational documentation**
- How to install and run the artifact.
- Step-by-step instructions.
- Expected outputs.
- Minimal working examples.

**Structural documentation**
- Folder structure.
- Description of files and components.

**Scientific documentation**
- How the artifact supports the paper.
- Mapping between scripts and results.
- Dataset descriptions.

Good documentation should:
- Enable quick validation (quick-start).
- Be clear and concise.
- Reduce ambiguity and guesswork.



### Citation information

To ensure discoverability, proper attribution, and reuse, artifacts should be easy to cite and to follow.

To support this:

- Provide a recommended citation in the `README`.
- Including a machine-readable citation file (e.g., `CITATION.cff`).
- Link to a DOI.

An automatized `.cff` file can be created at the [CFF website](https://citation-file-format.github.io/cff-initializer-javascript/#/).



## Versioning for submission

When submitting a paper, the artifact version must be stable and aligned with the evaluated results.

To ensure consistency:

- Create a tagged release that matches the submitted paper version.
- Avoid modifying the artifact during the review process.
- Use anonymized repositories when double-anonymization review is required.
- Clearly indicate the version used in the paper (e.g., via DOI or tag).

If changes are necessary after submission (e.g., fixes), create a new version instead of modifying the original one.

This ensures that reviewers and future users can access exactly the same artifact associated with the paper.


## Choosing a license for research artifacts

When sharing research artifacts, assigning an explicit license is essential. Without a license, others are not legally allowed to reuse, modify, or redistribute the artifact.

Licensing should be considered at the time of publication, taking into account ownership, reuse goals, and compatibility with publication venues and dependencies.


**Why licensing matters**

A well-chosen license:

- Enables reuse and reproducibility.
- Clarifies legal permissions and restrictions.
- Increases visibility and impact of the artifact.

An inappropriate license, on the other hand, may:

- Restrict reuse unnecessarily.
- Create incompatibilities with other artifacts or dependencies.
- Limit adoption by the community.


The steps below will help you to choose the appropriate license. For more detailed content visit the [Choosing appropriate licenses](/M6/licenses.md) page.

> **Step 1: Choose the license type**

The first decision is to distinguish between software and non-software artifacts:

- **Software licenses**: for code and executable artifacts (e.g., scripts, tools, pipelines)
- **Content licenses**: for non-software artifacts (e.g., datasets, documentation, surveys, reports)

Using the wrong type (e.g., MIT for datasets) should be avoided.


> **Step 2: Select an appropriate license**

**Software artifacts**
- **Copyleft licenses**
  - Require derivatives to remain open.
  - GPL family.

- **Permissive licenses (recommended)**
  - Allow broad reuse with minimal restrictions.
  - MIT, Apache 2.0.

**Practical guidance**: Prefer permissive licenses (MIT or Apache 2.0) unless you explicitly want to enforce openness of derivatives.

---

**Non-software artifacts**
- **CC0 (public domain dedication)**
  - Maximizes reuse (no restrictions)
  - Suitable for datasets and metadata
- **CC BY**
  - Requires attribution
  - Good default for most research artifacts
- **Restrictive variants (avoid when possible)**
  - NC (NonCommercial) and ND (NoDerivatives)
  - Limit reuse and may hinder reproducibility

**Practical guidance**: Use CC0 or CC BY whenever reuse and reproducibility are goals.

> **Step 3: Check compatibility and constraints**

Before finalizing the license:

- **Ownership**: Ensure you have the right to license the artifact (e.g., institution, funder).
- **Dependencies**: Verify compatibility with third-party licenses.
- **Publication venue**: Check publisher requirements.
- **Sensitive data**: Licensing does not override ethical or legal restrictions.


> **Step 4: Apply the license correctly**

To make the license effective:

- Include a LICENSE file in the repository.
- Clearly state what is covered (code, data, documentation).
- Indicate exceptions (e.g., third-party materials, restricted data).
- Provide a link to the full license text.

---

**Decision guide of recommended licenses**

- Code → **MIT** or **Apache 2.0**
- Data → **CC0** or **CC BY**
- Documentation → **CC BY**
- Avoid restrictive clauses (e.g., NC, ND) when reproducibility is a goal.

**Key takeaway**: Licensing is not just a legal formality, it directly affects how your artifact can be reused, reproduced, and extended. Choosing a simple, permissive, and compatible license is often the most effective way to maximize impact.


### Licenses and dependencies

Artifacts often include third-party components. In this case, you must:

- Respect their licenses.
- Ensure compatibility.
- Include required notices.

Be especially careful with:

- Copyleft licenses (e.g., GPL).
- Non-open licenses (e.g., source-available).



## Consent and data sharing permissions




## Legal and ethical considerations




## Artifact packaging formats
<!-- Survey2026 -->

**Package types**

- **Installation package**: Artifacts which consisting of a tool or software system, authors need to prepare an installation package so that the tool can be installed and run in the user's environment.

- **Simple Package**: Artifacts which only contains documents which can be used with a simple text editor, a PDF viewer, or some other common tool (e.g., a spreadsheet program in its basic configuration) the authors can just save all documents in a single package file (zip or tar.gz).


Artifacts should be easy to download, extract, and execute.


## Sharing the artifact

In addition to linking the artifact in the paper, you may share them on social media, mailing lists, or presenting them in talks. Making the work visible increases its impact and encourages reuse.

Publishing is not the final step: visibility also matters.

To increase impact:

- Link the artifact in the paper
- Include the DOI
- Share in talks, social media, and academic channels

Repositories allow version updates while preserving previous versions.
Use this responsibly when fixing issues or improving the artifact.




---

## References

This module builds on a shared set of references used throughout the GAPS material, including guidelines, standards, and research studies on Open Science and research artifacts.

To avoid redundancy and ensure consistency across modules, all references are centralized in the following document: [GAPS References](/references.md).

Contents in this module were adapted and synthesized from these sources.

---

## Table of contents

- [Module 6 - Packaging and sharing artifacts](#module-6---packaging-and-sharing-artifacts)
  - [Where to publish artifacts](#where-to-publish-artifacts)
  - [How to publish artifacts](#how-to-publish-artifacts)
    - [Shadow repositories](#shadow-repositories)
  - [What to publish](#what-to-publish)
    - [Transparency for restricted or processed data](#transparency-for-restricted-or-processed-data)
    - [Preparing the artifact package for distribution](#preparing-the-artifact-package-for-distribution)
      - [Key principles](#key-principles)
      - [Execution environments](#execution-environments)
      - [Versioning](#versioning)
    - [Documentation completeness](#documentation-completeness)
    - [Citation information](#citation-information)
  - [Versioning for submission](#versioning-for-submission)
  - [Choosing a license for research artifacts](#choosing-a-license-for-research-artifacts)
    - [Licenses and dependencies](#licenses-and-dependencies)
  - [Consent and data sharing permissions](#consent-and-data-sharing-permissions)
  - [Legal and ethical considerations](#legal-and-ethical-considerations)
  - [Artifact packaging formats](#artifact-packaging-formats)
  - [Sharing the artifact](#sharing-the-artifact)
  - [References](#references)
  - [Table of contents](#table-of-contents)


---
