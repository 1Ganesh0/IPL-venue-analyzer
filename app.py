import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🏏 IPL Venue Intelligence System")

df = pd.read_csv("IPL.csv")
df.columns = df.columns.str.strip()

venues = sorted(df['venue'].dropna().unique())
venue_name = st.selectbox("Select Venue", venues)

if st.button("Analyze Venue"):

    venue_df = df[df['venue'] == venue_name]

    st.subheader(f"{venue_name}")

    total_matches = venue_df['match_id'].nunique()
    st.write("Total Matches:", total_matches)

    scores = venue_df.groupby(['match_id','innings'])['runs_total'].sum().reset_index()
    avg_score = scores['runs_total'].mean()
    st.write("Average Score:", round(avg_score,2))

    pp_runs = venue_df[venue_df['over'] <= 6] \
        .groupby(['match_id','innings'])['runs_total'].sum().reset_index()
    pp_avg = pp_runs['runs_total'].mean()

    death_runs = venue_df[venue_df['over'] >= 16] \
        .groupby(['match_id','innings'])['runs_total'].sum().reset_index()
    death_avg = death_runs['runs_total'].mean()

    st.write("Avg Powerplay Runs:", round(pp_avg,2))
    st.write("Avg Death Runs:", round(death_avg,2))

    match_scores = scores.pivot_table(index='match_id', columns='innings', values='runs_total').reset_index()
    match_scores = match_scores[[col for col in match_scores.columns if col in ['match_id',1,2]]]
    match_scores.columns = ['match_id','inn1','inn2']

    match_scores['winner'] = np.where(match_scores['inn1'] > match_scores['inn2'], 1, 2)
    chasing_win_rate = (match_scores['winner'] == 2).mean()

    st.write("Chasing Win %:", round(chasing_win_rate*100,2))

    st.subheader("Insights")

    if avg_score > 170:
        st.write("High scoring venue")
    elif avg_score > 150:
        st.write("Moderate scoring venue")
    else:
        st.write("Low scoring venue")

    if chasing_win_rate > 0.55:
        st.write("Prefer chasing")
    elif chasing_win_rate < 0.45:
        st.write("Prefer defending")
    else:
        st.write("Toss neutral")

    fig, ax = plt.subplots()
    sns.histplot(scores['runs_total'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)
