# Principles of Design Podcast

Category: Podcast  
Series: Aladdin Client Stories, Tue, 30 May 2023  
Source page: https://www.blackrock.com/aladdin/discover/podcast/engineering-story-podcast-episode  
Media file: 696912df-8780-4e5e-9cef-d56efda43d89.mp3  
Transcript: published transcript (BlackRock page).

Description: Sue Zheng, Tech Fellow and Afwa Kandawire, Global Head of Aladdin Platforms share more about the platform developments (cloud, scale, API), product engineering and the fundamental pillars of engineering at BlackRock.

---

[AFWA KANDAWIRE]

I think there are a couple of disrupting forces, if I might describe them that way, that are upon us. One, no doubt, is the one I think everybody has been sort of tuned into, which is Generative AI and there are many, many different applications and use cases where it is going to change entire business models, it's going to change entire ways of working.

And I think the thing for us to grapple with as a business, as an organization, is going to be how do we prepare for those changes and how do we make sure that the value that our clients get from Aladdin is still relevant five years from now and ten years from now in that context, because things that may be viewed as valuable in Aladdin today may be seen as commodities five years from now. And I think we are only now starting to kind of ask that question and sort through what that might mean. And so, in many ways, I think more than scale or anything else, I think it's going to be navigating the disruption that is coming our way as a result of Generative AI. I think in terms of just nearer term, we have a significant amount of change that we are implementing, driven by moving from a traditional layered architecture to a services architecture, the cloud migration, what we've talked about, there's people and reskilling.

So, I think there's a lot of complexity that we have to navigate in an environment where the world around us is also changing. And so, again, figuring out how to sort of make sure that you're focusing on the right things and getting to the right things in the right timeframe is another thing. I think that we've got to sort of figure out how to execute, because if we stand still and we execute on the wrong things, which is the wrong things, we find ourselves maybe sort of being on dry ground.

[SUE ZHENG]

How was your trip to APAC?

[AFWA KANDAWIRE]

My trip to APAC was awesome. It's been two years in the making. Actually, today is my two-year anniversary at BlackRock. I feel like I've made it. And I hadn't been to Asia since I joined the firm and so just the ability to finally get out back to the region. I actually don't know whether you know this, I actually lived in Asia for five years.

[SUE ZHENG]

Oh no, which part?

[AFWA KANDAWIRE]

I lived in Tokyo and I covered the region for Tokyo for many years. And so, on a personal level, it was quite nice to get back there. I hadn't been back in many years, but in terms of meeting teams and just getting to know our business, I also had a chance to meet with some of the clients. It was just really great because you can get to know an organization incredibly quickly if you’re actually in the proximity of the people in the business there, and I feel like in many ways I've closed what has felt for me like somewhat of a gap in terms of my understanding and appreciation of BlackRock.

[SUE ZHENG]

I would love to know just a little bit more about how you're thinking around the platform engineering.

[AFWA KANDAWIRE]

I view the primary mission of the platform’s organization as being number one, let's make sure Aladdin is up and running for our clients every single day. And number two, when something's not broken, let's make sure that we're making it as easy for our engineers to build and innovate into Aladdin to deliver the capabilities that our clients need. And in order to do that, we had to sort of go about simplifying the operating model and really focusing it around very specific outcomes that would enable engineers to be more productive. And so, what that meant was moving to a product operating model and we've organized around what we call product families. And those product families have a very specific set of focuses in terms of the kind of products and capabilities that they are focused on.

And so we have, for example, mission control, whose entire focus is ensuring that Aladdin is up and running, responding to issues, but also making sure that the maintenance of the platform is happening on a regular basis with a cadence and in a highly controlled way. And then we have hosting services whose primary focus is ensuring that there is an environment in which we can deploy and run applications. We have engineering services whose principal job is to sort of make sure that all the friction points for developers are removed and that we can automate as much of our process around building, testing and deploying software rapidly. And then, of course, you know, we've got enterprise architecture where we're focused on really thinking about how do we continue to find those places which are blocking us in terms of our ability to scale and ensure that we've got a trajectory that continues to support the growth of the business. And then the final function is the product office, which is the enabling capability around making sure that we are really maturing our competency around product management.

[SUE ZHENG]

