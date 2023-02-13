import pydoc
from nptdms import TdmsFile
import base64
import datetime
import dash
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table,  Dash, html, dcc
import time
import timeit
import numpy as np



# Add Tailwind to make styling less of a hell
# external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

# app = Dash(
#     __name__,
#     external_scripts=external_script,
# )
# app.scripts.config.serve_locally = True

# app.layout = html.Div([
#     dcc.Upload(
#         id='upload-data',
#         children=html.Div([
#             'Drag and Drop or ',
#             html.A('Select Files')
#         ]),
#         style={
#             'width': '100%',
#             'height': '60px',
#             'lineHeight': '60px',
#             'borderWidth': '1px',
#             'borderStyle': 'dashed',
#             'borderRadius': '5px',
#             'textAlign': 'center',
#             'margin': '10px'
#         },
#         # Allow multiple files to be uploaded
#         multiple=True
#     ),
#     html.Div(id='output-data-upload'),
# ])


# # Loads a file of .tdms, which is what TI uses.
# def load_data(path: str):
#     if not path.endswith('.tdms'):
#         raise Exception("Data is not a labview data nor a CSV file")

#     if path.endswith('.tdms'):
#         with TdmsFile.open(path) as data_file:
#             data = data_file
#             data_groups = data_file.groups()  # get the group names
#             # data_file.close()
#         return ({
#             "tdms": data,
#             "group": data_groups
#         })
#     else:
#         # Loading the csv into a dataframe or something
#         return pd.read_csv(path)



# # Process input data
# def parse_contents(contents, filename, date):
#     content_type, content_string = contents.split(',')

#     decoded = base64.b64decode(content_string)
#     df = load_data(filename)
#     df['tdms']

#     return html.Div([
#         html.H5(filename),
#         html.H6(datetime.datetime.fromtimestamp(date)),

#         dash_table.DataTable(
#             # df.to_dict('records'),
#             # [{'name': i, 'id': i} for i in df.columns]
#             df
#         ),

#         html.Hr(),  # horizontal line

#         # For debugging, display the raw contents provided by the web browser
#         html.Div('Raw Content'),
#         html.Pre(contents[0:200] + '...', style={
#             'whiteSpace': 'pre-wrap',
#             'wordBreak': 'break-all'
#         })
#     ])



# @app.callback(Output('output-data-upload', 'children'),
#               Input('upload-data', 'contents'),
#               State('upload-data', 'filename'),
#               State('upload-data', 'last_modified'))
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children

# # print(load_data("data/Rad Test_TPS7H4010-SEP(Run-22)21_01_10.tdms")['group'])



if __name__ == '__main__':
    # t0 = time.process_time()
    # app.run_server(debug=True)
    # a = load_data("data/Rad Test_TPS7H4010-SEP(Run-22)21_01_10.tdms")
    # print("TDMS")
    # for i in a["tdms"]:
    #     print(i)
    # print("GROUP")
    # for i in a["tdms"]:
    #     print(i)
    # group = a["group"][3]
    # print(group)
    

    # tdms_file = TdmsFile.open("data/Rad Test_TPS7H4010-SEP(Run-22)21_01_10.tdms")
    # print(tdms_file.groups().pop().name)
    t0 = time.time()

    # Example of accessing a specific group and a specific channel within the group
    with TdmsFile.open("data/Rad Test_TPS7H4010-SEP(Run-22)21_01_10.tdms") as tdms_file:
        data = tdms_file

        groups = np.asarray(data.groups())
        print(len(groups))
        
        group_names = np.asarray( np.char.split(i.name, "_") for i in groups])
        print(group_names)
    t1 = time.time()
    print(t1-t0)
    

        # for i in groups:
        #     print( i.name)



        # print(data.groups())

        # You can't go outside the with statement, else you won't be able to access the channels of each group
        # data[group_name][channel][:range:range+n]
        # print(data["Beam1_SCOPE4-5172_13"]["VOUT4"][0:30])
        # print(data["Beam1_SCOPE4-5172_13"]["VOUT4"][:]) # All results of VOUT of SCOPE4 TEST 13
        # for i, y in zip(data.groups()[0]['Relative Time (ThermoCouple)'], data.groups()[0]['PVIN3 (A)']):
        #     print(i, "   ",  y)
        # print("\n\n")
        

        # print(data.groups()[0].channels()[1][:])

        # t1 = time.process_time()
        # print("Process time in CPU is ", abs(t0 - t1), "seconds")
        # print(data.groups()[0:3])
        # t1 = time.time()
        # print(abs(t0 - t1))
        # print(data.groups()[-1])
        # t0 = time.time()
        # print(abs(t0 - t1))




"""

"""