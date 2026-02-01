#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 23:00:14 2026

@author: lukhanyonyati
"""

import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Researcher Profile | Dr. Lukhanyo Nyati",
    layout="wide"
)

# --------------------------------------------------
# App title
# --------------------------------------------------
st.title("Researcher Profile Page with STEM Data")

# --------------------------------------------------
# Basic profile information
# --------------------------------------------------
name = "Dr. Lukhanyo Nyati"
field = "Nutritional & Life-course Epidemiology"
institution = "University of the Western Cape"
email = "hnyati@uwc.ac.za"

st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)",
    use_container_width=True
)

# --------------------------------------------------
# Sidebar navigation
# --------------------------------------------------
with st.sidebar:
    st.title("Sections")
    selection = st.radio(
        "Go to:",
        ["About", "Publications", "Projects", "Contact"]
    )

# --------------------------------------------------
# Profile text
# --------------------------------------------------
profile = """
I am a public health researcher and academic leader with extensive experience in child development, nutritional and life-course epidemiology, health data analytics, and community-oriented engagement.

I currently serve as the **Coordinator for the Master of Health Data Analytics programme** at the University of the Western Cape, where I guide curriculum design and lead efforts to train the next generation of health data scientists.

As a **Senior Lecturer in Nutritional and Life-course Epidemiology**, I teach and supervise research that examines health trajectories across populations and lifespans.

I am the **Principal Investigator of the Men in Transition research project**, a programme focused on understanding how constructions of gender shape health outcomes and social engagement.

I also serve as an **executive member of the Biomedical Research Ethics Committee (BMREC)** at UWC and am a certified **REDCap and quantitative research methodologies trainer**.

Beyond academia, I engage communities through programmes for men and boys and co-host **The Pulse of the Nation** on The Voice Lounge online radio platform.
"""

# --------------------------------------------------
# Page content routing
# --------------------------------------------------
if selection == "About":
    st.subheader("Educator • Researcher • Public Speaker • Trainer • Mentor & Coach")
    st.write(profile)

elif selection == "Publications":
    st.subheader("Publications")
    st.write(
        """
        • Over **30 peer-reviewed publications**  
        • More than **500 academic citations**  
        • Research spanning child health, nutrition, life-course epidemiology,
          masculinities, and public health systems
        """
    )

elif selection == "Projects":
    st.subheader("Research Projects")
    st.write(
        """
        **Men in Transition Research Project**  
        A multidisciplinary programme examining how men engage with health,
        identity, and social transformation in South Africa.

        **Health Data Analytics Capacity Building**  
        Projects focused on training health professionals in advanced data
        analytics, evidence-informed decision-making, and ethical data governance.
        """
    )

elif selection == "Contact":
    st.subheader("Contact Information")
    st.write(f"📧 **Email:** {email}")
    st.write("📍 **Institution:** University of the Western Cape")

# --------------------------------------------------
# Roles & responsibilities
# --------------------------------------------------
st.divider()
st.subheader("Selected Roles & Responsibilities")

st.write("### Academic Leadership")
st.write(
    """
    • Senior Lecturer, Nutritional and Life-course Epidemiology  
    • Coordinator, Master of Health Data Analytics Programme
    """
)

st.write("### Research Leadership")
st.write(
    """
    • Principal Investigator, Men in Transition Research Project  
    • Executive Member, Biomedical Research Ethics Committee (BMREC)
    """
)

st.write("### Training & Mentorship")
st.write(
    """
    • Trainer in Quantitative Research Methods & REDCap  
    • Postgraduate supervision and early-career researcher mentorship
    """
)

st.write("### Community & Media Engagement")
st.write(
    """
    • Coach for Men and Boys  
    • Radio Co-host, *The Pulse of the Nation* – The Voice Lounge
    """
)

# --------------------------------------------------
# Skills & expertise
# --------------------------------------------------
st.divider()
st.subheader("Core Areas of Expertise")

st.write(
    """
    • **Data & Tools:** R, REDCap  
    • **Statistical Modelling:** Longitudinal analysis, regression modelling, growth curves  
    • **Research Methods:** Survey design, protocol development, ethical research practice  
    • **Communication:** Academic writing, public speaking, radio broadcasting
    """
)