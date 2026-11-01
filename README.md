# B2B Tech Stack & Buying Intent Signals MCP Server

Turn your AI Agent (Claude Desktop, Cursor, Windsurf, or n8n) into an autonomous **AI SDR & Lead Intelligence Engine**.

Query real-time engineering hiring velocity, technology stack adoptions (e.g. *vLLM, Rust, Kubernetes, MCP*), and architectural pain points across 1,700+ roles at top AI & tech companies (Perplexity, Anthropic, Cognition, Linear, Vercel, Figma, etc.).

---

## 🔑 Quick Setup

### 1. Get your Free API Key
Get your free API key (50 free requests/month, no credit card required) on [RapidAPI](https://rapidapi.com/your-org/api/b2b-tech-stack-and-hiring-intent-signals).

### 2. Configure in Claude Desktop
Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "b2b-tech-signals": {
      "command": "python",
      "args": ["E:\\Workspace\\Projects\\mcp-server-b2b-signals\\server.py"],
      "env": {
        "B2B_SIGNALS_API_KEY": "YOUR_RAPIDAPI_KEY",
        "B2B_SIGNALS_API_HOST": "https://b2b-tech-signals.p.rapidapi.com"
      }
    }
  }
}
```

---

## 🛠 Available MCP Tools

| Tool | Description |
| :--- | :--- |
| `search_companies_by_tech_signal` | Find companies expanding in specific tech (`Rust`, `vLLM`, `MCP`, `ClickHouse`, `CUDA`). |
| `get_company_hiring_velocity` | Inspect all technical hiring signals and compensation tiers for a specific domain (`perplexity.ai`, `cognition.ai`). |
| `find_companies_with_pain_point` | Discover companies hiring for `GPU_INFERENCE_SCALING`, `SECURITY_AUDIT_COMPLIANCE`, or `BUILDING_PAYMENT_INFRA`. |

---

## 💡 Example Prompt for Claude / Cursor

> *"Find companies hiring for vLLM or GPU inference right now, check their pain points and budget, and draft a high-converting Cold Email to their Head of Infrastructure pitching our GPU optimization platform."*

---

## 💰 Pricing & Tiers
- **Basic (Free):** 50 requests/month (Perfect for personal research & testing)
- **Pro ($29/mo):** 2,500 requests/month (For solo founders & AI SDR automations)
- **Ultra ($99/mo):** 15,000 requests/month (For agencies, SMMA, and high-frequency n8n/Clay pipelines)

Upgrade anytime on [RapidAPI](https://rapidapi.com/your-org/api/b2b-tech-stack-and-hiring-intent-signals).
