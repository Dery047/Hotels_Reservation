const BASE_URL = "http://localhost:8000/api"; // ajusta si tu backend tiene otro path

export async function getFlights() {
  const res = await fetch(`${BASE_URL}/flights/`);
  return res.json();
}

export async function getFlightDetail(id) {
  const res = await fetch(`${BASE_URL}/flights/${id}/`);
  return res.json();
}

export async function createReservation(token, data) {
  const res = await fetch(`${BASE_URL}/reserve/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getMyReservations(token) {
  const res = await fetch(`${BASE_URL}/my-reservations/`, {
    headers: {
      "Authorization": `Bearer ${token}`,
    },
  });
  return res.json();
}

export async function cancelReservation(token, id) {
  const res = await fetch(`${BASE_URL}/cancel/${id}/`, {
    method: "DELETE",
    headers: {
      "Authorization": `Bearer ${token}`,
    },
  });
  return res.ok;
}
