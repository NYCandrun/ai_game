const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(async e => chromium.launch());
  const p = await b.newPage();
  await p.emulateMedia({ media: 'print' });
  await p.goto('file://' + process.argv[2]);
  const r = await p.evaluate(() => {
    const q = s => document.querySelector(s);
    const box = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return { top: r.top, h: r.height, mt: cs.marginTop, mb: cs.marginBottom }; };
    return { part3: box(q('#part-3')), h2: box(q('#part-3 h2')), p: box(q('#part-3 > p')), ex14: box(q('#exhibit-14')), svgdiv: box(q('#exhibit-14 div[role=img]')), svg: box(q('#pos')), note14: box(q('#exhibit-14 .notes')), ex15: box(q('#exhibit-15')), tbl: box(q('#exhibit-15 table')), note15: box(q('#exhibit-15 .notes')) };
  });
  console.log(JSON.stringify(r, null, 1)); await b.close();
})();
