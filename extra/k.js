const puppeteer = require('puppeteer');

async function automate() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  // Replace with the initial URL to visit
  const initialUrl = 'https://ww9.myasiantv.ru/watch-brewing-love-2024-episode-1-english-sub/';
  await page.goto(initialUrl);

  while (true) {
    // Wait for the 'download' link to appear
    const downloadLink = await page.$('.download');
    if (!downloadLink) {
      console.log("No more 'download' links found. Exiting loop.");
      break;
    }

    // Click the 'download' link
    await downloadLink.click();
    await page.waitForNavigation();

    // On the new page, click the last link with class 'mirror_link'
    const mirrorLinks = await page.$$('.mirror_link a');
    if (mirrorLinks.length > 0) {
      await mirrorLinks[mirrorLinks.length - 1].click();
      await page.waitForNavigation();
    }

    // Go back to the previous page
    await page.goBack();

    // Click the second link with class 'm3'
    const m3Links = await page.$$('.m3');
    if (m3Links.length > 1) {
      await m3Links[1].click();
      await page.waitForNavigation();
    }
  }

  await browser.close();
}

automate().catch(console.error);