<html>
<head>
<title>Result</title>
</head>
<body>

<form method="post">
	<input type="submit" value="back"><br>
</form>

<table style="width:100%">
  <tr>
    <td>STATION</td>
    <td>STATION_NAME</td> 
    <td>ELEVATION</td>
    <td>LATITUDE</td>
    <td>LONGITUDE</td>
    <td>DATE</td>
    <td>PRCP</td>
    <td>SNWD</td>
    <td>TMAX</td>
    <td>TMIN</td>
  </tr>
%for item in Items:
<tr>
<td> {{item['STATION']}} </td>
<td> {{item['STATION_NAME']}} </td>
<td> {{item['ELEVATION']}} </td>
<td> {{item['LATITUDE']}} </td>
<td> {{item['LONGITUDE']}} </td>
<td> {{item['DATE']}} </td>
<td> {{item['PRCP']}} </td>
<td> {{item['SNWD']}}</td>
<td> {{float(item['TMAX'])/10}}</td>
<td> {{float(item['TMIN'])/10}}</td>
</tr>
%end

</table>



</body>
</html>