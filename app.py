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


# Create a Dash app
dash_app = dash.Dash(__name__, url_base_pathname="/sale-analyse/")

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
    html.H1("Asrejadid sales analysis", style=custom_font_style),

    # Dropdown for selecting a column
    dcc.Dropdown(
        id='dropdown-column',
        options=[{'label': col, 'value': col} for col in new_df.columns],
        value=new_df.columns[0]  # Set the default value here
    ),

    # Plot to display the selected column
    dcc.Graph(id='bar-plot'),
    dcc.Graph(id='bar-plot1')  # We can add so many plots but with different `id`
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
                 color_continuous_scale=px.colors.sequential.Inferno)
    fig.update_layout(height=600)  # Set height of plot and the width is default value
    tick_label_font_size = 16      # This code set number of size of x labels and x values
    # Set xlabel and their configuration
    fig.update_xaxes(title_text="<b>Branches</b>", title_font=dict(size=18), tickfont=dict(size=tick_label_font_size))
    # Set ylabel and their configuration We don't change the size of y values
    fig.update_yaxes(title_text="<b>Branches score between 0-100</b>", title_font=dict(size=18))
    # Set the title for plot
    fig.update_layout(title=f'<i>distribution of sales in {selected_column} category of each branch</i>',
                      title_font=dict(family='Helvetica, Arial, sans-serif', size=20, color='gray'))
    return fig


if __name__ == '__main__':
    dash_app.run_server(debug=True)


# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
