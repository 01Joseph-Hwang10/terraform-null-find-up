# Find Up

Implementation of the famous [find-up](https://www.npmjs.com/package/find-up) npm package in Python
that is packaged as a terraform module.

It searches specified file (or files) in the current directory and all parent directories.

## Requirements

- Terraform
- Python 3.6 or later

## Usage

Basic usage:
```hcl
module "workspace_root" {
  source = "01Joseph-Hwang10/find-up/null"

  targets = "requirements.txt"
}
```

Multiple targets:
```hcl
module "workspace_root" {
  source = "01Joseph-Hwang10/find-up/null"

  targets = ["requirements.txt", "pyproject.toml"]
}
```
