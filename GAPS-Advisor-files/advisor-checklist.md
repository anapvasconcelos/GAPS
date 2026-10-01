# GAPS Advisor Checklist

Priority legend: **[E]** Essential · **[R]** Recommended · **[G]** Good practice

- **[E] - Essential:** Item considered fundamental for understanding, accessing, executing, reproducing, or appropriately using the artifact, when applicable to the artifact characteristics.

- **[R] - Recommended:** Item strongly recommended to support the artifact's understanding, execution, reproduction, evaluation, or reuse.

- **[G] - Good practice:** Item that further improve the artifact's quality, clarity, maintainability, transparency, or reuse, but are not generally necessary for its basic use or evaluation.

# 1. Planning the Research and the Artifact

## 1.1. Artifact-oriented planning

+ The research materials that may need to be preserved and shared have been identified. **[R]**
+ The project has been planned so that its relevant materials can be organized into a shareable artifact or replication package. **[R]**
+ Artifact preparation is treated as an ongoing activity rather than a final step before submission. **[R]**
+ Artifact organization and sharing plans have been discussed with collaborators. **[G]**

## 1.2. Organization and traceability

+ An organization for the research materials that can be maintained throughout the project has been established. **[R]**
+ A plan exists for keeping important decisions, procedures, and results traceable. **[R]**
+ A plan exists for preserving relevant versions and intermediate outputs. **[R]**
+ Conventions have been established to keep the artifact consistent with the terminology and structure of the research publication. **[G]**

## 1.3. Data and file formats

+ A plan exists for distinguishing and maintaining raw, processed, and derived data. **[E]**
+ Original data are preserved without direct modification. **[E]**
+ Appropriate file formats have been selected for the materials expected to be shared. **[R]**
+ Open, widely supported, and well-documented formats have been considered whenever suitable alternatives exist. **[R]**

## 1.4. Reproducibility and workflow

+ A plan exists for documenting and, where appropriate, automating the research workflow. **[R]**
+ The potential for regenerating data processing, analyses, figures, and tables has been considered. **[R]**
+ The environments, dependencies, or other conditions that may need to be preserved for reproduction have been identified. **[R]**
+ The artifact is planned to remain aligned with the study and its published results. **[R]**

## 1.5. Sharing constraints

+ Ethical, legal, institutional, consent, privacy, or licensing constraints that may affect artifact sharing have been identified. **[E]**
+ Alternative ways of providing transparency have been considered when some materials may not be publicly shareable. **[R]**
+ A plan exists for documenting restricted data or other non-shared components and, when possible, providing access under appropriate conditions. **[R]**
+ Anonymization requirements have been considered early enough to avoid making them a last-minute step. **[E]**

## 1.6. Reuse and long-term accessibility

+ The potential for the artifact to support reuse beyond the original study has been considered. **[R]**
+ Choices that facilitate reuse, such as modular organization, open licensing, and accessible data or software, have been considered where relevant. **[R]**
+ Potential dependencies on external datasets, APIs, repositories, or other resources that may become unavailable have been considered. **[R]**
+ A plan exists for keeping the artifact accessible independently of the continued availability of the paper or the researchers' development accounts. **[E]**

---

# 2. Developing and maintaining the artifact

## 2.1. Artifact organization

+ Research materials are organized according to the established project structure. **[R]**
+ Data, code, documentation, and other relevant materials are kept in their designated locations. **[R]**
+ The repository structure remains consistent as the project evolves. **[R]**
+ Naming conventions are consistent with the terminology used in the research and, when applicable, the publication. **[R]**
+ Essential research materials are distinguishable from temporary or auxiliary materials. **[R]**

## 2.2. Versioning and traceability

+ Relevant data, code, documentation, and other research materials are versioned as they evolve. **[R]**
+ Important intermediate versions and outputs are preserved. **[R]**
+ Original or intermediate materials that may be needed to understand or reproduce the research are not overwritten. **[E]**
+ Important research decisions and changes remain traceable. **[R]**
+ Sufficient version history is maintained to understand how the artifact evolved. **[R]**

## 2.3. Data management

