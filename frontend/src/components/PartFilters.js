import { useState, useEffect } from 'react';
import api                         from '../api';  // default-импорт

export default function PartFilters({ onChange }) {
  const [manufacturers, setManufacturers] = useState([]);
  const [nodes, setNodes]                 = useState([]);

  useEffect(() => {
    api.get('/manufacturers/')
      .then(res => setManufacturers(res.data))
      .catch(err => console.error(err));
    api.get('/assembly_nodes/')
      .then(res => setNodes(res.data))
      .catch(err => console.error(err));
  }, []);

  // сюда вставьте оставшуюся логику фильтров
  // и вызывайте onChange(новыеФильтры) при изменении
  return (
    <div>
      {/* пример: */}
      <label>Производитель:
        <select onChange={e => onChange(prev => ({ ...prev, manufacturer_id: e.target.value }))}>
          <option value="">Все</option>
          {manufacturers.map(m => (
            <option key={m.id} value={m.id}>{m.name}</option>
          ))}
        </select>
      </label>
      {/* и т.д. */}
    </div>
  );
}
