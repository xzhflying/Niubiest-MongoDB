<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
	<style type="text/css">
	body, html,#allmap {width: 100%;height: 90%;margin:0;font-family:"微软雅黑";}
	</style>
	<script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=6l5K2xmDZK0HrYEaIp6ujXtp"></script>
	<title>Find places with condition</title>
</head>
<body>
	<div id="allmap"></div>
	<div>
	<form method="post">
		Place: <select id="station_name" name="station_name" onchange = "center_point();"> 
 		<tr>
 			<option></option>
 		</tr>
 		%for option in PlaceOptions:
 		<tr>
 			<option value={{option['lon_and_lat']}}>{{option['city']}}</option>
 		</tr>
 		%end
 		</select>
 		<br>
		Input distance: <input id="distance" type = "text" name="distance" oninput = "circle();" ><br>
 		Input condition:<br>
 		Date: <input type="text" name="mindate" value=20150101>~<input type="text" name="maxdate" value = 20150220><br>
 		Precipitation: <input type="text" name="minprcp">~<input type="text" name="maxprcp"><br>
 		SnowDepth: <input type="text" name="minsnwd">~<input type="text" name="maxsnwd"><br>
 		Max Temperature: <input type="text" name="mintmax">~<input type="text" name="maxtmax"><br>
 		Min Temperature: <input type="text" name="mintmin">~<input type="text" name="maxtmin"><br>
 		<input type="submit" value="search"><br>
	</form>
	</div>
</body>
</html>

<script type="text/javascript">
	// Baidu map API
	var map = new BMap.Map("allmap");    // Create map instance
	map.centerAndZoom(new BMap.Point(116.404, 39.915), 5); 
	map.addControl(new BMap.MapTypeControl());
	map.enableScrollWheelZoom(true);

	function center_point()
	{
		map.clearOverlays();
		var index = document.getElementById("station_name").selectedIndex
		var city = document.getElementById("station_name").options[index]
		var longitude = city.value.split(",")[1]
		var latitude = city.value.split(",")[0]
		var point = new BMap.Point(longitude,latitude);
		var marker = new BMap.Marker(point);
		map.centerAndZoom(point,5);
		map.addOverlay(marker);
		marker.setAnimation(BMAP_ANIMATION_BOUNCE);
		var sContent ="<h4 style='margin:0 0 5px 0;padding:0.2em 0'>输入框</h4>" + 
	"<textarea></textarea>" + "</div>";
		var infoWindow = new BMap.InfoWindow(sContent);
		marker.addEventListener("click", function(){          
			this.openInfoWindow(infoWindow);
		});
	}
	
	function circle()
	{
		var index = document.getElementById("station_name").selectedIndex
		var city = document.getElementById("station_name").options[index]
		var longitude = city.value.split(",")[1]
		var latitude = city.value.split(",")[0]
		var distance = parseFloat(document.getElementById("distance").value);
		if (longitude && latitude){
			center_point();
			var point = new BMap.Point(longitude,latitude);
			var circle = new BMap.Circle(point,distance,{strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5});
			map.centerAndZoom(point,7);
			map.addOverlay(circle);
		}
	}
	
</script>