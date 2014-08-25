import json
import webbrowser
import html_writer

PLOT_LIST = []
PLOT_FILE = "output.html"
DATA_FILE = "data.js"


def plot(x_list, y_list):
    data_list = html_writer.data_to_flotr_format(x_list, y_list)
    line_object = html_writer.flotr_line_object(data_list)
    PLOT_LIST.append(line_object)


def show():
    html_writer.make_html_file(PLOT_LIST, PLOT_FILE, DATA_FILE)
    webbrowser.open(PLOT_FILE)
