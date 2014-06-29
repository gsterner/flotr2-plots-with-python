import html_page
import json
import webbrowser

NEWLINE = '\n'
COMMA = ','
PLOT_FILE = "output.html"

def write_html_to_file(html_file_string):
    out_file = open(PLOT_FILE,'w')
    out_file.write(html_file_string)
    out_file.close()

def put_data_into_html_string(plot_list_as_string):
    data_string = "plot_list = " + plot_list_as_string + COMMA + NEWLINE
    html_file_string = html_page.top + data_string + html_page.bottom
    return html_file_string

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
    html_file_string = put_data_into_html_string(plot_list_as_string)
    write_html_to_file(html_file_string)
    webbrowser.open(PLOT_FILE)


x_vals = range(1,10)
y_vals = range(1,10)

plot(x_vals, y_vals)
