# Keep-Alive Browser Bot

## Overview
A Python script using Playwright that keeps a browser session active on a target URL by simulating natural, human-like interactions.

## Features
- Headless Chromium browser via Playwright
- Random mouse movements with variable step counts
- Occasional small scrolls (up or down)
- Random hover actions over the page
- Random delays between actions (12–55 seconds)
- Continuous loop until manually stopped

## Files
- `keep_alive.py` — Main script
- `requirements.txt` — Python dependencies (`playwright==1.44.0`)
- `Procfile` — Heroku worker process definition
- `heroku_setup.sh` — One-time Heroku browser installation helper

## Usage

### Run locally (in this Repl)
The "Keep-Alive Bot" workflow runs it automatically.

Or manually:
```bash
python keep_alive.py
# or with a custom URL:
python keep_alive.py https://example.com
```

### Heroku Deployment
1. Add the Playwright buildpack so Chromium installs on Heroku:
   ```bash
   heroku buildpacks:add --index 1 https://github.com/mxschmitt/heroku-playwright-buildpack
   heroku buildpacks:add heroku/python
   ```
2. Push this repo to Heroku
3. Scale up the worker dyno:
   ```bash
   heroku ps:scale worker=1
   ```
4. The bot will run continuously until the dyno is stopped.

## Architecture
- Uses `asyncio` + Playwright async API for efficient non-blocking I/O
- Actions (mouse move, scroll, hover) are chosen randomly each cycle
- Delays between cycles: 12–55 seconds (uniformly random)
- Headless Chromium with a realistic user-agent string