+ Original data are kept separate from processed and derived data. **[E]**
+ Original data are not modified directly when generating processed or derived data. **[E]**
+ Scripts or other reproducible procedures are used to generate derived data when applicable. **[R]**
+ Data-processing procedures are kept together with the materials they produce. **[R]**
+ Relevant data collection, preprocessing, cleaning, inclusion, and exclusion procedures are documented as they occur. **[E]**
+ Data documentation is sufficiently detailed to support later interpretation and reuse. **[R]**

## 2.4. Documentation and decisions

+ Documentation is kept up to date as the artifact develops. **[R]**
+ Relevant decisions and procedures are recorded while they are still part of the research process. **[R]**
+ Non-obvious processing or analysis steps are documented. **[E]**
+ The relationship between research materials, procedures, and results remains traceable. **[R]**
+ Documentation is updated when the artifact's structure, terminology, or workflow changes. **[R]**

## 2.5. Reproducible workflows

+ Important undocumented manual procedures are replaced with scripted or otherwise reproducible procedures when appropriate. **[R]**
+ Repetitive research procedures are automated when appropriate. **[R]**
+ The generation of results, figures, or tables is automated when appropriate. **[R]**
+ Workflows and their outputs remain traceable. **[R]**
+ Unnecessary manual steps that would need to be reconstructed when preparing the artifact later are avoided. **[R]**

## 2.6. Environments and dependencies

+ The research environment and its relevant requirements are documented as they evolve. **[R]**
+ Relevant software and dependency versions are recorded. **[E]**
+ Important environment configurations remain reproducible. **[E]**
+ External datasets, APIs, repositories, or services on which the artifact depends are identified. **[R]**
+ Unnecessary dependencies on unstable external resources are avoided. **[R]**
+ Critical dependencies are preserved or archived when feasible. **[R]**

## 2.7. Privacy, ethics, and sharing constraints

+ Privacy, ethical, legal, institutional, and consent-related constraints are reassessed as the research develops. **[E]**
+ Anonymization is applied when required and treated as an iterative process rather than a final step. **[E]**
+ The effect of anonymization on the interpretability and analytical value of the data is considered. **[R]**
+ Components that may need to remain restricted or unavailable for sharing are identified and tracked. **[E]**
+ When full sharing is not possible, the documentation, metadata, and access conditions needed to maximize transparency are maintained. **[R]**

## 2.8. Reuse during development

+ Components are structured so they can be reused or adapted when appropriate. **[R]**
+ Modular organization is used where appropriate. **[R]**
+ Reusable source materials are kept available rather than only final outputs. **[R]**
+ The potential for datasets, code, or other components to support uses beyond the original study is considered. **[R]**
+ Design decisions that unnecessarily restrict future reuse or extension are avoided. **[G]**

---

# 3. Preparing the artifact for sharing

## 3.1. Artifact completeness and organization

+ All components necessary to understand, reproduce, or reuse the study are included, when applicable. **[E]**
+ The repository structure is clear and consistent. **[R]**
+ Essential components are distinguished from supplementary or optional components. **[R]**
+ Temporary, obsolete, or irrelevant files have been removed. **[R]**
+ Unused code, dependencies, test files, backups, and outdated versions have been removed. **[G]**
+ Intermediate or irrelevant results that are not part of the artifact have been removed. **[R]**
+ The artifact does not contain incomplete or placeholder components. **[E]**
+ The artifact is not unnecessarily dependent on the authors' personal files, accounts, or development environment. **[E]**

## 3.2. Artifact documentation

