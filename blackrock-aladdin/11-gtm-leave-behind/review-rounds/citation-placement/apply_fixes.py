import re,sys
p=sys.argv[1]; h=open(p,encoding="utf-8").read()
def rep(a,b):
    global h; assert h.count(a)==1,(h.count(a),a[:70]); h=h.replace(a,b)
sup=lambda *n:'<sup class="fnref">'+', '.join(f'<a href="#s{x}">{x}</a>' for x in n)+'</sup>'
# Exhibit 1
rep('Portfolio risk analysis and proposals for advisors.','Portfolio risk analysis and proposals for advisors'+sup(901)+'.')
rep('puts Aladdin and outside data in one place.','puts Aladdin and outside data in one place'+sup(23)+'.')
rep('Investment accounting and performance. Its public APIs','Investment accounting and performance'+sup(902)+'. Its public APIs')
# Exhibit 4
rep('A managed data store on Snowflake, with Fivetran moving the data.','A managed data store on Snowflake, with Fivetran moving the data'+sup(14,26)+'.')
rep('Woodhead'+sup(1)+' and Goel'+sup(38)+'. BlackRock gives no count.','Woodhead'+sup(1)+', Goel'+sup(38)+' and Fivetran'+sup(26)+'. BlackRock gives no count.')
# Exhibit 9
rep('against the fund’s estimate of up to £55 million'+sup(55),'against the fund’s estimate of up to £55 million'+sup(54,55))
rep('Nest chose BlackRock’s Aladdin over six other bids'+sup(57),'Nest chose BlackRock’s Aladdin over six other bids'+sup(56,57))
# Page 9
rep('Attributing them to Studio is my inference'+sup(11)+'.','Attributing them to Studio is my inference.')
rep('among the fee terms it names'+sup(11,12),'among the fee terms it names'+sup(12))
# Page 10
rep('according to a secondary summary of its results slides'+sup(2,69),'according to a secondary summary of its results slides'+sup(69))
# Page 13
rep('Arcesium an AI platform, and others will likely follow'+sup(7,8,70,71),'Arcesium an AI platform, and others will likely follow'+sup(7,8,71))
# Exhibit 15
rep('a portfolio manager approves before anything trades. Sewdass','a portfolio manager approves before anything trades'+sup(6)+'. Sewdass')
# Exhibit 16 Hear row
old='Big Little Questions video series</a>'+sup(82)+', '
i=h.index(old); j=i+len(old)
rep(old, old+'<a href="https://www.blackrock.com/aladdin/discover/client-story/client-testimonial-royal-london">client story video</a>'+sup(46)+', <a href="https://www.blackrock.com/aladdin/discover/expertise/webinars/build-vs-buy-how-asset-managers-are-rethinking-key-decisions-today">webinar replay</a>'+sup(10)+', ')
# Exhibit 17
m=re.search(r'(Source: my test of each platform’s public pages)<sup class="fnref">(.*?)</sup>',h)
nums=sorted(set([int(x) for x in re.findall(r'>(\d+)</a>',m.group(2))]+[8,70]))
h=h.replace(m.group(0),m.group(1)+sup(*nums),1)
rep('allow a first API call only for licensed clients'+sup(4,87),'allow a first API call only for licensed clients'+sup(87,96))
# new register entries
i=h.index('<div class="register">')+len('<div class="register">\n')
new=('<p id="s901"><b class="n">901</b><span class="g">P</span><span class="t">Aladdin Wealth product page</span>. BlackRock, as of October 2026. <a href="https://www.blackrock.com/aladdin/platforms/solutions/aladdin-wealth">https://www.blackrock.com/aladdin/platforms/solutions/aladdin-wealth</a></p>\n'
     '<p id="s902"><b class="n">902</b><span class="g">P</span><span class="t">Aladdin Accounting product page</span>. BlackRock, as of October 2026. <a href="https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting">https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting</a></p>\n')
h=h[:i]+new+h[i:]
open(p,"w",encoding="utf-8").write(h); print("applied")
