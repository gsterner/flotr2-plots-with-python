function_call_template = """      (function () {
        var
          container = document.getElementById('container'),
          plot_list = $plot_data_string,
          graph, i;

        // Draw Graph
        graph = Flotr.draw(container, plot_list, {
        });
      })();"""
