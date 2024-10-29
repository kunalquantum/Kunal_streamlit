import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from scipy.fft import fft

# Create a Streamlit app
st.title("Time Series Analysis Techniques")

# Upload a CSV file
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload your time series data (CSV file)", type=["csv"])

if uploaded_file is not None:
    try:
        
            # Separate target and input variables
            target_parameters = st.sidebar.multiselect("Select target parameter(s)", numeric_columns)
            input_variables = [col for col in numeric_columns if col not in target_parameters]

            # Optional input variable selection
            st.sidebar.header("Select Input Variable(s) (Optional)")
            selected_input_variables = st.sidebar.multiselect("Select input variable(s)", input_variables, default=[])

            # Descriptive Analysis
            st.header("Descriptive Analysis")
            st.write("Summary Statistics:")
            st.write(data[target_parameters].describe())

            # Visualize Time Series
            st.subheader("Time Series Plot")
            fig = px.line(data, x=data.index, y=target_parameters, title='Time Series Plot')
            st.plotly_chart(fig)

            # Smoothing
            st.header("Smoothing")
            smoothing_method = st.selectbox("Select Smoothing Method", ["Moving Average", "Exponential Smoothing"])
            if smoothing_method == "Moving Average":
                window = st.slider("Select Window Size", 2, len(data))
                smoothed_data = data[target_parameters].rolling(window=window).mean()
                st.subheader("Smoothed Time Series (Moving Average)")
                fig_smoothed = px.line(data_frame=data, x=data.index, y=target_parameters, title='Smoothed Time Series (Moving Average)')
                fig_smoothed.add_scatter(x=data.index, y=smoothed_data, mode='lines', name='Smoothed Data')
                st.plotly_chart(fig_smoothed)
            elif smoothing_method == "Exponential Smoothing":
                alpha = st.slider("Select Smoothing Parameter (Alpha)", 0.0, 1.0, 0.1)
                smoothed_data = data[target_parameters].ewm(alpha=alpha).mean()
                st.subheader("Smoothed Time Series (Exponential Smoothing)")
                fig_smoothed = px.line(data_frame=data, x=data.index, y=target_parameters, title='Smoothed Time Series (Exponential Smoothing)')
                fig_smoothed.add_scatter(x=data.index, y=smoothed_data, mode='lines', name='Smoothed Data')
                st.plotly_chart(fig_smoothed)

            # Autocorrelation and Cross-correlation
            st.header("Autocorrelation and Cross-correlation")
            st.subheader("Autocorrelation")
            fig_acf, ax_acf = plt.subplots()
            plot_acf(data[target_parameters], lags=40, ax=ax_acf)
            st.pyplot(fig_acf)

            st.subheader("Partial Autocorrelation")
            fig_pacf, ax_pacf = plt.subplots()
            plot_pacf(data[target_parameters], lags=40, ax=ax_pacf)
            st.pyplot(fig_pacf)

            # Additional Analysis (optional, based on selected input variables)
            if selected_input_variables:
                st.header("Correlation Analysis")
                corr_matrix = data[target_parameters + selected_input_variables].corr()
                st.write(corr_matrix)

                # ... other potential analyses using input variables (e.g., regression, feature importance)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Footer and Information
st.sidebar.markdown("---")
st.sidebar.header("About")
st.sidebar.info(
    "This Streamlit app demonstrates various Time Series Analysis Techniques, "
    "including Descriptive Analysis, Smoothing, Autocorrelation, "
    "Cross-correlation, Seasonal Decomposition, Fourier Transforms, and Residual Analysis."
)
st.sidebar.info("Built with Streamlit by Sagittaruis Team")