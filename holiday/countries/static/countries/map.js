// For basic map display. Used at homepage
var map = L.map('map').setView([1.3521, 103.8198], 11);
var marker = L.marker([1.3521, 103.8198]).addTo(map);
marker.bindPopup("<b>Hello world!</b><br>I am at Singapore.").openPopup();

var popup = L.popup();
function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);



L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);



