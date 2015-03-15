<html>
<head>
<title>Result</title>
</head>
<body>
<form method="post">
	<input type="submit" value="back"><br>
</form>
<ul>
	%for item in Items:
	<li>{{item['STATION_NAME']}} {{item['DATE']}}</li>
%end
</ul>
</body>
</html>