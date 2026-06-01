<table style="width: 100%; border-collapse: collapse; margin: auto;">
  <tbody>
    <tr>
      <td style="border: 0px"> <a href="/supplementary-material/main.md"><nobr>Supplementary material</nobr></a> </td>
      <td style="width: 50%; border: 0px"> </td>
      <td style="border: 0px"> <a href="/structure.md"><nobr>GAPS structure</nobr></a> </td>
      <td style="width: 50%; border: 0px"></td>
      <td style="border: 0px"> <a href="/glossary.md"><nobr>Glossary</nobr></a> </td>
    </tr>
  </tbody>
</table>

---

![](../GAPS-logo.png)

# Checklists



## Pre-launch

<!-- OpenSourceGuides -->
Ready to open source your project? Here’s a checklist to help. Check all the boxes? You’re ready to go! Click "publish" and pat yourself on the back.

>**Documentation**

<input type="checkbox"> Project has a LICENSE file with an open source license

<input type="checkbox"> Project has basic documentation (README, CONTRIBUTING, CODE_OF_CONDUCT)

<input type="checkbox"> The name is easy to remember, gives some idea of what the project does, and does not conflict with an existing project or infringe on trademarks

<input type="checkbox"> The issue queue is up-to-date, with issues clearly organized and labeled

>**Code**

<input type="checkbox"> Project uses consistent code conventions and clear function/method/variable names

<input type="checkbox"> The code is clearly commented, documenting intentions and edge cases

<input type="checkbox"> There are no sensitive materials in the revision history, issues, or pull requests (for example, passwords or other non-public information)

>**People**

***If you’re an individual:***

<input type="checkbox"> You've talked to the legal department and/or understand the IP and open source policies of your company (if you're an employee somewhere)

***If you’re a company or organization:***

<input type="checkbox"> You've talked to your legal department

<input type="checkbox"> You have a marketing plan for announcing and promoting the project

<input type="checkbox"> Someone is committed to managing community interactions (responding to issues, reviewing and merging pull requests)

<input type="checkbox"> At least two people have administrative access to the project

---

## LLM sharing

The following checklist helps authors assess the maturity of their artifacts across four Reproducibility Maturity Model tiers (RMM-Tiers). <!-- SiddiqEtAl2025 -->

> **RMM-0: Minimal Reproducibility (Low Maturity)**

Artifacts are missing, inaccessible, or only partially available. Environment specifications are vague or absent, versions are unpinned, reproduction depends heavily on implicit assumptions. Multiple reproducibility smells can co-occur.

<input type="checkbox"> All artifacts are accessible and available.

<input type="checkbox"> Environment details are sufficient to recreate the setup.

<input type="checkbox"> Versions are explicitly specified (not floating).

<input type="checkbox"> Licensing is clear and allows reuse.

<!-- 
Reviewer checklist.
<input type="checkbox"> Are any artifacts inaccessible or missing?
<input type="checkbox"> Are the environmental details insufficient to recreate the setup?
<input type="checkbox"> Are versions unspecified or floating?
<input type="checkbox"> Does legal ambiguity prevent reuse?
<input type="checkbox"> -->


> **RMM-1: Operational Reproducibility (Intermediate Maturity)**

Artifacts are functional at publication time but vulnerable to dependency drift.
Instructions exist, but require manual reconstruction. Containers or scripts may exist, but are incomplete or rely on deprecated APIs.

<input type="checkbox"> Installation steps are clearly documented and robust.

<input type="checkbox"> Versions are documented across components.

<input type="checkbox"> Pipelines are runnable with reasonable effort.

<input type="checkbox"> Licenses are present and cover the main components.

<!-- 
Reviewer checklist.
<input type="checkbox"> Are installation steps documented but potentially brittle?
<input type="checkbox"> Are versions given but not pinned at all hierarchy levels?
<input type="checkbox"> Are pipelines runnable but not fully automated?
<input type="checkbox"> Are licenses present but incomplete or unclear?
-->


> **RMM-2: Durable Reproducibility (High Maturity)**

Artifacts are fully runnable, containerized, versioned, and legally open. All five axes are satisfied. Outputs can be reproduced end-to-end with no manual inference.

<input type="checkbox"> A containerized or automated pipeline is provided.

<input type="checkbox"> All dependencies are pinned (OS, libraries, models).

<input type="checkbox"> Datasets and models are persistently hosted with stable identifiers.

<input type="checkbox"> All components are clearly licensed for reuse.

<!--
Reviewer checklist.
<input type="checkbox"> Is a containerized or automated pipeline provided?
<input type="checkbox"> Are all dependencies pinned, including OS, libraries, and models?
<input type="checkbox"> Are datasets and models persistently hosted with stable identifiers?
<input type="checkbox"> Are all components licensed for reuse?
-->


> **RMM-3: Independently Verified Reproducibility (Very High Maturity)**

This artifact reflects a level of reproducibility that extends beyond the authors' own artifacts. An external reviewer or independent research group can successfully reexecute the full experimental pipeline and reproduce the key findings using the provided artifacts without modification. Because this tier requires substantial effort outside the standard publication workflow, we treat it as an optional, evaluation-driven extension analogous to the ACM Results Reproduced badge rather than a requirement for authors at submission time.

<input type="checkbox"> The results can be reproduced using only the provided artifacts and instructions.

