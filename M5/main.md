<table style="width: 100%; border-collapse: collapse; margin: auto;">
  <tbody>
    <tr>
      <td style="border: 0px"> <a href="/M4/main.md"><nobr><- Previous module</nobr></a> </td>
      <td style="width: 50%; border: 0px"> </td>
      <td style="border: 0px"> <a href="/SUMMARY.md"><nobr>GAPS Summary</nobr></a> </td>
      <td style="width: 50%; border: 0px"></td>
      <td style="border: 0px"> <a href="/M6/main.md"><nobr>Next module -></nobr></a> </td>
    </tr>
  </tbody>
</table>

<!--
[README](/README.md) > [GAPS](../SUMMARY.md) > Module 5 - Reproducibility and transparency-->

---

![GAPS logo](../GAPS-logo.png)


# Module 5 - Reproducibility and transparency


## How to ensure verifiability



### Validating artifacts before release
<!-- Survey2026 -->

Before sharing an artifact, it is essential to verify that it can be executed and reproduced by others under realistic conditions. Validation should not be limited to confirming that the artifact works in the original development environment, but should simulate how external users (e.g., reviewers or other researchers) will interact with it.

A fundamental step is to perform full reruns of the artifact to ensure that all results can be reproduced from scratch. This includes executing the entire workflow, from raw inputs to final outputs, without manual intervention. In addition, a manual reproducibility check should be conducted by carefully following the provided documentation to confirm that all instructions are complete, accurate, and sufficient.

Artifacts should be tested in clean environments to ensure that no hidden dependencies or undocumented configuration steps are required. Running the artifact on a clean machine, where no prior setup exists, helps reveal implicit assumptions in the setup process. Ideally, the artifact should also be tested on multiple machines and operating systems to identify platform-specific issues.

Validation should also simulate the perspective of a new user. Researchers should follow their own documentation exactly as written, without relying on prior knowledge. Alternatively, colleagues, students, or collaborators who were not directly involved in the artifact preparation should be asked to execute the artifact and provide feedback. This external validation helps identify unclear instructions, missing steps, and usability issues. The process can be repeated iteratively until no major issues remain.

To further strengthen reliability, automated testing practices can be incorporated. Unit tests, automated tests, and sanity-check scripts can help verify that individual components behave as expected and that the overall workflow produces consistent outputs. These checks are particularly useful for detecting regressions or unintended changes during development.

Care should also be taken to preserve the integrity of archived results. During validation, code should be executed on test inputs when possible, avoiding modifications to the final archived outputs included in the artifact.

Finally, using virtual machines or containerized environments during testing can help approximate the conditions under which users will execute the artifact, reducing the risk of environment-related failures and improving reproducibility.



## Version control practices
<!-- Survey2026 -->

Version control systems provide a structured way to manage changes in research artifacts over time. Instead of manually creating multiple copies of files, these systems store snapshots of a project in a repository, allowing researchers to track what was changed, when, and by whom. This makes it easier to collaborate, maintain consistency, and recover previous versions when needed. <!-- WilsonEtAl2017 -->

In practice, researchers work on local copies of their files and record changes in the repository whenever they want to create a permanent version or share progress with others. When multiple contributors edit the same files, the system helps detect overlapping changes and requires conflicts to be resolved before integrating them. This ensures that contributions are coordinated and that no work is accidentally overwritten. Repositories can also be shared and synchronized across collaborators, supporting distributed collaboration and reducing the risk of data loss. <!-- WilsonEtAl2017 -->

Compared to manual approaches, version control systems offer several advantages. They automatically record the history of changes without requiring users to manage file naming conventions or maintain separate logs. They also store only the differences between versions rather than full copies, making the process more efficient. Importantly, they provide an accurate record of what actually changed, which is essential for debugging, validation, and reproducibility. <!-- WilsonEtAl2017 -->

However, version control is not equally effective for all types of files. It works best with plain text files, such as source code, where differences between versions can be easily identified. For binary files (e.g., PDFs or Word documents), changes cannot be inspected in detail, limiting the usefulness of version tracking. Similarly, large files can be problematic, as most systems are not designed to handle them efficiently. <!-- WilsonEtAl2017 -->

In addition, not all research materials need to be versioned. Raw data, which should remain unchanged, typically do not require version control. Intermediate data and results can also be excluded if they can be regenerated from the original data and scripts. Nonetheless, small datasets and results may still be versioned when this supports collaboration and comparison across versions. <!-- WilsonEtAl2017 - --> <!-- Survey2026 -->

In practice, version control systems (such as Git) are commonly used to organize and manage research artifacts and facilitate sharing. When appropriate, code and data can be maintained under separate version control or distribution strategies, depending on their characteristics and usage. Ensuring that all collaborators have access to a shared repository further supports coordination and transparency throughout the project. <!-- Survey2026 --> <!-- WilsonEtAl2017 - -->





## Managing dependencies and isolated environments

When developing software as part of a research artifact, it is important to adopt practices that support portability and reuse. Using portable programming languages can facilitate execution across different environments. Scriptable environments (e.g., R or Python) are preferable, as they allow workflows to be automated and version controlled, avoiding reliance on manual interactions. Whenever possible, software should be structured in a way that enables reuse, for example by organizing it as a library or modular component. <!-- Survey2026 -->


## Managing dependencies and isolated environments
<!-- Survey2026 -->

Preparing a research artifact requires careful management of its execution environment to ensure that it can be reliably built and executed across different systems. This includes controlling dependencies, defining reproducible environments, and minimizing external constraints that may hinder reuse.

