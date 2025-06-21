// src/pages/OrderPage.jsx
import React from 'react';




{
  items: [
    { part_id: 1, quantity: 2 },
    { part_id: 5, quantity: 1 },
  ]
}



api.post("/orders", { items })
   .then(res => alert(`Заказ №${res.data.id} создан!`))
   .catch(err => console.error(err));

   export default function OrderPage() {
  return (
    <div style={{ padding: 20 }}>
      <h1>Оформление заказа</h1>
      <p>Здесь будет форма создания заказа.</p>
    </div>
  );
}