Right. Because I remember years ago when I started, one of the engineering ethos we always had was one database. You join, people tell you it's one database, you cannot create another database. But at some point, the company continued to grow and the industry grew, you realize there's a physical constraint to one database. So, then we evolved one database to one source of truth or something like that. So, it's not a physical database. But I remember, when we first started to challenge that in trading, we were trying to figure out how to keep up with the growing trading volume and the need for more speed without impacting the rest of the system. And we realized that we probably have to take parts of the order management or order execution system and put it on top of a different real time transactional database, but still need to figure out how do we keep the access for information accessible to the rest of system.

That was interesting, at that point we leveraged Cassandra. So, before that everything was in one database, a side base database. But when we started thinking about can we move parts of the system out to something else, like Cassandra, we had to go through quite a bit of experimenting, getting people comfortable, but also thinking creatively around technique like writing behind, so that yes, we're going to be in a separate database so that we can reduce the contagion risk, but also making sure everyone still has access to the same information no different than before. So, that allowed us to start this beginning of changing what one database really means. But throughout my 20 plus years here, we always believed that there should be one source of truth. So that's always, like, something I remind myself.

[AFWA KANDAWIRE]

Look, and I think that that has been one of the powers of Aladdin, right? When I think about sort of why we've been able to scale this business and do it so effectively and not sort of become encumbered by complexity, is the fact that there are core set of design principles around which Aladdin was founded and as you point out, that principle can sort of remain intact and continue to have longevity. It doesn't mean you constrain yourself to sort of the original solution. And so, to your point, we've been able to segment the database and continue to sort of maintain that notion of single source of truth. And by the way, if we've been in this architecture for almost two decades over the last few years, we’ve started to migrate away from our layered architecture to a services architecture, which is a complete transformation in terms of kind of the way we think about building and deploying applications. You know, you go from thousands of applications to hundreds of thousands and maybe at some point millions of services. We have to sort of maintain many of those core principles around which Aladdin is founded, right? Every single client environment looks the same, is built the same way, we have a single control plane and a single source of truth.

And so, you know, one of the things that we're starting to introduce is this notion of domain driven design and the idea being that the database is no longer the single source of truth, but rather the domain is the single source of truth for that domain. And so, as long as you continue to sort of preserve this notion of the principle, you can manifest in different ways.

[SUE ZHENG]

Yeah, absolutely. And it's interesting. It's powerful because the other thing I think I always have to tell people like it’s hard; Aladdin always strived to be a multi-asset end-to-end system. And it's much easier for me to build maybe a standalone fixed income system, standalone equity system, standalone currency system than a multi-asset system. Because like how do you come up with the right domain, the data model that fits all the asset classes but still preserve the nuances of each asset class. So, you sort of have the ability to see everything in one place, but not trying to fit square peg into a round hole situation. Now we're actually trying to take it to a different level by taking on private market. So, not just a public market but private market with all the nuances of private market, the non-standard nature of private market, and how you now fit into very, try to be standard nature of the Aladdin ecosystem.

[AFWA KANDAWIRE]

Have you found one, the types of challenges to be different in the private market space relative to sort of the public asset space in terms of how you sort of think about the problems that you have to be solving for from a capability standpoint?

[SUE ZHENG]

Yeah. So, definitely I find a lot of differences between private market and public market, but I also find similarities. And especially as we think about if what everyone says is true, which is more capital to be deployed to private market, you're going to see the volume private market investment increases. Eventually for everyone to cope with that increase, you also need scale.

And that usually means you need to start to think about standards, and technologies like standards because it’s easy to codify things and then you can implement and build a solution against it. For now, for example, I'm focusing on private credit as an asset class, so we debate it like, do you think about private

credit, do you want to build it in a private credit specific system, or do you want to try to work in a multi-asset nature?

Obviously, we lean with the more multi-asset nature because you have public credit, you have private credit, you have similarities between them and differences too. But the key has been, at least when it comes to designing a data model, just identify what the structural features are. Can you codify the structural features such that we can build technology to automate, to calculate cash flow, to try to figure out, hey, if a loan has these features, they should behave this way. But certain features may not be limited to private credit or loans but could be another asset class that exhibits the same feature, it’s been fun learning about private market for someone who knows more about public market because a lot of what I thought I knew I had to revisit it and change the way I think about public market. When it comes to settlement, there's a lot more post-trade STP (straight-through processing), where in private market, no such thing. Things we take for granted in the public market in terms of like when it comes to post-trade settlements like DVP (delivery versus payment), no such thing. So, you think about how do you reconcile your cash versus your position? It works differently in the private market versus the public market. But I do see some benefits of how you can apply features of public market to private market, such as we're trying to like use Aladdin’s SWIFT capability to send our cash wires out for private market because why not just because it's private markets. It’s still a cash wire. You should be able to use SWIFT capabilities. So, it’s interesting. It’s fascinating to learn about the different things, but also trying to figure out how do you leverage the scale of Aladdin to simplify and create efficiency for the private market?

