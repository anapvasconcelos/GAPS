<!--

<table style="width: 100%; border-collapse: collapse; margin: auto;">
  <tbody>
    <tr>
      <td style="border: 0px"> <a href="/README.md"><nobr>README</nobr></a> </td>
      <td style="width: 50%; border: 0px"> </td>
      <td style="border: 0px"> <nobr>GAPS Summary</nobr> </td>
      <td style="width: 50%; border: 0px"></td>
      <td style="border: 0px"> <a href="/glossary.md"><nobr>Glossary</nobr></a> </td>
    </tr>
  </tbody>
</table>

-->

<div align="center"><nobr>

[README](/README.md) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
GAPS Summary &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
[Glossary](/glossary.md)

</nobr></div>


---


<!--# GAPS - Guidance for Artifact Preparing and Sharing-->

![GAPS logo](GAPS-logo.png)

## Summary

> **[Module 1 - Foundations of research artifacts](Content/M1.md)**

- [Learning objectives](Content/M1.md#learning-objectives)
- [Open Science](Content/M1.md#open-science)
- [Research Artifacts](Content/M1.md#research-artifacts)
- [Types of research artifacts](Content/M1.md#types-of-research-artifacts)
- [Key characteristics of good research artifacts](Content/M1.md#key-characteristics-of-good-research-artifacts)
- [Artifact life cycle](Content/M1.md#artifact-life-cycle)
- [Key takeaways](Content/M1.md#key-takeaways)
- [Supplementary material](Content/M1.md#supplementary-material)


> **[Module 2 - Artifact-first mindset](Content/M2.md)**

- [Learning objectives](#learning-objectives)
- [Why the artifact-first mindset matters](#why-the-artifact-first-mindset-matters)
  - [Why artifact-last fails](#why-artifact-last-fails)
  - [Benefits of artifact-first workflows](#benefits-of-artifact-first-workflows)
- [What is the artifact-first mindset](#what-is-the-artifact-first-mindset)
  - [Artifact-first vs. artifact-last](#artifact-first-vs-artifact-last)
  - [Example: From artifact-last to artifact-first](#example-from-artifact-last-to-artifact-first)
  - [Treat artifacts as first-class research outputs](#treat-artifacts-as-first-class-research-outputs)
- [Designing studies for reproducibility](#designing-studies-for-reproducibility)
  - [Plan artifacts during study design](#plan-artifacts-during-study-design)
  - [Align data structure with the analysis plan](#align-data-structure-with-the-analysis-plan)
  - [Thinking ahead: designing for future reuse](#thinking-ahead-designing-for-future-reuse)
    - [Will someone understand this in 2 years?](#will-someone-understand-this-in-2-years)
    - [Can a collaborator rerun this?](#can-a-collaborator-rerun-this)
    - [What happens if I leave the project?](#what-happens-if-i-leave-the-project)
    - [Can reviewers inspect the workflow?](#can-reviewers-inspect-the-workflow)
- [Planning artifacts early](#planning-artifacts-early)
  - [What artifacts should be collected](#what-artifacts-should-be-collected)
    - [Open Data](#open-data)
    - [Open Material and Open Source](#open-material-and-open-source)
    - [Open Access](#open-access)
- [Structuring repositories and workflows](#structuring-repositories-and-workflows)
  - [Structure the project repository as the artifact](#structure-the-project-repository-as-the-artifact)
  - [Minimum quality expectations](#minimum-quality-expectations)
    - [Suggested directory structure](#suggested-directory-structure)
    - [Separate raw and processed data](#separate-raw-and-processed-data)
    - [Naming conventions](#naming-conventions)
    - [README hierarchy](#readme-hierarchy)
    - [Outputs](#outputs)
    - [Reproducible environments](#reproducible-environments)
  - [Maintain artifacts continuously](#maintain-artifacts-continuously)
- [Automation and version control](#automation-and-version-control)
  - [Manual vs scripted workflows](#manual-vs-scripted-workflows)
  - [Why version control matters](#why-version-control-matters)
  - [Design principles for reproducibility](#design-principles-for-reproducibility)
    - [Automating reproducible workflows](#automating-reproducible-workflows)
      - [Pipelines](#pipelines)
      - [Scripts](#scripts)
      - [Makefiles](#makefiles)
      - [Notebooks](#notebooks)
      - [CI](#ci)
      - [Automatic figure generation](#automatic-figure-generation)
- [Planning data sharing and restrictions](#planning-data-sharing-and-restrictions)
  - [Plan data sharing feasibility upfront](#plan-data-sharing-feasibility-upfront)
  - [File formats and long-term accessibility](#file-formats-and-long-term-accessibility)
- [Practical checklist: what should usually be included?](#practical-checklist-what-should-usually-be-included)
- [Common pitfalls](#common-pitfalls)
- [Key takeaways](#key-takeaways)
- [References](#references)
- [Supplementary material](#supplementary-material)
  - [Table of contents](#table-of-contents)




> **[Module 3 - Preparing research artifacts](Content/M3.md)**

- [Learning objectives](#learning-objectives)
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



> **[Module 4 - Documentation and usability](Content/M4.md)**

- [Internal repository organization: structure and directory organization](#internal-repository-organization-structure-and-directory-organization)
  - [Artifact structure](#artifact-structure)
- [How to write an effective README](#how-to-write-an-effective-readme)
- [Execution guide](#execution-guide)
- [Re-running guide](#re-running-guide)
- [Reproduction guide](#reproduction-guide)
- [Metadata and artifact citation standards](#metadata-and-artifact-citation-standards)
- [Documenting limitations and non-shared components](#documenting-limitations-and-non-shared-components)
- [Documentation and communication artifacts](#documentation-and-communication-artifacts)
- [References](#references)
- [Table of contents](#table-of-contents)



> **[Module 5 - Reproducibility and transparency](Content/M5.md)**

- [How to ensure verifiability](#how-to-ensure-verifiability)
  - [Validating artifacts before release](#validating-artifacts-before-release)
- [Version control practices](#version-control-practices)
- [Managing dependencies and isolated environments](#managing-dependencies-and-isolated-environments)
- [Managing dependencies and isolated environments](#managing-dependencies-and-isolated-environments-1)
- [*Optional*: containerization for reproducibility](#optional-containerization-for-reproducibility)
- [Sharing scripts, pipelines, and parameters](#sharing-scripts-pipelines-and-parameters)
- [Supporting independent reproduction](#supporting-independent-reproduction)
- [Limitations (especially for qualitative data)](#limitations-especially-for-qualitative-data)
- [References](#references)
- [Table of contents](#table-of-contents)






> **[Module 6 - Packaging and sharing artifacts](Content/M6.md)**

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



> **[Module 7 - Artifact submission and review context](Content/M7.md)**


- [Double-anonymous](#double-anonymous)
- [Anonymization strategies when required ](#anonymization-strategies-when-required-)
- [Sources](#sources)
- [What reviewers typically check in research artifacts](#what-reviewers-typically-check-in-research-artifacts)
- [References](#references)
- [Table of contents](#table-of-contents)



> **[Module 8 - Sustainability and long-term maintenance](Content/M8.md)**

- [Choosing appropriate archival platforms (avoid personal/institutional pages)](#choosing-appropriate-archival-platforms-avoid-personalinstitutional-pages)
- [Semantic versioning](#semantic-versioning)
- [Releases and changelogs](#releases-and-changelogs)
- [Issue and pull request management](#issue-and-pull-request-management)
- [Maintaining artifact usability over time (e.g., environment decay, deprecated dependencies)](#maintaining-artifact-usability-over-time-eg-environment-decay-deprecated-dependencies)
- [Strategies to prevent bit rot](#strategies-to-prevent-bit-rot)
- [Long-term archiving](#long-term-archiving)
- [Sources](#sources)
- [References](#references)
- [Table of contents](#table-of-contents)




> **[Supplementary materials](/supplementary-material.md)**

- [Supplementary materials](#supplementary-materials)
  - [Checklists](#checklists)
  - [References](#references)
  - [Table of contents](#table-of-contents)






> [About the GAPS](/README.md)
  
- [Purpose of the GAPS](/README.md#purpose-of-the-gaps)
- [GAPS Structure](/README.md#gaps-structure)
- [Sources](/README.md#sources)
- [Authors](/README.md#authors)
- [How to cite this material](/README.md#how-to-cite-this-material)
- [GAPS citation file](/CITATION.cff)
- [License and use](/README.md#license-and-use)
- [GAPS License](/LICENSE)
- [GAPS Glossary](/glossary.md)
- [GAPS References](/references.md)
