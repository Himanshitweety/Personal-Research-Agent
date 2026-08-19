# Personal-Research-Agent
Give it a topic, it searches the web (via API), scrapes/reads pages, and writes a structured summary report. Teaches: calling LLM APIs, tool-calling/function-calling patterns, chaining multiple steps (search → fetch → summarize), basic prompt engineering. This is a very "AI agent 101" project.


Personal Research Agent → deep on agent concepts, shallow on infrastructure

This project is almost entirely about the actual "AI agent" mechanics:

The core loop (LLM decides to search → gets results → decides to fetch a page → reads it → decides if it has enough → writes summary) is the classic agentic pattern (ReAct-style). You'll implement this loop yourself, which forces you to actually understand it instead of just using a framework.
You'll deal with real tool-calling/function-calling schemas, multi-turn context passing, and the LLM deciding when to stop — which is the hard, interesting part of agent design.
Prompt engineering is central here, not incidental — how you describe tools, how you feed back results, how you ask for the final structured report all matter a lot to output quality.
Infrastructure is light: no scraping fragility, no scheduling, no DB really required. Almost your whole effort goes into agent logic.
