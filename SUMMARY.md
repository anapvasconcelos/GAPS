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

---


# GAPS - Guidance for Artifact Preparing and Sharing

## Summary

> **[Module 1 - Foundations of research artifacts](M1/main.md)**

  - [Learning objectives](M1/main.md#learning-objectives)
  - [Open Science](M1/main.md#open-science)
  - [Research Artifacts](M1/main.md#research-artifacts)
  - [Types of research artifacts](M1/main.md#types-of-research-artifacts)
  - [Key characteristics of good research artifacts](M1/main.md#key-characteristics-of-good-research-artifacts)
  - [Common pitfalls and good practices in research artifacts](M1/main.md#common-pitfalls-and-good-practices-in-research-artifacts)
  - [Artifact life cycle](M1/main.md#artifact-life-cycle)
  - [Practical example](M1/main.md#practical-example)
  - [References](M1/main.md#references)
  - [Table of Contents](M1/main.md#table-of-contents)





> **[Module 2 - Artifact-first mindset](M2/main.md)**

  - [Learning objectives](M2/main.md#learning-objectives)
  - [The artifact-first mindset](M2/main.md#the-artifact-first-mindset)
  - [Artifact-first vs. artifact-last](M2/main.md#artifact-first-vs-artifact-last)
  - [Why the artifact-first mindset matters](M2/main.md#why-the-artifact-first-mindset-matters)
  - [Common pitfalls in artifact-first practices](M2/main.md#common-pitfalls-in-artifact-first-practices)
  - [What artifacts should be collected](M2/main.md#what-artifacts-should-be-collected)
  - [Minimum quality expectations](M2/main.md#minimum-quality-expectations)
  - [Design principles for reproducibility](M2/main.md#design-principles-for-reproducibility)
  - [Key takeaway](M2/main.md#key-takeaway)
  - [References](M2/main.md#references)
  - [Table of contents](M2/main.md#table-of-contents)




> **[Module 3 - Preparing research artifacts](M3/main.md)**

- [Module 3 - Preparing research artifacts](#module-3---preparing-research-artifacts)
  - [Data curation](#data-curation)
    - [Qualitative data](#qualitative-data)
  - [Sensitive vs shareable data](#sensitive-vs-shareable-data)
  - [Anonymization strategies](#anonymization-strategies)
  - [Sharing qualitative data](#sharing-qualitative-data)
  - [Shadow repositories](#shadow-repositories)
  - [Internal repository organization: structure and directory organization](#internal-repository-organization-structure-and-directory-organization)
  - [Version control practices](#version-control-practices)
  - [Managing dependencies and isolated environments](#managing-dependencies-and-isolated-environments)
  - [*Optional*: containerization for reproducibility](#optional-containerization-for-reproducibility)
  - [References](#references)
  - [Table of Contents](#table-of-contents)



> **[Module 4 - Documentation and usability](M4/main.md)**

- [Module 4 - Documentation and usability](#module-4---documentation-and-usability)
  - [How to write an effective README](#how-to-write-an-effective-readme)
  - [Execution guide](#execution-guide)
  - [Re-running guide](#re-running-guide)
  - [Reproduction guide](#reproduction-guide)
  - [Metadata and artifact citation standards](#metadata-and-artifact-citation-standards)
  - [Documenting limitations and non-shared components](#documenting-limitations-and-non-shared-components)
  - [References](#references)
  - [Table of contents](#table-of-contents)



> **[Module 5 - Reproducibility and transparency](M5/main.md)**

- [Module 5 - Reproducibility and transparency](#module-5---reproducibility-and-transparency)
  - [How to ensure verifiability](#how-to-ensure-verifiability)
  - [Sharing scripts, pipelines, and parameters](#sharing-scripts-pipelines-and-parameters)
  - [Supporting independent reproduction](#supporting-independent-reproduction)
  - [Limitations (especially for qualitative data)](#limitations-especially-for-qualitative-data)
  - [References](#references)
  - [Table of contents](#table-of-contents)





> **[Module 6 - Packaging and sharing artifacts](M6/main.md)**

- [Module 6 - Packaging and sharing artifacts](#module-6---packaging-and-sharing-artifacts)
  - [Where to publish artifacts (platforms)](#where-to-publish-artifacts-platforms)
  - [Repository structuring for publication](#repository-structuring-for-publication)
  - [What to include and what to omit](#what-to-include-and-what-to-omit)
  - [Assigning DOIs](#assigning-dois)
    - [Providing citation information](#providing-citation-information)
  - [Versioning for submission](#versioning-for-submission)
  - [Choosing appropriate licenses](#choosing-appropriate-licenses)
    - [Why licensing matters](#why-licensing-matters)
    - [Types of licenses](#types-of-licenses)
    - [License comparison](#license-comparison)
      - [Software licenses](#software-licenses)
      - [Content licenses](#content-licenses)
    - [Choosing the right license](#choosing-the-right-license)
        - [Software licenses](#software-licenses-1)
        - [Content licenses](#content-licenses-1)
      - [Choosing licenses by artifact type](#choosing-licenses-by-artifact-type)
    - [Licenses and dependencies](#licenses-and-dependencies)
  - [Consent and data sharing permissions](#consent-and-data-sharing-permissions)
  - [Legal and ethical considerations](#legal-and-ethical-considerations)
  - [Share the artifacts](#share-the-artifacts)
  - [Artifact sharing checklist](#artifact-sharing-checklist)
  - [References](#references)
  - [Table of contents](#table-of-contents)



> **[Module 7 - Artifact submission and review context](M7/main.md)**


- [Module 7 - Artifact submission and review context](#module-7---artifact-submission-and-review-context)
  - [Double-anonymous](#double-anonymous)
  - [Anonymization strategies when required ](#anonymization-strategies-when-required-)
  - [Sources](#sources)
  - [What reviewers typically check in research artifacts](#what-reviewers-typically-check-in-research-artifacts)
  - [References](#references)
  - [Table of contents](#table-of-contents)



> **[Module 8 - Sustainability and long-term maintenance](M8/main.md)**

- [Module 8 - Sustainability and long-term maintenance](#module-8---sustainability-and-long-term-maintenance)
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




> **[Supplementary materials](/supplementary-material/main.md)**

- [Supplementary materials](#supplementary-materials)
  - [Checklists](#checklists)
  - [References](#references)
  - [Table of contents](#table-of-contents)






> [About the GAPS](/README.md)
  
  - [Purpose of the GAPS](#purpose-of-the-gaps)
  - [GAPS Structure](#gaps-structure)
  - [Sources](#sources)
  - [Authors](#authors)
  - [How to cite this material](#how-to-cite-this-material)
  - [GAPS citation file](/CITATION.cff)
  - [License and use](#license-and-use)
  - [GAPS License](/LICENSE)
  - [GAPS Glossary](/glossary.md)
  - [GAPS References](/references.md)
