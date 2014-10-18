body_template="""
<html>
  <head>
    <script type="text/javascript" src="flotr2.min.js"></script>
    <script type="text/javascript" src="data.js"></script>
    <style type="text/css">
      body {
        margin: 0px;
        padding: 0px;
      }
    </style>
  </head>
  <body>
$div_tag
$function_call_tag
  </body>
</html>
"""
div_tag_template="""<div id="container" style="width : ${width}px; height : ${height}px;"></div>"""

script_tag_template="""<script type="text/javascript">
$script
</script>"""
