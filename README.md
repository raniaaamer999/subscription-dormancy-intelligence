# Subscription Dormancy Intelligence

A data-driven product case study identifying the gap in Revolut's existing subscription feature, built as part of my application for the Revolut Product Owner Internship 2027.

## The problem

Revolut already detects recurring charges and sends renewal alerts. But neither that feature nor AIR, Revolut's AI assistant launched in 2026, proactively flags subscriptions the user has stopped engaging with. Users will not ask AIR about a charge they do not remember making.

My analysis of 500,000 transactions across 1,219 users found that 82% of detected recurring charges show signs of disengagement based on historical transaction patterns. That translates to approximately $13 wasted per user per month.

## The proposal

A dormancy scoring engine built on top of Revolut's existing subscription infrastructure. When a subscription crosses a 60 day disengagement threshold, Revolut sends a single proactive notification three days before the next renewal. One tap to keep it. One tap to request cancellation.

## What is in this repo

The notebooks folder contains the full Python analysis including data cleaning, subscription detection, dormancy flagging, user segmentation, and key findings.

The data folder contains the processed outputs used by the dashboard.

The dashboard.py file is a Streamlit dashboard visualising the findings. To run it locally, install dependencies and run streamlit run dashboard.py.

The prd folder contains the full Product Requirements Document including problem statement, user personas, feature prioritisation, tradeoffs, and success metrics.

## Key findings

82% of detected recurring charges show signs of disengagement based on transaction patterns.

1,218 out of 1,219 users are affected.

Approximately $13 average monthly waste per user.

Approximately $184,000 total annual waste across the dataset.

## Tools used

Python, pandas, Streamlit, Plotly

## Data source

Synthetic banking transaction dataset sourced from Kaggle covering 500,000 transactions across 1,219 users from 2010 to 2019. The dataset uses anonymous merchant IDs. Absolute figures are conservative estimates. The dormancy threshold of 60 days would be validated through A/B testing in production.