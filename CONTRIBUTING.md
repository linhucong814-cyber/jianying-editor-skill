# Contributing

Use a feature branch and keep pull requests focused. Include the platform, the JianYing version where relevant, and the checks you ran. Use synthetic media and a separate draft folder for testing.

Install Python 3.12 and the packages listed in `requirements.txt`. Run the local checks from the repository root.

```bash
python -m unittest discover -s tests -v
python tools/check_repo_hygiene.py
python tools/validate_data_schema.py
```

The [GitHub Actions configuration](tools/github-ci.yml) defines the same checks and linting for Windows and macOS. To enable it, place it at `.github/workflows/ci.yml` and push with an account authorized to manage workflows.
