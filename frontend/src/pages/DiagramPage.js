// src/pages/DiagramPage.js
import HotspotMap from '../components/HotspotMap'

export default function DiagramPage() {
  return (
    <div style={{ padding: 20 }}>
      <h1>Схема установки</h1>
      <HotspotMap drawingId={1} />
    </div>
  )
}
