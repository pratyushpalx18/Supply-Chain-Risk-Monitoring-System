# Supply Chain Risk Monitoring System

## Multi-Agent System Project

**Domain:** Business, Finance & Operations  
**Problem Statement:** Supply Chain Risk Monitoring System  
**Framework:** LangGraph + LangChain  
**Interface:** Streamlit  
**Language:** Python

### 1. Objective

The system uses multiple specialized AI agents to monitor supply-chain risks from:
- news and geopolitical events,
- weather conditions,
- supplier performance data.

A Risk Manager Agent combines the evidence and produces a risk assessment and mitigation plan.

### 2. Agents

1. **News & Geopolitical Risk Agent**
   - Uses the News Search tool.
   - Identifies geopolitical disruptions, strikes, sanctions, trade restrictions, conflicts and transport disruptions.
   - Demo mode uses deterministic sample news when no API key is configured.

2. **Weather Risk Agent**
   - Uses a weather tool.
   - Detects heavy rain, storms, floods, extreme temperature and other transport-impacting conditions.
   - Demo mode uses sample weather data.

3. **Supplier Risk Agent**
   - Uses the supplier CSV tool.
   - Evaluates delivery delay rate, quality score, financial risk, inventory coverage and supplier location.

4. **Risk Manager Agent**
   - Receives all agent findings.
   - Calculates a consolidated risk level.
   - Produces mitigation actions.

### 3. Architecture

```text
                       USER
                         |
                         v
                 +---------------+
                 |   LangGraph   |
                 | Orchestrator  |
                 +-------+-------+
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
 +-------------+  +-------------+  +-------------+
 | News Agent  |  | Weather     |  | Supplier    |
 |             |  | Agent       |  | Agent       |
 +------+------+  +------+------+  +------+------+
        |                |                |
        v                v                v
  News Tool        Weather Tool      CSV Tool
        |                |                |
        +----------------+----------------+
                         |
                         v
                +----------------+
                | Risk Manager   |
                | Agent          |
                +-------+--------+
                        |
                        v
                 Risk Report
              + Mitigation Plan
```

### 4. Project Structure

```text
supply-chain-risk-monitor/
├── agents/
│   ├── news_agent.py
│   ├── weather_agent.py
│   ├── supplier_agent.py
│   └── risk_manager.py
├── tools/
│   ├── news_tool.py
│   ├── weather_tool.py
│   └── supplier_tool.py
├── data/
│   └── suppliers.csv
├── graph/
│   └── workflow.py
├── docs/
│   ├── REPORT.md
│   └── VIVA.md
├── app.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

### 5. Installation

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

### 6. Environment Variables

Copy `.env.example` to `.env`.

The project works in **demo mode without API keys**.

For LLM mode, configure:
```env
OPENAI_API_KEY=your_key_here
```

Optional:
```env
OPENWEATHER_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

### 7. Run

Command-line:
```bash
python main.py
```

Streamlit:
```bash
streamlit run app.py
```

### 8. Example

Try:
```text
Supplier: SUP-001
```

The system combines:
- supplier performance,
- weather risk,
- external/news risk,

and returns a consolidated assessment.

### 9. Assignment Requirements Mapping

| Requirement | Implementation |
|---|---|
| Minimum 3 agents | 4 agents |
| Suitable framework | LangGraph |
| Tool calling | News, Weather, Supplier CSV tools |
| Orchestration | LangGraph StateGraph |
| Individual code | GitHub-ready repository |
| README | Included |
| Report | `docs/REPORT.md` |
| Demo | Streamlit + CLI |

### 10. Important Note

This is an academic prototype. Risk levels are decision-support outputs and should be validated against authoritative operational data before real business decisions.


### Enhanced Demonstration UI

The Streamlit dashboard visibly demonstrates:
- four agents,
- the tool called by each specialist agent,
- tool results,
- LangGraph fan-out/fan-in orchestration,
- consolidated risk score,
- mitigation actions,
- an architecture view.

The workflow uses a **fan-out/fan-in pattern**: News, Weather and Supplier agents are independent branches, and the Risk Manager receives all three outputs before producing the final result.
