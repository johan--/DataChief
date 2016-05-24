
var map, heatmap;
// Blue - positive
gradient1 = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 225, 255, 1)',
    'rgba(0, 200, 255, 1)',
    'rgba(0, 175, 255, 1)',
    'rgba(0, 160, 255, 1)',
    'rgba(0, 145, 223, 1)',
    'rgba(0, 125, 191, 1)',
    'rgba(0, 110, 255, 1)',
    'rgba(0, 100, 255, 1)',
    'rgba(0, 75, 255, 1)',
    'rgba(0, 50, 255, 1)',
    'rgba(0, 25, 255, 1)',
    'rgba(0, 0, 255, 1)'
  ]
// Red - negative
gradient2 = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]


window.onload  = function initMap() {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
    zoom: 5,
    center: {lat: 39.5, lng: -98.35},
    mapTypeId: google.maps.MapTypeId.HYBRID
  });

  heatmapPostive = new google.maps.visualization.HeatmapLayer({
    data: getPositive(),
    map: map
  });
  heatmapNegative = new google.maps.visualization.HeatmapLayer({
    data: getNegative(),
    map: map
  });
    heatmapPostive.setMap(null);
    heatmapNegative.setMap(null);
     heatmapPostive.set('gradient', gradient1);
    heatmapNegative.set('gradient', null);
}

function toggleHeatmap(){
    togglePosHeatmap()
    toggleNegHeatmap()
}
function togglePosHeatmap() {
  heatmapPostive.setMap(heatmapPostive.getMap() ? null : map);
}
function toggleNegHeatmap() {
  heatmapNegative.setMap(heatmapNegative.getMap() ? null : map);
}


function changePosGradient() {
  heatmap.set('gradient', heatmapPostive.get('gradient') ? null : gradient1);
}

function changeNegGradient() {
  heatmap.set('gradient', heatmap2.get('gradient') ? null : gradient2);
}

function changeRadius() {
  heatmap.set('radius', heatmap.get('radius') ? null : 20);
}

function changeOpacity() {
  heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
}

// Heatmap data: 500 Points
function getPositive() {
  return [
    {location: new google.maps.LatLng(38.782551, -122.445368),
    weight: 1.0},
    {location: new google.maps.LatLng(39.782551, -122.445368),
    weight: 0.5},
    {location: new google.maps.LatLng(40.782551, -122.445368),
    weight: 0.5},
  ];
}
function getNegative() {
  return [
    {location: new google.maps.LatLng(37.782551, -124.445368),
    weight: 1.0},
    {location: new google.maps.LatLng(35.782551, -127.445368),
    weight: 0.5},
    {location: new google.maps.LatLng(44.782551, -122.445368),
    weight: 0.5},
  ];
}