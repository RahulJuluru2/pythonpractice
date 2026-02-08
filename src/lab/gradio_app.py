import subprocess
import sys
from typing import Tuple

import gradio as gr

from src.lab.data import LAB_TOPICS

ALLOWED_IMPORTS = {
    "time",
    "contextlib",
    "dataclasses",
    "typing",
    "asyncio",
    "functools",
    "itertools",
}


def run_user_code(code: str) -> str:
    runner = (
        "import builtins, sys, traceback\n"
        "try:\n"
        "    import resource\n"
        "    resource.setrlimit(resource.RLIMIT_CPU, (1, 1))\n"
        "    resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))\n"
        "    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))\n"
        "except Exception:\n"
        "    pass\n"
        f"ALLOWED_IMPORTS = {sorted(ALLOWED_IMPORTS)!r}\n"
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
            input=code,
            text=True,
            capture_output=True,
            timeout=2,
        )
    except subprocess.TimeoutExpired:
        return "Execution timed out."

    output = (result.stdout or "") + (result.stderr or "")
    return output.strip() or "(no output)"


def topic_choices():
    return [(value["label"], key) for key, value in LAB_TOPICS.items()]


def example_titles(topic_key: str):
    return [item["title"] for item in LAB_TOPICS[topic_key]["examples"]]


def example_code(topic_key: str, example_index: int) -> str:
    return LAB_TOPICS[topic_key]["examples"][example_index]["code"]


def example_prompts(topic_key: str) -> str:
    prompts = LAB_TOPICS[topic_key].get("prompts", [])
    if not prompts:
        return "No prompts available yet."
    return "\n".join([f"{idx + 1}. {text}" for idx, text in enumerate(prompts)])


def select_topic(topic_key: str) -> Tuple[gr.Dropdown, gr.Radio, gr.Code, gr.Markdown]:
    titles = example_titles(topic_key)
    first_code = example_code(topic_key, 0)
    return (
        gr.Dropdown(value=topic_key),
        gr.Radio(choices=titles, value=titles[0]),
        gr.Code(value=first_code, language="python"),
        gr.Markdown(value=example_prompts(topic_key)),
    )


def select_example(topic_key: str, example_title: str) -> gr.Code:
    titles = example_titles(topic_key)
    index = titles.index(example_title)
    return gr.Code(value=example_code(topic_key, index), language="python")


def build_lab() -> gr.Blocks:
    with gr.Blocks(title="Python Concepts Lab", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# Python Concepts Lab\nPick a topic, explore examples, run code, and practice.")

        with gr.Row():
            with gr.Column(scale=5):
                topic = gr.Dropdown(
                    label="Topic",
                    choices=topic_choices(),
                    value=topic_choices()[0][1],
                )
                examples = gr.Radio(
                    label="Examples",
                    choices=example_titles(topic_choices()[0][1]),
                    value=example_titles(topic_choices()[0][1])[0],
                )
                code = gr.Code(
                    label="Code",
                    value=example_code(topic_choices()[0][1], 0),
                    language="python",
                )

            with gr.Column(scale=1, min_width=120):
                run = gr.Button("Run", variant="primary")

            with gr.Column(scale=5):
                output = gr.Textbox(label="Output", lines=16)
                prompts = gr.Markdown(value=example_prompts(topic_choices()[0][1]))

        topic.change(
            select_topic,
            inputs=topic,
            outputs=[topic, examples, code, prompts],
        )
        examples.change(
            select_example,
            inputs=[topic, examples],
            outputs=code,
        )
        run.click(run_user_code, inputs=code, outputs=output)

    return demo
