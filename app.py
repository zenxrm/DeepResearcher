import streamlit as st
import time
from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain
)

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="DEEPRESEARCHER | AI Research System",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #090d12;
    --surface: #101720;
    --surface-light: #151f2b;
    --border: #24313e;
    --text: #edf3f7;
    --muted: #8998a8;
    --accent: #a4f4c5;
    --accent-dark: #65c993;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg);
    color: var(--text);
    font-family: 'Manrope', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: var(--surface);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit branding */

#MainMenu, footer {
    visibility: hidden;
}

/* Top navigation */

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 0 25px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 55px;
}

.brand {
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 2px;
    color: var(--text);
}

.brand span {
    color: var(--accent);
}

.nav-label {
    color: var(--muted);
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 1px;
}

/* Hero section */

.eyebrow {
    color: var(--accent);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    margin-bottom: 18px;
}

.hero-title {
    font-size: clamp(42px, 6vw, 70px);
    line-height: 1.08;
    font-weight: 800;
    letter-spacing: -3px;
    color: var(--text);
    margin: 0;
}

.hero-title span {
    color: var(--accent);
}

.hero-subtitle {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.9;
    max-width: 720px;
    margin-top: 22px;
    margin-bottom: 35px;
}

/* Workflow */

.workflow {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    margin: 35px 0 55px 0;
}

.workflow-step {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 12px 17px;
    border-radius: 7px;
    color: #cbd6df;
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.5px;
}

.workflow-arrow {
    color: var(--accent);
    font-size: 14px;
}

/* Section headings */

.section-label {
    color: var(--accent);
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 8px;
}

.section-description {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.7;
    margin-bottom: 25px;
}

/* Input area */

[data-testid="stTextInput"] input {
    background: #101720 !important;
    border: 1px solid #2a3947 !important;
    border-radius: 8px !important;
    color: white !important;
    padding: 15px !important;
    font-size: 14px !important;
}

[data-testid="stTextInput"] input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 1px var(--accent) !important;
}

.stTextInput label {
    color: #cbd6df !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}

/* Buttons */

.stButton > button {
    background: var(--accent) !important;
    color: #07110c !important;
    border: none !important;
    border-radius: 7px !important;
    font-weight: 800 !important;
    font-size: 12px !important;
    letter-spacing: 0.5px !important;
    padding: 13px 22px !important;
    min-height: 45px;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: #c2ffda !important;
    transform: translateY(-1px);
}

/* Pipeline cards */

.pipeline-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 19px;
    height: 145px;
}

.pipeline-number {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--accent);
    margin-bottom: 15px;
}

.pipeline-name {
    color: var(--text);
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 7px;
}

.pipeline-desc {
    color: var(--muted);
    font-size: 11px;
    line-height: 1.6;
}

/* Result sections */

.result-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 22px;
    margin-bottom: 15px;
}

.result-heading {
    font-size: 15px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 12px;
}

.result-meta {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--accent);
    margin-bottom: 15px;
    letter-spacing: 1px;
}

/* Report content */

.report-content {
    color: #cbd6df;
    font-size: 13px;
    line-height: 1.9;
}

/* Download button */

[data-testid="stDownloadButton"] button {
    background: transparent !important;
    color: var(--accent) !important;
    border: 1px solid var(--accent) !important;
    border-radius: 7px !important;
}

/* Expander */

[data-testid="stExpander"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
}

/* Divider */

hr {
    border-color: var(--border) !important;
    margin: 40px 0 !important;
}

/* Footer */

