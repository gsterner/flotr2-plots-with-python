body_template="""
<html>
  <head>
    <script type="text/javascript" src="flotr2.min.js"></script>
    <style type="text/css">
      body {
        margin: 0px;
        padding: 0px;
      }
    </style>
  </head>
  <body>
$plot_table
$function_call_tag
  </body>
</html>
"""
container_tag_template="""<div id="${container_id}" style="width : ${width}px; height : ${height}px;"></div>"""

table_template="""
<div style="width: 1300px; height:400px; display: table;">
  ${table_row}
</div>"""

table_row_template="""<div style="display: table-row">
  ${container}
</div>"""


script_tag_template="""<script type="text/javascript">
$script
</script>"""
