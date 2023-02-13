# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(
    __name__,
    external_scripts=external_script,
)
app.scripts.config.serve_locally = True

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4.2, 1.0, 2.1, 2.32, 4.20, 5.0],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

fruit_count = df.Fruit.count()
total_amt = df.Amount.sum()
city_count = df.City.count()
variables = df.shape[1]

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig1 = px.box(df, x="City", y="Amount", color="City")

app.layout = html.Div(
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H1(children="Dash Tailwindcss Mastery", className=" py-3 text-5xl font-bold text-gray-800"),
                    html.Div(
                        children="""
        Dash with Tailwindcss = 💝 .
    """,
                        className="text-left prose prose-lg text-2xl  py-3 text-gray-600",
                    ),
                ],
                className="w-full mx-14 px-16 shadow-lg bg-white -mt-14 px-6 container my-3 ",
            ),
            html.Div(
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                f"${total_amt}",
                                html.Br(),
                                html.Span("Total Sales", className="text-lg font-bold ml-4"),
                            ],
                            className=" shadow-xl py-4 px-14 text-5xl bg-[#76c893] text-white  font-bold text-gray-800",
                        ),
                        html.Div(
                            children=[
                                fruit_count,
                                html.Br(),
                                html.Span("Fruit Count", className="text-lg font-bold ml-4"),
                            ],
                            className=" shadow-xl py-4 px-24 text-5xl bg-[#1d3557] text-white  font-bold text-gray-800",
                        ),
                        html.Div(
                            children=[
                                variables,
                                html.Br(),
                                html.Span("Variabales", className="inline-flex items-center text-lg font-bold ml-4"),
                            ],
                            className=" shadow-xl py-4 px-24 text-5xl bg-[#646ffa] text-white  font-bold text-gray-800",
                        ),
                        html.Div(
                            children=[
                                city_count,
                                html.Br(),
                                html.Span("City Count", className="text-lg font-bold ml-4"),
                            ],
                            className="w-full shadow-xl py-4 px-24 text-5xl bg-[#ef553b] text-white  font-bold text-gray-800",
                        ),
                    ],
                    className="my-4 w-full grid grid-flow-rows grid-cols-1 lg:grid-cols-4 gap-y-4 lg:gap-[60px]",
                ),
                className="flex max-w-full justify-between items-center ",
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            dcc.Graph(id="example-graph", figure=fig),
                        ],
                        className="shadow-xl w-full border-3 rounded-sm",
                    ),
                    html.Div(
                        children=[
                            dcc.Graph(id="example-graph1", figure=fig1),
                        ],
                        className="w-full shadow-2xl rounded-sm",
                    ),
                ],
                className="grid grid-cols-1 lg:grid-cols-2 gap-4",
            ),
        ],
        className="bg-[#ebeaee]  flex py-14 flex-col items-center justify-center ",
    ),
    className="bg-[#ebeaee] container mx-auto px-14 py-4",
)

if __name__ == "__main__":
    app.run_server(debug=True)