.footer {
    text-align: center;
    color: #667482;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 1px;
    padding-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "research_data" not in st.session_state:
    st.session_state.research_data = None

if "last_topic" not in st.session_state:
    st.session_state.last_topic = ""


# =========================================================
# NAVIGATION
# =========================================================

st.markdown("""
<div class="navbar">
    <div class="brand">DEEP<span>RESEARCHER</span></div>
    <div class="nav-label">MULTI-AGENT AI RESEARCH SYSTEM &nbsp; / &nbsp; V1.0</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="eyebrow">◈ &nbsp; AUTONOMOUS RESEARCH WORKFLOW</div>

<h1 class="hero-title">
    From a question<br>
    to <span>understanding.</span>
</h1>

<div class="hero-subtitle">
    A project demonstrating how deep-research workflows in AI systems can work:
    specialized agents search the web, inspect useful sources, synthesize findings
    into a report, and review the result for clarity and quality.
</div>
""", unsafe_allow_html=True)


# =========================================================
# WORKFLOW
# =========================================================

st.markdown("""
<div class="workflow">
    <div class="workflow-step">01 &nbsp; SEARCH</div>
    <div class="workflow-arrow">→</div>
    <div class="workflow-step">02 &nbsp; READ</div>
    <div class="workflow-arrow">→</div>
    <div class="workflow-step">03 &nbsp; SYNTHESIZE</div>
    <div class="workflow-arrow">→</div>
    <div class="workflow-step">04 &nbsp; REVIEW</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# RESEARCH INPUT
# =========================================================

st.markdown("""
<div class="section-label">01 / START YOUR RESEARCH</div>
<div class="section-title">What would you like to explore?</div>
<div class="section-description">
    Enter a research topic. The agents will work together to investigate it and
    prepare a structured report.
</div>
""", unsafe_allow_html=True)

topic = st.text_input(
    "RESEARCH TOPIC",
    placeholder="e.g. How are AI agents transforming software development?",
    label_visibility="visible"
)

run_button = st.button(
    "◈  START DEEP RESEARCH",
    use_container_width=True
)


# =========================================================
# PIPELINE OVERVIEW
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-label">02 / THE SYSTEM</div>
<div class="section-title">Four stages. One research process.</div>
<div class="section-description">
    Each stage has a specific responsibility in the research pipeline.
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-number">STAGE 01</div>
        <div class="pipeline-name">Search Agent</div>
        <div class="pipeline-desc">
            Searches the web and identifies relevant information and sources.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-number">STAGE 02</div>
        <div class="pipeline-name">Reader Agent</div>
        <div class="pipeline-desc">
            Visits useful pages and extracts relevant content for analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-number">STAGE 03</div>
        <div class="pipeline-name">Writer Chain</div>
        <div class="pipeline-desc">
            Combines collected information into a structured research report.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-number">STAGE 04</div>
        <div class="pipeline-name">Critic Chain</div>
        <div class="pipeline-desc">
            Reviews the report and provides feedback on its quality.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# RESEARCH PIPELINE EXECUTION
# =========================================================

if run_button:

    if not topic.strip():
        st.warning("Please enter a research topic before starting.")

    else:

        st.session_state.research_data = None
        st.session_state.last_topic = topic.strip()

        search_output = None
        reader_output = None
        writer_output = None
        critic_output = None

        st.markdown("---")

        st.markdown("""
        <div class="section-label">03 / LIVE EXECUTION</div>
        <div class="section-title">Research in progress</div>
        """, unsafe_allow_html=True)

        progress_bar = st.progress(0)
        status = st.empty()

        try:

            # -------------------------------------------------
            # STAGE 1: SEARCH AGENT
            # -------------------------------------------------

            status.markdown("🔎 **Stage 1/4 — Search Agent:** Searching the web...")
            search_agent = build_search_agent()

            search_output = search_agent.invoke({
                "messages": [
                    {
                        "role": "user",
                        "content": f"Search the web for this research topic: {topic}"
                    }
                ]
            })

            search_output = str(search_output)

            progress_bar.progress(25)

            # -------------------------------------------------
            # STAGE 2: READER AGENT
            # -------------------------------------------------

            status.markdown("📖 **Stage 2/4 — Reader Agent:** Reading relevant sources...")
            reader_agent = build_reader_agent()

            reader_output = reader_agent.invoke({
                "messages": [
                    {
                        "role": "user",
                        "content": f"""
                        Research topic: {topic}

                        Here are the search results:
                        {search_output}

                        Visit the relevant URLs, extract useful information,
                        and summarize the findings.
                        """
                    }
                ]
            })

            reader_output = str(reader_output)

            progress_bar.progress(50)

            # -------------------------------------------------
            # STAGE 3: WRITER CHAIN
            # -------------------------------------------------

            status.markdown("✍️ **Stage 3/4 — Writer Chain:** Preparing the research report...")

            writer_output = writer_chain.invoke({
                "topic": topic,
                "research": reader_output
            })

            writer_output = str(writer_output)

            progress_bar.progress(75)

            # -------------------------------------------------
            # STAGE 4: CRITIC CHAIN
            # -------------------------------------------------

            status.markdown("🧠 **Stage 4/4 — Critic Chain:** Reviewing the report...")

            critic_output = critic_chain.invoke({
                "topic": topic,
                "report": writer_output
            })

            critic_output = str(critic_output)

            progress_bar.progress(100)

            # -------------------------------------------------
            # SAVE RESULTS
            # -------------------------------------------------

            st.session_state.research_data = {
                "topic": topic,
                "search": search_output,
                "reader": reader_output,
                "writer": writer_output,
                "critic": critic_output
            }

            status.success("Research completed successfully!")

        except Exception as e:

            status.error(f"Something went wrong: {str(e)}")

            st.error(
                "The research pipeline could not complete. "
                "Check your API key, rate limits, and terminal output."
            )


# =========================================================
# DISPLAY RESEARCH RESULTS
# =========================================================

if st.session_state.research_data:

    data = st.session_state.research_data

    st.markdown("---")

    st.markdown("""
    <div class="section-label">04 / RESEARCH OUTPUT</div>
    <div class="section-title">Your research report</div>
    <div class="section-description">
        The agents have completed their work. Here is the final output.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-meta">RESEARCH TOPIC</div>
            <div class="result-heading">{data['topic']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # FINAL REPORT
    # -----------------------------------------------------

    st.markdown("""
    <div class="result-box">
        <div class="result-meta">GENERATED BY WRITER CHAIN</div>
        <div class="result-heading">Research Report</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(data["writer"])

    # -----------------------------------------------------
    # CRITIC FEEDBACK
    # -----------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="result-box">
        <div class="result-meta">GENERATED BY CRITIC CHAIN</div>
        <div class="result-heading">Review & Feedback</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(data["critic"])

    # -----------------------------------------------------
    # DOWNLOAD REPORT
    # -----------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    report_markdown = f"""# DEEPRESEARCHER

## Research Topic
{data['topic']}

---

## Research Report

{data['writer']}

---

## Critic Review

{data['critic']}
"""

    st.download_button(
        label="↓  DOWNLOAD RESEARCH REPORT",
        data=report_markdown,
        file_name="deepresearcher_report.md",
        mime="text/markdown"
    )

    # -----------------------------------------------------
    # RAW PIPELINE OUTPUTS
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown("""
    <div class="section-label">05 / PIPELINE DETAILS</div>
    <div class="section-title">Explore agent outputs</div>
    <div class="section-description">
        Inspect the information collected and processed at each stage.
    </div>
    """, unsafe_allow_html=True)

    with st.expander("01 — Search Agent Output"):
        st.write(data["search"])

    with st.expander("02 — Reader Agent Output"):
        st.write(data["reader"])


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div class="footer">
    DEEPRESEARCHER &nbsp; · &nbsp; MULTI-AGENT AI RESEARCH SYSTEM
    <br><br>
    BUILT TO DEMONSTRATE HOW DEEP RESEARCH WORKFLOWS CAN WORK
</div>
""", unsafe_allow_html=True)