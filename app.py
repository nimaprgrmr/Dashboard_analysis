import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from data_preprocessing import read_data, make_score
from fastapi import FastAPI

path = '2021_sales.csv'
# Sample data
df = read_data(path)
new_df = make_score(df)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Create a Dash app
dash_app = dash.Dash(__name__, url_base_pathname="/sale-analyse/", external_stylesheets=external_stylesheets)

# different values of font-family styles = ['Arial, sans-serif', 'Helvetica, Arial', 'sans-serif', 'Georgia, serif',
#                       'Palatino, serif', 'Times New Roman, serif, 'Courier New, monospace', 'Cursive' or 'fantasy'
#                                          ]
# Define a CSS class for the custom font
custom_font_style = {
    'font-family': 'Helvetica, Arial, sans-serif',
    'font-size': '26px',  # Adjust the font size as needed
    'color': 'Black'  # Adjust the font color as needed
}

values = [range(1, 23)]

# Define the layout of the app
dash_app.layout = html.Div([
    html.Div([
        html.H4(f"Asre jadid sales analysis"),
        # Help Button
        html.Button('Help', id='help-button', n_clicks=0,
                    style={'margin-left': '1100px', 'background-color': 'rgb(13,152,186)', 'color': 'white'}),
    ], style={'display': 'flex', 'align-items': 'center'}),

    # Dropdown for selecting a column
    html.Div([
        dcc.Dropdown(
            id='dropdown-column',
            options=[{'label': col, 'value': col} for col in new_df.columns],
            value=new_df.columns[0],  # Set the default value here
            style={'background-color': 'rgb(230,240,245)'}
        ), ]
    ),

    html.Div([
        dcc.Graph(id='bar-plot'), ], style={'margin-top': '25px'}),
    # dcc.Graph(id='bar-plot1')  # We can add so many plots but with different `id`

    html.Div(id='help-modal', style={'display': 'none'}, children=[
        html.Div([
            html.H4("Dashboard Guide"),
            dcc.Markdown("""
                    This is a guide for using your dashboard.

                    1. Use the dropdowns to select the desired category.
                    2. The y-axis values are between 0 to 100, representing the score of each branch in the category.
                    3. Click on the "Help" button to close this guide.

                    Enjoy using the dashboard!
                """, style={'color': 'white', 'background-color': 'rgba(13,152,186, 0.7)', 'padding': '10px', 'border-radius': '10px'}),
        ], style={'position': 'fixed', 'top': '15%', 'left': '55%', 'transform': 'translate(-26%, -50%)'}),
        html.Div(id='modal-background',
                 style={'position': 'fixed', 'top': 50, 'left': 50, 'width': '100%', 'height': '50%',
                        'background-color': 'rgba(0, 0, 0, 0.5)', 'display': 'none'}),
    ]),
])


# Create a callback to update the plot. This is the relation between the value selected in dropdown-column and bar-plot
@dash_app.callback(
    Output('bar-plot', 'figure'),
    Input('dropdown-column', 'value')
)
# The color_continuous_scale values = [px.colors.sequential.Rainbow,
#                              px.colors.sequential.Viridis, px.colors.sequential.Cividis, px.colors.sequential.Inferno,
#                              px.colors.sequential.Plasma, px.colors.sequential.Magma, px.colors.sequential.CubeYF]
def update_plot(selected_column):
    fig = px.bar(new_df, x=new_df.index, y=selected_column, color=selected_column,
                 color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_traces(hovertemplate='%{y:.3f}')
    fig.update_layout(height=600)  # Set height of plot and the width is default value
    tick_label_font_size = 16  # This code set number of size of x labels and x values
    # Set xlabel and their configuration
    fig.update_xaxes(title_text="Branches", title_font=dict(size=18), tickfont=dict(size=tick_label_font_size))
    # Set ylabel and their configuration We don't change the size of y values
    fig.update_yaxes(title_text="Branches score between 0-100", title_font=dict(size=18))
    # Set the title for plot
    fig.update_layout(title=f'distribution of sales in "{selected_column}" category for each branch',
                      )
    return fig


@dash_app.callback(
    Output('help-modal', 'style'),
    Output('modal-background', 'style'),
    Input('help-button', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_modal(help_clicks):
    if help_clicks is None:
        help_clicks = 0
    if help_clicks % 2 == 1:  # Odd number of clicks on Help or Close button
        return {'display': 'block'}, {'display': 'block'}
    else:
        return {'display': 'none'}, {'display': 'none'}


if __name__ == '__main__':
    dash_app.run_server(debug=True)
