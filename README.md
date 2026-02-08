# Python Practice Workspace

This workspace is set up for practicing Python development.

Setup (macOS, zsh):

1. Create and activate the virtual environment:

   python3 -m venv .venv
   source .venv/bin/activate

2. Upgrade pip and install dependencies:

   pip install --upgrade pip
   pip install -r requirements.txt -r dev-requirements.txt

3. Run tests:

   pytest -q

4. Format code with Black:

   black src tests

VS Code:
- The workspace is configured to use the `.venv` Python interpreter when present.
- A `tasks.json` is included to run tests and format code.

