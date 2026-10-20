import sys
p=sys.argv[1]; h=open(p,encoding="utf-8").read()
def rep(old,new):
    global h
    assert h.count(old)==1,(h.count(old),old[:80]); h=h.replace(old,new)
sup=lambda *ns: '<sup class="fnref">'+', '.join(f'<a href="#s{n}">{n}</a>' for n in ns)+'</sup>'
old=('<p>The client base is large. BlackRock serves hundreds of Aladdin clients in 70 countries, and its technology services revenue was $2.0 billion in 2025'+sup(8,11)+
     '. It projects API calls to grow 17x by 2030, and AI tools acting for clients could become a large source of them'+sup(10)+
     '. Linking that figure to Studio is my inference. How many clients use the APIs today, or run their own AI tools, is not public.</p>')
new=('<p>The client base is large. BlackRock serves hundreds of Aladdin clients in 70 countries'+sup(8)+
     ', and its technology services revenue was $2.0 billion in 2025'+sup(11)+
     '. A 2026 job posting for Aladdin Graph, the team behind the API layer, says it builds for BlackRock and over 200 institutions that rely on its technology'+sup(71)+
     ". BlackRock sizes Aladdin’s addressable market at more than $20 billion"+sup(10)+
     '. It projects API calls to grow 17x by 2030, and AI tools acting for clients could become a large source of them'+sup(10)+
     '. Linking that figure to Studio is my inference. How many of those institutions run their own AI tools is not public.</p>')
rep(old,new)
url="https://careers.blackrock.com/job/new-york/associate-software-engineer-aladdin-graph/45831/100968495568"
entry=(f'<p id="s71"><b class="n">71</b><span class="g">P</span><span class="t">Job posting: Associate, Software Engineer, Aladdin Graph (R266598, New York)</span>. '
       f'BlackRock Careers, as of October 2026. <a href="{url}">{url}</a></p>\n')
i=h.index('<p id="s60">'); j=h.index('</p>\n',i)+5
h=h[:j]+entry+h[j:]
old10='<span class="t">BlackRock 2025 Investor Day presentation</span>. BlackRock, June 2025.'
rep(old10,'<span class="t">BlackRock 2025 Investor Day presentation</span>. BlackRock, June 2025. Slide 23 for the 17x figure, slide 34 for the market size.')
open(p,"w",encoding="utf-8").write(h); print("ok")
