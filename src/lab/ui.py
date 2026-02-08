def lab_html() -> str:
    return """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Python Lab</title>
    <style>
      :root {
        --bg: #f4f0e8;
        --panel: #ffffff;
        --ink: #1d1d1f;
        --muted: #6b6b6f;
        --accent: #f05d23;
        --accent-ink: #ffffff;
        --border: #e1dad1;
        --shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
      }

      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        font-family: "Space Grotesk", "Avenir Next", system-ui, -apple-system, sans-serif;
        color: var(--ink);
        background: radial-gradient(circle at 20% 20%, #fff2df 0%, transparent 50%),
          radial-gradient(circle at 80% 0%, #ffe1d1 0%, transparent 45%),
          var(--bg);
        min-height: 100vh;
        display: flex;
        flex-direction: column;
      }

      header {
        padding: 24px clamp(20px, 5vw, 60px);
      }

      h1 {
        margin: 0 0 6px 0;
        font-size: clamp(28px, 4vw, 44px);
      }

      p {
        margin: 0;
        color: var(--muted);
      }

      main {
        flex: 1;
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        gap: 24px;
        padding: 0 clamp(20px, 5vw, 60px) 40px;
      }

      .panel {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 18px;
        box-shadow: var(--shadow);
        display: flex;
        flex-direction: column;
        min-height: 360px;
      }

      .panel header {
        padding: 16px 18px 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
      }

      .panel h2 {
        margin: 0;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
      }

      .toolbar {
        display: flex;
        align-items: center;
        gap: 10px;
      }

      select {
        font-family: inherit;
        font-size: 13px;
        padding: 6px 10px;
        border-radius: 999px;
        border: 1px solid var(--border);
        background: #fff7ed;
        color: var(--ink);
      }

      .ghost {
        font-family: inherit;
        font-size: 12px;
        padding: 6px 12px;
        border-radius: 999px;
        border: 1px solid var(--border);
        background: transparent;
        color: var(--muted);
        cursor: pointer;
      }

      .examples {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        padding: 0 18px 12px;
      }

      .example-btn {
        border: 1px solid var(--border);
        background: #fff7ed;
        color: var(--ink);
        border-radius: 999px;
        padding: 6px 12px;
        font-size: 12px;
        cursor: pointer;
      }

      .example-btn.active {
        background: var(--accent);
        color: var(--accent-ink);
        border-color: var(--accent);
      }

      textarea {
        flex: 1;
        border: none;
        padding: 18px;
        font-family: "Fira Code", "JetBrains Mono", monospace;
        font-size: 15px;
        resize: none;
        background: transparent;
        color: var(--ink);
      }

      textarea:focus {
        outline: none;
      }

      pre {
        margin: 0;
        padding: 18px;
        font-family: "Fira Code", "JetBrains Mono", monospace;
        font-size: 14px;
        overflow: auto;
        white-space: pre-wrap;
      }

      .questions {
        padding: 0 18px 18px;
        color: var(--muted);
        font-size: 14px;
        display: flex;
        flex-direction: column;
        gap: 10px;
      }

      .questions strong {
        color: var(--ink);
        font-weight: 600;
        letter-spacing: 0.02em;
      }

      .question {
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 10px;
        align-items: start;
      }

      .question span {
        font-weight: 600;
        color: var(--accent);
      }

      .controls {
        display: flex;
        align-items: center;
        justify-content: center;
      }

      button#run {
        width: 84px;
        height: 84px;
        border-radius: 28px;
        border: none;
        background: var(--accent);
        color: var(--accent-ink);
        font-size: 30px;
        box-shadow: var(--shadow);
        cursor: pointer;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
      }

      button#run:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 30px rgba(240, 93, 35, 0.35);
      }

      button#run:active {
        transform: translateY(1px) scale(0.98);
      }

      .status {
        text-align: center;
        color: var(--muted);
        font-size: 12px;
        margin-top: 10px;
      }

      @media (max-width: 980px) {
        main {
          grid-template-columns: 1fr;
          gap: 16px;
        }

        .controls {
          order: 2;
        }
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Python Concepts Lab</h1>
      <p>Pick a topic, explore examples, run code, and practice.</p>
    </header>
    <main>
      <section class="panel">
        <header>
          <h2>Code</h2>
          <div class="toolbar">
            <select id="topic" aria-label="Choose a topic"></select>
            <button class="ghost" id="reset" type="button">Reset</button>
          </div>
        </header>
        <div class="examples" id="examples"></div>
        <textarea id="code" spellcheck="false"></textarea>
      </section>

      <section class="controls">
        <div>
          <button id="run" aria-label="Run code">▶</button>
          <div class="status" id="status">Ready</div>
        </div>
      </section>

      <section class="panel">
        <header><h2>Output</h2></header>
        <pre id="output">Press play to execute the code.</pre>
        <div class="questions" id="questions">
          <strong>Practice prompts</strong>
          <div class="question"><span>1.</span><div>Pick a topic to see questions.</div></div>
        </div>
      </section>
    </main>
    <script>
      const runButton = document.getElementById("run");
      const output = document.getElementById("output");
      const status = document.getElementById("status");
      const code = document.getElementById("code");
      const topic = document.getElementById("topic");
      const reset = document.getElementById("reset");
      const questions = document.getElementById("questions");
      const examples = document.getElementById("examples");

      const state = {
        topics: {},
        currentTopic: null,
        currentExample: 0,
      };

      function storageKey(topicName, exampleIndex) {
        return `py-lab-${topicName}-${exampleIndex}`;
      }

      function persistCurrent() {
        if (!state.currentTopic) return;
        localStorage.setItem(
          storageKey(state.currentTopic, state.currentExample),
          code.value
        );
        localStorage.setItem("py-lab-last-topic", state.currentTopic);
        localStorage.setItem("py-lab-last-example", String(state.currentExample));
      }

      function renderQuestions(topicName) {
        const items = state.topics[topicName]?.prompts || [];
        questions.innerHTML = "<strong>Practice prompts</strong>";
        if (items.length === 0) {
          questions.innerHTML +=
            "<div class=\"question\"><span>1.</span><div>No prompts available yet.</div></div>";
          return;
        }
        items.forEach((text, idx) => {
          const row = document.createElement("div");
          row.className = "question";
          row.innerHTML = `<span>${idx + 1}.</span><div>${text}</div>`;
          questions.appendChild(row);
        });
      }

      function setExample(topicName, exampleIndex) {
        const example = state.topics[topicName]?.examples?.[exampleIndex];
        if (!example) return;
        const saved = localStorage.getItem(storageKey(topicName, exampleIndex));
        code.value = saved ?? example.code;
        state.currentExample = exampleIndex;
        [...examples.children].forEach((btn, idx) => {
          btn.classList.toggle("active", idx === exampleIndex);
        });
        renderQuestions(topicName);
      }

      function renderExamples(topicName) {
        examples.innerHTML = "";
        const exampleList = state.topics[topicName]?.examples || [];
        exampleList.forEach((item, idx) => {
          const btn = document.createElement("button");
          btn.className = "example-btn";
          btn.type = "button";
          btn.textContent = item.title;
          btn.addEventListener("click", () => {
            persistCurrent();
            setExample(topicName, idx);
          });
          examples.appendChild(btn);
        });
        const lastExample = Number(localStorage.getItem("py-lab-last-example") || 0);
        const safeIndex = Number.isFinite(lastExample)
          ? Math.min(lastExample, exampleList.length - 1)
          : 0;
        setExample(topicName, safeIndex >= 0 ? safeIndex : 0);
      }

      function renderTopics(topicName) {
        topic.innerHTML = "";
        Object.entries(state.topics).forEach(([key, value]) => {
          const option = document.createElement("option");
          option.value = key;
          option.textContent = value.label;
          topic.appendChild(option);
        });
        topic.value = topicName;
      }

      async function loadData() {
        try {
          const response = await fetch("/lab-data");
          if (!response.ok) throw new Error("Failed to load topics");
          state.topics = await response.json();
          const lastTopic = localStorage.getItem("py-lab-last-topic");
          const fallback = Object.keys(state.topics)[0];
          state.currentTopic =
            lastTopic && state.topics[lastTopic] ? lastTopic : fallback;
          renderTopics(state.currentTopic);
          renderExamples(state.currentTopic);
        } catch (error) {
          output.textContent = "Failed to load lab data.";
        }
      }

      topic.addEventListener("change", () => {
        persistCurrent();
        state.currentTopic = topic.value;
        renderExamples(state.currentTopic);
      });
      reset.addEventListener("click", () => {
        const example =
          state.topics[state.currentTopic].examples[state.currentExample];
        code.value = example.code;
        persistCurrent();
      });
      code.addEventListener("input", persistCurrent);

      async function runCode() {
        status.textContent = "Running...";
        output.textContent = "";
        runButton.disabled = true;

        try {
          const response = await fetch("/run", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: code.value }),
          });
          const payload = await response.json();
          if (!response.ok) {
            output.textContent = payload.detail || "Error running code.";
          } else {
            output.textContent = payload.output || "(no output)";
          }
        } catch (error) {
          output.textContent = "Failed to contact server.";
        } finally {
          runButton.disabled = false;
          status.textContent = "Ready";
        }
      }

      runButton.addEventListener("click", runCode);
      loadData();
    </script>
  </body>
</html>
"""
