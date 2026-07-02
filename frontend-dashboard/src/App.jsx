
import "./App.css";
import { useEffect, useState } from "react";

function App() {
  const [metrics, setMetrics] = useState(null);
  const [funnel, setFunnel] = useState(null);
const [heatmap, setHeatmap] = useState({});
const [lastUpdated, setLastUpdated] = useState("");
  const [anomalies, setAnomalies] = useState([]);


  // Stable demo values from dataset intelligence
  

 const [events, setEvents] = useState([]);
const [liveTracking, setLiveTracking] = useState(null);

  useEffect(() => {
  fetchData();

  const interval = setInterval(() => {
    fetchData();
  }, 5000);

  return () => clearInterval(interval);
}, []);

const fetchData = async () => {
  try {
    const metricsRes = await fetch(
      "https://ai-powered-store-intelligence-system-2.onrender.com/stores/1/metrics"
    );

    const funnelRes = await fetch(
      "https://ai-powered-store-intelligence-system-2.onrender.com/stores/1/funnel"
    );

    const heatmapRes = await fetch(
      "https://ai-powered-store-intelligence-system-2.onrender.com/stores/1/heatmap"
    );

    const anomaliesRes = await fetch(
      "https://ai-powered-store-intelligence-system-2.onrender.com/stores/1/anomalies"
    );

    const liveRes = await fetch(
      "https://ai-powered-store-intelligence-system-2.onrender.com/live-tracking"
    );

    const metricsData = await metricsRes.json();
    const funnelData = await funnelRes.json();
    const heatmapData = await heatmapRes.json();
    const anomaliesData = await anomaliesRes.json();
    const liveData = await liveRes.json();

    setMetrics(metricsData);
    setFunnel(funnelData.funnel);
    setHeatmap(heatmapData);
    setAnomalies(anomaliesData.anomalies);
    setLiveTracking(liveData);
    setEvents(liveData.events || []);
    setLastUpdated(new Date().toLocaleTimeString());

  } catch (err) {
    console.log(err);
  }
};

 if (!metrics || !funnel || !liveTracking) {
  return <h1>Loading...</h1>;
}

  const healthScore =
    Math.round(
      metrics.conversion_rate +
        (100 - metrics.abandonment_rate) +
        Math.min(metrics.queue_depth * 20, 100)
    ) / 3;

  return (
  <div className="container">
      <h1>AI-Powered Store Intelligence Dashboard</h1>

      <p
        style={{
          textAlign: "center",
          color: "green",
          fontWeight: "bold",
          marginBottom: "20px",
        }}
      >
        🟢 Live Monitoring Active | Last Updated:{lastUpdated}
      </p>

     
      
      <p className="subtitle">
        Real-time AI-powered retail intelligence for customer behavior,
        conversion tracking, queue monitoring, anomaly detection,
        and business insights.
      </p>

  <div className="card" style={{ marginBottom: "30px" }}>
  <h2>Store Health Score</h2>

  <p
    style={{
      fontSize: "50px",
      color:
        healthScore > 75
          ? "green"
          : healthScore > 50
          ? "orange"
          : "red",
    }}
  >
    {healthScore.toFixed(1)}/100
  </p>
</div>
      {/* Funnel */}
      <h2>Funnel</h2>

      <div className="card-grid">
        <Card title="Entry" value={funnel.entry} />
        <Card title="Zone Visit" value={funnel.zone_visit} />
        <Card title="Billing Queue" value={funnel.billing_queue} />
        <Card title="Purchase" value={funnel.purchase} />
      </div>

      {/* Heatmap */}
    <h2 className="section-title">Heatmap</h2>

<div className="card-grid">
  {heatmap.zones?.map((zone, index) => (
    <div className="card" key={index}>
      <h3>{zone.zone}</h3>
      <p>Visitors: {zone.visitors}</p>
      <p>Attention: {zone.attention}</p>
    </div>
  ))}
</div>

      {/* Anomalies */}
    
<h2 className="section-title">Anomalies</h2>

<div className="card-grid">
  {anomalies.map((item, index) => (
    <div className="card high" key={index}>
      <h3>⚠ {item.type}</h3>
      <p>{item.message}</p>
    </div>
  ))}
</div>
      {/* Live Insights */}

<h2 className="section-title">Live Insights</h2>

      <div className="card-grid">
        {metrics.queue_depth > 2 && (
          <div className="card high">
            <h3>⚠ Billing Queue Alert</h3>
            <p>Queue is high. Consider opening another counter.</p>
          </div>
        )}

        {metrics.conversion_rate < 70 && (
          <div className="card medium">
            <h3>📉 Conversion Opportunity</h3>
            <p>
              Conversion is below ideal. Improve customer engagement and
              promotions.
            </p>
          </div>
        )}

        {metrics.abandonment_rate > 20 && (
          <div className="card high">
            <h3>🚶 Queue Abandonment Risk</h3>
            <p>
              High abandonment detected. Reduce billing wait time.
            </p>
          </div>
        )}

        {heatmap.high_attention_zone && (
  <div className="card low">
    <h3>🔥 High Attention Zone</h3>
    <p>
      {heatmap.high_attention_zone} has the highest customer attention.
    </p>
    <p>Dwell Time: {heatmap.dwell_time}s</p>
  </div>
)}
      </div>

      {/* Resource-Based Camera Intelligence */}
      <h2>Resource-Based Camera Intelligence</h2>

      <div className="card-grid">
        <div className="card insight-card">
          <h3>🎥 Entry Monitoring</h3>
          <p>
            <strong>Dataset Used:</strong> entry_1.mp4, entry_2.mp4
          </p>
          <p>
            <strong>Visitors Detected:</strong>
{liveTracking?.visitors || 0}
          </p>
          <p>
            <strong>Insight:</strong> Customer footfall and entry behavior
            tracked.
          </p>
        </div>

        <div className="card insight-card">
          <h3>🛒 Billing Queue Monitoring</h3>
          <p>
            <strong>Dataset Used:</strong> billing_area.mp4
          </p>
          <p>
            <strong>Queue Depth:</strong>
{liveTracking?.queue_depth || 0}
          </p>
          <p>
            <strong>Risk:</strong>{" "}
            {metrics.queue_depth >= 3 ? "HIGH" : "LOW"}
          </p>
        </div>

        <div className="card insight-card">
          <h3>🔥 Zone Intelligence</h3>
      <p>
  <strong>Dataset Used:</strong> zone.mp4 + store-layout.png
</p>

<p>
  <strong>High Attention Zone:</strong>{" "}
  {liveTracking?.high_attention_zone || "N/A"}
</p>

<p>
  <strong>Dwell Time:</strong>{" "}
  {liveTracking?.dwell_time || 0}s
</p>

</div>
          
        
      </div>

      {/* CCTV Events */}
     <div className="card-grid">
  {events.length === 0 ? (
    <div className="card">
      <h3>No Live Events</h3>
      <p>Waiting for CCTV detections...</p>
    </div>
  ) : (
    events.map((item, index) => (
      <div
        className="card"
        key={index}
        style={{ minHeight: "140px" }}
      >
        <h3>{item.time}</h3>
        <p>{item.event}</p>
        <small>Source: {item.source}</small>
      </div>
    ))
  )}
</div>

<footer
  style={{
    textAlign: "center",
    marginTop: "50px",
    paddingBottom: "30px",
    color: "#555",
  }}
>
  <h3>Business Value Delivered</h3>

  <p>
    Detects queue spikes, improves conversion visibility,
    tracks customer movement, identifies high attention zones,
    and provides real-time operational intelligence for stores.
  </p>

  <p>
    Tech Stack: FastAPI + React + Event Analytics +
    Funnel Intelligence + Heatmap Analysis +
    Anomaly Detection + Dataset-Based CCTV Intelligence
  </p>
</footer>

</div>
);
}
  
function Card({ title, value }) {
  return (
    <div className="card">
      <h2>{title}</h2>
      <p>{value}</p>
    </div>
  );
}

export default App;


