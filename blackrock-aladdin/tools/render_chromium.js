const { chromium } = require('playwright');
(async () => {
  const [src, dst] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(async () => chromium.launch());
  const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(src), { waitUntil: 'load' });
  await p.emulateMedia({ media: 'print' });
  await p.pdf({ path: dst, preferCSSPageSize: true, printBackground: true, displayHeaderFooter: false });
  await b.close();
  console.log('wrote', dst);
})();