+ A clear summary of what the artifact contains and what it enables is provided. **[E]**
+ The repository structure and the purpose of its main components are documented. **[E]**
+ The technical background expected from users is identified. **[R]**
+ The operating system, hardware, software dependencies, and relevant versions are documented. **[E]**
+ Installation and preparation requirements are documented. **[E]**
+ Complete execution instructions are provided, when applicable. **[E]**
+ Relevant parameters and configurations are documented. **[E]**
+ Expected inputs, including required files, formats, and relevant input characteristics, are documented. **[E]**
+ Expected outputs and where they are generated are stated. **[E]**
+ Outputs required for the workflow are distinguished from reference or supplementary outputs, when relevant. **[R]**
+ Relevant human effort, execution time, and resource requirements are documented. **[R]**
+ Known errors, expected failures, and troubleshooting information are documented, including enough information to distinguish normal behavior from problems requiring intervention. **[R]**
+ The documentation is consistent with the final artifact. **[E]**
+ Additional requirements needed to use or execute the artifact, such as credentials, API keys, licenses, external resources, or specialized access, are documented when applicable. **[E]**
+ Potential risks, side effects, resource-intensive operations, external access requirements, irreversible actions, and other safety considerations are documented before execution, when applicable. **[E]**
+ Instructions for obtaining the artifact and, when applicable, accessing the specific version associated with the published study are available. **[E]**
+ A quick way to verify that the artifact has been correctly obtained, prepared, and installed is documented when a separate quick validation is useful. **[R]**
+ A reduced execution workflow is provided when the full reproduction requires substantial time or computational resources. **[G]**
+ The relationship between the reduced workflow and the full reproduction workflow is clearly documented. **[R]**
+ Relevant side effects and conditions indicating successful completion are documented for the execution steps, when applicable. **[E]**
+ Hardware architecture and other architecture-specific requirements, such as x86, ARM, or GPU dependencies, are documented when applicable. **[E]**
+ Execution steps are designed to be repeatable without causing unintended changes or inconsistent states, when applicable. **[R]**

## 3.3. Connection to the research and publication

+ The relationship between the artifact and the research study is clearly explained. **[E]**
+ The main components that support the study are identified. **[R]**
+ Relevant artifact outputs are mapped to the corresponding figures, tables, sections, or claims in the publication. **[E]**
+ Claims that are not supported by the artifact are identified. **[E]**
+ Unsupported claims or omitted components that are outside the artifact's scope are explained. **[E]**
+ Terminology, variable names, metrics, outputs, and experimental conditions are consistent with the publication. **[E]**
+ Relevant differences between the artifact and the published work are documented. **[R]**

## 3.4. Data and provenance

*When the artifact includes data:*

+ Sufficient information to understand the data's purpose, scope, and structure is provided. **[E]**
+ The size or composition of each dataset is documented when relevant. **[R]**
+ Data collection procedures are documented. **[E]**
+ Preprocessing and cleaning procedures are documented. **[E]**
+ Inclusion and exclusion criteria are documented. **[E]**
+ Relevant variables, fields, metrics, units, and representations are documented. **[R]**
+ Data provenance and relevant processing history are documented. **[R]**
+ Raw, processed, and derived data are clearly distinguished. **[E]**
+ The shared data representation is consistent with the publication. **[R]**

## 3.5. Privacy, ethics, and restricted components

+ Components that cannot be publicly shared are identified. **[E]**
+ The reason for each relevant restriction is clearly documented. **[E]**
+ Sensitive information has been removed or anonymized before sharing. **[E]**
+ Direct and indirect identifiers, including combinations of attributes that could enable re-identification, have been assessed when applicable. **[E]**
+ Credentials, personal information, confidential information, and proprietary material that should not be disclosed have been removed. **[E]**
+ The impact of anonymization on data interpretation is documented, when applicable. **[R]**
+ When full sharing is not possible, appropriate alternatives such as metadata, protocols, coding schemes, anonymized or aggregated data, or intermediate analysis materials are provided. **[R]**
+ When controlled access is possible, the access conditions and how access can be requested are documented. **[E]**

## 3.6. File formats and packaging

+ Shared files use appropriate, open, widely supported, and well-documented formats whenever suitable. **[R]**
+ Machine-readable representations are provided where they are relevant to automated or reproducible workflows. **[R]**
+ The artifact does not rely on proprietary or tool-specific formats when suitable alternatives are available. **[R]**
+ Compressed archives contain the complete intended artifact. **[E]**
+ The package structure is understandable without requiring access to the authors' development environment. **[R]**

## 3.7. Final documentation quality

+ The artifact documentation has been proofread. **[G]**
+ Spelling, grammatical, formatting, and consistency problems have been corrected. **[G]**
+ Hyperlinks, cross-references, and embedded resources work. **[R]**
+ The documentation does not assume knowledge that external users are unlikely to have. **[R]**
+ Operational details that may seem obvious to the authors are documented when necessary for use. **[R]**
+ Complementary documentation is included when it meaningfully improves understanding or use, such as code comments, notebooks, diagrams, or demonstration materials. **[G]**

