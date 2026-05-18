<div align="center"><nobr>

[README](/README.md) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
GAPS structure &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
[Glossary](/glossary.md)

</nobr></div>

---

![GAPS logo](GAPS-logo.png)

# structure

## [Module 1 - Foundations of research artifacts](Content/M1.md)

- [Module 1 - Foundations of research artifacts](Content/M1.md)
  - [Learning objectives](Content/M1.md#learning-objectives)
  - [Open Science](Content/M1.md#open-science)
  - [Research Artifacts](Content/M1.md#research-artifacts)
  - [Types of research artifacts](Content/M1.md#types-of-research-artifacts)
  - [Key characteristics of good research artifacts](Content/M1.md#key-characteristics-of-good-research-artifacts)
  - [Artifact life cycle](Content/M1.md#artifact-life-cycle)
  - [Key takeaways](Content/M1.md#key-takeaways)
  - [Supplementary material of the module](Content/M1.md#supplementary-material-of-the-module)

## [Module 2 - Artifact-first mindset](Content/M2.md)

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
    - [Keep reproduction effort reasonable](#keep-reproduction-effort-reasonable)
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
- [Internal repository organization: structure and directory organization](#internal-repository-organization-structure-and-directory-organization)
  - [Structure the project repository as the artifact](#structure-the-project-repository-as-the-artifact)
  - [Minimum quality expectations](#minimum-quality-expectations)
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
      - [Automate reproducibility](#automate-reproducibility)
      - [Scripts](#scripts)
      - [Pipelines, makefiles, and CI](#pipelines-makefiles-and-ci)
      - [Notebooks](#notebooks)
      - [CI](#ci)
      - [Automatic figure generation](#automatic-figure-generation)
- [Planning data sharing and restrictions](#planning-data-sharing-and-restrictions)
  - [Plan data sharing feasibility upfront](#plan-data-sharing-feasibility-upfront)
  - [File formats and long-term accessibility](#file-formats-and-long-term-accessibility)
- [Practical checklist: what should usually be included?](#practical-checklist-what-should-usually-be-included)
- [Common pitfalls](#common-pitfalls)
- [Key takeaways](#key-takeaways)
- [Supplementary material of the module](#supplementary-material-of-the-module)


## [Module 3 - Preparing research artifacts](Content/M3.md)

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
- [Avoiding hardcoded paths](#avoiding-hardcoded-paths)
- [Supplementary material of the module](#supplementary-material-of-the-module)


## [Module 4 - Documentation and usability](Content/M4.md)

- [Learning objectives](#learning-objectives)
- [Why documentation matters](#why-documentation-matters)
  - [Documentation as a usability and reproducibility factor](#documentation-as-a-usability-and-reproducibility-factor)
  - [Documentation debt and late-stage documentation](#documentation-debt-and-late-stage-documentation)
- [Documentation levels](#documentation-levels)
  - [Operational documentation](#operational-documentation)
  - [Structural documentation](#structural-documentation)
    - [Introduction](#introduction)
    - [Hardware Dependencies section](#hardware-dependencies-section)
    - [Getting Started Guide](#getting-started-guide)
    - [Step-by-Step Instructions](#step-by-step-instructions)
    - [Reusability Guide](#reusability-guide)
  - [Scientific documentation](#scientific-documentation)
      - [Study context](#study-context)
      - [Data](#data)
      - [Reproducibility](#reproducibility)
        - [Reproducibility mapping](#reproducibility-mapping)
      - [Extra experimentation](#extra-experimentation)
      - [Artifact scope and limitations](#artifact-scope-and-limitations)
      - [Transparency](#transparency)
- [Documenting artifact structure](#documenting-artifact-structure)
  - [Why structure documentation matters](#why-structure-documentation-matters)
  - [Documenting folder structure](#documenting-folder-structure)
  - [Explaining naming conventions](#explaining-naming-conventions)
  - [Documenting raw vs processed data](#documenting-raw-vs-processed-data)
  - [Repository navigation and entry points](#repository-navigation-and-entry-points)
  - [Common repository documentation mistakes](#common-repository-documentation-mistakes)
- [How to write an effective README](#how-to-write-an-effective-readme)
  - [Writing style and usability](#writing-style-and-usability)
  - [Required README sections](#required-readme-sections)
    - [Summary of artifacts](#summary-of-artifacts)
    - [Artifact description](#artifact-description)
    - [Citation](#citation)
      - [CITATION.cff](#citationcff)
    - [Licenses](#licenses)
    - [Authors](#authors)
    - [Potential risks](#potential-risks)
    - [Quick start execution guide](#quick-start-execution-guide)
      - [Getting Started Guide](#getting-started-guide-1)
- [Execution and installation documentation](#execution-and-installation-documentation)
  - [INSTALL.md](#installmd)
    - [Purpose](#purpose)
    - [When needed](#when-needed)
    - [Relation to README](#relation-to-readme)
  - [REQUIREMENTS.md / REQUIREMENTS.txt](#requirementsmd--requirementstxt)
  - [System requirements](#system-requirements)
  - [Installation instructions](#installation-instructions)
    - [Steps to reproduce](#steps-to-reproduce)
  - [Container and VM instructions](#container-and-vm-instructions)
  - [Quick validation](#quick-validation)
  - [Troubleshooting](#troubleshooting)
    - [Support](#support)
- [Re-running and reproduction guides](#re-running-and-reproduction-guides)
  - [Re-running guide](#re-running-guide)
    - [Step-by-Step Instructions](#step-by-step-instructions-1)
  - [Reproduction guide](#reproduction-guide)
  - [Mapping scripts to figures and tables](#mapping-scripts-to-figures-and-tables)
  - [Expected behavior and result variability](#expected-behavior-and-result-variability)
- [Metadata and artifact citation standards](#metadata-and-artifact-citation-standards)
  - [Persistent identifiers](#persistent-identifiers)
  - [Citation metadata](#citation-metadata)
  - [Structured metadata for reusable artifacts](#structured-metadata-for-reusable-artifacts)
    - [Structured artifact characterization](#structured-artifact-characterization)
- [Documenting limitations and non-shared components](#documenting-limitations-and-non-shared-components)
  - [Artifact scope and limitations](#artifact-scope-and-limitations-1)
- [Usage instructions](#usage-instructions)
- [Supplementary communication artifacts](#supplementary-communication-artifacts)
  - [Demonstration videos and screencasts](#demonstration-videos-and-screencasts)
- [Documentation enables reproducibility](#documentation-enables-reproducibility)
- [Supplementary material](#supplementary-material)
  - [Support](#support-1)
  - [Limitations and expected behavior](#limitations-and-expected-behavior)
- [Common pitfalls](#common-pitfalls)
- [Key takeaways](#key-takeaways)
- [Sections missing to organize](#sections-missing-to-organize)
    - [Data description](#data-description)
    - [Reproducibility mapping](#reproducibility-mapping-1)
    - [Limitations and expected behavior](#limitations-and-expected-behavior-1)
    - [Support and troubleshooting](#support-and-troubleshooting)
- [Supplementary material of the module](#supplementary-material-of-the-module)


## [Module 5 - Reproducibility and transparency](Content/M5.md)

- [Learning objectives](#learning-objectives)
- [How to ensure verifiability](#how-to-ensure-verifiability)
  - [Validating artifacts before release](#validating-artifacts-before-release)
- [Version control practices](#version-control-practices)
- [Managing dependencies and isolated environments](#managing-dependencies-and-isolated-environments)
- [*Optional*: containerization for reproducibility](#optional-containerization-for-reproducibility)
- [Sharing scripts, pipelines, and parameters](#sharing-scripts-pipelines-and-parameters)
  - [Automate reproducibility](#automate-reproducibility)
    - [End-to-End Automation](#end-to-end-automation)
    - [Modular and incremental execution](#modular-and-incremental-execution)
- [Supporting independent reproduction](#supporting-independent-reproduction)
- [Limitations (especially for qualitative data)](#limitations-especially-for-qualitative-data)
- [Virtualized vs bare-metal execution](#virtualized-vs-bare-metal-execution)
- [What to do before sharing artifacts](#what-to-do-before-sharing-artifacts)
  - [Clean and curate the artifact before release](#clean-and-curate-the-artifact-before-release)
- [Supplementary material of the module](#supplementary-material-of-the-module)


## [Module 6 - Packaging and sharing artifacts](Content/M6.md)

- [Learning objectives](#learning-objectives)
- [Where to publish artifacts](#where-to-publish-artifacts)
  - [Repository selection criteria](#repository-selection-criteria)
- [How to publish artifacts](#how-to-publish-artifacts)
  - [Shadow repositories](#shadow-repositories)
- [What to publish](#what-to-publish)
  - [Transparency for restricted or processed data](#transparency-for-restricted-or-processed-data)
    - [Data Availability Statements (DAS)](#data-availability-statements-das)
  - [Preparing the artifact package for distribution](#preparing-the-artifact-package-for-distribution)
    - [Key principles](#key-principles)
    - [Execution environments](#execution-environments)
    - [Versioning](#versioning)
  - [Documentation completeness](#documentation-completeness)
    - [Structural level documentation](#structural-level-documentation)
        - [Introduction](#introduction)
        - [Hardware Dependencies section](#hardware-dependencies-section)
        - [Getting Started Guide](#getting-started-guide)
        - [Step-by-Step Instructions](#step-by-step-instructions)
        - [Reusability Guide](#reusability-guide)
      - [Documentation content](#documentation-content)
  - [Citation information](#citation-information)
- [Versioning for submission](#versioning-for-submission)
- [Choosing a license for research artifacts](#choosing-a-license-for-research-artifacts)
  - [Licenses and dependencies](#licenses-and-dependencies)
    - [Legal and licensing compliance](#legal-and-licensing-compliance)
- [Consent and data sharing permissions](#consent-and-data-sharing-permissions)
- [Legal and ethical considerations](#legal-and-ethical-considerations)
- [Artifact packaging formats](#artifact-packaging-formats)
  - [Package types](#package-types)
    - [Installation package](#installation-package)
    - [Simple Package](#simple-package)
- [Sharing the artifact](#sharing-the-artifact)
- [The artifact supplementary material](#the-artifact-supplementary-material)
- [Supplementary material of the module](#supplementary-material-of-the-module)


## [Module 7 - Artifact submission and review context](Content/M7.md)

- [Learning objectives](#learning-objectives)
- [Review models and anonymization requirements](#review-models-and-anonymization-requirements)
  - [Open review](#open-review)
  - [Single anonymous review](#single-anonymous-review)
  - [Double anonymous review](#double-anonymous-review)
- [Anonymization strategies when required ](#anonymization-strategies-when-required-)
- [Artifact evaluation tips](#artifact-evaluation-tips)
  - [Require the fewest dependencies](#require-the-fewest-dependencies)
  - [Do not expect the AEC to have lots of physical resources](#do-not-expect-the-aec-to-have-lots-of-physical-resources)
  - [Estimate human + compute time and declare it upfront](#estimate-human--compute-time-and-declare-it-upfront)
  - [Explain side-effects before they occur](#explain-side-effects-before-they-occur)
  - [Enable quick turnaround (via approximation if needed)](#enable-quick-turnaround-via-approximation-if-needed)
  - [Support hotfixing and failure recovery](#support-hotfixing-and-failure-recovery)
  - [Cross-reference claims from the paper (and explain what’s missing)](#cross-reference-claims-from-the-paper-and-explain-whats-missing)
  - [Produce results in a standard human-readable format](#produce-results-in-a-standard-human-readable-format)
  - [Use consistent terminology](#use-consistent-terminology)
- [What reviewers typically check in research artifacts](#what-reviewers-typically-check-in-research-artifacts)
  - [Reproducibility mapping](#reproducibility-mapping)
  - [How to point to the correct artifact](#how-to-point-to-the-correct-artifact)
- [Clarification period and reviewer interaction](#clarification-period-and-reviewer-interaction)
- [Supplementary material of the module](#supplementary-material-of-the-module)


## [Module 8 - Sustainability and long-term maintenance](Content/M8.md)

- [Learning objectives](#learning-objectives)
- [Choosing appropriate archival platforms (avoid personal/institutional pages)](#choosing-appropriate-archival-platforms-avoid-personalinstitutional-pages)
  - [Long-term preservation](#long-term-preservation)
  - [Artifact-paper consistent linking](#artifact-paper-consistent-linking)
- [Semantic versioning](#semantic-versioning)
- [Releases and changelogs](#releases-and-changelogs)
- [Issue and pull request management](#issue-and-pull-request-management)
- [Maintaining artifact usability over time (e.g., environment decay, deprecated dependencies)](#maintaining-artifact-usability-over-time-eg-environment-decay-deprecated-dependencies)
- [Strategies to prevent bit rot](#strategies-to-prevent-bit-rot)
- [Long-term archiving](#long-term-archiving)
  - [Long-term preservation](#long-term-preservation-1)
- [Supplementary material of the module](#supplementary-material-of-the-module)


## [Supplementary material of the modules](Content/supplementary-material.md)

- [Checklists](#checklists)
- [Templates](#templates)
- [README examples](#readme-examples)
- [INSTALL.md examples](#installmd-examples)
- [Supplementary material of the module](#supplementary-material-of-the-module)


## [About the GAPS](/README.md)
  
- [Purpose of the GAPS](/README.md#purpose-of-the-gaps)
- [GAPS Structure](/README.md#gaps-structure)
- [Sources](/README.md#sources)
- [Authors](/README.md#authors)
- [How to cite this material](/README.md#how-to-cite-this-material)
- [Citation file](/CITATION.cff)
- [License and use](/README.md#license-and-use)
- [License](/LICENSE)
- [Glossary of terms](/glossary.md)
- [References](/references.md)


<!-- 
# Summary

- [About the GAPS](/README.md)
  - Purpose of the GAPS
  - [GAPS Structure](/structure.md)
  - Sources
  - Authors
  - How to cite this material
  - Citation file
  - License and use
  - License
  - [Glossary of terms](/glossary.md)
  - [References](/references.md)
- [Module 1 - Foundations of research artifacts](Content/M1.md)
  - Learning objectives
  - Open Science
  - Research Artifacts
  - Types of research artifacts
  - Key characteristics of good research artifacts
  - Artifact life cycle
  - Key takeaways
  - Supplementary material of the module
- [Module 2 - Artifact-first mindset](Content/M2.md)
  - Learning objectives
  - Why the artifact-first mindset matters
  - What is the artifact-first mindset
  - Designing studies for reproducibility
  - Planning artifacts early
  - Structuring repositories and workflows
  - Internal repository organization: structure and directory organization
  - Automation and version control
  - Planning data sharing and restrictions
  - Practical checklist: what should usually be included?
  - Common pitfalls
  - Key takeaways
  - Supplementary material of the module
- [Module 3 - Preparing research artifacts](Content/M3.md)
  - Learning objectives
  - Data curation
  - Sensitive vs shareable data
  - Anonymization strategies
  - Archival requirements for Open Science
  - Avoiding hardcoded paths
  - Supplementary material of the module
- [Module 4 - Documentation and usability](Content/M4.md)
  - Learning objectives
  - Why documentation matters
  - Documentation levels
  - Documenting artifact structure
  - How to write an effective README
  - Execution and installation documentation
  - Re-running and reproduction guides
  - Metadata and artifact citation standards
  - Documenting limitations and non-shared components
  - Usage instructions
  - Supplementary communication artifacts
  - Documentation enables reproducibility
  - Supplementary material
  - Common pitfalls
  - Key takeaways
  - Sections missing to organize
  - Supplementary material of the module
- [Module 5 - Reproducibility and transparency](Content/M5.md)
  - Learning objectives
  - How to ensure verifiability
  - Version control practices
  - Managing dependencies and isolated environments
  - Optional: containerization for reproducibility
  - Sharing scripts, pipelines, and parameters
  - Supporting independent reproduction
  - Limitations (especially for qualitative data)
  - Virtualized vs bare-metal execution
  - What to do before sharing artifacts
  - Supplementary material of the module
- [Module 6 - Packaging and sharing artifacts](Content/M6.md)
  - Learning objectives
  - Where to publish artifacts
  - How to publish artifacts
  - What to publish
  - Versioning for submission
  - Choosing a license for research artifacts
  - Consent and data sharing permissions
  - Legal and ethical considerations
  - Artifact packaging formats
  - Sharing the artifact
  - The artifact supplementary material
  - Supplementary material of the module
- [Module 7 - Artifact submission and review context](Content/M7.md)
  - Learning objectives
  - Review models and anonymization requirements
  - Anonymization strategies when required
  - Artifact evaluation tips
  - What reviewers typically check in research artifacts
  - Clarification period and reviewer interaction
  - Supplementary material of the module
- [Module 8 - Sustainability and long-term maintenance](Content/M8.md)
  - Learning objectives
  - Choosing appropriate archival platforms (avoid personal/institutional pages)
  - Semantic versioning
  - Releases and changelogs
  - Issue and pull request management
  - Maintaining artifact usability over time (e.g., environment decay, deprecated dependencies)
  - Strategies to prevent bit rot
  - Long-term archiving
  - Supplementary material of the module
- [Supplementary material of the modules](Content/supplementary-material.md)
  - Checklists
  - Templates
  - README examples
  - INSTALL.md examples
  - Supplementary material of the module
 -->