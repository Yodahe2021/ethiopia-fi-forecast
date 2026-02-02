import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- Page Config ---
st.set_page_config(page_title="Ethiopia FI Forecast", layout="wide")

# --- Load Data ---
@st.cache_data
def load_all_data():
    hist_df = pd.read_csv('data/processed/ethiopia_fi_enriched.csv')
    forecast_df = pd.read_csv('data/processed/ethiopia_fi_forecast_2027.csv')
    weights_df = pd.read_csv('data/processed/calibrated_impact_weights.csv', index_col=0)
    return hist_df, forecast_df, weights_df

try:
    hist_df, forecast_df, weights_df = load_all_data()
except Exception as e:
    st.error(f"Please ensure all data files are in data/processed/. Error: {e}")
    st.stop()

# --- Sidebar ---
st.sidebar.title("Selam Analytics")
st.sidebar.image("https://img.icons8.com/fluency/96/000000/financial-growth_analysis.png")
page = st.sidebar.selectbox("Navigate", ["Overview", "Trends Analysis", "2027 Forecasts"])

# --- PAGE: OVERVIEW ---
if page == "Overview":
    st.title("Ethiopia Digital Financial Transformation")
    st.markdown("### Tracking progress toward the 60% National Financial Inclusion Target")
    
    # Key Metrics
    col1, col2, col3 = st.columns(3)
    latest_acc = forecast_df.iloc[0]['Access (%)']
    proj_acc = forecast_df.iloc[-1]['Access (%)']
    latest_usg = forecast_df.iloc[0]['Usage (%)']
    proj_usg = forecast_df.iloc[-1]['Usage (%)']
    
    col1.metric("Current Access (2024)", f"{latest_acc}%", "+3% vs 2021")
    col2.metric("Projected Access (2027)", f"{proj_acc}%", f"{proj_acc - latest_acc}% growth")
    col3.metric("Projected Usage (2027)", f"{proj_usg}%", f"{proj_usg - latest_usg}% growth")

    st.divider()
    
    st.subheader("The P2P/ATM Crossover Ratio")
    st.info("A ratio > 1.0 indicates that digital transfers have surpassed cash withdrawals.")
    # Assuming USG_CROSSOVER exists in your data
    crossover_val = hist_df[hist_df['indicator_code'] == 'USG_CROSSOVER']['value_numeric'].max()
    st.write(f"### Current Ratio: **{crossover_val}**")
    st.progress(min(crossover_val/2, 1.0))

# --- PAGE: TRENDS ---
elif page == "Trends Analysis":
    st.title("Historical Trend Analysis")
    
    indicator = st.selectbox("Select Indicator", hist_df['indicator_code'].unique())
    sub_df = hist_df[hist_df['indicator_code'] == indicator].sort_values('observation_date')
    
    fig = px.line(sub_df, x='observation_date', y='value_numeric', markers=True, 
                  title=f"Trend for {indicator}")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Event Impact Weights")
    st.write("These calibrated weights drive our forecast model:")
    st.dataframe(weights_df.style.background_gradient(cmap='RdYlGn'))

# --- PAGE: FORECASTS ---
elif page == "2027 Forecasts":
    st.title("Scenario Projections: 2025 - 2027")
    
    # Forecast Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast_df['Year'], y=forecast_df['Access (%)'], name="Access (Forecast)", line=dict(width=4)))
    fig.add_trace(go.Scatter(x=forecast_df['Year'], y=forecast_df['Usage (%)'], name="Usage (Forecast)", line=dict(dash='dash', width=4)))
    fig.add_hline(y=60, line_dash="dot", line_color="green", annotation_text="60% Target")
    
    fig.update_layout(template="plotly_white", yaxis_title="Percentage (%)")
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("### Analysis: Ethiopia is on track to exceed the 60% Access target. The primary challenge remains closing the Usage gap through interoperable P2P systems.")