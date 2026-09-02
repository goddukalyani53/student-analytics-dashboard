import streamlit as st
import pandas as pd
import sqlite3

# Page Configuration Setup 
st.set_page_config(page_title="College Analytics Dashboard", layout="wide")
st.title("🎓 College Analytics Dashboard")

# Connect to database 
conn = sqlite3.connect("college.db")

# Sidebar Filter Configuration
try:
    branches_df = pd.read_sql_query("SELECT DISTINCT branch FROM students", conn)
    branches = ["All"] + list(branches_df["branch"].values)
except:
    branches = ["All", "CSE", "ECE", "ME", "EEE", "Civil"]

selected_branch = st.sidebar.selectbox("Select Branch/Department", branches)

# Dynamic Logical Base Filter Query Allocation
if selected_branch == "All":
    students_df = pd.read_sql_query("SELECT * FROM students", conn)
    attendance_df = pd.read_sql_query("SELECT * FROM attendance", conn)
else:
    students_df = pd.read_sql_query(f"SELECT * FROM students WHERE branch = '{selected_branch}'", conn)
    attendance_df = pd.read_sql_query(f"""
        SELECT a.* FROM attendance a 
        JOIN students s ON a.student_id = s.student_id 
        WHERE s.branch = '{selected_branch}'
    """, conn)

resources_df = pd.read_sql_query("SELECT resource_name, downloads FROM resources ORDER BY downloads DESC", conn)

# 1. Top Core Metrics KPIs Block
total_students = len(students_df)

if len(attendance_df) > 0:
    present_count = len(attendance_df[attendance_df['status'] == 'Present'])
    avg_attendance = (present_count / len(attendance_df)) * 100
    attendance_metric_value = f"{avg_attendance:.1f}%"
else:
    attendance_metric_value = "0.0%"

top_resource = resources_df["resource_name"].iloc[0] if not resources_df.empty else "N/A"

# Grid Columns Generation Matrix Layout Rendering
m1, m2, m3 = st.columns(3)
m1.metric("Total Students", total_students)
m2.metric("Average Attendance Rate", attendance_metric_value)
m3.metric("Top Study Resource", top_resource)

st.markdown("---")

# 2. Charts Visual Grid Layout
chart_col, data_col = st.columns(2)

with chart_col:
    st.subheader("📊 Attendance Overview (Present vs Absent)")
    if len(attendance_df) > 0:
        status_counts = attendance_df['status'].value_counts()
        st.bar_chart(status_counts)
    else:
        st.info("No data tracking entries mapped.")

with data_col:
    st.subheader("💡 Top Downloaded Resources Track Analytics")
    st.dataframe(resources_df, use_container_width=True, hide_index=True)

conn.close()