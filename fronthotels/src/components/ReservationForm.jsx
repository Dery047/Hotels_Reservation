import { useState } from "react";
import { createReservation } from "../api/flights";

export default function ReservationForm({ flightId, token }) {
  const [status, setStatus] = useState("");

  const handleReserve = async () => {
    if (!token) return alert("You must login first");
    const res = await createReservation(token, { flight: flightId });
    setStatus(res.id ? "Reservation Created" : "Error to create reservation");
  };

  return (
    <div>
      <button onClick={handleReserve}>Reservar este vuelo</button>
      <p>{status}</p>
    </div>
  );
}