<input type="checkbox"> Reproduction has been validated by an independent party (if available).

<input type="checkbox"> Outputs (tables, figures, metrics) match those reported in the paper.

<input type="checkbox"> The full pipeline runs successfully in a clean environment.

<!--
Reviewer checklist.
<input type="checkbox"> Can the results be reproduced exactly using only the provided artifacts and
instructions?
<input type="checkbox"> Was the reproduction performed independently, without author intervention?
<input type="checkbox"> Are all outputs (tables, figures, metrics) consistent with those reported in the paper?
<input type="checkbox"> Does the reproduction process complete successfully in a clean environment?
-->


-----------
<!--
## Artifact maturity level <!-- SiddiqEtAl2025 -- >

| Axis | Minimal | Operational | Durable |
| --- | --- | --- | --- |
| Accessibility | <input type="checkbox"> No or fragmented artifacts; links missing, private, or ephemeral | <input type="checkbox"> Artifacts hosted but with fragile links (personal cloud, ad-hoc URLs); partial coverage of code/data/models. | <input type="checkbox"> Artifacts versioned and persistently hosted (e.g., DOI, archival repository) with clear mapping to experiments. |
| Environment Specification | <input type="checkbox"> Environment details largely absent; no explicit hardware/software requirements. | <input type="checkbox"> Basic installation steps documented, but incomplete dependency lists and implicit assumptions about the platform. | <input type="checkbox"> Complete, machinereadable environment specification (e.g., lockfiles, container specs) covering OS, libraries, and hardware. |
| Versioning Rigor | <input type="checkbox"> Floating versions or unspecified model/dataset snapshots; reproducibility depends on latest defaults. | <input type="checkbox"> Some versions documented (e.g., major library versions), but not consistently pinned across the stack. | <input type="checkbox"> Pinned versions at all hierarchy levels (datasets, models, frameworks, CUDA, etc.), with change logs or manifests. |
| Execution Fidelity | <input type="checkbox"> No runnable scripts; only high-level prose or pseudo-code. | <input type="checkbox"> Pipelines runnable with manual effort (e.g., several shell commands, manual downloads, adhoc scripts). | <input type="checkbox"> End-to-end, automated pipelines or containers that re-create results from scratch with minimal manual steps. |
| Legal Openness | <input type="checkbox"> Licenses absent, incompatible, or ambiguous; reuse is legally risky. | <input type="checkbox"> Some components licensed, but coverage incomplete or terms unclear for key artifacts (e.g., models, datasets). | <input type="checkbox"> Explicit, compatible licenses for all artifacts required to reproduce results, enabling legal reuse and redistribution. |

-----------
-->

--

## The FAIR Data Principles
<!-- WilkonsonEtAl2018 -->

> **To be Findable:**

<input type="checkbox"> F1. (meta)data are assigned a globally unique and eternally persistent identifier.

<input type="checkbox"> F2. data are described with rich metadata.

<input type="checkbox"> F3. (meta)data are registered or indexed in a searchable resource.

<input type="checkbox"> F4. metadata specify the data identifier.

>**To be Accessible:**

<input type="checkbox"> A1. (meta)data are retrievable by their identifier using a standardized communications protocol.

<input type="checkbox"> A1.1 the protocol is open, free, and universally implementable.

<input type="checkbox"> A1.2 the protocol allows for an authentication and authorization procedure, where necessary.

<input type="checkbox"> A2 metadata are accessible, even when the data are no longer available.

>**To be Interoperable:**

