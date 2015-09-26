function initialize() {
        var mapCanvas = document.getElementById('map');
        var mapOptions = {
          center: new google.maps.LatLng(39.952219, -75.193214),
          zoom: 8,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        }
         map = new google.maps.Map(mapCanvas, mapOptions)

    for (var c = 0; c < coordinates.length; c++) {
       console.log(
       coordinates[c].latitude)
       lat = coordinates[c].latitude;
       lon = coordinates[c].longitude;
       notes = coordinates[c].notes
       var counterwindow = c
       var counterwindow = new google.maps.InfoWindow({
        content: '<p>'+notes+'</p>'
       })
       var marker = c
          var marker = new google.maps.Marker({
            position : {lat: lat,lng: lon},
            map : map,
            title : notes
          });
          marker.addListener('click', function() {
             counterwindow.open(map, marker);
          });
        }
      }

      google.maps.event.addDomListener(window, 'load', initialize);

   