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

def plot(x_list, y_list):
    data_list = data_to_flotr_format(x_vals, y_vals)
    plot_list = flotr_line_object(data_list)
    plot_list_as_string = json.dumps(plot_list)    
    js_data_string = put_data_into_js_string(plot_list_as_string)
    html_string = get_html()
    write_html_to_file(html_string)
    write_data_to_file(js_data_string)

def show():
    webbrowser.open(PLOT_FILE)


x_vals = range(1,10)
y_vals = range(1,10)

plot(x_vals, y_vals)
show()
