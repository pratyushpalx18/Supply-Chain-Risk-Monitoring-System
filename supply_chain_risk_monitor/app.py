import streamlit as st
from graph.workflow import run_workflow
from tools.supplier_tool import get_supplier_data

st.set_page_config(
    page_title="Supply Chain Risk Monitor",
    page_icon="📦",
    layout="wide",
)

st.markdown("""
<style>
.block-container {padding-top: 2rem; padding-bottom: 3rem;}
.hero {
    padding: 1.4rem 1.6rem;
    border-radius: 16px;
    background: linear-gradient(135deg, #172033, #202a3d);
    border: 1px solid #34415a;
    margin-bottom: 1rem;
}
.hero h1 {margin: 0; font-size: 2.35rem;}
.hero p {margin: .35rem 0 0; color: #b8c3d9;}
.trace {
    padding: .8rem 1rem;
    border-radius: 12px;
    border: 1px solid #30394a;
    margin: .45rem 0;
    background: #151a24;
}
.tool {
    font-family: monospace;
    color: #7dd3fc;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>📦 Supply Chain Risk Monitoring System</h1>
  <p>Multi-Agent Decision-Support Prototype • LangGraph + Python</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ System Controls")
    st.caption("Academic prototype / demo mode")
    supplier_id = st.selectbox(
        "Select Supplier",
        ["SUP-001", "SUP-002", "SUP-003", "SUP-004", "SUP-005"],
    )
    analyze = st.button(
        "🚀 Analyze Supply Chain Risk",
        type="primary",
        use_container_width=True,
    )
    st.divider()
    st.markdown("**Agents**")
    st.write("📰 News & Geopolitical")
    st.write("🌦️ Weather")
    st.write("🏭 Supplier")
    st.write("🛡️ Risk Manager")
    st.divider()
    st.caption("Tools: News Search • Weather • Supplier CSV")

supplier = get_supplier_data(supplier_id)

if "error" not in supplier:
    st.subheader("Supplier Profile")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Supplier", supplier["supplier_name"])
    c2.metric("Location", supplier["location"])
    c3.metric("On-time Delivery", f"{supplier['on_time_delivery_pct']}%")
    c4.metric("Inventory Coverage", f"{supplier['inventory_coverage_days']} days")

    st.info(
        "💡 Select a supplier and click **Analyze Supply Chain Risk** "
        "to run the agents through the LangGraph orchestrator."
    )

    if analyze:
        with st.spinner("Running 3 specialist agents and the Risk Manager..."):
            result = run_workflow(supplier_id, supplier["location"])

        final = result["final"]

        st.subheader("📊 Consolidated Risk Dashboard")
        r1, r2, r3, r4 = st.columns(4)
        r1.metric("Overall Risk", final["overall_risk"])
        r2.metric("Risk Score", f"{final['risk_score']}/100")
        r3.metric("News Risk", result["news"]["risk_level"])
        r4.metric("Weather Risk", result["weather"]["risk_level"])

        score = int(final["risk_score"])
        st.progress(score / 100, text=f"Consolidated risk score: {score}/100")

        st.subheader("🔄 Agent & Tool Execution Trace")
        st.caption(
            "This trace makes the multi-agent orchestration and tool calling "
            "visible for project demonstration."
        )

        for i, item in enumerate(result.get("execution_trace", []), start=1):
            st.markdown(
                f"""
                <div class="trace">
                  <b>{i}. {item['agent']}</b><br>
                  ↳ {item['action']}<br>
                  <span class="tool">Tool/State: {item['tool']}</span><br>
                  ✓ Result: {item['result']}
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.subheader("🤖 Specialist Agent Findings")

        with st.expander("📰 News & Geopolitical Agent", expanded=True):
            st.caption(f"Tool called: `{result['news']['tool_call']}`")
            for event in result["news"]["events"]:
                st.markdown(f"**{event['severity']} — {event['title']}**")
                st.write(event["summary"])

        with st.expander("🌦️ Weather Risk Agent", expanded=True):
            st.caption(f"Tool called: `{result['weather']['tool_call']}`")
            weather = result["weather"]["weather"]
            w1, w2, w3 = st.columns(3)
            w1.metric("Condition", weather["condition"])
            w2.metric(
                "Temperature",
                f"{weather['temperature_c']} °C"
                if weather["temperature_c"] is not None
                else "N/A",
            )
            w3.metric("Risk", weather["risk"])
            st.write(weather["reason"])

        with st.expander("🏭 Supplier Risk Agent", expanded=True):
            st.caption(f"Tool called: `{result['supplier']['tool_call']}`")
            for finding in result["supplier"]["findings"]:
                st.write("• " + finding)

        st.subheader("🛡️ Mitigation Plan")
        for i, action in enumerate(final["mitigation_actions"], 1):
            st.markdown(f"**{i}.** {action}")

        st.success(final["executive_summary"])

        with st.expander("🏗️ View Orchestration Architecture"):
            st.code(
                """
USER
  │
  ▼
LANGGRAPH ORCHESTRATOR
  │
  ├──► News Agent ─────► News Search Tool
  │
  ├──► Weather Agent ──► Weather Tool
  │
  └──► Supplier Agent ─► Supplier CSV Tool
             │
             └──────────────┐
                            ▼
                    RISK MANAGER AGENT
                            │
                            ▼
                    FINAL RISK REPORT
            + MITIGATION ACTIONS
                """,
                language="text",
            )
else:
    st.error(supplier["error"])
