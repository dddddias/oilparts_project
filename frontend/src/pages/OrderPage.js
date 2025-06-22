import React from 'react';
import api from '../api';

export default function OrderPage() {
  const handleCreateOrder = () => {
    const items = [
      { part_id: 1, quantity: 2 },
      { part_id: 5, quantity: 1 },
    ];

 api.post('/orders', { items })
       .then(res => alert(`Заказ №${res.data.id} создан!`))
       .catch(err => console.error(err));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Оформление заказа</h1>
       <button onClick={handleCreateOrder}>Создать тестовый заказ</button>
    </div>
  );
}
