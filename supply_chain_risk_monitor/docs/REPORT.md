# Project Report
## Supply Chain Risk Monitoring System

### 1. Introduction

Modern supply chains are exposed to multiple external and internal risks. Weather disruptions, geopolitical events, transportation problems and supplier performance issues can affect production and delivery schedules.

This project proposes a Multi-Agent System that independently monitors different risk sources and then combines their findings through a Risk Manager Agent.

### 2. Problem Statement

**Title:** Supply Chain Risk Monitoring System

**Description:** Agents monitor news, weather, geopolitical events, and supplier data to detect risks and suggest mitigation actions.

### 3. Objectives

- Monitor multiple supply-chain risk sources.
- Use specialized AI agents for different information domains.
- Demonstrate tool calling.
- Demonstrate multi-agent orchestration.
- Generate a consolidated risk assessment.
- Suggest practical mitigation actions.

### 4. Proposed Agents

#### Agent 1 — News & Geopolitical Risk Agent
Input: Supplier location  
Tool: News search  
Output: External event list and risk level.

#### Agent 2 — Weather Risk Agent
Input: Supplier location  
Tool: Weather API  
Output: Weather condition and disruption risk.

#### Agent 3 — Supplier Risk Agent
Input: Supplier ID  
Tool: CSV supplier database  
Output: Supplier performance risk.

#### Agent 4 — Risk Manager Agent
Input: Outputs of the three specialist agents  
Tool/Logic: Risk aggregation and mitigation rules  
Output: Overall risk and recommended actions.

### 5. System Architecture

```text
User
 |
 v
LangGraph Orchestrator
 |
 +--> News Agent ------> News Tool
 |
 +--> Weather Agent ---> Weather Tool
 |
 +--> Supplier Agent --> CSV Tool
 |
 v
Risk Manager Agent
 |
 v
Risk Report + Mitigation Plan
```

### 6. Workflow

1. User selects a supplier.
2. Supplier location is identified.
3. News Agent checks external events.
4. Weather Agent checks weather risk.
5. Supplier Agent checks historical supplier performance.
6. Risk Manager combines all outputs.
7. System generates an overall risk level.
8. System provides mitigation actions.

### 7. Risk Scoring

The prototype uses three component risk levels:

- Low = 1
- Medium = 2
- High = 3

Supplier performance has 50% weight, while news and weather each have 25%.

Overall score:

```text
Combined Score =
0.50 × Supplier Risk
+ 0.25 × News Risk
+ 0.25 × Weather Risk
```

The score is converted to a 0–100 display score.

### 8. Tool Calling

The project demonstrates three tools:

1. News Search Tool
2. Weather Tool
3. Supplier CSV Retrieval Tool

When API keys are unavailable, deterministic demo data allows the system to run during evaluation.

### 9. Orchestration

LangGraph is used to define a stateful workflow.

```text
START
  ↓
News Agent
  ↓
Weather Agent
  ↓
Supplier Agent
  ↓
Risk Manager Agent
  ↓
END
```

Each node writes its result into shared workflow state.

### 10. Technologies

- Python
- LangGraph
- LangChain ecosystem
- Streamlit
- Requests
- Pandas
- CSV
- Optional OpenAI API
- Optional OpenWeather API
- Optional News API
- GitHub

### 11. Expected Output

For a high-risk supplier, the system may identify:

- low on-time delivery,
- high average delay,
- limited inventory coverage,
- adverse weather,
- external logistics disruption.

It then recommends actions such as alternative sourcing, safety-stock adjustment, route evaluation and supplier follow-up.

### 12. Advantages

- Modular architecture.
- Different agents specialize in different tasks.
- Tools can be replaced independently.
- Easy to extend with databases and enterprise APIs.
- Demonstrates practical AI-agent orchestration.

### 13. Limitations

- Demo news/weather data is used when APIs are not configured.
- The risk model is a prototype and not a production risk model.
- Real organizations require validated data sources.
- External news can contain incomplete or incorrect information.

### 14. Future Scope

- Add real-time news feeds.
- Add live supplier ERP data.
- Add port and shipping APIs.
- Add inventory forecasting.
- Add historical risk analytics.
- Add alert notifications.
- Add human approval before mitigation actions.
- Add database persistence and authentication.

### 15. Conclusion

The Supply Chain Risk Monitoring System demonstrates how multiple specialized agents can collaborate through orchestration and tool calling. By combining supplier performance, weather and external-event information, the system provides a structured risk assessment and mitigation plan.
