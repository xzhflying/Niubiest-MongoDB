<html>
<head>
<title>Result</title>
</head>
<body>
<ul>
%for item in Items:
<li>{{item['STATION_NAME']}} {{item['DATE']}}</li>
%end
</ul>
</body>
</html>