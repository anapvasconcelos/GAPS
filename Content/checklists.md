<table style="width: 100%; border-collapse: collapse; margin: auto;">
  <tbody>
    <tr>
      <td style="border: 0px"> <a href="/supplementary-material/main.md"><nobr>Supplementary material</nobr></a> </td>
      <td style="width: 50%; border: 0px"> </td>
      <td style="border: 0px"> <a href="/SUMMARY.md"><nobr>GAPS Summary</nobr></a> </td>
      <td style="width: 50%; border: 0px"></td>
      <td style="border: 0px"> <a href="/glossary.md"><nobr>Glossary</nobr></a> </td>
    </tr>
  </tbody>
</table>

---

![GAPS logo](../GAPS-logo.png)

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

## FAIR Data Self-Assessment Tool

- https://ardc.edu.au/resource/fair-data-self-assessment-tool/

---

## Sources

This module builds on a shared set of references used throughout the GAPS material, including guidelines, standards, and research studies on Open Science and research artifacts.

To avoid redundancy and ensure consistency across modules, all references are centralized in the following document: [GAPS References](/references.md).

Contents in this module were adapted and synthesized from these sources.