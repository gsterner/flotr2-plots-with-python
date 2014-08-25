import json
import webbrowser
import html_writer


def plot(x_list, y_list):
    data_list = html_writer.data_to_flotr_format(x_list, y_list)
    plot_list = html_writer.flotr_line_object(data_list)
    plot_list_as_string = json.dumps(plot_list)    
    js_data_string = html_writer.put_data_into_js_string(plot_list_as_string)
    html_string = html_writer.get_html()
    html_writer.write_html_to_file(html_string)
    html_writer.write_data_to_file(js_data_string)

def show():
    webbrowser.open(html_writer.PLOT_FILE)
