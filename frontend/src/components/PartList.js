export default function PartList({ parts }) {
  if (!parts.length) {
    return <p>Ничего не найдено.</p>;
  }

  return (
    <table>
      <thead>
        <tr>
          <th>Название</th>
          <th>Производитель</th>
          <th>Узел</th>
          <th>Цена</th>
        </tr>
      </thead>
      <tbody>
        {parts.map(p => (
          <tr key={p.id}>
            <td>{p.name}</td>
            <td>{p.manufacturer.name}</td>
            <td>{p.assembly_node.name}</td>
            <td>{p.price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
