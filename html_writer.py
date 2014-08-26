import html_page
import jstemplate
import json
import webbrowser
from string import Template

NEWLINE = '\n'
COMMA = ','

def write_string_to_file(file_string, file_name):
    out_file = open(file_name,'w')
    out_file.write(file_string)
    out_file.close()

def write_html_to_file(html_file_string, plot_file):
    write_string_to_file(html_file_string, plot_file)

def write_data_to_file(data_file_string, plot_list):
    write_string_to_file(data_file_string, plot_list)

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

def set_line_properties(property_string, line_object):
    if 'o' in property_string:
        line_object['points'] = {'show':True}
    if '-' in property_string:
        line_object['lines'] = {'show':True}
    return line_object

def flotr_line_object(data, property_string):
    line_object = {'data':data}
    line_object = set_line_properties(property_string, line_object)
    return line_object

def make_html_file(plot_data_json, plot_file, data_file):
    plot_list_as_string = json.dumps(plot_data_json)
    js_data_string = put_data_into_js_string(plot_list_as_string)
    html_string = get_html()
    write_html_to_file(html_string, plot_file)
    write_data_to_file(js_data_string, data_file)
