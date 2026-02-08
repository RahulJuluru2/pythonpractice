import subprocess
import sys
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from src.lab.data import LAB_TOPICS
from src.lab.ui import lab_html

router = APIRouter()


class RunRequest(BaseModel):
    code: str = Field(..., min_length=1, max_length=10000)


@router.get("/lab", response_class=HTMLResponse)
def lab():
    return lab_html(LAB_TOPICS)


@router.get("/lab-data")
def lab_data():
    return LAB_TOPICS


@router.post("/run")
def run_code(request: RunRequest):
    runner = (
        "import builtins, sys, traceback\n"
        "try:\n"
        "    import resource\n"
        "    resource.setrlimit(resource.RLIMIT_CPU, (1, 1))\n"
        "    resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))\n"
        "    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))\n"
        "except Exception:\n"
        "    pass\n"
        "ALLOWED_IMPORTS = {\n"
        "    'time', 'contextlib', 'dataclasses', 'typing',\n"
        "    'asyncio', 'functools', 'itertools'\n"
        "}\n"
        "original_import = builtins.__import__\n"
        "def _limited_import(name, globals=None, locals=None, fromlist=(), level=0):\n"
        "    root = name.split('.')[0]\n"
        "    if root not in ALLOWED_IMPORTS:\n"
        "        raise ImportError('Imports are restricted in this lab.')\n"
        "    return original_import(name, globals, locals, fromlist, level)\n"
        "builtins.__import__ = _limited_import\n"
        "code = sys.stdin.read()\n"
        "globals_dict = {}\n"
        "try:\n"
        "    exec(compile(code, '<user-code>', 'exec'), globals_dict, globals_dict)\n"
        "except Exception:\n"
        "    traceback.print_exc()\n"
    )

    try:
        result = subprocess.run(
            [sys.executable, "-I", "-S", "-c", runner],
            input=request.code,
            text=True,
            capture_output=True,
            timeout=2,
        )
    except subprocess.TimeoutExpired:
        return {"output": "Execution timed out."}

    output = (result.stdout or "") + (result.stderr or "")
    return {"output": output.strip()}