## 3.8. Final disclosure and scope information

+ The artifact's contents are clearly stated. **[E]**
+ What the artifact does not include is clearly stated, when relevant. **[R]**
+ Relevant limitations and omissions are explained. **[R]**
+ Contextual factors that may affect reproduction or interpretation are documented. **[R]**
+ Expected variability in results is documented when exact reproduction is not expected. **[R]**
+ Claims about reproducibility, applicability, automation, scalability, or platform support do not exceed what the artifact actually supports. **[E]**
+ A disclosure statement is included in the README when relevant information could affect interpretation, evaluation, or transparency, including conflicts of interest, funding, ethical considerations, limitations, and material inclusions or exclusions. **[G]**

## 3.9. Reusability
+ Reusable components are identified, when applicable. **[R]**
+ The adaptations required to reuse the artifact are documented, when applicable. **[R]**
+ Dependencies and constraints affecting reuse are documented. **[R]**
+ Limitations affecting adaptation, extension, or use in contexts different from the original study are documented. **[R]**
+ Relevant extension scenarios are documented, when applicable. **[G]**


## 3.10. Final sharing readiness

+ All information necessary for replication or reproduction is available, when applicable. **[E]**
+ Access permissions are configured appropriately. **[E]**
+ The artifact can be accessed independently of the authors' personal development environment. **[E]**
+ No sensitive information remains unintentionally exposed. **[E]**
+ The artifact is ready to be subjected to the validation process. **[R]**

---

# 4. Validating the artifact before publication

## 4.1. Independent and clean-environment validation

+ The artifact has been tested in a clean environment rather than only in the original development environment. **[E]**
+ When possible, the validation has been performed by someone who was not directly involved in developing the artifact. **[R]**
+ The artifact can be obtained and set up within a reasonable time frame. **[R]**
+ The installation and preparation procedures work as documented. **[E]**
+ The execution workflow works as documented. **[E]**
+ The artifact does not depend on undocumented local configurations or files. **[E]**
+ The environments in which the artifact has been tested are documented. **[R]**
+ Untested platforms or configurations are not presented as supported. **[E]**

## 4.2. File integrity and completeness

+ All required files are present. **[E]**
+ Downloaded or packaged files are intact. **[E]**
+ Compressed packages can be unpacked and used successfully. **[E]**
+ Important files or packages have been checked for integrity when appropriate. **[R]**
+ Virtual machines, containers, or other packaged environments start and operate as expected, when applicable. **[E]**
+ The artifact does not crash during basic execution. **[E]**

## 4.3. Execution and expected outputs

+ The documented workflow has been executed from beginning to end, when feasible. **[E]**
+ Each major execution step completes as expected. **[E]**
+ Expected output files are produced. **[E]**
+ Outputs are stored in the documented locations. **[E]**
+ Outputs are readable and interpretable. **[E]**
+ Generated outputs are consistent with the documented expected outputs. **[E]**
+ The execution time and resource requirements are consistent with the documentation. **[R]**

## 4.4. Reproduction of reported results

+ The results reported in the publication have been reproduced, when feasible. **[E]**
+ The results corresponding to the relevant figures, tables, and claims have been verified. **[E]**
+ The experimental conditions used during validation match those documented for the study. **[E]**
+ Relevant parameters, configurations, software versions, hardware conditions, and random seeds have been verified. **[E]**
+ The artifact provides sufficient information to understand any differences between reproduced and published results. **[E]**

## 4.5. Result variability and deviations

+ The artifact's results have been characterized as deterministic or variable. **[G]**
+ When results are variable, the relevant sources and expected magnitude of variation are documented. **[R]**
+ When applicable, the number of executions, warm-up procedures, aggregation methods, and variability measures have been verified. **[R]**
+ The acceptable range of variation has been defined or verified. **[R]**
+ Reproduced results are compared against the expected range rather than requiring exact numerical equality when variability is inherent. **[R]**
+ Relevant deviations from the results reported in the paper are identified and documented. **[R]**
+ The reasons for deviations considered acceptable or unavoidable are explained. **[R]**

## 4.6. Artifact-paper consistency

