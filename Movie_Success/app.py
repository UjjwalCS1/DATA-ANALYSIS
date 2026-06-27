import pickle
from pathlib import Path

import pandas as pd
import streamlit as st


MODEL_PATH = Path("best_model.pkl")
DATA_PATH = Path("movie_success_rate.csv")

GENRE_COLUMNS = [
    "Action",
    "Adventure",
    "Aniimation",
    "Biography",
    "Comedy",
    "Crime",
    "Drama",
    "Family",
    "Fantasy",
    "History",
    "Horror",
    "Music",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Sport",
    "Thriller",
    "War",
    "Western",
]


@st.cache_resource
def load_model():
    with MODEL_PATH.open("rb") as file:
        return pickle.load(file)


@st.cache_data
def load_defaults():
    if not DATA_PATH.exists():
        return {}

    df = pd.read_csv(DATA_PATH)
    numeric_columns = [
        "Year",
        "Runtime (Minutes)",
        "Rating",
        "Votes",
        "Revenue (Millions)",
        "Metascore",
    ]
    return df[numeric_columns].median(numeric_only=True).to_dict()


def build_input_row(model, values, selected_genres):
    feature_columns = list(model.feature_names_in_)
    row = {column: 0 for column in feature_columns}

    for key, value in values.items():
        if key in row:
            row[key] = value

    for genre in selected_genres:
        if genre in row:
            row[genre] = 1

    return pd.DataFrame([row], columns=feature_columns)


st.set_page_config(page_title="Movie Success Predictor", layout="centered")

st.title("Movie Success Predictor")
st.caption("Predict whether a movie is likely to be successful using the saved Random Forest model.")

if not MODEL_PATH.exists():
    st.error("best_model.pkl was not found. Please keep it in the same folder as app.py.")
    st.stop()

model = load_model()
defaults = load_defaults()

with st.form("movie_form"):
    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input(
            "Year",
            min_value=1900,
            max_value=2035,
            value=int(defaults.get("Year", 2016)),
            step=1,
        )
        runtime = st.number_input(
            "Runtime (Minutes)",
            min_value=1,
            max_value=300,
            value=int(defaults.get("Runtime (Minutes)", 110)),
            step=1,
        )
        rating = st.number_input(
            "Rating",
            min_value=0.0,
            max_value=10.0,
            value=float(defaults.get("Rating", 6.5)),
            step=0.1,
        )

    with col2:
        votes = st.number_input(
            "Votes",
            min_value=0,
            value=int(defaults.get("Votes", 100000)),
            step=1000,
        )
        revenue = st.number_input(
            "Revenue (Millions)",
            min_value=0.0,
            value=float(defaults.get("Revenue (Millions)", 40.0)),
            step=1.0,
        )
        metascore = st.number_input(
            "Metascore",
            min_value=0.0,
            max_value=100.0,
            value=float(defaults.get("Metascore", 60.0)),
            step=1.0,
        )

    selected_genres = st.multiselect("Genres", GENRE_COLUMNS)
    submitted = st.form_submit_button("Predict")

if submitted:
    values = {
        "Year": year,
        "Runtime (Minutes)": runtime,
        "Rating": rating,
        "Votes": votes,
        "Revenue (Millions)": revenue,
        "Metascore": metascore,
    }
    input_row = build_input_row(model, values, selected_genres)

    prediction = int(model.predict(input_row)[0])
    probability = float(model.predict_proba(input_row)[0][1])

    if prediction == 1:
        st.success(f"Prediction: Successful movie")
    else:
        st.warning(f"Prediction: Not successful movie")

    st.metric("Success probability", f"{probability * 100:.2f}%")

    with st.expander("Input sent to model"):
        st.dataframe(input_row, use_container_width=True)
