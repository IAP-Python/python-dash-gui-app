from dash.dependencies import Input, Output, State
from dash import dcc, dash_table,  Dash, dcc, html
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
import pandas as pd

# TODOs LIST
# TODO Design better test files
# TODO Design Figma file layout 
# TODO Add TI color pallete (done)

theme = {
    "dark":   False,
    "red":    "#D92832",
    "gray-1": "#787878",
    "gray-2": "#454545",
    "gray-3": "#DCDCDC",
    "black":  "#000000"
}

font_title = "Roboto, Arial, Helvetica, sans-serif"
font_normal = "Inter, Arial, Helvetica, sans-serif"


TEST_PLZ = np.array(["SCOPE 4", "SCOPE 3", "SCOPE 8"])
TEST_PLZ_2 = np.array(["5172", "5162", "0555"])


def random_data_generator(num_samples, x_range, y_range):
    x = np.arange(x_range[0], x_range[1])
    # x = np.random.uniform(x_range[0], x_range[1], num_samples)
    y = np.random.randint(y_range[0], y_range[1], num_samples)
    print(y)
    # y = np.random.uniform(y_range[0], y_range[1], num_samples)
    data = np.column_stack((x, y))
    df = pd.DataFrame(data, columns=['X', 'Y'])
    return df


TEST_PLZ_3 = random_data_generator(100, [0, 100], [0, 100])





def __parse_to_labels__(n, nval=None):
    if nval == None:
        return {'label': n, 'value': n}
    return {'label': n, 'value': nval}
    
parse_to_labels = np.vectorize(__parse_to_labels__)


# TODO: Finish this graph component
def signal_graph_component(n, signal_id="scope-graph"):
    graph = dcc.Graph(
        id=signal_id,
        className="scope",


    )
    return graph


def upload_component():
    upload = html.Div([
        dcc.Upload(
            id='upload-data',
            multiple=True,
            children=html.Div([
                dbc.Button(
                    "Drag and drop or Click here", 
                    color='info', 
                    outline=True
            )])
        )
    ])
    return upload


def parse_to_label_components(data: np.array):
    tab_counter = -1
    def __foo__(n):
        nonlocal tab_counter
        tab_counter +=1
        return {'label': n, 'value': tab_counter}
    foo = np.vectorize(__foo__)

    return foo(data)

def tab_component(data:np.array=None, data_id:str='tabs'):
    
    tabs = parse_to_label_components(data)
    print(tabs)
    button_group = html.Div([
            dbc.RadioItems(
                id="radios",
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=tabs,
                value=1, # Always pick the first one :D
            ),
            html.Div(id="output"),
        ],
        className="radio-group",)
    return button_group


def drop_down_component(data:np.array=None, data_id:str='select', data_placeholder="Epic Placeholder"):
    labels = parse_to_labels(data)
    selection = dbc.Select(
        name= "selection-"+data_id,
        id=data_id,
        options=labels,
        size="lg", 
        className="mb-3",
        placeholder=data_placeholder,
    )
    return selection

def main_layout() -> html.Div:
    top_side = html.Div([
        html.Img(src="/src/images/tilogo.png"),
        html.H3("DucoFire", className=" my-3", style={"padding-top":"1.25rem"}),
        
    ])

    scope_selector = [
        dbc.CardHeader("Scope"),
        dbc.CardBody(drop_down_component(TEST_PLZ_2, "scope"))
    ]

    signal_selector = [
        dbc.CardHeader("signal"),
        dbc.CardBody(drop_down_component(TEST_PLZ_2, "signal"))
    ]

    offset_selector = [
        dbc.CardHeader("offset"),
        dbc.CardBody(drop_down_component(TEST_PLZ_2, "offset"))
    ]

    x_axis = [
        dbc.CardHeader("X-axis"),
        dbc.CardBody(drop_down_component(TEST_PLZ_2, "x-axis"))
    ]

    y_axis = [
        dbc.CardHeader("Y-axis"),
        dbc.CardBody(drop_down_component(TEST_PLZ_2, "y-axis"))
    ]

    tabs = dbc.Tabs([
        # This is auto-generated but ok
        dbc.Tab(
            label="SET",
            activeTabClassName="fw-bold fst-italic",
            label_class_name="fs-4"
        ),
        dbc.Tab(
            label="SEL",
            activeTabClassName="fw-bold fst-italic",
            label_class_name="fs-4"
        )
    ])

    row_1 = dbc.Row([
        dbc.Col(dbc.Card(scope_selector, color="primary", outline=True)),
        dbc.Col(dbc.Card(signal_selector, color="secondary")),
        dbc.Col(dbc.Card(offset_selector, color="terciary"))
    ], className="mb-4",)

    row_2 = dbc.Row([
        dbc.Col(dbc.Card(x_axis)),
        dbc.Col(dbc.Card(y_axis))
    ], className="mb-4",)
    
    # Move this to some function or something idk 
    fig = go.Figure(
        data=[
            go.Line(

                x=TEST_PLZ_3['X'],
                y=TEST_PLZ_3['Y'],
                opacity=0.8,
                line_shape='spline'
            )]
    )

    # className="w-100"

    body_side = dbc.Container(dbc.Row([
        dbc.Col(dbc.Row([
            row_1, row_2
        ]), className="align-self-center"),
        dbc.Col(dbc.Row([
            dcc.Graph(id="graph-basic-2", figure=fig, clear_on_unhover=True),
            dcc.Graph(id="graph-basic-3", figure=fig, clear_on_unhover=True)
        ]))
    ]), className="mw-100")

    main_div = html.Div([
        top_side,
        dbc.Card([
            dbc.CardHeader(tabs),
            dbc.CardBody(body_side)
        ],)
    ])
    return main_div

def main():
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.ZEPHYR , dbc.icons.FONT_AWESOME, "https://tailwindcss.com/"])
    app.title = "Ducofire"

    app.layout = main_layout()


    return app

if __name__ == '__main__':
    main().run_server(debug=True)
    