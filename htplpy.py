import json
import webbrowser
import html_writer

#PLOT_LIST = []
PLOT_FILE = "output.html"
DATA_FILE = "data.js"


class PlotInfo:
    def __init__(self):
        self._config = (1,1)
        self._current_plot = 0
        self._sub_plots = [[]]

    def append_line_to_current(self, line_object):
        self._sub_plots[self._current_plot].append(line_object)

    def get_current_line_list(self):
        return self._sub_plots[self._current_plot]

plot_info = PlotInfo()

def plot(x_list, y_list, property_string='-'):
    data_list = html_writer.data_to_flotr_format(x_list, y_list)
    line_object = html_writer.flotr_line_object(data_list, property_string)
    plot_info.append_line_to_current(line_object)


def show():
    plot_list = plot_info.get_current_line_list()
    html_writer.make_html_file(plot_list, PLOT_FILE, DATA_FILE)
    webbrowser.open(PLOT_FILE)