+ Artifact terminology is consistent with the publication. **[E]**
+ Variable names, metrics, datasets, configurations, and outputs correspond to those described in the paper. **[E]**
+ The experimental setup represented in the artifact matches the publication. **[E]**
+ Outputs can be mapped to the relevant figures, tables, and claims. **[E]**
+ Differences between the artifact and the paper are explicitly documented. **[R]**
+ Claims about reproducibility, applicability, automation, scalability, or platform support do not exceed what was actually evaluated. **[E]**

## 4.7. Access, links, and permissions

+ All artifact links resolve correctly. **[E]**
+ Hyperlinks, cross-references, and embedded resources work. **[E]**
+ The configured permissions allow the intended users to access the artifact. **[E]**
+ Restricted components follow their documented access conditions. **[E]**
+ All publicly shared components can be obtained without requiring undocumented author intervention. **[E]**

## 4.8. Final safety and disclosure check

+ No credentials, personal data, confidential information, or proprietary material are unintentionally exposed. **[E]**
+ Restricted or non-shared components are explicitly identified. **[E]**
+ The reasons for relevant exclusions are documented. **[R]**
+ Appropriate alternatives are provided when restricted components are essential to understanding or evaluating the study. **[R]**
+ Relevant limitations, ethical considerations, and constraints are disclosed. **[R]**

## 4.9. Final validation decision

+ All identified problems have been resolved or explicitly documented. **[E]**
+ The artifact is complete enough to support its stated scope. **[E]**
+ The documented instructions correspond to the artifact version being released. **[E]**
+ The artifact is ready for publication or submission. **[E]**

---

# 5. Submitting and publishing the artifact

## 5.1. Artifact identification
+ The artifact has a clear and unambiguous name. **[E]**
+ The artifact is explicitly associated with the corresponding publication or research study. **[E]**
+ The publication is identified with its persistent identifier (PID), when available. **[R]**
+ The preprint or accepted version of the paper is identified or made accessible, when applicable. **[R]**
+ The artifact has a persistent identifier (PID). **[E]**
+ The study goal supported by the artifact is clearly identified. **[E]**
+ The artifact version used to produce the reported results is clearly identified. **[E]**

## 5.2. Repository and preservation

+ The selected repository is appropriate for the artifact type and its preservation needs. **[R]**
+ The repository provides persistent identification for the published artifact. **[E]**
+ The repository provides appropriate versioning and preservation mechanisms. **[E]**
+ Any additional distribution platforms used during development or collaboration are complemented by an archival repository when needed. **[E]**
+ The selected repository can accommodate the artifact's storage and format requirements. **[R]**

## 5.3. Artifact version

+ The version being published is the version associated with the reported research results. **[E]**
+ The published version is clearly identified. **[E]**
+ The version has an explicit version number, tag, or equivalent identifier. **[R]**
+ The published version is treated as immutable once associated with the publication. **[E]**
+ If the artifact has multiple versions, the relationship between the published version and other versions is clear. **[R]**

## 5.4. Persistent identifier

+ A persistent identifier (PID) has been assigned to the published artifact. **[E]**
+ The PID identifies the appropriate artifact version for the publication. **[E]**
+ The version-specific PID is available for citation in the paper. **[E]**
+ The relationship between version-specific and version-agnostic identifiers is understood, when both are provided by the repository. **[R]**

## 5.5. Licensing

+ A license has been specified for the artifact. **[E]**
+ The license is appropriate for the artifact and its components. **[E]**
+ Software and non-software components have appropriate licensing information. **[E]**
+ License compatibility and applicable constraints have been checked. **[E]**
+ The license is clearly associated with the component(s) to which it applies. **[R]**
+ The right to redistribute or license the artifact and its components has been verified, including applicable institutional, funder, employer, or third-party restrictions. **[E]**

## 5.6. Authorship and citation

+ Author and contributor information is correct. **[E]**
+ The artifact provides the information needed for citation. **[E]**
+ Citation metadata identifies the published artifact and its version. **[E]**
+ A machine-readable citation file is provided when applicable. **[R]**
+ The artifact information provided in the paper is consistent with the published artifact and its version. **[E]**
+ The artifact citation and the paper's artifact information are consistent. **[E]**