[AFWA KANDAWIRE]

What sort have been profoundly impressive to me is just how Aladdin has continued to sort of be flexible. And I always come back to one of the first things that struck me when I joined BlackRock and I sort of had a chance to peek under the hood of Aladdin is while Aladdin was conceived of almost two decades ago now maybe more than that, I'm sort of getting my time frame is a little bit off here. The core design principles have really stood the length of time, and you touched on it a little bit in terms of the core ethos. You've been around BlackRock for quite some time, and so you have the benefit of what was sort of some of that early thinking. For somebody who's joined more recently, I reflect and think, wow, these guys were so forward-thinking in terms of thinking about the modularity of Aladdin and our ability to sort of scale and continue to grow the business with an architecture that has stood the test of time for more than two decades and will continue to evolve and adapt because many of the principles that you see in modern cloud architectures are actually inherent in Aladdin.

I’d just love to kind of get inside of the room of some of the conversations with people like Charlie Hallac that you had a chance to kind of work with. What was that thinking and was it by accident or were there some really important concepts that impressed upon you and have stood the test of time?

[SUE ZHENG]

I would definitely say it was not by accident. Charlie, for someone who was so senior was always so focused on details. So, I remember as an analyst spending a lot of time in his office because he was trying to pick, believe it or not, the right shades of blue and red, because we were trying to change front-end too. But he cares. He puts a lot of heart and thought into every decision. He would check every database change. You want to make sure that again, we stick to the one database. If you’re going to write to this, make sure there's only one application writing to it. So, a lot of that nowadays we like of course by then if you think about 20 plus years ago, it was easier to do things the quick way. It was harder to do things the right way. But the right way, I think, helped us grow to where we are today. Things like, yes, you can write some pro script, you can update things here, but why not build a service that becomes a central writer to this piece of data? Everyone calls it services. So, if you ever have to make changes, you have autonomy to change. You don't have to coordinate across 15 things, right? So that's something I remember like growing up here and learning as a software engineer, working on different project over the years, it was always impressed upon me that, hey, I want to make sure there's no multiple application writing to the same thing. If I'm with the owner of the data, I'm the provider of a service, everyone is going to update the data through my service.

The service was just called a BMS service back then, but it’s the same concept. If someone's querying my data, let me provide them some access ability to query the data and then if someone is doing the same thing as I am – why? Like, let's just create a separate module or service so that they can reuse it. I remember like rebuilding an old C++ application into Java and we were coming across this feature in there that was basically I guess it’s a data compliance service now. But this application was doing everything sort of directly within the applications and we have another app that needs to do the same thing. Strip that piece out, we’re going to build this other server sitting on top of the service that handles the compliance

checks such that these two applications get the same experience, that user using the two applications gets the same experience.

[AFWA KANDAWIRE]

How are you scaling, sort of, making sure that design principles are codified in an architecture in such a way that, you can ensure that the integrity of the system, as an engineer lead, how do you sort of keep that alive?

[SUE ZHENG]

I always prefer if there's a way to do it in whether through libraries, in a way where you can then force a standard architecture without having to make sure people memorize everything because it's hard and everyone as human being will like to deviate their own way at some point. So, if there's a way for us to integrate these principles into practice by either putting in a structure or a framework library such that it's almost like, hey, you don't have to think about it. You focus on the feature itself. Don't worry about the structure around this application, then that also allows, I think, platform team, your team, to have more autonomy. When you want to make changes and when you want to apply standards versus hey, let's get everyone together, let's get and sign off and we all make change on the same day.

[AFWA KANDAWIRE]

I love that example because I was with a bunch of my engineers at Google and a couple of West Coast companies maybe two or three years ago. And one of the things we asked them was how they enable velocity, but also consistency in their platform. They talk about this idea of application frameworks and frankly, what they talked about was the same concept that you've just described, which is try as much as possible to abstract away the complexity of the platform from the engineers so they can focus on features.

