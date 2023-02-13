import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

app = dash.Dash(external_stylesheets=[dbc.themes.COSMO, dbc.icons.BOOTSTRAP])

LOGO = "https://upload.wikimedia.org/wikipedia/commons/b/ba/TexasInstruments-Logo.svg"

navbar = dbc.Navbar(

        [
            html.A(
                dbc.Row([
                    dbc.Col(html.Img(src=LOGO, height="50px")),
                ])
            ),

            dbc.NavItem(children=[
                dbc.DropdownMenu(children=[
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ], label="...")
            ]),
            "File"
        ]

)

alerts = html.Div(
    [
        dbc.Alert(
            [
                html.I(className="bi bi-info-circle-fill me-2"),
                "An example info alert with an icon",
            ],
            color="info",
            className="d-flex align-items-center",
        ),
        dbc.Alert(
            [
                html.I(className="bi bi-check-circle-fill me-2"),
                "An example success alert with an icon",
            ],
            color="success",
            className="d-flex align-items-center",
        ),
        dbc.Alert(
            [
                html.I(className="bi bi-exclamation-triangle-fill me-2"),
                "An example warning alert with an icon",
            ],
            color="warning",
            className="d-flex align-items-center",
        ),
        dbc.Alert(
            [
                html.I(className="bi bi-x-octagon-fill me-2"),
                "An example danger alert with an icon",
            ],
            color="danger",
            className="d-flex align-items-center",
        ),
    ]
)
app.layout = html.Div(alerts)

# Debugging an temporary
app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True)
