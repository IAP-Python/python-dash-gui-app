from nptdms import TdmsFile
import base64
import datetime
import io
import dash
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State
from dash import dcc, dash_table,  Dash, dcc, html
import dash_bootstrap_components as dbc

# Add Tailwind to make styling less of a hell
# external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

# app = Dash(
#     __name__,
#     external_scripts=external_script,
# )
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, "https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}])


app.layout = html.Div([
    dbc.Container(
        dbc.Alert("Hello Bootstrap and Tailwind!", color="success"),
        className="p-5",
    ),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            dbc.Button("Drag and drop or Click here", color='info', outline=True, className='px-5')
            ]) ,
        className='mx-auto text-center',
        multiple=True
    ),
    html.Div(id='output-data-upload')
])

# Parse stuff
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
              
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

# Debugging an temporary
app.scripts.config.serve_locally = True


if __name__ == '__main__':
    app.run_server(debug=True)
