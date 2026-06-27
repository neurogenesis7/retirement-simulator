import numpy as np
import plotly.graph_objects as go


# ----------------------------
# FAN CHART
# ----------------------------

def plot_fan_chart(quantiles_dict):
    """
    quantiles_dict:
        {
            0.01: array,
            0.05: array,
            0.5: array,
            0.95: array,
            0.99: array
        }
    """

    x = np.arange(len(next(iter(quantiles_dict.values()))))

    fig = go.Figure()

    # outer band (1–99)
    if 0.01 in quantiles_dict and 0.99 in quantiles_dict:
        fig.add_trace(go.Scatter(
            x=x,
            y=quantiles_dict[0.99],
            line=dict(width=0),
            showlegend=False,
            name="99%",
        ))

        fig.add_trace(go.Scatter(
            x=x,
            y=quantiles_dict[0.01],
            fill='tonexty',
            fillcolor='rgba(0,100,80,0.1)',
            line=dict(width=0),
            name="1–99%",
        ))

    # inner band (5–95)
    if 0.05 in quantiles_dict and 0.95 in quantiles_dict:
        fig.add_trace(go.Scatter(
            x=x,
            y=quantiles_dict[0.95],
            line=dict(width=0),
            showlegend=False,
            name="95%",
        ))

        fig.add_trace(go.Scatter(
            x=x,
            y=quantiles_dict[0.05],
            fill='tonexty',
            fillcolor='rgba(0,100,80,0.25)',
            line=dict(width=0),
            name="5–95%",
        ))

    # median
    fig.add_trace(go.Scatter(
        x=x,
        y=quantiles_dict[0.5],
        mode='lines',
        name='Median',
        line=dict(color='black', width=2)
    ))

    fig.update_layout(
        title="Retirement Portfolio Fan Chart",
        xaxis_title="Months",
        yaxis_title="Portfolio Value",
        template="plotly_white"
    )

    return fig

def plot_final_distribution(final_values):
    fig = go.Figure()

    fig.add_trace(go.Histogram(
        x=final_values,
        nbinsx=60,
        marker=dict(line=dict(width=0.5))
    ))

    fig.update_layout(
        title="Final Portfolio Distribution",
        xaxis_title="Portfolio Value at End",
        yaxis_title="Frequency",
        template="plotly_white"
    )

    return fig

def plot_survival_curve(results):
    """
    results: (n_sims, time_steps)
    """

    survival = np.mean(results > 0, axis=0)

    x = np.arange(len(survival))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=survival,
        mode='lines',
        line=dict(color='green', width=2),
        name="Survival Probability"
    ))

    fig.update_layout(
        title="Probability of Portfolio Survival Over Time",
        xaxis_title="Months",
        yaxis_title="Survival Probability",
        yaxis=dict(range=[0, 1]),
        template="plotly_white"
    )

    return fig

def retirement_success_indicator(stats_summary):
    """
    Takes summary dict from SimulationStatistics.summary()
    """

    success = stats_summary["retirement_success_rate"]

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=success * 100,
        title={"text": "Retirement Success Probability"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkgreen"},
            "steps": [
                {"range": [0, 50], "color": "red"},
                {"range": [50, 80], "color": "orange"},
                {"range": [80, 100], "color": "green"},
            ],
        }
    ))

    return fig