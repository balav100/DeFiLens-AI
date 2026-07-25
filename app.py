import streamlit as st
import ollama

from rag.vector_store import VectorStore
from rag.embeddings import EmbeddingEngine
from rag.retriever import Retriever
from rag.llm import DeFiRiskAnalyzer


def get_available_models():
    try:
        list_resp = ollama.list()
        if hasattr(list_resp, 'models'):
            models = [m.model for m in list_resp.models]
        elif isinstance(list_resp, dict) and 'models' in list_resp:
            models = [m.get('model', m.get('name')) for m in list_resp['models']]
        else:
            models = []
    except Exception:
        models = []

    if not models:
        models = ["gemma3:1b", "llama3:latest", "mistral:latest", "phi:latest", "llama3.1:8b"]
    return models

# --------------------------------------------------

st.set_page_config(
    page_title="DeFiLens AI",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------

@st.cache_resource
def load_pipeline():

    vector_store = VectorStore.load()

    embedding_engine = EmbeddingEngine()

    retriever = Retriever(
        vector_store,
        embedding_engine
    )

    assistant = DeFiRiskAnalyzer(
        retriever
    )

    return assistant

# --------------------------------------------------

assistant = load_pipeline()

# --------------------------------------------------

st.title("🛡️ DeFiLens AI")

st.caption(
    "AI-Powered DeFi Risk Analyzer using Hybrid RAG"
)

st.divider()

question = st.text_input(

    "Ask anything about a DeFi protocol",

    placeholder="Example: Is Aave secure?"

)

with st.sidebar:
    st.header("⚙️ Configuration")

    models = get_available_models()

    default_idx = 0
    if "gemma3:1b" in models:
        default_idx = models.index("gemma3:1b")
    elif "llama3:latest" in models:
        default_idx = models.index("llama3:latest")

    selected_model = st.selectbox(
        "Ollama Model",
        options=models,
        index=default_idx,
        help="Select the local Ollama model to use for analysis."
    )

    st.caption(f"Active model: `{selected_model}`")

    top_k = st.slider(
        "Number of Retrieved Chunks",
        min_value=3,
        max_value=10,
        value=5,
        help="Number of document chunks to retrieve for context."
    )

# --------------------------------------------------

if st.button("Analyze Risk", use_container_width=True):

    if not question.strip():

        st.warning("Please enter a question.")

        st.stop()

    with st.spinner("Analyzing..."):

        assistant.model = selected_model
        result = assistant.ask(
            question,
            top_k
        )

    st.success("Analysis Completed")

    st.divider()

    # --------------------------------------------------

    risk = result["risk_level"].lower()

    if risk == "low":

        st.success(f"Risk Level : {result['risk_level']}")

    elif risk == "medium":

        st.warning(f"Risk Level : {result['risk_level']}")

    elif risk == "high":

        st.error(f"Risk Level : {result['risk_level']}")

    else:

        st.info(f"Risk Level : {result['risk_level']}")

    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Executive Summary")

        st.write(result["summary"])

    with col2:

        st.subheader("Mitigations")

        if result["mitigations"]:

            for item in result["mitigations"]:

                st.markdown(f"- {item}")

        else:

            st.write("No mitigations available.")

    st.divider()

    st.subheader("Potential Risks")

    if result["potential_risks"]:

        for item in result["potential_risks"]:

            st.markdown(f"- {item}")

    else:

        st.write("No risks identified.")

    st.divider()

    st.subheader("Referenced Documents")

    if result["sources"]:

        for source in result["sources"]:

            st.markdown(f"- {source}")

    st.divider()

    with st.expander("Retrieved Chunks"):

        docs = result["retrieved_documents"]

        for doc in docs:

            st.markdown("---")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Similarity",
                doc["similarity_score"]
            )

            c2.metric(
                "Trust Bonus",
                doc["trust_bonus"]
            )

            c3.metric(
                "Final Score",
                doc["final_score"]
            )

            st.write(f"**Type:** {doc['document_type']}")

            st.write(f"**File:** {doc['file']}")

            st.write(f"**Page:** {doc['page']}")

            st.write(doc["text"])

    with st.expander("Retrieved Context"):

        st.code(result["context"])