A key aspect of this process is dependency control. All required dependencies should be explicitly specified and documented, preferably with pinned versions to ensure consistent behavior over time. This can be achieved using lock files or dependency management tools, which record the exact versions of libraries and packages used. Incomplete or implicit dependency specifications should be avoided, as they may lead to failures when the artifact is executed in a different environment. Additionally, tools that help maintain dependencies over time (e.g., automated update tools) can support long-term sustainability, provided that updates are carefully managed.

Another important aspect is the definition of the execution environment. Artifacts should be prepared in a way that encapsulates their dependencies and configuration. This can be achieved by packaging the environment together with the source code, for example using container-based or virtualized solutions. Providing fully specified environments helps ensure that the artifact behaves consistently regardless of the underlying system. When possible, these environments should be complete and self-contained, avoiding the need for additional manual configuration steps.

When preparing such environments, it is also important to consider compatibility across different platforms and hardware architectures. Ensuring that the artifact can be executed in commonly used environments reduces the barrier for reuse and evaluation.

External dependencies should be carefully managed and minimized whenever possible. Relying on complex, proprietary, or unstable third-party components can limit the accessibility and longevity of the artifact. Whenever feasible, open-source tools should be preferred. If proprietary dependencies are unavoidable, they should be clearly documented, including instructions on how they can be obtained and used. Researchers should also be aware that some dependencies may become unavailable over time, which can compromise reproducibility.

Finally, artifacts should be designed to be as self-contained as possible. Minimizing reliance on external services, undocumented configurations, or transient resources helps ensure that the artifact remains usable and reproducible in the long term.


## *Optional*: containerization for reproducibility

<!-- MendezEtAl2020 -->
To keep the working environment stable in terms of software versions, you can use a virtual machine or a container (Docker, Singularity, etc.).



## Sharing scripts, pipelines, and parameters

To support reproducibility, research software and executable artifacts should be designed to run in a consistent and automated way. Scriptable environments (such as R or Python) are preferable, as they enable the full analysis workflow to be executed programmatically and version controlled. In contrast, workflows that depend on manual interactions (e.g., click-and-point tools) are harder to reproduce and should be avoided whenever possible. <!-- Survey2026 -->

In addition, using portable programming languages can facilitate execution across different environments. When applicable, software developed during the research should be structured so that it can be reused by others, for example as a library or modular component. This improves not only reproducibility but also the potential for reuse and extension by other researchers. <!-- Survey2026 -->



## Supporting independent reproduction


Reproducibility is not a single property, but a combination of multiple dimensions. Research artifacts may satisfy these dimensions to different degrees, which directly affects how easily others can understand, reuse, and reproduce the results.

The table below summarizes key dimensions of reproducibility and illustrates how artifacts evolve from limited usability to fully reproducible and durable research assets.

<!-- SiddiqEtAl2025 -->
| Dimension | Bad artifact | Operational artifact | Durable artifact |
| --- | --- | --- | --- |
| Accessibility | No or fragmented artifacts; links missing, private, or ephemeral. | Artifacts hosted but with fragile links (personal cloud, ad-hoc URLs); partial coverage of code/data/models. | Artifacts versioned and persistently hosted (e.g., DOI, archival repository) with clear mapping to experiments. |
| Environment Specification | Environment details largely absent; no explicit hardware/software requirements. | Basic installation steps documented, but incomplete dependency lists and implicit assumptions about the platform. | Complete, machine-readable environment specification (e.g., lockfiles, container specs) covering OS, libraries, and hardware. |
| Versioning Rigor | Floating versions or unspecified model/dataset snapshots; reproducibility depends on latest defaults. | Some versions documented (e.g., major library versions), but not consistently pinned across the stack. | Pinned versions at all hierarchy levels (datasets, models, frameworks, CUDA, etc.), with change logs or manifests. |
| Execution Fidelity | No runnable scripts; only high-level prose or pseudo-code. | Pipelines runnable with manual effort (e.g., several shell commands, manual downloads, ad hoc scripts). | End-to-end, automated pipelines or containers that re-create results from scratch with minimal manual steps. |
| Legal Openness | Licenses absent, incompatible, or ambiguous; reuse is legally risky. | Some components licensed, but coverage incomplete or terms unclear for key artifacts (e.g., models, datasets). | Explicit, compatible licenses for all artifacts required to reproduce results, enabling legal reuse and redistribution. |

These dimensions provide a practical lens for evaluating how well an artifact supports independent reproduction. In general, the more dimensions an artifact satisfies at the "durable" level, the higher its potential for long-term reuse, verification, and extension by other researchers.



## Limitations (especially for qualitative data)







---

## References

This module builds on a shared set of references used throughout the GAPS material, including guidelines, standards, and research studies on Open Science and research artifacts.

To avoid redundancy and ensure consistency across modules, all references are centralized in the following document: [GAPS References](/references.md).

Contents in this module were adapted and synthesized from these sources.

---

## Table of contents


- [Module 5 - Reproducibility and transparency](#module-5---reproducibility-and-transparency)
  - [How to ensure verifiability](#how-to-ensure-verifiability)
    - [Validating artifacts before release](#validating-artifacts-before-release)
  - [Sharing scripts, pipelines, and parameters](#sharing-scripts-pipelines-and-parameters)
  - [Supporting independent reproduction](#supporting-independent-reproduction)
  - [Limitations (especially for qualitative data)](#limitations-especially-for-qualitative-data)
  - [References](#references)
  - [Table of contents](#table-of-contents)


---

