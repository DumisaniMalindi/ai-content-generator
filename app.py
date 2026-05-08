import streamlit as st
from openai import OpenAI
import os

from prompt import build_prompt

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Content Generator (Groq)",
    layout="centered"
)



st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap');

    /* ✅ Apply robot font ONLY to main app container */
    .stApp h1,
    .stApp h2,
    .stApp h3 {
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 0.5px;
    }

    .stApp p,
    .stApp label,
    .stApp span,
    .stApp input,
    .stApp textarea,
    .stApp button,
    .stApp div[data-baseweb] {
        font-family: 'Orbitron', sans-serif !important;
    }

    /* ✅ Do NOT touch Streamlit menu */
    section[data-testid="stSidebar"],
    header,
    footer {
        font-family: initial !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    :root {
        --neon: #4fc3f7;
    }

    .stApp h1,
    .stApp h2,
    .stApp h3 {
        color: var(--neon) !important;
        text-shadow: 0 0 6px rgba(79, 195, 247, 0.45);
    }

    .stApp button {
        background-color: transparent !important;
        border: 1px solid var(--neon) !important;
        color: var(--neon) !important;
        box-shadow: 0 0 6px rgba(79, 195, 247, 0.35);
        transition: all 0.2s ease-in-out;
    }

    .stApp button:hover {
        background-color: var(--neon) !important;
        color: #0e1117 !important;
        box-shadow: 0 0 14px rgba(79, 195, 247, 0.8);
        transform: translateY(-1px);
    }

    .stApp input:focus,
    .stApp textarea:focus {
        border-color: var(--neon) !important;
        box-shadow: 0 0 8px rgba(79, 195, 247, 0.5) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)




st.title("🧠 PHADEs Content Generator")
st.write("Dumisani Malindi Project")

# -----------------------------
# User inputs
# -----------------------------
content_type = st.selectbox(
    "Content Type",
    [
        "LinkedIn Post",
        "Marketing Copy",
        "Blog Introduction",
        "Email",
        "Product Description"
    ]
)

industry = st.text_input("Industry / Topic", placeholder="e.g. Healthcare")
audience = st.text_input("Target Audience", placeholder="e.g. Founders")

tone = st.selectbox(
    "Tone",
    ["Professional", "Casual", "Persuasive", "Inspirational"]
)

goal = st.text_area(
    "Content Goal",
    placeholder="What should this content achieve?"
)

# -----------------------------
# Generate content
# -----------------------------
# -----------------------------
# Generate content
# -----------------------------
if st.button("Generate Content"):
    if not industry or not audience or not goal:
        st.warning("Please fill in all fields before generating content.")
    else:
        client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)
        prompt = build_prompt(
            content_type=content_type,
            industry=industry,
            audience=audience,
            tone=tone,
            goal=goal
        )


        response = client.responses.create(
    model="llama-3.3-70b-versatile",
    input=prompt
        )


generated_text = response.output[0].content[0].text

st.subheader("✅ Generated Content")
st.markdown(
    f"<div class='ai-output'>{generated_text}</div>",
    unsafe_allow_html=True
)

