from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.goto("https://template.studio.alcreonlabs.com/", wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(1500)
    page.screenshot(path="mockup-preview.png", full_page=False, clip={"x": 0, "y": 0, "width": 1440, "height": 900})
    browser.close()
    print("OK")
