<div align="center"><nobr>

[README](/README.md) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
[GAPS Structure](../content/structure.md) &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; 
[Supplementary materials](../content/supplementary-material.md)

</nobr></div>

---

![](../GAPS-logo.png)

# README template

**About the template.** This README template was developed based on the guidance provided by GAPS (Guidance for Artifact Preparing and Sharing), with the corresponding GAPS sections referenced throughout the template. It aims to provide comprehensive guidance for documenting research artifacts. The sections and items are classified according to their priority: E (Essential), R (Recommended), and G (Good practice). The classification indicates the importance of the information when applicable. It does not imply that every section applies to every type of research artifact. Some essential sections may therefore be marked as not applicable when they are not relevant to a particular artifact.

- **[E] - Essential:** Information considered fundamental for understanding, accessing, executing, reproducing, or appropriately using the artifact, when applicable to the artifact characteristics.

- **[R] - Recommended:** Information strongly recommended to support the artifact's understanding, execution, reproduction, evaluation, or reuse.

- **[G] - Good practice:** Information or practices that further improve the artifact's quality, clarity, maintainability, transparency, or reuse, but are not generally necessary for its basic use or evaluation.

**Applicability.** The priority classification does not imply that every section applies to every research artifact. Some essential sections may be irrelevant to particular artifact types. Authors should assess the applicability of each section and explicitly indicate when an essential section is not applicable. The template should therefore be adapted to the characteristics of each artifact while preserving the information needed to understand, execute, reproduce, evaluate, and reuse it.

---
---

# 1. [Artifact name] [E]

