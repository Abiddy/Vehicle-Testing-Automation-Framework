import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import pandas as pd

class VTAFDashboard:
    def __init__(self):
        st.set_page_config(
            page_title="VTAF Dashboard",
            page_icon="🚗",
            layout="wide"
        )
        
    def render_header(self):
        st.title("🚗 Vehicle Testing Automation Framework")
        st.subheader("Real-time Testing Metrics Dashboard")
        
    def render_metrics(self, metrics):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            self.metric_card(
                "Defect Density",
                f"{metrics['defect_density']*100:.1f}%",
                "lower is better",
                "red" if metrics['defect_density'] > 0.2 else "green"
            )
            
        with col2:
            self.metric_card(
                "Test Coverage",
                f"{metrics['test_coverage']:.1f}%",
                "higher is better",
                "green" if metrics['test_coverage'] > 80 else "orange"
            )
            
        with col3:
            self.metric_card(
                "Performance Score",
                f"{metrics['performance_score']:.1f}%",
                "higher is better",
                "green" if metrics['performance_score'] > 80 else "orange"
            )
    
    def metric_card(self, title, value, description, color):
        st.markdown(
            f"""
            <div style="padding: 1rem; border-radius: 0.5rem; background: #1E1E1E; margin-bottom: 1rem;">
                <h3 style="color: #FFFFFF; margin: 0;">{title}</h3>
                <h2 style="color: {color}; margin: 0.5rem 0;">{value}</h2>
                <p style="color: #AAAAAA; margin: 0;">{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def render_protocol_status(self, results):
        st.subheader("Protocol Test Status")
        
        # Create protocol status data
        status_data = []
        for protocol, result in results.items():
            status_data.append({
                'Protocol': protocol,
                'Status': result['status'],
                'Success': 1 if result['status'] == 'success' else 0
            })
        
        df = pd.DataFrame(status_data)
        
        # Create protocol status chart
        fig = go.Figure(data=[
            go.Bar(
                x=df['Protocol'],
                y=df['Success'],
                marker_color=['#00FF00' if x == 1 else '#FF0000' for x in df['Success']],
                text=df['Status'],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            title="Protocol Test Results",
            yaxis_title="Status (1=Success, 0=Failure)",
            template="plotly_dark",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_historical_trends(self, metrics_history):
        st.subheader("Historical Trends")
        
        # Create sample historical data
        df = pd.DataFrame(metrics_history)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['defect_density'], 
                                name="Defect Density", line=dict(color="#FF0000")))
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['test_coverage'], 
                                name="Test Coverage", line=dict(color="#00FF00")))
        fig.add_trace(go.Scatter(x=df['timestamp'], y=df['performance_score'], 
                                name="Performance Score", line=dict(color="#0000FF")))
        
        fig.update_layout(
            title="Metrics Trends Over Time",
            xaxis_title="Time",
            yaxis_title="Score (%)",
            template="plotly_dark",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

def main():
    # Sample data
    metrics = {
        'defect_density': 0.333,
        'test_coverage': 66.67,
        'performance_score': 66.67
    }
    
    results = {
        'CAN': {'status': 'success', 'protocol': 'CAN'},
        'Ethernet': {'status': 'success', 'protocol': 'Ethernet'},
        'MQTT': {'status': 'error', 'protocol': 'MQTT'}
    }
    
    # Sample historical data
    metrics_history = [
        {'timestamp': '2024-03-01', 'defect_density': 40, 'test_coverage': 60, 'performance_score': 65},
        {'timestamp': '2024-03-02', 'defect_density': 35, 'test_coverage': 65, 'performance_score': 70},
        {'timestamp': '2024-03-03', 'defect_density': 33.3, 'test_coverage': 66.67, 'performance_score': 66.67}
    ]
    
    dashboard = VTAFDashboard()
    dashboard.render_header()
    dashboard.render_metrics(metrics)
    dashboard.render_protocol_status(results)
    dashboard.render_historical_trends(metrics_history)

if __name__ == "__main__":
    main() 