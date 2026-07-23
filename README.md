# Agent Swarm 🐝

> **Lightweight TypeScript Framework for AI Multi-Agent Workflow Orchestration**

`agent-swarm` is a flexible, lightweight TypeScript orchestrator designed to manage and coordinate complex multi-agent workflows. It provides simple primitives for registering specialized autonomous agents, routing tasks, managing intermediate pipeline states, and executing sequential or parallel agent workflows.

---

## ⚡ Key Features

- **Agent Registration & Lifecycle**: Easily register customized agents implementing common execution interfaces.
- **Stateful Workflow Pipelines**: Pass and transform state across multi-step agent pipelines with execution logging.
- **TypeScript Native**: Full type safety for agent inputs, outputs, and orchestration configurations.
- **Extensible Architecture**: Support for pluggable communication strategies, error handlers, and state management.

---

## 🚀 Quick Start

### Installation

```bash
npm install
```

### Usage Example

```typescript
import { Orchestrator, Agent } from "./orchestrator";

// Create custom agent implementation
class ResearcherAgent implements Agent {
  name = "Researcher";
  async process(input: string): Promise<string> {
    return `Research results for: ${input}`;
  }
}

// Initialize orchestrator and register agents
const orchestrator = new Orchestrator();
orchestrator.registerAgent(new ResearcherAgent());

// Run an agent workflow
const result = await orchestrator.runWorkflow(["Researcher"]);
console.log("Workflow Result:", result);
```

---

## 🛠 Project Structure

```
.
├── orchestrator.ts    # Main Orchestrator class & Agent interface definition
├── main.ts            # Entry point for agent workflow executions
├── config.ts          # Orchestrator & agent environment configurations
├── utils.ts           # Shared utilities and logging helpers
└── package.json       # Project dependencies & scripts
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
