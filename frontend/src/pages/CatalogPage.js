import { useState, useEffect } from 'react';
import PartFilters from '../components/PartFilters';
import PartList    from '../components/PartList';
// импортируем default-экспорт из api/index.js
import api         from '../api';

export default function CatalogPage() {
  const [filters, setFilters] = useState({});
  const [parts, setParts]     = useState([]);

  useEffect(() => {
    api.get('/parts/', { params: filters })
      .then(res => setParts(res.data))
      .catch(err => console.error(err));
  }, [filters]);

  return (
    <div style={{ padding: 20 }}>
      <h1>Каталог запчастей</h1>
      <PartFilters onChange={setFilters} />
      <PartList parts={parts} />
    </div>
  );
}
