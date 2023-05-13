import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("SVCmodel.pkl", "rb"))

def buy_encoder(buy):
	if buy == "high":
		return 0
	elif buy == "low":
		return 1
	elif buy == "med":
		return 2
	else:
		return 3

def maint_encoder(maint):
	if maint == "high":
		return 0
	elif maint == "low":
		return 1
	elif maint == "med":
		return 2
	else:
		return 3

def lugboot_encoder(lug_boot):
	if lug_boot == "big":
		return 0
	elif lug_boot == "med":
		return 1
	else:
		return 2

def safety_encoder(safety):
	if safety == "high":
		return 0
	elif safety == "low":
		return 1
	else:
		return 2

def doors_encoder(doors):
	if doors == "2":
		return 0
	elif doors == "3":
		return 1
	elif doors == "4":
		return 2
	else:
		return 3

def persons_encoder(persons):
	if persons == "2":
		return 0
	elif persons == "4":
		return 1
	else:
		return 2

def res_encoder(res):
	if res == 0:
		return st.success("Accurate!")
	elif res == 1:
		return st.success("Good!")
	elif res == 2:
		return st.success("Unaccurate!")
	else:
		return st.success("Very Good!")

st.title("Car Acceptability Predictor")
buying = st.selectbox("Buying", ("high", "low", "med", "vhigh"))
maint = st.selectbox("Maint", ("high", "low", "med", "vhigh"))
doors = st.selectbox("Doors", ("2", "3", "4", "5more"))
persons = st.selectbox("Persons", ("2", "4", "more"))
lug_boot = st.selectbox("Lug_boot", ("big", "med", "small"))
safety = st.selectbox("Safety", ("high", "low", "med"))

if st.button("Predict"):
	buying = buy_encoder(buying)
	maint = maint_encoder(maint)
	doors = doors_encoder(doors)
	persons = persons_encoder(persons)
	lug_boot = lugboot_encoder(lug_boot)
	safety = safety_encoder(safety)

	res = model.predict([[buying, maint, doors, persons, lug_boot, safety]]).item()
	#print(res)
	res_encoder(res)

