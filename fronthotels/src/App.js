import { useState } from "react";
import FlightList from "./components/FlightList";
import FlightDetail from "./components/FlightDetail";
import ReservationForm from "./components/ReservationForm";
import MyReservations from "./components/MyReservations";
import "./App.css";

export default function App() {
  const [selectedFlight, setSelectedFlight] = useState(null);
  const [token] = useState("AQUI_TU_TOKEN_JWT_O_DE_PRUEBA");

  return (
    <div className="App">
      <h1>🛫 Sistema de Reservas de Vuelos</h1>
      <FlightList onSelect={setSelectedFlight} />
      <FlightDetail flightId={selectedFlight} />
      {selectedFlight && <ReservationForm flightId={selectedFlight} token={token} />}
      <MyReservations token={token} />
    </div>
  );
}
