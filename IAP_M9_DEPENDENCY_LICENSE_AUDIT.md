# IAP-M9 â€” Dependency and License Audit

**Project:** Student Task Tracker
**Course:** EECE 4081 â€” Software Engineering
**Student:** George Kakra Obeng
**Audit date:** November 17, 2026
**Repository:** https://github.com/obenggeorge-art/eece4081-iap-task-tracker

## 1. Purpose and scope

This audit reviews the dependency declarations in `requirements.txt`, the Python version selected by GitHub Actions, and the licensing and compatibility checks needed before release. It follows the syllabus requirement for M9: a dependency and licence audit that identifies one compatibility risk with reasoning. This is a **repository-based preliminary audit**; it is not a completed installed-environment license scan.

## 2. Dependency inventory

The following packages and versions are copied from the repository's `requirements.txt` as inspected on November 17, 2026. A pinned version is evidence of a declaration, not proof that the package installed successfully.

| Dependency | Pinned version | Role / reason to review | License verification status |
|---|---|---|---|
| asgiref | 3.12.1 | Django async/server support | Verify installed distribution metadata |
| colorama | 0.4.6 | Terminal color support | Verify installed distribution metadata |
| Django | 6.1.1 | Web framework | Verify installed distribution metadata |
| iniconfig | 2.3.0 | pytest configuration support | Verify installed distribution metadata |
| packaging | 26.3 | Package/version handling | Verify installed distribution metadata |
| pluggy | 1.6.0 | pytest plugin system | Verify installed distribution metadata |
| Pygments | 2.21.0 | Syntax highlighting | Verify installed distribution metadata |
| pytest | 9.1.1 | Test runner | Verify installed distribution metadata |
| pytest-django | 4.14.0 | Django testing integration | Verify installed distribution metadata |
| sqlparse | 0.6.0 | SQL parsing support | Verify installed distribution metadata |
| tzdata | 2026.4 | Time-zone data | Verify installed distribution metadata |

**License assessment:** The repository does not itself establish the exact license metadata for every pinned distribution. Licenses must be checked against installed package metadata and the corresponding distribution license files before a definitive compatibility conclusion. In particular, permissive open-source licensing does not eliminate the obligation to preserve any required notices when redistributing code or packages.

## 3. Compatibility risk and reasoning

**Risk identified: runtime-version mismatch.** The GitHub Actions workflow `.github/workflows/ci.yml` selects Python **3.12**, while `requirements.txt` pins **Django 6.1.1**. Django releases have specific supported-Python ranges. Without checking the pinned Django distribution's `Requires-Python` metadata and running a clean installation, it is not safe to assume that the declared combination is supported. If the range excludes Python 3.12, `pip install -r requirements.txt` may fail and prevent the application and tests from starting.

**Evidence needed:** Run a clean installation under Python 3.12, record `python --version`, `python -m pip check`, and `python -m pytest -v`, and compare with the latest GitHub Actions run for the same commit. A successful CI run on an earlier commit is not proof that a newly pinned version installs.

**Recommended resolution:** Keep the project interpreter, CI Python version, and framework release in a documented supported combination. If incompatibility is confirmed, select a Django release supporting the chosen Python version, update `requirements.txt`, then rerun installation, migrations, Django checks, and tests. Do not change versions without recording the before/after evidence.

## 4. License and supply-chain procedure

1. In a fresh virtual environment, run `python -m pip install -r requirements.txt`.
2. Run `python -m pip list --format=freeze` and `python -m pip check`; save the output.
3. Run `python -m pip install pip-licenses` and `python -m piplicenses --format=markdown --with-urls --with-license-file --no-license-path` (check command support in the installed tool version). Save the output and inspect ambiguous or missing license fields manually.
4. For any package the application redistributes, review the license text and any attribution/notice requirements. Record the actual license name and source URL in an updated inventory.
5. Review the project repository for third-party copied code, assets, or snippets not represented in `requirements.txt`.
6. Record the compatibility test results and any remediation in the prompt-and-diff log.

**Current result:** The dependency declarations and one compatibility risk have been identified. Package-by-package license verification, installation validation, and vulnerability scanning are **pending execution**; this document does not claim those checks passed.

## 5. Reproducible evidence to capture

| Evidence file | Command / source |
|---|---|
| `M9_01_Requirements_Before.png` | Screenshot of `requirements.txt` in VS Code |
| `M9_02_Python_Version.txt` | `python --version` |
| `M9_03_Install_Output.txt` | `python -m pip install -r requirements.txt` |
| `M9_04_Pip_Check.txt` | `python -m pip check` |
| `M9_05_License_Inventory.txt` | License inventory command output |
| `M9_06_Test_Output.txt` | `python -m pytest -v` |
| `M9_07_CI_Run.png` | GitHub Actions run for the audited commit |
| `M9_08_Commit_Diff.png` | GitHub commit showing the audit and any version changes |

## 6. Conclusion

The Task Tracker uses pinned Python dependencies, which improves repeatability but does not guarantee compatibility or licensing compliance. The most important identified risk is the need to verify the pinned Django version against the Python 3.12 environment configured in CI. The next step is to run and record a clean installation and obtain actual distribution license metadata. The audit should be updated with those results before describing M9 as fully verified.

## 7. AI-use and prompt-and-diff log entry

**Tool:** ChatGPT (OpenAI).
**Purpose:** Help inspect repository dependency declarations, organize the M9 audit, identify a compatibility question, and draft a reproducible verification procedure.
**Human verification required:** Run the commands, inspect license metadata, confirm the Python/framework support range, correct any errors, and record the actual outputs.
**Diff summary:** New `IAP_M9_DEPENDENCY_LICENSE_AUDIT.md` document; no application code or dependencies changed by this draft.
