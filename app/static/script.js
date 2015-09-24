$(function() {
 var map = new GMaps({
    div: '#map',
    lat: 1.1,
    lng: 2.2
 });

 for (var i = 0; i < coordinates.length; i++) {
        map.addMarker({
          lat: coordinates[i].latitude,
          lng: coordinates[i].longitude,
          infoWindow: {
            content: '<p>' + coordinates[i].notes + '</p>'
          }
        });
      }
});

