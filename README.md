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

## Docker Usage

Build the Docker image:

```sh
docker build -t python-practice-app .
```

Run the container:

```sh
docker run -d -p 8000:8000 python-practice-app
```

Visit http://localhost:8000/hello/World to test the API.

Interactive lab:
- http://localhost:8000/lab

The lab executes Python on the server for learning purposes. Do not expose it publicly.
