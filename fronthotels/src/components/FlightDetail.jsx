import { useEffect, useState } from "react";
import { getFlightDetail } from "../api/flight";

export default function FlightDetail({ flightId }) {
  const [flight, setFlight] = useState(null);

  useEffect(() => {
    if (flightId) getFlightDetail(flightId).then(setFlight);
  }, [flightId]);

  if (!flight) return <p>Select a flight to see details</p>;

  return (
    <div>
      <h3>Flight Details</h3>
      <p>Origin: {flight.origin}</p>
      <p>Destination: {flight.destination}</p>
      <p>Date: {flight.date}</p>
      <p>Price: ${flight.price}</p>
    </div>
  );
}
