# Group g02 fixes (Exhibit 2, page 4)

## p04-06: FIX

- Current: compares a changed portfolio with the original before anything is traded [21]
- Proposed: shows a changed portfolio and the original side by side [21]
- Why: The recording shows the original and the what-if portfolio "side by side" (BahCi45_BTc captions ~11:09) but never mentions trading. "Before anything is traded" was the author's inference, so it goes.

## p04-11: FIX

- Current: Any violation then carries an owner, a disposition and a resolution comment [6]
- Proposed: A violation record has fields for an owner and a user’s resolution comment. A disposition is added when the violation is closed [6]
- Why: The Violation spec says the disposition "will be populated for closed violations" and the comment is one "populated by a user". Only actionStatus is required, so not every violation carries all three.

## p04-13: FIX

- Current: (ComplianceRule spec); no application is named [6]
- Proposed: (ComplianceRule spec). The Level spec names the application “Aladdin Compliance” [6]
- Why: Source 6's Level spec says "A unique name for a rule in Aladdin Compliance", and step 5 already counts Aladdin Accounting from the same kind of spec text. The alternative is to drop Aladdin Accounting from step 5 so both rows use the stricter standard, but that throws away a true fact.

## p04-22: FIX

- Current: BrokerConfirmRoutingAPI routes the confirm [6]
- Proposed: BrokerConfirmRoutingAPI holds each broker’s instructions for delivering confirms [6]
- Why: The spec says BrokerConfirmRouting "describes instructions for delivering trade information to a broker desk" and that routings "are setup at broker level". Its only operations create, update, remove, validate and filter those records, so it does not send the confirm itself.

## p04-28: FIX

- Current: Positions appear only as fields: a positions source in PortfolioToolkitAPI, and a violation’s
- Proposed: Positions appear only as fields. Examples are a positions source in PortfolioToolkitAPI, collateral positions in CollateralStatementAPI and a violation’s
- Why: "Only as fields" holds, but the colon made two examples read as the full list. CollateralStatementAPI also has "Details of collateral positions" (swagger.json:979), so the sentence now gives examples.

## p04-41: FIX

- Current: the Aladdin Accounting episode with David Schneid and Daniel Shannon, which does not label who is speaking [20]
- Proposed: the Aladdin Accounting episode with David Schneid and Daniel Shannon [20]
- Also change (Exhibit 2, step 3, product column): "Schneid or Shannon of Aladdin Accounting describes the run" becomes "David Schneid, head of product management for Aladdin Accounting, describes the run"
- Also change (Exhibit 2, step 5, who acts): "The accounting team, which says of itself: “we are data managers more than anything else” (Schneid or Shannon) [20]" becomes "The accounting team. Daniel Shannon, BlackRock’s head of outsourced platform services, says “we are data managers more than anything else” [20]"
- Also change (Exhibit 2, step 6, who acts): "heads of performance” (Schneid or Shannon) [20]" becomes "heads of performance” (Schneid) [20]"
- Also change (Sources register, entry 20): "David Schneid and Daniel Shannon, Aladdin Accounting, BlackRock, undated; the recording does not label which of the two is speaking." becomes "David Schneid, Head of Product Management for Aladdin Accounting, and Daniel Shannon, Head of Outsourced Platform Services, BlackRock, undated."
- Why: The video names each speaker on screen: Shannon at 0:13 ("Head of Outsourced Platform Services, BlackRock") and Schneid at 0:35 ("Head of Product Management for Aladdin Accounting"), checked on frames of the published video. Shannon says "data managers" (1:05). Schneid says "heads of performance" (0:35) and "from that first order" (1:23).

## p04-43: FIX

- Current: The specifications name no order screen and hold no position or event API, and they do not say in what sequence steps 4 to 6 happen.
- Proposed: The Order spec names one order screen, the Order Monitor in Aladdin Dashboard. The specifications hold no position or event API. They do not say in what sequence steps 4 to 6 happen.
- Why: OrderAPI swagger.json:2244 says the Basket ID "is visible in the Basket column in Order Monitor of Aladdin Dashboard". So the specifications do name an order screen.