And that enables consistency but also enables a high degree of velocity. And again, I just use that as another proof point of how some of the thinking of Aladdin was well ahead of its time because we've had this notion of an application framework embedded in the platform for quite a while, and it's something that's enabling us to sort of continue to, I think, scale but maintain the integrity of the platform quite well.

As an engineer, how do you think or what are you thinking about in terms of the promise, the excitement to the unlock of being able to be in the cloud now and start to kind of leverage more cloud native services?

[SUE ZHENG]

If I think about it, we always design for the worst-case scenario, so maybe it's not always the most cost effective, but stability is a feature we want to make sure that you can plan for the worst-case scenario and the worst day. But that also means, hey, when you move to the cloud, you have options now, you don't have to because you could be more elastic in nature, but that would also mean that we need to maybe change how our application functions because a lot of times the application, you know, expect the worst. So, we eagerly cache so many things, right? We're very fast. We tried to cache many things. So, you get that user experience of, hey, it’s very nimble because you do something, something happens simultaneously, you don’t have to worry about the provisioning. That’s not something we have to concern about. There’s a massive scale there if you can make to even on the fly provisioning possible, such that we don’t have to say okay like I don’t want to wait for this thing to materialize in three weeks, so, I mean, just ask for extra. I remember years ago, just make sure whatever you ask, plus another like 20 or 30% just in case. So, we don’t want to wait another few months to make that happen. So, I think, whether it’s a provisioning for the compute, whether it’s designing the application such that we can take advantages like things more real-time, more elastic. That will be really interesting to see how we can benefit from that.

[AFWA KANDAWIRE]

And again, I think this is a place where I’ve been really impressed with the thinking about our cloud strategy. I arrived, I joined at a point in time where we had made a decision on how we were going to migrate to the cloud. We had chosen our cloud provider. And one of the core, as you know, principles around the migration is that the first stage would be a lift and shift, and that meant really focusing on moving the infrastructure. There’s been minimal change we’ve had to make in applications to actually conform because in part Aladdin already had quite a flexible architecture and the principal reason for doing a lift and shift was to ensure that we could actually enable Aladdin to be available to more prospects in more regions than we had datacentres available. And so, this idea of leveraging the public cloud to really enter new markets was I think a very insightful and very strategic principal objective.

Obviously, we want to now start to begin to unlock other benefits of the cloud, such as elasticity, as you say, and as well as potentially sort of the other path services. But I think that for the most part, what we're seeing is real value unlock in terms of kind of enabling us to reach clients where they are. I know the engineers would sort of love to have sort of been the first constituent, but I think it's just, again, one of those things that if we stay anchored to focusing on our clients, we end up focusing on the things that are most important.

[SUE ZHENG]

That's right.

[AFWA KANDAWIRE]

I’d just love to kind of as you think in your role about trading off features against other priorities, how do you sort of keep grounded in ensuring that we're always doing the right things for the client?

[SUE ZHENG]

It's tough because it's almost like I would tell someone sometimes, every day it's a trade-off decision. The one thing I always try to remind myself is, one, I want to design and build a solution that works for the industry, not necessarily just for that one client that asked for it, whether this client is BlackRock or not, because ultimately the other principle I didn't mention earlier, I should have mentioned, you mentioned this earlier, in Aladdin we always try to push the same software out to all clients. So, I know in the back of my mind being in a position to support software so many years, I don't want to be on the hook for saying I have like 50 different versions out there. I don't know which one you’re using. So, I need to make sure that the same version of software is out eventually everywhere. So, if I'm making a decision or I'm designing a solution, I just need to make sure that solution works for what we consider like the best practice.

[AFWA KANDAWIRE]

That notion of a single code base at all clients leads to simplicity, it’s what enables the scale, it’s what enables the reliability. And so, yet again, one of those core principles that continues to stand the test of time.

[SUE ZHENG]

And I think it's also important for the client to know that BlackRock, the house, is using the same software, right? We have skin in the game in terms of the software we deploy. We design solution. Our user provider model depends on the fact that we work closely with BlackRock. BlackRock is using the software we build for clients as well.

So, that’s one thing that I believe a lot in, and I want us to always stick to it.

[AFWA KANDAWIRE]

Hundred percent.
