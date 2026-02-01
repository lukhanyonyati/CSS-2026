#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 13:48:38 2026

@author: lukhanyonyati
"""

import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Dr. Lukhanyo Nyati"
field = "Nutritional & Life-course Epidemiology"
institution = "University of the Western Cape"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

# Add sections of the profile
profile = """I am a researcher public health and academic leader with extensive experience in child growth, nutritional and life-course epidemiology, health data analytics, and community-oriented engagement. My work covers scientific research, curriculum innovation, research governance, and public empowerment.

I currently serve as the Coordinator for the Master of Health Data Analytics programme at the University of the Western Cape, where I guide curriculum design and lead efforts to train the next generation of health data scientists. This Master’s programme is a key postgraduate qualification offered through the Faculty of Community and Health Sciences, equipping students with advanced analytical skills to interpret and apply health data for decision-making and systems improvement.  

As a Senior Lecturer in Nutritional and Life-course Epidemiology, I teach and supervise research that examines health trajectories across populations and lifespans, combining nutritional insights with epidemiological methods. My academic contributions focus on generating evidence that supports healthier lives and systems, particularly in global and African contexts.

I am the Principal Investigator of the Men in Transition research project, a programme committed to understanding and engaging men in health, identity, and social transformation, building on broader work in men and masculinities that explores how constructions of gender shape health outcomes and social engagement.  

My leadership extends beyond research and teaching. I serve as an executive member of the Biomedical Research Ethics Committee (BMREC) at UWC, contributing to the ethical governance of research to protect research participants and uphold integrity. I am also a certified trainer in REDCap and quantitative research methodologies, equipping researchers with practical, robust skills for data collection, management, and analysis using cutting-edge digital tools.  

In the community sphere, I conduct initiatives focused on men and boys, promoting positive health behaviours, social responsibility, and transformative engagement that addresses structural and behavioural determinants of health. I also co-host The Pulse of the Nation on The Voice Lounge - a dynamic online radio platform that amplifies meaningful dialogue on societal issues, health, and empowerment, merging media outreach with educational and social discourse."""

# Add over view of profile
st.subheader("Educator • Epidemiology Researcher • Public Speaker • Mentor & Coach")
st.write(f"{profile}")


# Add a contact section
st.header("Contact Information")
email = "hnyati@uwc.ac.za"
st.write(f"You can reach {name} at {email}.")