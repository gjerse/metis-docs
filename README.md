## Metis Documentation & Example Gallery


Solar Orbiter Metis Data Analysis & Documentation
This repository provides guides, examples, and tools for working with Solar Orbiter Metis data using Python.

https://metis-docs.readthedocs.io/en/latest/index.html

# Metis Documentation (INAF → GitHub Mirror)

This repository hosts the documentation for the **Metis** project.

## Workflow

- Main source code and docs live in the internal INAF GitLab:
  - https://www.ict.inaf.it/gitlab/metis/metis-docs
- A mirror of this repository is automatically pushed to:
  - https://github.com/gjerse/metis-docs

ReadTheDocs builds are triggered from the GitHub mirror.

## Local build

```bash
pip install -r docs/requirements.txt
sphinx-build -b html docs _build/html
```

## Mirror setup

Run the script `mirror_setup.sh` to manually sync GitLab → GitHub,  
or configure push mirroring in GitLab settings.
