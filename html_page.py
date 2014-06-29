top="""
<html>
  <head>
    <style type="text/css">
      body {
        margin: 0px;
        padding: 0px;
      }
      #container {
        width : 600px;
        height: 384px;
        margin: 8px auto;
      }
    </style>
  </head>
  <body>
    <div id="container"></div>
    <!--[if IE]>
    <script type="text/javascript" src="path/to/flashcanvas.js"></script>
    <![endif]-->
    <script type="text/javascript" src="flotr2.min.js"></script>
    <script type="text/javascript">
      (function () {
        var
          container = document.getElementById('container'),
"""

bottom="""
          graph, i;

        // Draw Graph
        graph = Flotr.draw(container, plot_list, {
        });
      })();
    </script>
  </body>
</html>
"""
