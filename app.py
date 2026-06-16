import streamlit as st
import pandas as pd

from utils.data_loader import DataLoader
from utils.eda import EDA
from utils.visualizer import Visualizer
from utils.ai_insights import AIInsights

st.set_page_config(
    page_title="AI Dataset Explorer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Dataset Explorer")
st.subheader("Your Personal Mini Data Scientist")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"],
    key="dataset_upload"
)

if uploaded_file is not None:

    try:
        df = DataLoader.load_csv(uploaded_file)

        st.success("Dataset Uploaded Successfully!")

        # =====================
        # Preview
        # =====================

        st.header("Dataset Preview")
        st.dataframe(df.head(10))

        # =====================
        # Dataset Info
        # =====================

        info = DataLoader.dataset_info(df)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Rows", info["Rows"])
        col2.metric("Columns", info["Columns"])
        col3.metric("Memory (MB)", info["Memory"])
        col4.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

        # =====================
        # EDA
        # =====================

        st.header("Exploratory Data Analysis")

        st.subheader("Data Types")
        st.dataframe(EDA.data_types(df))

        st.subheader("Missing Values")
        st.dataframe(EDA.missing_values(df))

        st.subheader("Numerical Summary")
        st.dataframe(EDA.numerical_summary(df))

        st.subheader("Categorical Summary")
        st.dataframe(EDA.categorical_summary(df))

        st.subheader("Outlier Analysis")
        st.dataframe(EDA.outlier_summary(df))

        # =====================
        # Visualization
        # =====================

        st.header("Visualizations")

        numeric_cols = df.select_dtypes(
            include="number"
        ).columns.tolist()

        categorical_cols = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        if numeric_cols:

            selected_num = st.selectbox(
                "Select Numeric Column",
                numeric_cols
            )

            Visualizer.histogram(
                df,
                selected_num
            )

            Visualizer.boxplot(
                df,
                selected_num
            )

        if len(numeric_cols) >= 2:

            x_col = st.selectbox(
                "X Axis",
                numeric_cols,
                key="x"
            )

            y_col = st.selectbox(
                "Y Axis",
                numeric_cols,
                index=1,
                key="y"
            )

            Visualizer.scatter(
                df,
                x_col,
                y_col
            )

            Visualizer.correlation_heatmap(df)

        if categorical_cols:

            cat_col = st.selectbox(
                "Categorical Column",
                categorical_cols
            )

            Visualizer.pie_chart(
                df,
                cat_col
            )

        # =====================
        # AI Insights
        # =====================

        st.header("AI Insights")

        if st.button("Generate AI Insights"):

            with st.spinner(
                "Generating insights..."
            ):

                insight = AIInsights.generate(
                    df
                )

                st.write(insight)

    except Exception as e:
        st.error(str(e))