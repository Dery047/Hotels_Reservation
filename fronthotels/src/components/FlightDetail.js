import { useEffect, useState } from "react";
import { getFlightDetail } from "../api/flight";

export default function FlightDetail({ flightId }) {
  const [flight, setFlight] = useState(null);

  useEffect(() => {
    if (flightId) getFlightDetail(flightId).then(setFlight);
  }, [flightId]);

  if (!flight) return <p>Selecciona un vuelo para ver detalles.</p>;

  return (
    <div>
      <h3>Detalles del vuelo</h3>
      <p>Origen: {flight.origin}</p>
      <p>Destino: {flight.destination}</p>
      <p>Fecha: {flight.date}</p>
      <p>Precio: ${flight.price}</p>
    </div>
  );
}
