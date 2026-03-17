import asyncio
import random
import sys
from playwright.async_api import async_playwright

TARGET_URL = "https://replit.com/join/qkyqeujyrv-worldchampion2"


async def human_pause(min_sec=10, max_sec=60):
    delay = random.uniform(min_sec, max_sec)
    print(f"  Waiting {delay:.1f}s before next action...")
    await asyncio.sleep(delay)


async def random_mouse_move(page):
    viewport = page.viewport_size or {"width": 1280, "height": 800}
    x = random.randint(50, viewport["width"] - 50)
    y = random.randint(50, viewport["height"] - 50)
    steps = random.randint(5, 15)
    print(f"  Moving mouse to ({x}, {y}) over {steps} steps")
    await page.mouse.move(x, y, steps=steps)
    await asyncio.sleep(random.uniform(0.2, 0.8))


async def slight_scroll(page):
    direction = random.choice(["down", "up"])
    amount = random.randint(40, 180)
    if direction == "up":
        amount = -amount
    print(f"  Scrolling {direction} by {abs(amount)}px")
    await page.mouse.wheel(0, amount)
    await asyncio.sleep(random.uniform(0.3, 1.0))


async def random_hover(page):
    viewport = page.viewport_size or {"width": 1280, "height": 800}
    x = random.randint(100, viewport["width"] - 100)
    y = random.randint(100, viewport["height"] - 100)
    steps = random.randint(3, 8)
    print(f"  Hovering near ({x}, {y})")
    await page.mouse.move(x, y, steps=steps)
    await asyncio.sleep(random.uniform(0.5, 2.0))


async def run_session(page, url):
    print(f"Navigating to {url} ...")
    await page.goto(url, wait_until="domcontentloaded", timeout=60000)
    print("Page loaded. Starting keep-alive loop.")

    actions = [
        ("mouse_move", random_mouse_move),
        ("scroll", slight_scroll),
        ("hover", random_hover),
    ]

    cycle = 0
    while True:
        cycle += 1
        print(f"\n[Cycle {cycle}]")

        num_actions = random.randint(1, 3)
        chosen = random.choices(actions, k=num_actions)

        for name, fn in chosen:
            print(f"  Action: {name}")
            try:
                await fn(page)
            except Exception as e:
                print(f"  Warning during {name}: {e}")
            await asyncio.sleep(random.uniform(0.5, 2.5))

        await human_pause(min_sec=12, max_sec=55)


async def main():
    url = sys.argv[1] if len(sys.argv) > 1 else TARGET_URL

    async with async_playwright() as pw:
        chromium_path = (
            "/nix/store/qa9cnw4v5xkxyip6mb9kxqfq1z4x2dx1-chromium-138.0.7204.100/bin/chromium-browser"
        )

        browser = await pw.chromium.launch(
            executable_path=chromium_path,
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--single-process",
            ],
        )

        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
        )

        page = await context.new_page()

        try:
            await run_session(page, url)
        except KeyboardInterrupt:
            print("\nStopped by user.")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
