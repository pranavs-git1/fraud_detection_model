import pandas as pd
import plotly.express as px
import plotly.io as pio


def create_interactive_plot(filepath):
    """Loads data and creates an interactive Plotly HTML file."""

    print(f"Loading data from {filepath} for Plotly report...")
    df = pd.read_csv(filepath)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Convert 'is_fraud' to a categorical string for better plot labels
    df['Status'] = df['is_fraud'].map({0: 'Legitimate', 1: 'Fraud'})

    print("Generating interactive scatter plot...")
    # Create an interactive 3D scatter plot
    # This helps visualize clusters of fraud
    fig = px.scatter_3d(
        df.sample(n=3000),  # Sample to keep the plot fast
        x='amount',
        y='timestamp',
        z='location',
        color='Status',
        color_discrete_map={'Legitimate': 'blue', 'Fraud': 'red'},
        title='Interactive 3D View of Transactions (Sampled)',
        hover_data=['transaction_id', 'device']
    )

    # Set a dark theme
    fig.update_layout(template='plotly_dark')

    # Save to HTML
    output_filename = 'interactive_fraud_report.html'
    pio.write_html(fig, file=output_filename, auto_open=False)

    print(f"\nSuccessfully created interactive report: {output_filename}")
    print("Open this file in your web browser to interact with the plot.")


if __name__ == "__main__":
    create_interactive_plot('transactions.csv')
