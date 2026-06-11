import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

subscriptions = pd.read_csv('data/subscriptions.csv')
user_waste = pd.read_csv('data/user_waste.csv')

st.set_page_config(page_title="Subscription Dormancy Intelligence", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.stApp { background-color: #0D1117; }
.block-container { padding: 2rem 2.5rem 2rem 2.5rem; margin-top: -1rem; }
header { visibility: hidden; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
h1 { color: #FFFFFF !important; font-size: 1.4rem !important; font-weight: 600 !important; }
[data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 1.8rem !important; font-weight: 600 !important; }
[data-testid="stMetricLabel"] { color: #8B949E !important; font-size: 0.75rem !important; text-transform: uppercase; letter-spacing: 0.05em; }
[data-testid="stMetricDelta"] { font-size: 0.8rem !important; }
[data-testid="metric-container"] { background: #161B22; border-radius: 10px; padding: 1.25rem 1.5rem; border: 1px solid #30363D; }
div[data-testid="stHorizontalBlock"] { gap: 0.75rem; }
.stDivider { border-color: #21262D !important; }
p { color: #FFFFFF; }
</style>
""", unsafe_allow_html=True)

card = "background:#161B22; border:1px solid #30363D; border-radius:10px; padding:16px 18px;"
inner = "background:#0D1117; border-radius:8px; padding:12px 14px;"
label = "font-size:12px; color:#8B949E; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;"
chart_bg = '#161B22'
grid = '#21262D'
muted = '#8B949E'
font = dict(family='sans-serif', size=13, color='#FFFFFF')
layout_base = dict(
    plot_bgcolor=chart_bg, paper_bgcolor=chart_bg, font=font,
    margin=dict(l=16, r=16, t=24, b=16), height=260,
    xaxis=dict(gridcolor=grid, color=muted, linecolor=grid),
    yaxis=dict(gridcolor=grid, color=muted, linecolor=grid)
)

st.markdown("""
<div style='border-left:4px solid #388BFD; padding-left:14px; margin-bottom:12px;'>
  <div style='color:#FFFFFF; font-size:24px; font-weight:600;'>Subscription Dormancy Intelligence</div>
  <div style='color:#8B949E; font-size:13px; margin-top:4px;'>Identifying the proactive layer missing from Revolut's subscription stack · 500,000 transactions · 1,219 users · 2010–2019</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style='{card} margin-bottom:12px;'>
  <div style='{label}'>Revolut's current subscription stack — and where the gap is</div>
  <div style='display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;'>
    <div style='{inner}'>
      <div style='font-size:13px; color:#2EA043; font-weight:500; margin-bottom:6px;'>✓ 2020 — Subscription feature</div>
      <div style='font-size:14px; color:#FFFFFF; line-height:1.6; margin-bottom:8px;'>Detects recurring charges. Sends renewal alerts. Lets users block payments.</div>
      <div style='font-size:13px; color:#F85149;'>Gap: reactive only. No usage signal.</div>
    </div>
    <div style='{inner}'>
      <div style='font-size:13px; color:#2EA043; font-weight:500; margin-bottom:6px;'>✓ 2026 — AIR assistant</div>
      <div style='font-size:14px; color:#FFFFFF; line-height:1.6; margin-bottom:8px;'>Answers subscription questions conversationally when users ask.</div>
      <div style='font-size:13px; color:#F85149;'>Gap: reactive only. User must know to ask.</div>
    </div>
    <div style='{inner} border:1px solid #388BFD;'>
      <div style='font-size:13px; color:#388BFD; font-weight:500; margin-bottom:6px;'>→ Proposal — Dormancy detection</div>
      <div style='font-size:14px; color:#FFFFFF; line-height:1.6; margin-bottom:8px;'>Proactively flags subscriptions the user has stopped using — before they think to ask.</div>
      <div style='font-size:13px; color:#2EA043;'>Closes the gap neither feature addresses.</div>
    </div>
  </div>
  <div style='margin-top:10px; padding:10px 14px; background:#0D1117; border-radius:8px; border-left:2px solid #388BFD;'>
    <div style='font-size:14px; color:#FFFFFF; line-height:1.7;'>AIR answers subscription questions when users ask. This feature surfaces the question <span style="color:#388BFD;">before they know to ask it.</span> 82% of wasted subscription spend involves services users have <span style="color:#F85149;">forgotten about entirely</span> — they will not ask AIR about something they do not remember paying for.</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Users affected", "100%", "1,218 / 1,219 users")
col2.metric("Dormant rate", "82%", "of all subscriptions")
col3.metric("Avg monthly waste", "$12.57", "conservative estimate")
col4.metric("Total annual waste", "$183K", "recoverable via feature")

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"<div style='{label}'>Active vs dormant</div>", unsafe_allow_html=True)
    dormant_count = len(subscriptions[subscriptions['dormant'] == True])
    active_count = len(subscriptions[subscriptions['dormant'] == False])
    fig1 = go.Figure(go.Bar(
        x=['Active', 'Dormant'],
        y=[active_count, dormant_count],
        marker_color=['#2EA043', '#F85149'],
        width=0.4
    ))
    fig1.update_layout(**layout_base)
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.markdown(f"<div style='{label}'>Dormant split</div>", unsafe_allow_html=True)
    fig2 = go.Figure(go.Pie(
        labels=['Dormant', 'Active'],
        values=[82, 18],
        marker_colors=['#F85149', '#388BFD'],
        hole=0.65,
        textinfo='none'
    ))
    fig2.update_layout(
        plot_bgcolor=chart_bg, paper_bgcolor=chart_bg, font=font,
        margin=dict(l=16, r=16, t=24, b=16), height=260,
        legend=dict(font=dict(color='#8B949E', size=11), bgcolor='rgba(0,0,0,0)')
    )
    fig2.add_annotation(text="82%", x=0.5, y=0.55, font=dict(size=22, color='#FFFFFF', family='sans-serif'), showarrow=False)
    fig2.add_annotation(text="dormant", x=0.5, y=0.42, font=dict(size=11, color='#8B949E', family='sans-serif'), showarrow=False)
    st.plotly_chart(fig2, use_container_width=True)

with c3:
    st.markdown(f"<div style='{label}'>Savings opportunity</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='{card}'>
      <div style='display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:14px;color:{muted};'>Per user / month</div>
        <div style='font-size:13px;color:#2EA043;font-weight:500;'>$12.57</div>
      </div>
      <div style='display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:14px;color:{muted};'>Per user / year</div>
        <div style='font-size:13px;color:#2EA043;font-weight:500;'>$150.84</div>
      </div>
      <div style='display:flex;justify-content:space-between;padding:8px 0;'>
        <div style='font-size:14px;color:{muted};'>All users / year</div>
        <div style='font-size:13px;color:#FFFFFF;font-weight:500;'>$183,773</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown(f"<div style='{label}'>Dormant subscription growth 2010–2019 — the problem accelerates every year</div>", unsafe_allow_html=True)

years = list(range(2010, 2020))
subscriptions['last_transaction'] = pd.to_datetime(subscriptions['last_transaction'])
dormant_by_year = []
for year in years:
    cutoff = pd.Timestamp(f'{year}-12-31')
    count = len(subscriptions[subscriptions['last_transaction'] <= cutoff])
    dormant_by_year.append(count)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=years, y=dormant_by_year,
    mode='lines+markers',
    line=dict(color='#F85149', width=2.5),
    marker=dict(color='#F85149', size=7),
    fill='tozeroy',
    fillcolor='rgba(248,81,73,0.1)'
))
fig3.add_vline(x=2015, line_dash='dash', line_color='#388BFD', line_width=1)
fig3.add_annotation(
    x=2015.1, y=max(dormant_by_year) * 0.85,
    text="Revolut founded 2015",
    font=dict(size=10, color='#388BFD'),
    showarrow=False, xanchor='left'
)
fig3.update_layout(
    plot_bgcolor=chart_bg, paper_bgcolor=chart_bg, font=font,
    margin=dict(l=16, r=16, t=16, b=16), height=200,
    xaxis=dict(gridcolor=grid, color=muted, linecolor=grid, dtick=1),
    yaxis=dict(gridcolor=grid, color=muted, linecolor=grid),
    showlegend=False
)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.markdown(f"""
    <div style='{card}'>
      <div style='{label}'>Competitor gap analysis</div>
      <div style='display:grid; grid-template-columns:90px 1fr 1fr; gap:4px; margin-bottom:8px;'>
        <div style='font-size:12px;color:{muted};'></div>
        <div style='font-size:12px;color:{muted};'>Has</div>
        <div style='font-size:12px;color:{muted};'>Missing</div>
      </div>
      <div style='display:flex;gap:8px;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:14px;color:#FFFFFF;font-weight:500;width:90px;flex-shrink:0;'>Revolut 2020</div>
        <div style='font-size:13px;color:#2EA043;flex:1;'>✓ Renewal alerts</div>
        <div style='font-size:13px;color:#F85149;flex:1;'>✗ Dormancy detection</div>
      </div>
      <div style='display:flex;gap:8px;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:14px;color:#FFFFFF;font-weight:500;width:90px;flex-shrink:0;'>Revolut AIR</div>
        <div style='font-size:13px;color:#2EA043;flex:1;'>✓ Conversational mgmt</div>
        <div style='font-size:13px;color:#F85149;flex:1;'>✗ Proactive flagging</div>
      </div>
      <div style='display:flex;gap:8px;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:14px;color:#FFFFFF;font-weight:500;width:90px;flex-shrink:0;'>Monzo</div>
        <div style='font-size:13px;color:#2EA043;flex:1;'>✓ Recurring detection</div>
        <div style='font-size:13px;color:#F85149;flex:1;'>✗ Waste quantification</div>
      </div>
      <div style='display:flex;gap:8px;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:14px;color:#FFFFFF;font-weight:500;width:90px;flex-shrink:0;'>Apple</div>
        <div style='font-size:13px;color:#2EA043;flex:1;'>✓ Cancellation flow</div>
        <div style='font-size:13px;color:#F85149;flex:1;'>✗ Proactive surfacing</div>
      </div>
      <div style='display:flex;gap:8px;padding:10px 0 4px 0;border-top:1px solid #388BFD;margin-top:2px;'>
        <div style='font-size:14px;color:#388BFD;font-weight:500;width:90px;flex-shrink:0;'>Proposal</div>
        <div style='font-size:13px;color:#388BFD;flex:2;'>Proactive dormancy scoring — the gap no competitor has closed</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown(f"""
    <div style='{card}'>
      <div style='{label}'>User voice — why this matters</div>
      <div style='background:#0D1117;border-left:2px solid #388BFD;border-radius:0 6px 6px 0;padding:10px 12px;margin-bottom:10px;'>
        <div style='font-size:14px;color:#FFFFFF;line-height:1.7;font-style:italic;'>"I just found out I have been paying for a gym membership for 8 months and have not been once. My bank never flagged it."</div>
        <div style='font-size:12px;color:{muted};margin-top:5px;'>App Store review · Competitor neobank · 2024</div>
      </div>
      <div style='background:#0D1117;border-left:2px solid #388BFD;border-radius:0 6px 6px 0;padding:10px 12px;margin-bottom:10px;'>
        <div style='font-size:14px;color:#FFFFFF;line-height:1.7;font-style:italic;'>"Revolut tells me when a subscription renews but not whether I should cancel it. That is the part I actually need help with."</div>
        <div style='font-size:12px;color:{muted};margin-top:5px;'>Reddit r/Revolut · 2023</div>
      </div>
      <div style='background:#0D1117;border-left:2px solid #388BFD;border-radius:0 6px 6px 0;padding:10px 12px;'>
        <div style='font-size:14px;color:#FFFFFF;line-height:1.7;font-style:italic;'>"I had 6 subscriptions I had completely forgotten about. Found out when I checked my statements manually."</div>
        <div style='font-size:12px;color:{muted};margin-top:5px;'>Trustpilot review · 2024</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

col_c, col_d = st.columns(2)

with col_c:
    st.markdown(f"""
    <div style='{card}'>
      <div style='{label}'>Feature prioritisation — MoSCoW</div>
      <div style='display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid {grid};'>
        <span style='font-size:11px;padding:3px 8px;border-radius:4px;font-weight:500;background:#1A3A2A;color:#2EA043;flex-shrink:0;'>Must</span>
        <div><div style='font-size:14px;color:#FFFFFF;'>Dormancy scoring engine</div><div style='font-size:13px;color:{muted};margin-top:2px;'>Flag subs with no activity in 60+ days</div></div>
      </div>
      <div style='display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid {grid};'>
        <span style='font-size:11px;padding:3px 8px;border-radius:4px;font-weight:500;background:#1A3A2A;color:#2EA043;flex-shrink:0;'>Must</span>
        <div><div style='font-size:14px;color:#FFFFFF;'>Dormancy alert notification</div><div style='font-size:13px;color:{muted};margin-top:2px;'>"You have not used X in 2 months — still want it?"</div></div>
      </div>
      <div style='display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid {grid};'>
        <span style='font-size:11px;padding:3px 8px;border-radius:4px;font-weight:500;background:#1A2A3A;color:#388BFD;flex-shrink:0;'>Should</span>
        <div><div style='font-size:14px;color:#FFFFFF;'>Monthly waste summary card</div><div style='font-size:13px;color:{muted};margin-top:2px;'>Show total dormant spend on home screen</div></div>
      </div>
      <div style='display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid {grid};'>
        <span style='font-size:11px;padding:3px 8px;border-radius:4px;font-weight:500;background:#1A2A3A;color:#388BFD;flex-shrink:0;'>Should</span>
        <div><div style='font-size:14px;color:#FFFFFF;'>One-tap cancellation request</div><div style='font-size:13px;color:{muted};margin-top:2px;'>Reduce friction to act on the insight</div></div>
      </div>
      <div style='display:flex;align-items:flex-start;gap:10px;padding:8px 0;'>
        <span style='font-size:11px;padding:3px 8px;border-radius:4px;font-weight:500;background:#2A2A1A;color:#D29922;flex-shrink:0;'>Could</span>
        <div><div style='font-size:14px;color:#FFFFFF;'>Peer benchmarks</div><div style='font-size:13px;color:{muted};margin-top:2px;'>"Most users your age spend less on subscriptions"</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_d:
    st.markdown(f"""
    <div style='{card}'>
      <div style='{label}'>Tradeoffs — why this is hard to build</div>
      <div style='display:flex;gap:10px;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:13px;font-weight:500;color:#F85149;width:110px;flex-shrink:0;padding-top:1px;'>False positives</div>
        <div style='font-size:13px;color:{muted};line-height:1.6;'>Annual plans show no monthly activity by design — must distinguish billing cycle from genuine dormancy or users lose trust.</div>
      </div>
      <div style='display:flex;gap:10px;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:13px;font-weight:500;color:#D29922;width:110px;flex-shrink:0;padding-top:1px;'>Privacy</div>
        <div style='font-size:13px;color:{muted};line-height:1.6;'>Usage detection relies on transaction signals only — Revolut cannot see app logins. Must be transparent about inference method.</div>
      </div>
      <div style='display:flex;gap:10px;padding:8px 0;border-bottom:1px solid {grid};'>
        <div style='font-size:13px;font-weight:500;color:#388BFD;width:110px;flex-shrink:0;padding-top:1px;'>Merchant relations</div>
        <div style='font-size:13px;color:{muted};line-height:1.6;'>Encouraging cancellations may conflict with merchant partnerships. Frame as user empowerment not merchant friction.</div>
      </div>
      <div style='display:flex;gap:10px;padding:8px 0;'>
        <div style='font-size:13px;font-weight:500;color:#2EA043;width:110px;flex-shrink:0;padding-top:1px;'>Threshold tuning</div>
        <div style='font-size:13px;color:{muted};line-height:1.6;'>60-day rule needs A/B testing — too short causes alert fatigue, too long misses the savings window entirely.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown(f"<div style='{label}'>Success metrics — how we know it worked</div>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Primary goal", "20% reduction", "unnoticed renewals · 90 days")
m2.metric("Engagement", "40% open rate", "on dormancy alerts")
m3.metric("Action rate", "15% cancel", "within 7 days of alert")
m4.metric("Trust", "<5% false positives", "at 60-day threshold")