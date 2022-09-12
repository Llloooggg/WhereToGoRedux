<template>
  <l-map :zoom="zoom" :center="center" style='width: 80vw'>
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <l-marker :lat-lng="markerLatLng"></l-marker>
  </l-map>
</template>


<script>

import "leaflet/dist/leaflet.css"
import { LMap, LTileLayer, LMarker } from "@vue-leaflet/vue-leaflet";

export default {
  name: "MapPage",
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [51.505, -0.159],
      markerLatLng: [51.504, -0.159],
    };
  },
};
</script>
