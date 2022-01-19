### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project. Link any Issues addressed by this PR, if any. 

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.

### Plugin Acceptance Checklist 

TODO: Mark each as done or provide justification for skipping. Delete this section for non-plugin PRs.
- [ ] Issue linked to PR
- [ ] ReadMe provided in top-level folder with documentation on use and design. ReadMe includes:
  - [ ] Any dependencies and install instructions for opening and building the project
  - [ ] Any CustomDataTypes used are documented
  - [ ] Link to source code location for any built dependencies
- [ ] All State VIs and Project have VI Documentation indicating function and intent
- [ ] Compiled Code separated from Source for everything in project.
- [ ] TestSystemInterface tests written and documented showing happy path in source
  - [ ] TestCases.lvlib removed   
  - [ ] SubVIs or additional business logic beneath the level of PE States should have Unit Tests   
- [ ] TestSystemInterface tests written and documented for any expected failure modes
- [ ] Build added to azure-pipelines.yaml
