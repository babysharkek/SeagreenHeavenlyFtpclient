#!/usr/bin/env bash
# Run this once after deploying to Heroku to install the Chromium browser.
# Heroku buildpack: https://github.com/mxschmitt/heroku-playwright-buildpack
# Add it with: heroku buildpacks:add --index 1 https://github.com/mxschmitt/heroku-playwright-buildpack

python -m playwright install chromium