<input type="checkbox"> I1. (meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.

<input type="checkbox"> I2. (meta)data use vocabularies that follow FAIR principles.

<input type="checkbox"> I3. (meta)data include qualified references to other (meta)data.

>**To be Re-usable:**

<input type="checkbox"> R1. (meta)data have a plurality of accurate and relevant attributes.

<input type="checkbox"> R1.1. (meta)data are released with a clear and accessible data usage license.

<input type="checkbox"> R1.2. (meta)data are associated with their provenance.

<input type="checkbox"> R1.3. (meta)data meet domain-relevant community standards.

---


## How FAIR are your data?
<!-- não está nas referências: https://dmeg.cessda.eu/content/download/3845/35038/file/20170707_How_FAIR_are_your_data_Jones.pdf 
‘How FAIR are your data?’ checklist, CC-BY by Sarah Jones & Marjan Grootveld, EUDAT. Image CC-BY-SA by SangyaPundir-->

> **Findable:**

It should be possible for others to discover your data. Rich metadata should be available online in a searchable resource, and the data should be assigned a persistent identifier.

<input type="checkbox"> A persistent identifier is assigned to your data.

<input type="checkbox"> There are rich metadata, describing your data.

<input type="checkbox"> The metadata are online in a searchable resource e.g. a catalogue or data repository.

<input type="checkbox">. The metadata record specifies the persistent identifier



>**Accessible:**

It should be possible for humans and machines to gain access to your data, under specific conditions or restrictions where appropriate. FAIR does not mean that data need to be open! There should be metadata, even if the data aren’t accessible.

<input type="checkbox"> Following the persistent ID will take you to the data or associated metadata.

<input type="checkbox"> The protocol by which data can be retrieved follows recognised standards e.g. http.

<input type="checkbox"> The access procedure includes authentication and authorisation steps, if necessary.

<input type="checkbox"> Metadata are accessible, wherever possible, even if the data aren’t.



>**Interoperable:**

Data and metadata should conform to recognised formats and standards to allow them to be combined and exchanged.

<input type="checkbox"> Data is provided in commonly understood and preferably open formats.

<input type="checkbox"> The metadata provided follows relevant standards.

<input type="checkbox"> Controlled vocabularies, keywords, thesauri or ontologies are used where possible.

<input type="checkbox"> Qualified references and links are provided to other related data.



>**Re-usable:**
Lots of documentation is needed to support data interpretation and reuse. The data should conform to community norms and be clearly licensed so others know what kinds of reuse are permitted.

<input type="checkbox"> The data are accurate and well described with many relevant attributes.

<input type="checkbox"> The data have a clear and accessible data usage license.

<input type="checkbox"> It is clear how, why and by whom the data have been created and processed.

<input type="checkbox"> The data and metadata meet relevant domain standards.

---


## Core licensing checklist
<!-- SonjaEtAl2018 -->

When selecting and applying a license to research artifacts, consider the following:

- [ ] **Choose an appropriate license for the artifact type.**
- Use software licenses (e.g., MIT, Apache) for code and implementation artifacts.
- Use content licenses (e.g., CC BY, CC0) for datasets, documentation, and other non-software materials.

- [ ] **State the license clearly and prominently.**
- Include it in the repository by a `LICENSE` file.
<!--  - Prefer machine-readable license formats when possible (e.g., using standard identifiers such as SPDX and including a LICENSE file). This allows platforms and tools to automatically detect and interpret the license.-->

- [ ] **Provide references to the license.**
- Link to the full license text or official page.

- [ ] **Explain permissions and restrictions.**
- Clarify what others are allowed to do (reuse, modify, redistribute).
- Highlight any limitations that may affect reproducibility or reuse.

- [ ] **Clarify the scope of the license.**
- Explicitly state what parts of the artifact are covered (e.g., code, data, documentation).
- Make clear when some components are not covered (e.g., third-party materials, restricted data).
- Note that licensing metadata or documentation does not necessarily imply that all underlying content is open.

- [ ] **Ensure compatibility with dependencies.**
- Verify that the licenses of third-party libraries, datasets, or tools are compatible with your chosen license.
- Be especially careful with copyleft licenses (e.g., GPL, AGPL), which may impose constraints on your project.

- [ ] **Consider reuse and interoperability.**
- Prefer permissive licenses when the goal is broad reuse and integration.
- Avoid restrictive clauses (e.g., NC, ND) when reproducibility and reuse are priorities.

- [ ] **Explain the rationale for your choice.**
- Briefly justify why the license was selected (e.g., maximize reuse, ensure attribution, enforce openness of derivatives).

- [ ] **Clarify ownership and rights.**
- Identify who holds the copyright (e.g., authors, institution, funder).
Ensure that you have the rights to license all included materials.

---


## Artifact packaging and sharing step-by-step
<!-- Montgomery2024 -- > <!-- MendezEtAl2020 -- > <!-- Survey2026 -->

> - [ ] All files organized in a single root folder.
- Create a folder, and put every single file of your artifact into that folder.
- All the files must be in this folder.

> - [ ] Clean e anonymize the data.

> - [ ] Irrelevant files removed.
- Open each file in the artifact folder and decide what to share and what to discard.
  


> - [ ] Clear folder structure defined.

> - [ ] Define the appropriate licenses.

Now that you organize and know all the artifact files that will be made available, you should define the appropriate license for each type of artifact shared.

Note that each artifact may have a different license. The artifacts should have one or more licenses attached to explicitly describe how third-parties can use them. It depends on your choice.

There is no single "best" license for all artifacts. Instead, the choice should reflect how the artifact is intended to be reused. In general:
- Prefer CC0 for data.
- Prefer CC BY for content.
- Prefer software licenses for code

> - [ ] Create `LICENSE` file(s)

**For artifacts under CC licenses.**
- Use the [CC License Chooser](https://chooser-beta.creativecommons.org/) to create the license disclaimer text. It will look similar to: "Artifact © 2023 by Author is licensed under Attribution 4.0 International".

**For artifacts under other licenses.**
- Sites such as [choosealicense.com](https://choosealicense.com/) give you the full text of the license you have chosen.

**Put the license text in your artifact.**
- Create a file named `LICENSE` and put it in the top level artifact folder (in the root).
  - The norm is to place them at the top-level, but you may choose to place them within the folder that contains the appropriate content.
  - If your artifact have more than one license, put specific names for each one and put all license files in the top level artifact folder (in the root).
    - e.g., `LICENSE-MIT`, `LICENSE-CC`, `LICENSE-APACHE`, etc.

- Paste the full license texts in each `LICENSE` file and place them in the appropriate places. 

> - [ ] Create a `CITATION.cff` file
  
You can create a citation file at the [CFF website](https://citation-file-format.github.io/cff-initializer-javascript/#/).
  
To create this file you will need the DOI. So you first will initiate the upload process to generate the DOI and before submitting the artifacts to upload you will conclude the creation of the citation that will be included in the top level artifact folder (in the root).


> - [ ] Create a `INSTALL.md` file (if needed)

This file is essential if your artifact requires more than opening PDFs, CSVs, etc.

- Create a file named `INSTALL.md` and put it in the top level artifact folder (in the root).


> - [ ] Create a `README.md` file

Create a file named `README.md` and put it in the top level artifact folder (in the root).

> - [ ] Include a rich metadata

- The abstract description of a data set (metadata) could be found and accessed online, even if the access to the full data set would only be granted upon request and only for specific research purposes (carefully selected and laid out by the owners of that data set).

> - [ ] Artifact archived in DOI-enabled repository

- Choose an online public access platform which provide a DOI and immutable data to archive your artifacts.

> - [ ] Share the artifacts


---


## Practical checklist for implementing artifact-first practices
<!-- SonjaEtAl2018 -->

The following checklist operationalizes the artifact-first mindset. It provides concrete actions that can be applied throughout the research lifecycle.

> **Plan for reproducibility before you start**

- [ ] **Create a study plan or protocol.**
- Begin documentation at study inception by writing a study plan or protocol that includes your proposed study design and methods.
- Track changes to your study plan or protocol using version control.
- Calculate the power or sample size needed and report this calculation in your protocol as underpowered studies are prone to irreproducibility.

- [ ] **Choose reproducible tools and materials**
- Whenever possible, choose software and hardware tools where you retain ownership of your research and can migrate your research out of the platform for reuse.

- [ ] **Set-up a reproducible project**
- Centralize and organize your project management using an online platform, a central repository, or folder for all research files.
- Within your centralized project, follow best practices by separating your data from your code into different folders.
- Make your raw data read-only and keep separate from processed data.
- When saving and backing up your research files, choose formats and informative file names that allow for reuse.
- File names should be both machine- and human-readable.
- In your analysis and software code, use relative paths.
- Avoid proprietary file formats and use open file formats.



> **Keep track of things**

- [ ] **Registration**
- Preregister important study design and analysis information to increase transparency and counter publication bias of negative results.

- [ ] **Version control**
- Track changes to your files, especially your analysis code, using version control.

- [ ] **Documentation**
- Document everything done by hand in a README file.
- Create a data dictionary (also known as a codebook) to describe important information about your data.

- [ ] **Literate programming**
- Consider using approaches (e.g., Jupyter Notebooks, KnitR, Sweave) to literate programming to integrate your code with your narrative and documentation.



> **Share and license your research**

- [ ] **Data**
- Avoid supplementary files, decide on an acceptable permissive license, and share your data using a repository.

- [ ] **Materials**
- Share your materials so they can be reused.

- [ ] **Software, notebooks, and containers**
- License your code to inform about how it may be (re)used. 



> **Report your research transparently**

- [ ] Report and publish your methods and interventions explicitly and transparently and fully to allow for replication.


---

## Based on the ID-Card document
 <!-- AbualhaijaEtAl2024 -->

**1. Research context and purpose**

• **Research problem and scope**
- [ ] Is the research problem or task clearly defined?
- [ ] **Is the type of task or operation performed by the artifact explicitly characterized?**
- Clarifies the kind of operation performed by the artifact, such as classification, prediction, simulation, extraction, visualization, transformation, or analysis.

- [ ] Is the role of the artifact in the study explicitly described?
- [ ] Is the application domain or context specified?
- [ ] Are the goals, assumptions, or intended use cases documented?

• **Research contribution**
- [ ] Is it clear how the artifact supports the paper’s claims or findings?
- [ ] Are the limitations or known constraints documented?
  
- [ ] **Are potential reuse or repurposing scenarios discussed?**
- Describes how the artifact may be reused, extended, adapted, or repurposed in future studies or practical applications.

**2. Inputs, outputs, and workflow**

• **Inputs**
- [ ] Are the expected inputs clearly described?
- [ ] Are input formats, structures, or schemas documented?
- [ ] Are preprocessing or transformation steps explained?

• **Outputs**
- [ ] Are the generated outputs clearly described?
- [ ] Are output formats and interpretations documented?
- [ ] Are example inputs and outputs provided?

- [ ] **Is the semantic meaning or interpretation of outputs explained?**
- Explains what the produced outputs represent and how they should be interpreted by users or researchers.

• **Workflow traceability**
- [ ] Is the workflow connecting inputs, processing steps, and outputs understandable?
- [ ] Are intermediate artifacts or processing stages documented?

- [ ] **Are manual and automated steps in the workflow clearly distinguished?**
- Indicates which parts of the workflow depend on human intervention and which are fully automated, improving transparency and reproducibility.


**3. Data description and provenance**

• **Dataset characterization**
- [ ] Is the dataset size or scale reported?
- [ ] Are the data sources identified?
- [ ] Is the number of different sources from which the data originates reported?
- [ ] Are collection procedures described?
- [ ] Are the data domains or contexts documented?
- [ ] Are languages, formats, or modalities specified?
- [ ] Is the time period or interval when the data was produced specified?

• **Data provenance and licensing**
- [ ] Is the provenance of the data documented?
- [ ] Are licensing or usage restrictions specified?
- [ ] Is the dataset publicly available?
- [ ] If not publicly available, is the restriction justified?

• **Data quality and structure**
- [ ] Is the level of data structure or rigor documented?
- [ ] Are metadata or data dictionaries provided?

- [ ] **Is the abstraction level of the data documented (e.g., user-level, system-level, code-level)?**
- Specifies the level at which the data represents the phenomenon being studied, such as user-level, file-level, function-level, sentence-level, or system-level data.



**4. Annotation, curation, and preprocessing**

• **Annotation process**
- [ ] Is the annotation or labeling process described?
- [ ] Are annotator roles and expertise documented?
- [ ] Are annotation guidelines available?
- [ ] Is it specified whether entries were annotated by a single person or multiple annotators (with or without quality control)?
- [ ] Is the method for establishing the annotation scheme documented (e.g., oral agreement, written guidelines with examples)?

- [ ] **Is the context available to annotators/coders during labeling or classification documented?**
- Explains whether annotators had accessed only to isolated items or to additional surrounding context that could influence interpretation and labeling decisions.

- [ ] **Are potential quality threats during manual annotation or coding discussed (e.g., fatigue, drift, context loss)?**
- Documents factors that may affect annotation quality, such as annotator fatigue, inconsistent interpretation, context loss, or changes in coding behavior over time.

- [ ] Are the specific methods for resolving annotation conflicts (e.g., majority voting, expert resolution, discussion) clearly identified?

**Quality assurance**
- [ ] **Are agreement or consistency measures reported?**
- Indicates whether the consistency between annotators or coders was evaluated using measures such as Cohen’s kappa, Fleiss’ kappa, or percentage agreement.

- [ ] Are conflict resolution procedures documented?
- [ ] Are known sources of bias or subjectivity discussed?

**Preprocessing and transformation**
- [ ] Are preprocessing steps documented?
- [ ] Are cleaning, filtering, or transformation procedures reproducible?

**5. Implementation and infrastructure**

• **Software and tooling**
- [ ] Is the implementation publicly available?
- [ ] Are scripts, pipelines, or executables included?
- [ ] Are algorithms or major technical components described?
- [ ] Is the type of proposed solution explicitly described (e.g., script, library, API, standalone tool, plugin, model, framework)?
- [ ] Are the main algorithms, models, or computational techniques identified?
- [ ] If no executable tool is provided, is the absence of an implementation clearly justified?


• **Dependencies and environments**
- [ ] Are software dependencies documented?
- [ ] Are versions explicitly specified?
- [ ] Are operating system or platform requirements documented?
- [ ] Are hardware requirements specified when relevant?

- [ ] **Are dependency types documented (e.g., libraries, external services, hardware accelerators, operating system components)?**
- Identifies the kinds of external resources required by the artifact, including libraries, operating systems, cloud services, databases, GPUs, or APIs.


• **Packaging and distribution**
- [ ] Is the artifact distributed in a reusable format?
- [ ] Are containers, virtual environments, or reproducible environments provided?
- [ ] Is versioning information available?
- [ ] Is it clear which components were released (e.g., source code, datasets, models, scripts, containers, binaries, documentation)?
- [ ] Is the release/distribution format documented (e.g., repository, package manager, container image, VM, executable archive)?

- [ ] **Are the specific actions required to run the tool identified (e.g., no installation, compile and run, or reproduction from paper explanation)?**
- Explains the exact steps needed to execute the artifact, such as installation, compilation, configuration, dataset preparation, or command execution.



**Licensing**
- [ ] Is a clear license provided?
- [ ] Are third-party dependency licenses compatible?

**6. Documentation and usability**

• **Core documentation**
- [ ] Is there a clear README?
- [ ] Is the artifact structure explained?
- [ ] Are execution instructions provided?
- [ ] Are usage examples included?
- [ ] Are the types of provided documentation identified (e.g., README, API documentation, tutorials, notebooks, screencasts)?

• **Reusability support**
- [ ] Is troubleshooting guidance provided?
- [ ] Are expected execution behaviors documented?
- [ ] Are common failure scenarios explained?

• **User support**
- [ ] Are contact or support channels provided?
- [ ] Is citation information available?

**7. Reproduction and execution**

• **Installation and execution**
- [ ] Can the artifact be installed and executed from scratch?
- [ ] Are installation steps reproducible?
- [ ] Are execution commands clearly documented?

• **Reproducing results**
- [ ] Are steps to reproduce the paper’s results documented?
- [ ] Are scripts mapped to figures, tables, or results?
- [ ] Are expected outputs described?

• **Runtime considerations**
- [ ] Is the expected execution time reported?
- [ ] Are minimum working examples provided when execution is expensive?
- [ ] Are intermediate outputs available to facilitate reproduction?

• **8. Evaluation and validation**

• **Evaluation procedure**
- [ ] Is the validation methodology documented?
- [ ] Are evaluation metrics explained?

- [ ] **Are baselines or comparison methods sufficiently documented to support interpretation or replication?**
- Ensures that comparison methods or baseline approaches are described in enough detail for others to understand or reproduce the evaluation.

- [ ] Is the specific validation procedure identified (e.g., train-test split, cross-validation, or use of the entire dataset)?
  
- [ ] **Are the evaluation methods appropriate for the type of task performed by the artifact?**
- Verifies whether the chosen evaluation procedures and metrics are suitable for the artifact’s intended purpose and outputs.

• **Result interpretation**
- [ ] Are deviations from published results documented?
- [ ] Are threats to validity or limitations discussed?
- [ ] Is the relationship between the artifact and reported results traceable?
- [ ] Is it clear which datasets, inputs, or intermediate artifacts contribute to each reported result?
- Helps readers understand exactly which data, scripts, models, or intermediate artifacts were used to generate each reported result.

- [ ] **Is the relationship between inputs and produced outputs clearly characterized?**
- Explains how inputs are transformed into outputs, including whether one input generates one, multiple, or aggregated outputs.

- [ ] **Is the level of analysis or processing granularity documented?**
- Specifies the unit of analysis or processing adopted by the artifact, such as document-level, sentence-level, participant-level, file-level, or commit-level analysis.



**9. Preservation and accessibility**

• **Archival and persistence**
- [ ] Is the artifact archived in a persistent repository?
- [ ] Does the artifact have a DOI or persistent identifier?
- [ ] Is long-term accessibility considered?

• **Public availability**
- [ ] Can the artifact be accessed without registration?
- [ ] Are access restrictions clearly explained?

• **Sustainability**
- [ ] Are maintenance or update expectations documented?
- [ ] Are stable releases or archived versions identified?



---

## Based on BeyerWinter2025
<!-- == BeyerWinter2025 -->

• **Pre-assessment (“Kick the tires”):**

- [ ] Can the digital object be retrieved without revealing your identity?

- [ ] Is it packaged in an open format that you can work with?

- [ ] If the provided digital object is a compressed archive, can it be decompressed without errors?

- [ ] Is the artifact operable on your computing architecture?

- [ ] Are all documents required in the call for artifacts included in the submission?

- [ ] Do the documents contain the information asked for in the call for artifacts?
  

• **Full Review (Badging Decisions):**

**Available:**

- [ ] Is the artifact published on a long-term archival platform with declared retention policy (≥ 10 years)?

- [ ] Is a DOI provided? (A DOI implies long-term availability.)

- [ ] If the artifact is on Zenodo: Is it linked to via a version-specific DOI (as opposed to a concept DOI, which is always redirected to the latest version and should be avoided to support reproducibility)?

- [ ] Is the artifact linked to from the paper using the DOI link (or other long-term archive link)?

- [ ] Is a license specified for the artifact?


**Functional:**

- [ ] Is the artifact exercisable?

- [ ] Have the documentation guidelines in the call for artifacts been followed?

- [ ] Is the artifact sufficiently documented to be used for reproducing results from the paper?

- [ ] Does the artifact contain all relevant parts for reproducing results from the paper (are input data, plotting scripts, etc. included; are external dependencies expected to be permanently available)?

- [ ] Are results you have obtained using the artifact consistent with what is written in the paper?
  
**Reusable:**

- [ ] Is the artifact documentation sufficiently comprehensive and well-structured, such that the artifact can be used in other settings than reproducing the exact study presented in the paper?

- [ ] Are common standards for code, mechanized proofs, and data formats followed, so that it can be adapted with reasonable effort?


---


## Perform a final pre-release checklist

<!-- Survey2026 -->
Before publication:
1. Translate materials to English.
2. Perform final proofread and sanity check.
   - Review for typos, grammatical errors, and logical flow.
3. Remove or anonymize sensitive data.
   - Scrub internal comments, personal data, test credentials, and proprietary information.
4. Verify links and references.
   - Ensure all hyperlinks, cross-references, and embedded assets work and are accessible to the intended audience.
5. Apply consistent formatting.
   - Ensure visual consistency (fonts, spacing, headings, code indentation).
6. Define clear context and purpose.
   - Add a succinct summary, README, or "About This Document" section.
   - Be transparent in all levels and details overall.
   - Avoid all text that is not relevant to explain the artifact structure (i.e., the design decisions should go into the paper, while the manual presents where the ideas are implemented, do not justify why)
   - Deliberately include details that may appear trivial to use the artifacts.
7. Choose the right format and platform.
   - For compressed archive format use a widely available such as ZIP (.zip), tar and gzip (.tgz), or tar and bzip2 (.tbz2).
   - For documents use open formats such as .txt, .html, and .pdf.
   - For figures use widely accessible format such as .png.
8. Set appropriate permissions and security.
   - Configure share settings (view/edit) on platforms like Google Drive, GitHub, or SharePoint.
9. Making sure ALL details are available to enable replication and reproduction. 

---

## HOWTO for AEC Submitters
 <!-- == BarowyEtAl2023 -->

### How to Build a Good Software Artifact

- Provide documentation with your artifact.  We recommend that you prepare a Getting Started Guide.  It should explain:
   - how to download your artifact
   - how to install your artifact
   - how to run your artifact
   - how to compare your artifact’s outputs to outputs described in your paper.
- Explicitly enumerate your claims in both your paper and in your artifact’s documentation.
- Provide a VM if possible, and when appropriate.  VMs aid reproducibility because they help control for nuisance factors that are not central to an author’s claims, significantly facilitating the review process.  Nonetheless, reviewers may need to accept performance tradeoffs for VMs (e.g., because of the absence of special hardware).  These tradeoffs are acceptable as long as authors explain to reviewers how and why they should adjust their expectations.
- Provide step-by-step instructions, but make it easy for reviewers to supply their own inputs to your artifact.  When reviewers can “play” with your artifact, it gives them confidence that your ideas were implemented robustly.

### Source Code

- If you are not bound by a nondisclosure agreement, make every effort to supply reviewers with source code.  Good reviewers may read and modify your source code to learn the true capabilities of your artifact.
- Document your code.  You should sufficiently explain what is going on so that people who want to build on your work can do so.
- If you discuss a new algorithm or unique implementation approach in your paper, have a reference to its implementation in the source code.
- If you are pointing to a remote repository, make sure to create a stable AEC branch. If there are major changes between AEC submission and the decision deadline, reviewers may end up looking at code that breaks the build. We understand that bugs happen, and pushing bug fixes to your AEC branch is fine. However, if your source code and/or analyses are significantly different from paper, make sure you document those differences so reviewers know what to expect.

### Virtual Machines

- Use a familiar window manager, if you need one at all. Remember that not all reviewers will have a middle mouse button.
- Ship your VM in a portable format (OVA or OVF) so reviewers can use whatever virtualization software they already have installed.
- Delete snapshots from your VM, unless these are an important part of the artifact evaluation.
- Document the folder structure of the VM. e.g., point out where the artifact’s source code is, benchmark source code is, input data is, expected output data is, etc. A good strategy is to have a terminal open at startup, in the appropriate directory.

### Automated Benchmarks

- If your benchmarks take more than a trivial amount of time to run, please inform reviewers how long they should take with the hardware you used. Provide a shorter evaluation script that reviewers can use to make sure everything is working.
- Make it clear what the specifications of the hardware were that you used, and whether these hardware resources are adequately simulated in a virtual machine environment.
  - If performance claims cannot be reproduced in a virtual environment, consider adding instructions describing how to run the benchmarks on bare metal.
- You should make it easy to reproduce all of the data for your paper, ideally with a single batch script or mouse click.
- If your paper includes figures such as tables or charts, you should make it easy to reproduce those figures without having to manually create charts in Excel. There are many packages available for producing graphs programmatically:
  - R has built-in graphing functionality, but the ggplot package provides much more flexible graphing functionality.
  - Python has a compatible ggplot package, or you can use matplotlib directly.
  - JavaScript has many graphing libraries, including D3 and Google Charts.

---

## README template
 <!-- Wendler2024  -->

When creating a reproduction artifact, follow this checklist:

- **Data**
  - Added all raw results
  - Added single command for reproducing all tables and plots presented in the paper, from the existing raw results
  - Added single command for each table and plot presented in the paper to reproduce only that element, from the existing raw results

- **Tool Setup**
  - All dependencies included in artifact
  - No compilation necessary
  - No manual installation necessary
  - Artifact works with systems other than Ubuntu
  - Diagnosis command exists that allows user to check if the tool is runnable - Initial example, tests, etc.
  - README contains copy of expected tool output (verbatim!)
  - VM: US Keymap and English language!

- **Running the Tool**
  - Added single command for running an example
  - Added single command for running a small, expressive benchmark set
    - runtime below 24 hours in VM
  - Added single command for repeating all experiments
 
- **README for VM**
  - README next to the VM-file exists
    - States corresponding publication of artifact
    - States required VirtualBox version
    - States resource requirements of VM

- **README for tool**
  - README inside the VM exists
  - Link to README on Desktop (for finding it easily)
  - If dependencies must be installed, README contains exact versions required and the OS used.
  - README contains list of all tables, plots and claims made in the paper, and maps each to a single command to recreate that exact entity from the raw results
  - README contains instructions and the expected output for:
    - Setup on a bare system
    - Running the examples
    - Running the small, expressive benchmark
    - Running the full experiments

- **Final checks**
  - Disabled use of verifier-cloud for benchmark runs
  - All included repositories in correct revision/tag
  - Thorough cleanup of the VM:
    - Check cache directories such as ~/.cache or /var/cache whether they contain significant amounts of data.
    - Make sure unused sectors are zeroed and do not contain old data (fstrim should do this).
    - Removed personal data such as (bash) history in VM:
    - rm ~/.bash_history && history -c && exit and potentially other files depending on what was done
  - Archive tested by someone unfamiliar with the work:
    - VM import (make sure .ova is exported without network interface and shared folders)
    - Proofread
    - Full run (after VM reboot)

- **Publication of Artifact**
  - Zip everything in one zip archive, which has a README and LICENSE file at the top level
  - Dirk uploaded artifact to Zenodo
  - Checked checksum of artifact-file on Zenodo and local version
  - Supplementary webpage references artifact

---

## Badge checklist
<!-- Não sei ainda se vou usar, pois o conceito das badges dele tá enviesado https://sysartifacts.github.io/sosp2026/badges -->

**“Available” checklist**
- [ ] The artifact is available on a public archive with irrevocable versioning and long-term storage, such as Zenodo but not GitHub
- [ ] The artifact has a license that allows comparison and extension, such as the CC-BY or MIT licenses
- [ ] The artifact has a “read me” file referencing the paper

These criteria must be met at the time artifact evaluation finishes.

Authors only need to put the data in long-term storage once evaluators are otherwise satisfied. Development may take place on a platform like GitHub.

Promises of future availability are not acceptable, such as uploading the artifact to a private repository with the goal of “eventually” making it public.

**“Functional” checklist**
- [ ] The artifact has a “read me” file with:
  - [ ] A description of each artifact component and how it relates to the paper
  - [ ] A description of the exact environment the authors used, such as OS version and hardware
  - [ ] If the artifact includes code that deliberately performs malicious or destructive operations, appropriate warnings and context
- [ ] The artifact includes all code and data relevant to the paper, and only those
  - [ ] The artifact must not include obsolete or unrelated code nor data
  - [ ] If existing code or data has been modified, the artifact should clearly separate the modifications from the original
  - [ ] If the paper makes soundness claims, such as proofs, there should be simple scripts to verify these, such as listing proof assumptions
  - [ ] If the paper makes quantifiable claims, such as code size per module, there should be simple scripts to output these
- [ ] For data, modifications made to the raw data are documented
  - [ ] For instance, whether parts of the raw data were anonymized or discarded
- [ ] For executable artifacts, the “read me” file also contains documentation to:
  - [ ] Run and extend a “minimal working example”
  - [ ] Compile and execute the artifact, including pre-installation steps
  - [ ] Configure the artifact, such as selecting IP addresses or disks
  - [ ] Know the expected resource use per kind of experiment, such as “5 minutes, 10 GB of disk space”
  - [ ] Know what unusual behavior to expect, such as warning messages emitted by another system used as baseline for experiments
- [ ] For executable artifacts, the artifact includes a precise list of dependencies:
  - [ ] Whenever possible, it should be usable by a package manager
  - [ ] Exotic dependencies must have associated automation to download and build them
  - [ ] OS-level dependencies must involve a VM/container, accompanied by a script to generate the VM/container
  - [ ] Proprietary dependencies must have associated instructions to obtain them along with “mock” versions to demonstrate their use
- [ ] The artifact includes an example input and configuration for each kind of experiment in the paper
  - [ ] Authors are encouraged, but not required, to provide inputs, configurations, and outputs for all experiments described in the paper

Artifacts must be usable on other environments than the authors’, though software may require specific hardware such as one model of network card.

Manual work such as writing configuration files must be minimized. There must be no redundant manual steps such as writing the same configuration values in multiple places, as this inevitably leads to human error.

**“Reproduced” checklist:**
- [ ] The artifact includes a single script to run each experiment and output results, given the necessary input and configuration
  - [ ] The scripts must be documented, allowing researchers to ensure they correspond to the claims, merely producing the right output is not enough
  - [ ] The scripts must handle common edge cases in a reasonable fashion, such as forgetting arguments or running the same script twice
- [ ] The artifact includes a script to convert each experiment’s results into human-readable ones as close to the paper presentation as possible
  - [ ] For simple results presentation such as tables, this and the previous script can be merged into one
  - [ ] The artifact may contain separate installation steps for the dependencies of plotting scripts, subject to the same criteria

The expected workflow for an evaluator or a researcher looking to reuse the artifact is to install the artifact using a handful of commands, run experiments with one command each, and plot data as necessary.

In the absence of problems requiring debugging, active time must not exceed a few minutes.


## Checklist to Ensure Your Data Support the FAIR Principles
<!-- https://journalologytraining.ca/topic/checklist-to-ensure-your-data-support-the-fair-principles/ -->

### FAIR Checklist

**Dataset/Files**

- [ ] Your dataset should be open (if available).
- [ ] Your dataset should have a DOI.
- [ ] All files should be in open formats.
- [ ] Your data should be discoverable through an open search protocol (for example, via Google).

**Metadata**

- [ ] The metadata should include useful disciplinary notation and terminology.
- [ ] The metadata should include machine-readable standards where available (e.g. ORCIDs (for authors and/or data contributors)).
- [ ] Provide a citation format for the data.
- [ ] Indicate any terms of use clearly.
- [ ] The metadata exportable should be in a machine-readable structured text-based format (e.g., XML, JSON)​.


**Tips for Preparing Your Data for Sharing**

Preparing your data files:

- [ ] You should include raw or processed data or both, depending on what is most useful or common in a discipline.
- [ ] Your file formats should be common and open.
- [ ] Organize the files logically according to your project.

Documenting your data and files:

- [ ] Describe methods of data collection and file structures.
- [ ] Reference articles and include ORCIDs of all data contributors.

Depositing your data in a repository:  

- [ ] Zip up all files into one package or dataset.
- [ ] Select a well-known data repository and upload your data.
- [ ] Make sure the repository provides a DOI to access and re-use the data.
- [ ] Provide a license attribution for your data, so users can easily copy and attribute.

---

# Practical checklist: what should usually be included?

Before publication, verify whether your artifact package includes: <!-- Montgomery2024 -->  <!-- Survey2026 -->
- [ ] Protocols and study design artifacts
- [ ] Raw data
- [ ] Processed data
- [ ] Derived data
- [ ] Data collection scripts
- [ ] Data transformation scripts
- [ ] Analysis scripts
- [ ] Software tools
- [ ] Figures, tables, and extended findings
- [ ] Documentation and README
- [ ] Reproduction instructions
- [ ] Environment/configuration files
- [ ] Licensing information
- [ ] Links to the associated paper
- [ ] Notebooks, containers, software, and hardware



---

## FAIR Data Self-Assessment Tool

- https://ardc.edu.au/resource/fair-data-self-assessment-tool/

---

## Sources

This module builds on a shared set of references used throughout the GAPS material, including guidelines, standards, and research studies on Open Science and research artifacts.

To avoid redundancy and ensure consistency across modules, all references are centralized in the following document: [GAPS References](/references.md).

Contents in this module were adapted and synthesized from these sources.