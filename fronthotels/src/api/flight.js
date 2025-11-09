const BASE_URL = "http://localhost:8000/api";  //locla path

export async function getFlights() { // get list of all flights and return the data in json 
  const res = await fetch(`${BASE_URL}/flights/`);
  return res.json();
}

export async function getFlightDetail(id) {  
  const res = await fetch(`${BASE_URL}/flights/${id}/`);
  return res.json();
}

export async function createReservation(token, data) {  //recibe data y tokens  
  const res = await fetch(`${BASE_URL}/reserve/`, { //http solicitud 
    method: "POST", 
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`, //pasa el token jwt usando bearer 
    },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getMyReservations(token) { //requiere token para obtener los datos de reserva
  const res = await fetch(`${BASE_URL}/my-reservations/`, { //apunta a ruta 
    headers: {
      "Authorization": `Bearer ${token}`, 
    },
  });
  return res.json();
}

export async function cancelReservation(token, id) { //id de reserva es requerido
  const res = await fetch(`${BASE_URL}/cancel/${id}/`, {
    method: "DELETE", //se elimina la reserva
    headers: {
      "Authorization": `Bearer ${token}`,
    },
  });
  return res.ok;
}
