get_data_function_template = """function getPlotList()
{
var plot_list = $plot_data_string;
    return plot_list;
}"""

function_call_template = """      (function () {
        var
          container = document.getElementById('container'),
          plot_list = getPlotList(),
          graph, i;

        // Draw Graph
        graph = Flotr.draw(container, plot_list, {
        });
      })();"""
