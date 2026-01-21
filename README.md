# 🎓 AI Travel Planner

A **Streamlit web app** that helps users plan **budget-friendly, safe, and interest-based travel itineraries**. Powered by Hugging Face LLMs (Llama 3.1 & Qwen 2.5), it generates detailed multi-day travel plans including transport, daily activities, food, accommodation, budget tips, and sources for verification. While optimized for students, it can be used by anyone looking to travel efficiently.

---

## 📝 Project Overview

Planning a trip can be overwhelming, especially when trying to stay within budget and include activities you enjoy. This app uses AI to create personalized itineraries based on your preferences, duration, and budget, making travel planning simple and practical.

---

## 🛠 Features

- **AI-Powered Itinerary Generation**: Uses LLMs to create personalized travel plans.
- **Customizable Options**:
  - Source city & destination
  - Trip duration (1–14 days)
  - Budget range (₹)
  - Interests (Food, History, Nature, Shopping, Adventure)
- **Interactive Map**: View destination on Google Maps directly in the app.
- **Downloadable Itinerary**: Save generated plans as a Markdown file.
- **Multiple Models Support**: Choose between Llama 3.1 8B and Qwen 2.5 7B for itinerary generation.

---

## 💻 Tech Stack

- Python  
- Streamlit (Web App)  
- Requests (API calls)  
- Hugging Face LLMs (Llama 3.1 & Qwen 2.5)  
- Google Maps (embedded map for destinations)

---

## ⚙️ Configuration

- Insert your Hugging Face **API key** in `app.py` (replace `API_KEY`)  
- Ensure an active **internet connection** to use the AI models and map feature  

---

## 📂 Folder Structure

AI_travel_planner/
│
├─ app.py # Main Streamlit app
├─ README.md # Project documentation
├─ requirements.txt # Python dependencies

## 💻 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/student-travel-planner.git
   cd student-travel-planner

2. Install dependencies:

pip install -r requirements.txt

3. Set your Hugging Face API key:
Replace API_KEY in app.py with your Hugging Face token.

## 🚀 Usage

1. Run the Streamlit app:
 streamlit run app.py
2. Open the URL displayed in your terminal (usually http://localhost:8501).
3. Fill in:
 Source & Destination cities
 Trip duration
 Budget range
 Interests
 Select AI model from sidebar
4. Click "Generate My Student Itinerary".
5. View your itinerary, map, and optionally download it as a .md file.

## 🔄 How It Works

1. User enters source and destination cities.
2. Selects trip duration, budget, and interests.
3. Chooses AI model (Llama 3.1 or Qwen 2.5).
4. App sends request to Hugging Face API.
5. AI returns a detailed itinerary including transport, daily activities, food, accommodation, budget tips, and travel references.
6. App displays the itinerary and embedded map; user can download it.

## ⚠️ Limitations / Notes

1. Budget suggestions are indicative; always verify with real travel portals before booking.
2. Response time may vary depending on the selected AI model and internet speed.
3. Map feature requires an active internet connection.
