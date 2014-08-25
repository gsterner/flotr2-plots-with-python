import html_page
import jstemplate
import json
import webbrowser
from string import Template

NEWLINE = '\n'
COMMA = ','
PLOT_FILE = "output.html"
DATA_FILE = "data.js"

def write_string_to_file(file_string, file_name):
    out_file = open(file_name,'w')
    out_file.write(file_string)
    out_file.close()

def write_html_to_file(html_file_string):
    write_string_to_file(html_file_string, PLOT_FILE)

def write_data_to_file(data_file_string):
    write_string_to_file(data_file_string, DATA_FILE)

def put_data_into_js_string(plot_list_as_string):
    get_data_function = Template(jstemplate.get_data_function_template)
    return get_data_function.substitute(plot_data_string = plot_list_as_string)

def get_html():
    html = Template(html_page.body_template)
    return html.substitute()

def data_to_flotr_format(x_list, y_list):
    zipped = zip(x_list, y_list)
    return_list = []
    for z in zipped:
        return_list.append(list(z))
    return return_list

def flotr_line_object(data):
    #line_object = {'data':data, 'points':{'show':True}}
    line_object = {'data':data, 'points':{'show':True}}
    plot_list = [line_object]
    return plot_list