> - GAPS §3.5.1 - [Artifact purpose statement](../content/M3.md#351-artifact-purpose-statement)
> - GAPS §7.7.1 - [PIDs and immutability at publication](../content/M7.md#771-pids-and-immutability-at-publication)
> - GAPS §8.3.4 - [Version tagging](../content/M8.md#834-version-tagging)

> [!NOTE]
> **What to document:** Identify the artifact and provide the information needed to unambiguously relate it to the corresponding study, including its name, publication, persistent identifier, version, and study context.


**Artifact name:** 

**Replication package for:** 

**Publication:** 

**Paper PID:** 

**Preprint:** [Provide access to the accepted paper, either as a PDF within the artifact repository or as a link to a preprint in an archival repository.]

**Artifact PID:** 

**Version used in the paper:** [Version tag and/or commit identifier. If applicable, provide the version-specific persistent identifier used to produce the results reported in the paper.]


**Study goal:** [One sentence describing what the study investigates.]



## 1.1. Summary [E]

> - GAPS §3.5.1 - [Artifact purpose statement](../content/M3.md#351-artifact-purpose-statement)

> [!NOTE]
> **What to document:** Provide a brief, self-contained description of the artifact, including what it is, what it contains, and what users can do with it. The Summary should allow readers to understand the artifact without reading the rest of the README.


## 1.2. Artifact overview [R]

> - GAPS §3.4.1 - [Folder structure](../content/M3.md#341-folder-structure)
> - GAPS §3.5.1 - [Artifact purpose statement](../content/M3.md#351-artifact-purpose-statement)

> [!NOTE]
> **What to document:** Describe the artifact's main components and functions in more detail, and explain how they support the study. Use this section to provide an overview of how the artifact is organized and how its components relate to one another. Do not repeat the Summary.


## 1.3. Repository structure [E]

> - GAPS §3.4.1 - [Folder structure](../content/M3.md#341-folder-structure)
> - GAPS §3.4.4 - [Distinguishing essential from auxiliary components](../content/M3.md#344-distinguishing-essential-from-auxiliary-components)

> [!NOTE]
> **What to document:** Describe the organization of the repository and the purpose of its main directories and files. Distinguish components required for execution or reproduction from supplementary components so that users can identify which parts are essential to the artifact's operation.


# 2. System requirements [E]

> - GAPS §3.3.1 - [Assumed background and requirements](../content/M3.md#331-assumed-background-and-requirements)
> - GAPS §4.2 - [Reproducible environments](../content/M4.md#42-reproducible-environments)

> [!NOTE]
> **What to document:** Describe the technical requirements needed to use the artifact and provide information about the environment in which it was tested.


## 2.1. Technical background [R]

> - GAPS §3.3.1 - [Assumed background and requirements](../content/M3.md#331-assumed-background-and-requirements)

> [!NOTE]
> **What to document:** Describe the technical knowledge users need to understand and operate the artifact, including knowledge of tools, programming environments, execution procedures, or domain-specific concepts that cannot reasonably be assumed from the README instructions alone.

**Expected user background:** Familiarity with Python, basic knowledge of command-line operations, and the use of Conda environments. No prior knowledge of code-smell detection or large language models is required to reproduce the reported evaluation.


## 2.2. Tested environments [R]

> - GAPS §3.3.1 - [Assumed background and requirements](../content/M3.md#331-assumed-background-and-requirements)
> - GAPS §4.2 - [Reproducible environments](../content/M4.md#42-reproducible-environments)

> [!NOTE]
> **What to document:** Report the environments in which the artifact has actually been tested, including relevant hardware, operating system, software, dependency versions, and other environment characteristics that may affect execution or results. Do not present untested platforms or configurations as supported.


## 2.3. Minimum requirements [E]

> - GAPS §3.3.1 - [Assumed background and requirements](../content/M3.md#331-assumed-background-and-requirements)
> - GAPS §4.2.1 - [Dependency specification](../content/M4.md#421-dependency-specification)

> [!NOTE]
> **What to document:** Specify the minimum conditions required to execute the artifact. Distinguish required resources from optional resources and indicate any uncertainty when minimum requirements have not been directly established. Do not present untested configurations as tested or supported.


### 2.3.1. Hardware requirements

> - GAPS §3.3.1 - [Assumed background and requirements](../content/M3.md#331-assumed-background-and-requirements)
> - GAPS §4.2 - [Reproducible environments](../content/M4.md#42-reproducible-environments)


> [!NOTE]
> **What to document:** Specify the minimum hardware resources required for execution, including processing capacity, memory, storage, graphics hardware, or specialized equipment when applicable.


### 2.3.2. Software dependencies

> - GAPS §4.2.1 - [Dependency specification](../content/M4.md#421-dependency-specification)

> [!NOTE]
> **What to document:** List the software, libraries, frameworks, and other dependencies required for execution, including versions or version constraints sufficient to establish compatibility.


### 2.3.3. Additional requirements

> - GAPS §3.3.1 - [Assumed background and requirements](../content/M3.md#331-assumed-background-and-requirements)

> [!NOTE]
> **What to document:** Identify any additional conditions required to use or execute the artifact that are not covered by the hardware or software requirements, such as credentials, API keys, licenses, external resources, or specialized access, when applicable.


## 2.4. Potential risks and safety considerations [E]

> - GAPS §3.3.4 - [Documenting parameters and configurations](../content/M3.md#334-documenting-parameters-and-configurations)

> [!NOTE]
> **What to document:** Identify conditions or operations that users should know about before executing the artifact because they may affect system state, consume substantial resources, require external access, involve irreversible actions, or create privacy, security, or other safety concerns. Describe the relevant implications and any precautions users should take before execution.


# 3. Installation and setup [E]

> - GAPS §3.3.2 - [Step-by-step execution instructions](../content/M3.md#332-step-by-step-execution-instructions)

> [!NOTE]
> **What to document:** Provide the complete sequence of actions required to obtain, configure, and prepare the artifact for execution. Instructions should be sufficient for a user unfamiliar with the project to reach a ready-to-execute state without relying on undocumented steps.


## 3.1. Obtaining the artifact [E]

> - GAPS §3.3.2 - [Step-by-step execution instructions](../content/M3.md#332-step-by-step-execution-instructions)

> [!NOTE]
> **What to document:** Explain how to obtain the artifact and, when applicable, how to access the specific version associated with the published study. Make clear which version should be used to reproduce the results reported in the paper.


## 3.2. Preparing the artifact [E]

> - GAPS §3.3.2 - [Step-by-step execution instructions](../content/M3.md#332-step-by-step-execution-instructions)
> - GAPS §4.2.1 - [Dependency specification](../content/M4.md#421-dependency-specification)
> - GAPS §4.2.2 - [Environment isolation and portability](../content/M4.md#422-environment-isolation-and-portability)

> [!NOTE]
> **What to document:** Describe the actions required to configure and prepare the artifact for execution, including environment setup, configuration files, environment variables, credentials, licenses, external resources, or other prerequisites that must be addressed before execution.


# 4. Getting started [R]

> - GAPS §4.2.5 - [Ease of use](../content/M4.md#425-ease-of-use)
> - GAPS §4.3.3 - [Modular and incremental execution](../content/M4.md#433-modular-and-incremental-execution)
> - GAPS §10.5 - [Preparing for artifact evaluation](../content/M10.md#105-preparing-for-artifact-evaluation)

> [!NOTE]
> **What to document:** Provide a quick way for users to verify that the artifact has been correctly obtained, prepared, and installed and to observe its basic functionality. When a separate quick-start workflow is useful, describe the minimal steps required to perform this verification. If the full execution workflow already provides a sufficiently quick and straightforward way to perform this verification, do not duplicate it here. Use this section only when a separate quick-start workflow provides value. Do not duplicate the execution instructions.

> [!TIP]
> If the full execution workflow is already sufficiently quick to provide this validation, this section may be omitted.


# 5. Usage and execution [E]

> - GAPS §3.3.2 - [Step-by-step execution instructions](../content/M3.md#332-step-by-step-execution-instructions)
> - GAPS §3.3.3 - [Execution time and resource expectations](../content/M3.md#333-execution-time-and-resource-expectations)

> [!NOTE]
> **What to document:** Describe the procedures required to execute the artifact, from the main workflow through the generation and validation of its outputs. For each execution step, make clear the required context, inputs, outputs, relevant side effects, and conditions that indicate successful completion.


## 5.1. Execution time overview [R]

> - GAPS §3.3.3 - [Execution time and resource expectations](../content/M3.md#333-execution-time-and-resource-expectations)
> - GAPS §10.5 - [Preparing for artifact evaluation](../content/M10.md#105-preparing-for-artifact-evaluation)

> [!NOTE]
> **What to document:** Provide an overview of the human effort, computational time, and relevant resources required for each major execution step. Present this overview before the detailed execution instructions so that users can assess the expected effort and resource requirements in advance. When possible, indicate the environment used to obtain the estimates.


## 5.2. Full reproduction (all results) [E]

> - GAPS §3.3.2 - [Step-by-step execution instructions](../content/M3.md#332-step-by-step-execution-instructions)

> [!NOTE]
> **What to document:** Provide complete, ordered instructions for reproducing the study results using the artifact. Focus on the workflow required to obtain the results reported in the paper rather than on optional or exploratory uses of the artifact. Each step should identify the required execution context, inputs, outputs, relevant resource requirements, and any conditions or side effects that users need to understand before running it.


## 5.3. Demo run (reduced configuration) [G]

> - GAPS §4.2.5 - [Ease of use](../content/M4.md#425-ease-of-use)
> - GAPS §4.3.3 - [Modular and incremental execution](../content/M4.md#433-modular-and-incremental-execution)
> - GAPS §10.5 - [Preparing for artifact evaluation](../content/M10.md#105-preparing-for-artifact-evaluation)

> [!NOTE]
> **What to document:** If the full reproduction requires substantial execution time or computational resources, provide a reduced execution workflow that allows users to exercise the main functionality of the artifact with lower resource or time requirements. Clearly indicate which aspects of the full workflow it represents and whether its outputs are expected to differ from the results reported in the paper. If the full reproduction can be completed without substantial time or resource requirements, a separate demo run is not necessary.


## 5.4. Parameters and configurations [E]

> - GAPS §3.3.4 - [Documenting parameters and configurations](../content/M3.md#334-documenting-parameters-and-configurations)

> [!NOTE]
> **What to document:** Document the parameters, configuration settings, inputs, and other execution choices that can affect the results. Identify which settings were used to produce the results reported in the paper and indicate where the corresponding configuration is defined.


## 5.5. Expected result variability [R]

> - GAPS §6.4.1 - [Expected result variability](../content/M6.md#641-expected-result-variability)

> [!NOTE]
> **What to document:** Describe whether repeated executions of the artifact may produce different results. If results may vary, explain the source of variability and how users can determine whether the observed variation is consistent with the results reported in the paper. Include only the information relevant to your artifact, such as repeated runs, random seeds, expected ranges, or acceptable tolerances. If the artifact produces deterministic results, simply state this and specify any conditions required for reproducibility.


# 6. Expected outputs [E]

> - GAPS §3.3.2 - [Step-by-step execution instructions](../content/M3.md#332-step-by-step-execution-instructions)
> - GAPS §6.4.1 - [Expected result variability](../content/M6.md#641-expected-result-variability)
> - GAPS §3.5.3 - [Mapping outputs to paper results](../content/M3.md#353-mapping-outputs-to-paper-results)

> [!NOTE]
> **What to document:** Identify the outputs produced by successful execution and provide enough information for users to locate, recognize, and interpret them. Distinguish outputs required for the workflow from reference or supplementary outputs when relevant. Indicate which outputs should be compared with reference results when validating the execution.


## 6.1. Linking artifact outputs to paper claims and results [E]

> - GAPS §3.5.3 - [Mapping outputs to paper results](../content/M3.md#353-mapping-outputs-to-paper-results)
> - GAPS §3.5.4 - [Handling comparative evaluations](../content/M3.md#354-handling-comparative-evaluations)
> - GAPS §3.7.1 - [Scope and unsupported claims](../content/M3.md#371-scope-and-unsupported-claims)

> [!NOTE]
> **What to document:** Map the main paper claims, figures, tables, and results supported by the artifact to the corresponding artifact outputs and the scripts or workflow steps that generate them. Identify any relevant paper claims that cannot be supported by the shared artifact and explain why.


# 7. Data [E]

> - GAPS §3.5.2 - [Data description](../content/M3.md#352-data-description)
> - GAPS §2.5.1 - [Tracking data collection and transformation](../content/M2.md#251-tracking-data-collection-and-transformation)

> [!NOTE]
> **What to document:** Describe the data required, produced, or distributed by the artifact, including their structure, provenance, relationship to other data, and processing history. Document the information needed to understand how the data were obtained, transformed, and used in the research.


## 7.1. Dataset overview [R]

> - GAPS §3.5.2 - [Data description](../content/M3.md#352-data-description)

> [!NOTE]
> **What to document:** Provide an overview of each dataset, including its purpose, provenance, scope, size or composition, organization, and relationship to raw, processed, and derived data.


## 7.2. Field description [R]

> - GAPS §3.5.2 - [Data description](../content/M3.md#352-data-description)

> [!NOTE]
> **What to document:** Describe the fields, variables, or attributes needed to understand and use the data, including their meaning, type, units or representation when relevant, and any conventions necessary for correct interpretation.


## 7.3. Data collection and processing [E]

> - GAPS §3.5.2 - [Data description](../content/M3.md#352-data-description)
> - GAPS §2.5.1 - [Tracking data collection and transformation](../content/M2.md#251-tracking-data-collection-and-transformation)

> [!NOTE]
> **What to document:** Describe how the data were collected or obtained and how they were subsequently processed. Document the main preprocessing, cleaning, filtering, inclusion and exclusion criteria, transformations, and derivations that affect the data used in the study.


# 8. Privacy, ethics, and anonymization [E]

> - GAPS §3.7.2 - [Non-shared components](../content/M3.md#372-non-shared-components)
> - GAPS §3.7.4 - [Impact of anonymization on interpretability](../content/M3.md#374-impact-of-anonymization-on-interpretability)
> - GAPS §3.7.3 - [Disclosure statement](../content/M3.md#373-disclosure-statement)
> - GAPS §3.7.6 - [Controlled data access](../content/M3.md#376-controlled-data-access)
> - GAPS §5.2 - [Legal and ethical considerations](../content/M5.md#52-legal-and-ethical-considerations)
> - GAPS §5.3 - [Anonymization strategies](../content/M5.md#53-anonymization-strategies)
> - GAPS §5.4.1 - [Sharing strategies overview](../content/M5.md#541-sharing-strategies-overview)
> - GAPS §5.4.2 - [Shadow repositories](../content/M5.md#542-shadow-repositories)
> - GAPS §5.4.3 - [Preserving analytical value](../content/M5.md#543-preserving-analytical-value)

> [!NOTE]
> **What to document:** Describe the legal, ethical, privacy, confidentiality, and access conditions that affect the sharing, distribution, or use of the artifact. Explain any restrictions that apply to the artifact or its components and indicate how those restrictions affect what can be accessed, reproduced, or reused.

> [!IMPORTANT]
> **Applicability:** Include this section when the artifact involves data, participants, confidentiality, privacy, legal restrictions, or other conditions that affect sharing or use. If none apply, explicitly indicate that the section is not applicable. The subsections should be completed only when the corresponding condition applies.


## 8.1. Non-shared components [E]

> - GAPS §3.7.2 - [Non-shared components](../content/M3.md#372-non-shared-components)

> [!NOTE]
> **What to document:** Identify components that are not included in the shared artifact, explain the reason for their restriction or omission, and describe any alternative materials provided to support understanding, verification, reproduction, or reuse.


## 8.2. Access conditions [E]

> - GAPS §3.7.6 - [Controlled data access](../content/M3.md#376-controlled-data-access)

> [!NOTE]
> **What to document:** When restricted materials can be accessed under controlled conditions, describe who may request access, the conditions that must be satisfied, the procedure for requesting access, and any applicable governance or approval requirements.


## 8.3. Impact of anonymization [R]

> - GAPS §3.7.4 - [Impact of anonymization on interpretability](../content/M3.md#374-impact-of-anonymization-on-interpretability)

> [!NOTE]
> **What to document:** When anonymization or other privacy-preserving transformations affect the shared data, explain how they affect its interpretation, completeness, reproducibility, or reuse, including any limitations introduced by the transformation.


# 9. Scope and limitations [R]

> - GAPS §3.7.1 - [Scope and unsupported claims](../content/M3.md#371-scope-and-unsupported-claims)
> - GAPS §6.4 - [Documenting result variability and limitations](../content/M6.md#64-documenting-result-variability-and-limitations)

> [!NOTE]
> **What to document:** Define what the artifact covers and identify limitations that may affect its execution, results, interpretation, applicability, or reuse. Distinguish limitations inherent to the artifact from aspects of the study that are outside the artifact's scope.


## 9.1. Claims not supported by the artifact [R]

> - GAPS §3.7.1 - [Scope and unsupported claims](../content/M3.md#371-scope-and-unsupported-claims)

> [!NOTE]
> **What to document:** Identify paper claims, results, figures, or analyses that cannot be supported, verified, or reproduced using the shared artifact. Focus on gaps between what is reported in the paper and what the shared artifact makes available. For each unsupported item, explain why it cannot be supported.


## 9.2. Known artifact limitations [R]

> - GAPS §6.4 - [Documenting result variability and limitations](../content/M6.md#64-documenting-result-variability-and-limitations)
> - GAPS §3.7.5 - [Contextual variability in empirical studies](../content/M3.md#375-contextual-variability-in-empirical-studies)

> [!NOTE]
> **What to document:** Describe limitations of the artifact itself that may affect its execution, compatibility, results, interpretation, or reuse. Include limitations that users should consider when applying the artifact under conditions different from those used in its development or evaluation.


# 10. Troubleshooting and known issues [R]

> - GAPS §3.3.5 - [Error recovery](../content/M3.md#335-error-recovery)
> - GAPS §8.4 - [Active maintenance after publication](../content/M8.md#84-active-maintenance-after-publication)
> - GAPS §8.4.1 - [Keeping documentation current](../content/M8.md#841-keeping-documentation-current)

> [!NOTE]
> **What to document:** Document common problems, known issues, expected failures, and how users can resolve them or obtain help. Provide enough information for users to distinguish normal behavior from problems that require intervention.


## 10.1. Getting help [G]

> - GAPS §8.4 - [Active maintenance after publication](../content/M8.md#84-active-maintenance-after-publication)
> - GAPS §8.4.1 - [Keeping documentation current](../content/M8.md#841-keeping-documentation-current)

> [!NOTE]
> **What to document:** Provide a durable channel through which users can report unresolved problems, request clarification, or obtain assistance. Identify where issues should be reported and what information users should provide to facilitate diagnosis.


# 11. Reusability guide [G]

> - GAPS §9.2 - [Designing for reusability](../content/M9.md#92-designing-for-reusability)
> - GAPS §9.3 - [Reusability guide](../content/M9.md#93-reusability-guide)

> [!NOTE]
> **What to document:** Explain how the artifact can be reused or adapted beyond reproducing the original study, when such reuse is feasible. Use the subsections below to describe reusable components and relevant reuse limitations.


## 11.1. Reusable components [G]

> - GAPS §9.2 - [Designing for reusability](../content/M9.md#92-designing-for-reusability)
> - GAPS §9.3 - [Reusability guide](../content/M9.md#93-reusability-guide)

> [!NOTE]
> **What to document:** Identify components that can be reused independently or adapted for other studies, datasets, inputs, or contexts, when applicable. Describe what can be reused, what adaptation is required, and any dependencies or constraints that affect reuse.


## 11.2. Reuse limitations [G]

> - GAPS §9.2 - [Designing for reusability](../content/M9.md#92-designing-for-reusability)
> - GAPS §9.3 - [Reusability guide](../content/M9.md#93-reusability-guide)

> [!NOTE]
> **What to document:** Describe constraints that limit how the artifact can be adapted, extended, or applied to contexts different from the original study. If reuse is substantially limited or not feasible, explain the reasons for those limitations. 



# 12. Version and maintenance [R]

> - GAPS §8.3 - [Versioning and changelogs](../content/M8.md#83-versioning-and-changelogs)
> - GAPS §8.3.4 - [Version tagging](../content/M8.md#834-version-tagging)
> - GAPS §8.3.6 - [Immutability of published versions](../content/M8.md#836-immutability-of-published-versions)
> - GAPS §8.4 - [Active maintenance after publication](../content/M8.md#84-active-maintenance-after-publication)

> [!NOTE]
> **What to document:** Document the current artifact version, its release history, and its expected maintenance status. State whether future updates or maintenance are planned or whether the current release represents the final planned version. Use the subsections below to document the release history and factors that may affect the artifact's long-term maintenance and usability.


## 12.1. Changelog [G]

> - GAPS §3.8.1 - [Changelogs](../content/M3.md#381-changelogs)
> - GAPS §8.3.5 - [Changelog](../content/M8.md#835-changelog)

> [!NOTE]
> **What to document:** Record the changes introduced in each released version in reverse chronological order. Describe changes that may affect the artifact's execution, results, compatibility, structure, or use.


## 12.2. Known maintenance considerations [R]

> - GAPS §8.2 - [Artifact decay: causes and prevention](../content/M8.md#82-artifact-decay-causes-and-prevention)
> - GAPS §8.4 - [Active maintenance after publication](../content/M8.md#84-active-maintenance-after-publication)
> - GAPS §8.4.1 - [Keeping documentation current](../content/M8.md#841-keeping-documentation-current)

> [!NOTE]
> **What to document:** Identify dependencies, external resources, environment assumptions, file formats, services, or other factors that may affect the artifact's long-term usability. Describe any maintenance actions needed to preserve its functionality, accessibility, or reproducibility over time.


# 13. License [E]

> - GAPS §7.6.1 - [Distinguishing software from non-software artifacts](../content/M7.md#761-distinguishing-software-from-non-software-artifacts)
> - GAPS §7.6.2 - [Selecting an appropriate license](../content/M7.md#762-selecting-an-appropriate-license)
> - GAPS §7.6.3 - [Checking compatibility and constraints](../content/M7.md#763-checking-compatibility-and-constraints)
> - GAPS §7.6.4 - [Applying the license correctly](../content/M7.md#764-applying-the-license-correctly)

> [!NOTE]
> **What to document:** Identify the licenses governing the artifact and its individual components, when applicable. Distinguish between software and non-software components, verify that the selected licenses are compatible with the artifact and its dependencies, and indicate which license applies to each component.


# 14. Citation [R]

> - GAPS §7.7.1 - [PIDs and immutability at publication](../content/M7.md#771-pids-and-immutability-at-publication)
> - GAPS §7.7.2 - [CITATION.cff and AUTHORS file](../content/M7.md#772-citationcff-and-authors-file)
> - GAPS §7.7.3 - [Citing the artifact in the paper](../content/M7.md#773-citing-the-artifact-in-the-paper)

> [!NOTE]
> **What to document:** Provide the information required to cite both the paper and the specific artifact version used to produce the reported results. Identify the persistent identifier and version associated with the artifact and provide machine-readable citation metadata when available.


# 15. Authors and contact [G]

> - GAPS §7.7.2 - [CITATION.cff and AUTHORS file](../content/M7.md#772-citationcff-and-authors-file)
> - GAPS §8.4 - [Active maintenance after publication](../content/M8.md#84-active-maintenance-after-publication)

> [!NOTE]
> **What to document:** Identify the contributors responsible for the artifact and provide durable contact information that allows users to report issues, request clarification, or communicate about reuse or collaboration.


# 16. Disclosure statement [G]

> - GAPS §3.7.3 - [Disclosure statement](../content/M3.md#373-disclosure-statement)
> - GAPS §7.8 - [Data Availability Statements (DAS)](../content/M7.md#78-data-availability-statements-das)

> [!NOTE]
> **What to document:** Disclose information that may affect the interpretation, use, evaluation, or transparency of the artifact, including relevant conflicts of interest, funding, ethical considerations, limitations, and material inclusions or exclusions. Do not repeat information already documented elsewhere. Use this section to highlight disclosures that are relevant to the overall interpretation or transparency of the artifact.


> [!IMPORTANT]
> **Data Availability Statement vs. disclosure statement.** The [Data Availability Statement (DAS)](../content/M7.md#78-data-availability-statements-das) is part of the paper and describes which materials support the study, where they are stored, and how they can be accessed. The [Disclosure statement](../content/M3.md#373-disclosure-statement) in the README serves a different purpose: it provides relevant information about the artifact itself, such as limitations, ethical considerations, funding, conflicts of interest, or material inclusions and exclusions, when applicable.

> [!TIP]
> - The [Disclosure statement](../content/M3.md#373-disclosure-statement) **in the README** provides transparency about the artifact.
> - The [Data Availability Statement (DAS)](../content/M7.md#78-data-availability-statements-das) **in the paper** declares the availability and access conditions of the materials supporting the study.

---

*This README follows the structure recommended by [GAPS (Guidance for Artifact Preparing and Sharing)](https://doi.org/[GAPS-DOI]).*