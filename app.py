import streamlit as st
import requests
import time

# --- CONFIGURATION ---
import os
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not API_KEY:
    st.error("Hugging Face API key not found. Please set it in Streamlit Secrets.")
    st.stop()


MODELS = {
    "Llama 3.1 8B (Recommended)": "meta-llama/Llama-3.1-8B-Instruct",
    "Qwen 2.5 7B (Reliable)": "Qwen/Qwen2.5-7B-Instruct"
}

# --- HELPER FUNCTIONS ---
def query_llm(prompt, model_id):
    api_url = "https://router.huggingface.co/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "system",
                "content": "You are a professional Student Travel Guide. Provide budget-friendly, safe, and practical travel advice specifically for university students. You must always include a clearly labeled 'TRAVEL SOURCES & REFERENCES' section at the very end of your response detailing actual travel portals or forums used for the information."
            },
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1500,
        "temperature": 0.7,
        "stream": False
    }

    for delay in [1, 2, 4, 8]:
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            elif response.status_code in [503, 429, 504]:
                time.sleep(delay)
                continue
            else:
                return f"Error {response.status_code}: {response.text}"
        except Exception:
            time.sleep(delay)

    return "The AI service is currently busy. Please try again in a few moments."


# --- MAP INTEGRATION ADDED ---
def show_map(destination):
    map_url = f"https://www.google.com/maps?q={destination}&output=embed"
    st.markdown(
        f"""
        <iframe
            width="100%"
            height="450"
            style="border:0; border-radius:12px; margin-top:20px;"
            loading="lazy"
            allowfullscreen
            src="{map_url}">
        </iframe>
        """,
        unsafe_allow_html=True
    )


# --- UI DESIGN ---
def main():
    st.set_page_config(page_title="AI Student Travel Planner", page_icon="✈️", layout="centered")

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.55), rgba(255, 255, 255, 0.55)),
                    url('https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .stApp, .stApp p, .stApp span, .stApp label, .stMarkdown {
        color: #000000 !important;
        font-size: 1.1rem !important;
    }

    .main .block-container {
        background-color: rgba(255, 255, 255, 0.88);
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    h1 { font-size: 2.5rem !important; font-weight: 800; }
    h2, h3 { font-size: 1.8rem !important; font-weight: 800; }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        background-color: #4A90E2;
        color: white !important;
        font-weight: bold;
        font-size: 1.1rem !important;
        border: none;
    }

    .itinerary-box {
        background-color: white;
        padding: 30px;
        border-radius: 12px;
        border-left: 8px solid #4A90E2;
        margin-top: 20px;
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎓 Student AI Travel Planner")
    st.write("Plan your student adventure with departure routes and budget ranges (₹).")

    with st.sidebar:
        st.header("⚙️ Settings")
        selected_model_name = st.selectbox("Select AI Model", list(MODELS.keys()))
        selected_model_id = MODELS[selected_model_name]

    col1, col2 = st.columns(2)
    with col1:
        source_city = st.text_input("Source (Starting Point)")
    with col2:
        destination = st.text_input("Destination")

    duration = st.slider("Duration (Days)", 1, 14, 3)

    min_budget = st.number_input("Min Budget (₹)", value=5000)
    max_budget = st.number_input("Max Budget (₹)", value=15000)

    interests = st.multiselect(
        "Interests",
        ["Food & Cafes", "History & Culture", "Nature", "Shopping", "Adventure"]
    )

    if st.button("Generate My Student Itinerary"):
        if not source_city or not destination:
            st.warning("Enter both source and destination")
        else:
            prompt = (
                f"Create a detailed {duration}-day student itinerary from {source_city} to {destination}. "
                f"Budget ₹{min_budget}–₹{max_budget}. Interests: {', '.join(interests)}. "
                f"Include transport, daily plan, food, budget tips, hostels, and sources."
            )

            with st.spinner("Planning your trip..."):
                result = query_llm(prompt, selected_model_id)

            st.subheader(f"📍 Trip: {source_city} ➜ {destination}")
            st.markdown(f'<div class="itinerary-box">{result}</div>', unsafe_allow_html=True)

            # --- MAP DISPLAY ADDED ---
            st.subheader("🗺️ Destination Map")
            show_map(destination)

            st.download_button(
                "Download Itinerary",
                result,
                file_name=f"{destination}_itinerary.md"
            )


if __name__ == "__main__":
    main()
