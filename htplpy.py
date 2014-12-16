import json
import webbrowser
import html_writer

PLOT_FILE = "output.html"

class PlotInfo:
    def __init__(self):
        self._config = (1,1)
        self._current_plot = 0
        self._sub_plots = [[]]
        self.plot_size = {'width': 600, 'height' : 400}

    def append_line_to_current(self, line_object):
        self._sub_plots[self._current_plot].append(line_object)

    def get_current_line_list(self):
        return self._sub_plots[self._current_plot]

    def get_plot_size(self):
        return self.plot_size

plot_info = PlotInfo()

def plot(x_list, y_list, property_string='-'):
    data_list = html_writer.data_to_flotr_format(x_list, y_list)
    line_object = html_writer.flotr_line_object(data_list, property_string)
    plot_info.append_line_to_current(line_object)


def show():
    html_writer.make_html_file(plot_info, PLOT_FILE)
    webbrowser.open(PLOT_FILE)
