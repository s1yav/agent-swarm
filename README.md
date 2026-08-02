# Agent Swarm 🐝

> **Lightweight Framework for AI Multi-Agent Workflow Orchestration & Google ADK Agents**

`agent-swarm` is a flexible, lightweight orchestrator designed to manage and coordinate complex multi-agent workflows. It combines a TypeScript orchestration engine with specialized Python agents powered by the Google Agent Development Kit (ADK) and Gemini models.

---

## ⚡ Key Features

- **Specialized Python Autonomous Agents**: Built using Google ADK (`LlmAgent`, `BuiltInPlanner`, `ResponseSchema`, `GenerateContentConfig`).
  - **Executive Assistant Agent**: Answers questions about personal coding projects using a Product Manager perspective, simple language, structured output schema, and strict boundary rules.
  - **Director Agent**: Manages root-level workflow direction and task execution.
  - **Customer Support Agent**: Handles general user questions and support inquiries.
- **Structured Output & Planning**: Uses Pydantic schemas (`ResponseSchema`) and `BuiltInPlanner` with thinking budget controls.
- **Agent Lifecycle & Routing**: Register customized agents, route tasks dynamically, and manage execution state across pipelines.
- **TypeScript Native Orchestration**: Type-safe primitives for input/output definitions and multi-agent workflow pipelines.
- **Grafana Telemetry Integration**: Planned support for displaying agent swarm telemetry benchmarks on Grafana dashboards.

---

## 🛠 Project Structure

```
.
├── customer_support_agent/
│   ├── __init__.py
│   └── agent.py              # Customer Support LLM Agent
├── director_agent/
│   ├── __init__.py
│   └── agent.py              # Director / Workflow Steering LLM Agent
├── executive_assistant_agent/
│   ├── __init__.py
│   └── agent.py              # Executive Assistant LLM Agent (PM Persona, ADK Planner & Schema)
├── orchestrator.ts            # TypeScript Orchestrator class & Agent interface
├── main.ts                    # Entry point for TypeScript agent workflows
├── config.ts                  # Workspace & environment configurations
├── utils.ts                   # Utility functions & logging helpers
├── package.json               # TypeScript dependencies & scripts
└── README.md                  # Project documentation
```

---

## 🚀 Quick Start

### Python Agents (Google ADK)

1. **Set up Python Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install google-adk google-genai pydantic python-dotenv ruff
   ```

2. **Run an Agent**:
   ```python
   from executive_assistant_agent.agent import root_agent

   # Execute agent via Google ADK runner
   ```

### TypeScript Orchestrator

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Run Workflow**:
   ```typescript
   import { Orchestrator, Agent } from "./orchestrator";

   class ResearcherAgent implements Agent {
     name = "Researcher";
     async process(input: string): Promise<string> {
       return `Research results for: ${input}`;
     }
   }

   const orchestrator = new Orchestrator();
   orchestrator.registerAgent(new ResearcherAgent());

   const result = await orchestrator.runWorkflow(["Researcher"]);
   console.log("Workflow Result:", result);
   ```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

<!-- Last updated: August 2, 2026 -->


