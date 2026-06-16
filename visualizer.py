import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff


class Visualizer:

    @staticmethod
    def histogram(df, column):

        fig = px.histogram(
            df,
            x=column,
            title=f"Histogram - {column}"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    @staticmethod
    def boxplot(df, column):

        fig = px.box(
            df,
            y=column,
            title=f"Boxplot - {column}"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    @staticmethod
    def scatter(
        df,
        x_col,
        y_col
    ):

        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            title=f"{x_col} vs {y_col}"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    @staticmethod
    def pie_chart(df, column):

        counts = (
            df[column]
            .value_counts()
            .reset_index()
        )

        counts.columns = [
            column,
            "Count"
        ]

        fig = px.pie(
            counts,
            names=column,
            values="Count",
            title=f"{column} Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    @staticmethod
    def correlation_heatmap(df):

        corr = (
            df.select_dtypes(
                include="number"
            )
            .corr()
        )

        fig = ff.create_annotated_heatmap(
            z=corr.values,
            x=list(corr.columns),
            y=list(corr.index),
            annotation_text=round(
                corr,
                2
            ).values,
            showscale=True
        )

        fig.update_layout(
            title="Correlation Heatmap"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )