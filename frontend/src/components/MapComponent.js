import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const center = [11.1271, 78.6569];

function MapComponent() {
  return (
    <div style={{ height: "420px", borderRadius: "16px", overflow: "hidden", marginTop: "16px" }}>
      <MapContainer center={center} zoom={7} style={{ height: "100%", width: "100%" }}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={center}>
          <Popup>Sample wildlife risk zone</Popup>
        </Marker>
      </MapContainer>
    </div>
  );
}

export default MapComponent;
