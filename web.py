import os
from datetime import datetime, timezone
from flask import Flask

app = Flask(__name__)

START_TIME = datetime.now(timezone.utc)
TARGET_URL = os.environ.get(
    "TARGET_URL", "https://replit.com/join/qkyqeujyrv-worldchampion2"
)


@app.route("/")
def index():
    uptime = datetime.now(timezone.utc) - START_TIME
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime_str = f"{hours}h {minutes}m {seconds}s"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="refresh" content="30">
  <title>Keep-Alive Bot</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #0f1117;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 2rem;
    }}
    .card {{
      background: #1a1d27;
      border: 1px solid #2d3148;
      border-radius: 16px;
      padding: 2.5rem 3rem;
      max-width: 480px;
      width: 100%;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #0d2e1a;
      border: 1px solid #1a5c34;
      color: #4ade80;
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 4px 12px;
      border-radius: 99px;
      margin-bottom: 1.5rem;
    }}
    .dot {{
      width: 8px; height: 8px;
      border-radius: 50%;
      background: #4ade80;
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.3; }}
    }}
    h1 {{
      font-size: 1.6rem;
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: #f8fafc;
    }}
    .subtitle {{
      color: #64748b;
      font-size: 0.9rem;
      margin-bottom: 2rem;
    }}
    .stat {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.75rem 0;
      border-bottom: 1px solid #2d3148;
      font-size: 0.9rem;
    }}
    .stat:last-child {{ border-bottom: none; }}
    .stat-label {{ color: #64748b; }}
    .stat-value {{
      color: #e2e8f0;
      font-weight: 500;
      text-align: right;
      max-width: 60%;
      word-break: break-all;
    }}
    .url {{ color: #818cf8; }}
    .footer {{
      margin-top: 2rem;
      font-size: 0.78rem;
      color: #374151;
      text-align: center;
    }}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge"><span class="dot"></span> Active</div>
    <h1>Keep-Alive Bot</h1>
    <p class="subtitle">Simulating human activity to maintain an active session.</p>
    <div class="stat">
      <span class="stat-label">Status</span>
      <span class="stat-value">Running</span>
    </div>
    <div class="stat">
      <span class="stat-label">Target URL</span>
      <span class="stat-value url">{TARGET_URL}</span>
    </div>
    <div class="stat">
      <span class="stat-label">Uptime</span>
      <span class="stat-value">{uptime_str}</span>
    </div>
    <div class="stat">
      <span class="stat-label">Actions</span>
      <span class="stat-value">Mouse moves · Scrolls · Hovers</span>
    </div>
    <div class="stat">
      <span class="stat-label">Delay between cycles</span>
      <span class="stat-value">12 – 55 seconds (random)</span>
    </div>
    <p class="footer">Page auto-refreshes every 30 seconds.</p>
  </div>
</body>
</html>"""
    return html


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