## 5.7. Access and publication metadata

+ Access conditions are correctly configured. **[E]**
+ Components subject to restricted access have their access conditions documented. **[E]**
+ Metadata accurately describes the artifact and its contents. **[R]**
+ The published record clearly identifies what is included in the artifact. **[R]**
+ Non-shared or externally hosted components are identified where relevant. **[R]**
+ External resources required by the artifact are documented with sufficient information to identify them. **[R]**

## 5.8. Data Availability Statement (DAS)

+ The paper includes a Data Availability Statement. **[E]**
+ The DAS identifies the datasets, scripts, and other materials that support the reported results. **[E]**
+ The DAS identifies where the supporting materials are stored. **[E]**
+ The DAS provides the persistent identifier or persistent URL of the relevant materials. **[E]**
+ The DAS explains how the materials can be accessed. **[E]**
+ The DAS describes any restrictions on access or sharing. **[E]**
+ The DAS provides concrete access instructions when the materials are not openly accessible. **[R]**
+ The DAS is consistent with the artifact's actual contents, location, version, and access conditions. **[E]**

## 5.9. Final publication check

+ The deposited artifact corresponds to the version that was validated in section 4. **[E]**
+ The repository record and the artifact itself contain consistent information. **[E]**
+ The published artifact is accessible through its persistent identifier. **[E]**
+ The persistent identifier and repository link are ready to be included or updated in the paper. **[R]**
+ The published version has not been modified after publication. **[E]**

---

# 6. Maintaining the artifact after publication

## 6.1. Versioning and preservation

+ New releases are clearly versioned. **[R]**
+ The version associated with the publication remains preserved and immutable. **[E]**
+ New versions are released rather than modifying a previously published version. **[E]**
+ Version-specific persistent identifiers remain associated with the corresponding versions. **[E]**
+ The relationship between different artifact versions is clear. **[R]**
+ Changes that may affect execution, results, compatibility, structure, or use are recorded. **[R]**

## 6.2. Artifact decay and long-term usability

+ Dependencies are monitored for changes, deprecation, or incompatibility. **[R]**
+ External datasets, APIs, repositories, and other required resources are monitored for availability. **[R]**
+ Environment assumptions that may affect usability are reviewed when relevant. **[R]**
+ File formats and other preservation-relevant components are monitored for obsolescence. **[R]**
+ Factors that may affect the artifact's long-term usability are documented. **[R]**

## 6.3. Issues and maintenance

+ Reported issues are monitored and addressed when feasible. **[R]**
+ Known issues and expected failures are documented. **[R]**
+ Corrections and updates are released through new versions rather than silently modifying published versions. **[E]**
+ Significant maintenance changes are recorded in the changelog. **[G]**
+ Maintenance status remains clear, including whether further updates are planned or the artifact is considered a final archived release. **[R]**

## 6.4. Documentation and metadata

+ The README remains accurate after updates. **[E]**
+ Execution instructions are updated when commands or dependencies change. **[E]**
+ System requirements are updated when environment assumptions change. **[R]**
+ Links and references are periodically checked. **[R]**
+ Citation metadata remains current. **[R]**
+ Contact information remains valid or an alternative persistent contact is provided. **[G]**
+ A changelog records the evolution of the artifact. **[G]**
+ A durable channel for reporting unresolved problems, requesting clarification, or obtaining assistance is provided. **[G]**
+ The information users should provide when reporting problems is documented. **[G]**

## 6.5. Continued accessibility

+ The artifact remains available through its archival repository. **[E]**
+ Persistent identifiers continue to resolve to the intended artifact records. **[E]**
+ Access conditions remain correctly configured. **[E]**
+ External resources required for use remain documented. **[R]**
+ The artifact remains usable without depending on the authors' personal development environment or accounts. **[E]**

## 6.6. Maintenance and release consistency

+ Documentation corresponds to the currently released version. **[E]**
+ Changes that affect reproducibility or reuse are explicitly documented. **[R]**
+ Updated dependencies and environments are reflected in the artifact documentation. **[E]**
+ New releases do not alter the contents of previously published versions. **[E]**
+ The release history provides sufficient information to understand how the artifact has evolved. **[R]**
