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

def get_function_call_tag(plot_list_as_string):
    script_tag = Template(html_page.script_tag_template)
    function_call_js = Template(jstemplate.function_call_template)
    function_call_string = function_call_js.substitute(plot_data_string = plot_list_as_string)
    return script_tag.substitute(script = function_call_string)

def get_div_tag(plot_size_dict):
    div_tag = Template(html_page.div_tag_template)
    return div_tag.substitute(plot_size_dict)

def get_html(plot_size_dict, plot_list_as_string):
    html = Template(html_page.body_template)
    tags = {}
    tags['function_call_tag'] = get_function_call_tag(plot_list_as_string)
    tags['div_tag'] = get_div_tag(plot_size_dict)
    return html.substitute(tags)

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
    if 'r' in property_string:
        line_object['color'] = 'red'
    if 'b' in property_string:
        line_object['color'] = 'blue'
    if 'g' in property_string:
        line_object['color'] = 'green'
    if 'y' in property_string:
        line_object['color'] = 'yellow'
    if 'm' in property_string:
        line_object['color'] = 'magenta'
    if 'c' in property_string:
        line_object['color'] = 'cyan'
    if 'w' in property_string:
        line_object['color'] = 'white'
    if 'k' in property_string:
        line_object['color'] = 'black'
    return line_object

def flotr_line_object(data, property_string):
    line_object = {'data':data}
    line_object = set_line_properties(property_string, line_object)
    return line_object

def make_html_file(plot_info, plot_file):
    plot_list_as_string = json.dumps(plot_info.get_current_line_list())
    html_string = get_html(plot_info.get_plot_size(), plot_list_as_string)
    write_html_to_file(html_string, plot_file)

