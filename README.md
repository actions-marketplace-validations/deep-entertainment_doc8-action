# doc8-check docker action

This action checks paths of ReST files using [doc8](https://github.com/pycqa/doc8)

## Inputs

## `scan-paths`

**Required** A comma separated list of paths to check. Defaults to "."

## `ignore-paths`

**Required** A comma separated list of paths to ignore. Defaults to ""

## `add-annotations`

**Required** Set to true, to add error annotations for every error found during the check. Defaults to "true"

## Outputs

## `files_selected`

The number of files scanned.

## `files_ignored`

The number of files ignored.

## `total_errors`

Total number of errors.

## Example usage

```
- name: doc8-check
  uses: deep-entertainment/doc8-action@v1
  with:
    scan-paths: "/doc"
    ignore-paths: "/doc/_build"
```
