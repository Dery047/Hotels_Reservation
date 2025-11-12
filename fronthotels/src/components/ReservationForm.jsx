import { useState } from "react";
import { createReservation } from "../api/flights";

export default function ReservationForm({ flightId, token }) {
  const [status, setStatus] = useState("");

  const handleReserve = async () => {
    if (!token) return alert("Debes iniciar sesión");
    const res = await createReservation(token, { flight: flightId });
    setStatus(res.id ? "Reserva creada ✅" : "Error al reservar ❌");
  };

  return (
    <div>
      <button onClick={handleReserve}>Reservar este vuelo</button>
      <p>{status}</p>
    </div>
  );
}
