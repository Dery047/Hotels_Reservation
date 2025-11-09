import { useEffect, useState } from "react";
import { getFlights } from "../api/flights";

export default function FlightList({ onSelect }) {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    getFlights().then(setFlights);
  }, []);

  return (
    <div>
      <h2>Vuelos disponibles</h2>
      <ul>
        {flights.map(f => (
          <li key={f.id} onClick={() => onSelect(f.id)}>
            ✈️ {f.origin} → {f.destination} ({f.date})
          </li>
        ))}
      </ul>
    </div>
  );
}
