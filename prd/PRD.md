# Product Requirements Document
## Smart Subscription Dormancy Detection
Author: Rania Aamer | Date: June 2026 | Status: Proposal

## Problem statement

Every month, Revolut users are silently charged for services they may no longer be actively using. My analysis of 500,000 transactions across 1,219 users found that 82% of detected recurring charges show signs of disengagement based on transaction behaviour, meaning the user had no associated transaction activity in over 60 days. That translates to approximately $13 wasted per user per month, or approximately $150 a year.

Revolut already has a subscription tracking feature launched in 2020 and an AI assistant called AIR launched in 2026 that can answer subscription questions. But both are reactive. They only help when the user thinks to look. The core problem is that users forget they have these subscriptions entirely. They will not ask AIR about a charge they do not remember making.

This PRD proposes a dormancy detection layer that sits on top of Revolut's existing subscription infrastructure, proactively surfacing forgotten subscriptions before the next renewal hits.

## Who this is for

The passive accumulator is a 24 year old professional who signed up for a free trial during lockdown, forgot to cancel, and has been paying £9.99 a month for three years without noticing. They are not irresponsible with money. They are just busy. They would cancel immediately if someone told them.

The budget conscious switcher is a student who actively manages their finances but does not realise their annual subscriptions are silently renewing. They check their balance regularly but never connect the recurring charge to the forgotten service.

Both personas share one thing. They are not going to find this problem themselves. The product has to find it for them.

## What I am proposing

A dormancy scoring engine built into Revolut's existing subscription feature. Every recurring charge receives a dormancy score based on transaction patterns associated with that merchant and the user's historical engagement signals. When a subscription crosses the 60 day dormancy threshold, Revolut sends a single proactive notification:

"You haven't used [Merchant] in 2 months. Your next payment of £9.99 is in 3 days. Still want it?"

One tap to keep it. One tap to request cancellation.

## Feature prioritisation

Must have

Dormancy scoring engine that calculates engagement signals per user per subscription based on transaction patterns associated with each merchant.

Proactive dormancy alert as a push notification triggered at the 60 day threshold, sent 3 days before renewal.

Should have

Monthly waste summary card visible on the home screen showing total potentially dormant subscription spend.

One tap cancellation request that reduces friction between awareness and action.

Could have

Peer benchmarks showing users how their subscription spend compares to people their age.

Annual plan detection with separate logic for yearly subscriptions to avoid false positives.

Won't have yet

Direct cancellation execution, because legal and merchant relationship complexity makes this a later phase.

Cross bank subscription detection, because it requires Open Banking integration which is out of scope for v1.

## Tradeoffs I considered

False positives are the biggest risk. If Revolut flags an annual subscription as showing signs of disengagement because there has been no associated activity for 60 days, the user cancels it, and then realises they needed it, that is a trust destroying experience. My solution is to build a billing cycle detector that identifies annual plans and applies a separate 365 day dormancy threshold, and to A/B test the 60 day threshold aggressively before full rollout.

Privacy is non negotiable. Revolut cannot see whether a user has opened the Netflix app. It can only see transaction data. The dormancy signal is therefore an inference based on transaction behaviour, not a confirmed fact about usage. Every notification must make this clear. Transparency over precision.

Merchant relationships matter. Revolut has commercial relationships with many of the merchants whose subscriptions this feature would encourage users to reconsider. The feature must be framed around user empowerment, not merchant friction. The goal is not cancellation. It is informed choice.

Alert fatigue is real. If every subscription showing disengagement signals triggers a notification, users will start ignoring them. The solution is to cap alerts at two per month maximum, prioritised by highest monthly spend.

## How I would measure success

The primary metric is a 20% reduction in unnoticed subscription renewals within 90 days of feature launch, measured by comparing renewal rates for users who received dormancy alerts versus a control group.

Secondary metrics include dormancy alert open rate with a target of 40%, cancellation request rate within 7 days of alert with a target of 15%, and false positive rate which must stay below 5% at the 60 day threshold.

The guardrail metric is Net Promoter Score for the subscription feature. If this drops, the alert frequency or messaging needs revisiting immediately.

## Why now

The subscription economy has grown every year for the past decade. My analysis shows recurring charges showing disengagement signals grew consistently across the dataset period, and the proliferation of streaming services and SaaS tools since then has only accelerated the problem. Revolut is well positioned to address this because it already has the transaction data, subscription infrastructure, and customer scale required to test and deploy this feature. This appears to be an underexplored area in most consumer banking apps today, which makes this a strong near term opportunity.

## Methodology note

The 82% figure comes from a synthetic banking transaction dataset sourced from Kaggle, covering 500,000 transactions across 1,219 users from 2010 to 2019. A subscription was defined as any merchant appearing in a user's transaction history across 3 or more distinct calendar months. Disengagement was flagged when a user had no transaction activity associated with that merchant in the 60 days prior to the dataset end date.

It is important to note that transaction data alone cannot confirm whether a user is actively using a service. A user may pay for Netflix monthly and use it daily without generating additional transactions. The dormancy signal is therefore a proxy for potential disengagement, not a direct measure of usage. This is why the proposed notification uses language like "still want it?" rather than asserting the user has stopped using the service.

The dataset uses anonymous merchant IDs rather than real merchant names, so absolute figures are conservative estimates. The dormancy threshold of 60 days was chosen because two consecutive missed monthly billing cycles is a meaningful behavioural signal, and would be validated and refined through A/B testing in production.