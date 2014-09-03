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
      #container {
        width : 600px;
        height: 384px;
        margin: 8px auto;
      }
    </style>
  </head>
  <body>
    <div id="container">
$function_call_tag
    </div>
  </body>
</html>
"""

script_tag_template="""<script type="text/javascript">
$script
</script>"""
