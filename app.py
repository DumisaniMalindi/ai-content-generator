import streamlit as st
from openai import OpenAI
from prompt import build_prompt

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Content Generator (Groq)",
    layout="centered"
)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap');

    .stApp h1, .stApp h2, .stApp h3 {
        font-family: 'Orbitron', sans-serif;
    }

    .ai-output {
        background: #1c1f26;
        padding: 1rem;
        border-radius: 8px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# App Header
# -----------------------------
st.title("🧠 PHADEs Content Generator")
st.write("Dumisani Malindi Project")

# -----------------------------
# User inputs
# -----------------------------
content_type = st.selectbox(
    "Content Type",
    ["LinkedIn Post", "Marketing Copy", "Blog Introduction", "Email", "Product Description"]
)

industry = st.text_input("Industry / Topic", placeholder="e.g. Healthcare")
audience = st.text_input("Target Audience", placeholder="e.g. Founders")
tone = st.selectbox("Tone", ["Professional", "Casual", "Persuasive", "Inspirational"])
goal = st.text_area("Content Goal", placeholder="What should this content achieve?")

# -----------------------------
# Generate content
# -----------------------------
if st.button("Generate Content", key="generate_btn"):

    if not industry or not audience or not goal:
        st.warning("Please fill in all fields before generating content.")
    else:
        client = OpenAI()  # Uses OPENAI_API_KEY and OPENAI_BASE_URL from secrets

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