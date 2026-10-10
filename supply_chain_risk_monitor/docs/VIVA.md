# Viva Questions and Answers

### Q1. What is a Multi-Agent System?
A Multi-Agent System contains multiple autonomous or semi-autonomous agents that perform specialized tasks and cooperate to solve a larger problem.

### Q2. Why did you use multiple agents?
Supply-chain risk has different information sources. Separate agents allow news, weather and supplier information to be analyzed independently.

### Q3. Why LangGraph?
LangGraph provides a graph-based way to define agent workflows, state and transitions.

### Q4. What is an agent?
An agent is a software component that observes information, uses tools or reasoning, and produces an action or result toward a goal.

### Q5. What is tool calling?
Tool calling allows an agent to invoke an external function, API, database or service to obtain information or perform an operation.

### Q6. Which tools are used?
A news search tool, weather tool and supplier CSV retrieval tool are included.

### Q7. What is orchestration?
Orchestration controls how different agents execute and how their outputs move through the system.

### Q8. Why is the Risk Manager Agent needed?
Individual agents produce separate findings. The Risk Manager combines these findings into one consolidated assessment.

### Q9. What happens if an API is unavailable?
The prototype uses fallback demonstration data so the project can still be demonstrated.

### Q10. How can the system be improved?
It can be connected to ERP, shipment tracking, inventory, port, supplier financial and real-time news systems.

### Q11. Is the risk score a machine-learning prediction?
No. In this academic prototype it is a transparent weighted decision-support calculation.

### Q12. How does the system satisfy the assignment?
It has four agents, tool calling, LangGraph orchestration, a README, source code and a demonstration interface.
