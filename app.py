"""Run locally with: streamlit run app.py"""
from datetime import date
import pandas as pd
import streamlit as st
from storage import add_meal, add_symptom, connect, get_rows

st.set_page_config(page_title='IBD Nutrition & Symptom Tracker', layout='wide')
st.title('IBD Nutrition & Symptom Tracker')
st.caption('A local, personal logging tool for meals and symptoms—not medical advice or a diagnostic system.')
st.info('Privacy: entries are saved to a SQLite file on the computer running this app. Do not deploy publicly with personal health records without adding authentication, encryption, and a privacy review.')
con = connect('tracker.db')
tab_meal, tab_symptom, tab_insights = st.tabs(['Log meals', 'Log symptoms', 'Dashboard'])
with tab_meal:
    with st.form('meal_form', clear_on_submit=True):
        day = st.date_input('Meal date', date.today())
        food = st.text_input('Food / meal')
        calories = st.number_input('Estimated calories (kcal)', min_value=0, value=300)
        protein = st.number_input('Estimated protein (g)', min_value=0.0, value=10.0)
        notes = st.text_area('Notes (optional)')
        if st.form_submit_button('Save meal'):
            try:
                add_meal(con, day.isoformat(), food, calories, protein, notes)
                st.success('Meal saved locally.')
            except ValueError as exc: st.error(str(exc))
with tab_symptom:
    with st.form('symptom_form', clear_on_submit=True):
        day = st.date_input('Symptom date', date.today())
        symptom = st.selectbox('Symptom', ['Abdominal pain', 'Urgency', 'Bloating', 'Fatigue', 'Other'])
        severity = st.slider('Self-reported severity (0 to 10)', 0, 10, 3)
        notes = st.text_area('Notes (optional)', key='symptom_notes')
        if st.form_submit_button('Save symptom'):
            try:
                add_symptom(con, day.isoformat(), symptom, severity, notes)
                st.success('Symptom saved locally.')
            except ValueError as exc: st.error(str(exc))
with tab_insights:
    meals = pd.DataFrame(get_rows(con, 'meals'))
    symptoms = pd.DataFrame(get_rows(con, 'symptoms'))
    m1, m2 = st.columns(2)
    m1.metric('Meals logged', len(meals))
    m2.metric('Symptoms logged', len(symptoms))
    if not meals.empty:
        daily = meals.groupby('entry_date', as_index=True)[['calories','protein_g']].sum().sort_index()
        st.subheader('Daily estimated calories')
        st.line_chart(daily[['calories']])
        st.dataframe(meals[['entry_date','food','calories','protein_g','notes']], use_container_width=True)
        st.download_button('Export meals CSV', meals.to_csv(index=False), 'meals.csv', 'text/csv')
    else: st.info('Log meals to see calorie trends.')
    if not symptoms.empty:
        daily_s = symptoms.groupby('entry_date', as_index=True)['severity'].mean().sort_index()
        st.subheader('Mean logged symptom severity per day')
        st.line_chart(daily_s)
        st.dataframe(symptoms[['entry_date','symptom','severity','notes']], use_container_width=True)
        st.download_button('Export symptoms CSV', symptoms.to_csv(index=False), 'symptoms.csv', 'text/csv')
    else: st.info('Log symptoms to see self-reported severity trends.')
    st.caption('Patterns in self-reported data do not demonstrate causality or identify food triggers. Talk with your healthcare professional about treatment or dietary changes.')
