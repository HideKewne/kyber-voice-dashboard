const { chromium } = require('playwright');

async function screenshot() {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto('file:///home/ubuntu/voice-agent-ui/test/white-v7.html');
    await page.waitForLoadState('networkidle');
    await page.screenshot({ path: '/home/ubuntu/voice-agent-ui/test/screenshot.png', fullPage: false });
    await browser.close();
    console.log('Screenshot saved');
}

screenshot().catch(console.error);
