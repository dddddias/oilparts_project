import { useEffect, useState } from "react";
import api from "../api";

export default function HotspotMap({ drawingId }) {
  const [zones, setZones] = useState([]);

  useEffect(() => {
    api.get(`/hotzones/drawing/${drawingId}`)
       .then(res => setZones(res.data))
       .catch(console.error);
  }, [drawingId]);

  return (
    <div style={{ position: "relative", display: "inline-block" }}>
      <img src="/diagram.png" alt="Схема" />
      {zones.map(z => (
        <a
          key={z.id}
          href={`/parts/${z.part_id}`}
          style={{
            position: "absolute",
            left: z.x,
            top: z.y,
            width: z.width,
            height: z.height,
            textDecoration: "none",
            cursor: "pointer",
          }}
        >
          <div
            style={{
              border: "2px solid rgba(255,0,0,0.5)",
              width: "100%",
              height: "100%",
            }}
          />
          <span
            style={{
              position: "absolute",
              left: 0,
              top: 0,
              background: "rgba(255,0,0,0.7)",
              color: "#fff",
              padding: "2px 4px",
              fontSize: "12px",
            }}
          >
            {z.number}
          </span>
        </a>
      ))}
    </div>
  );
}
