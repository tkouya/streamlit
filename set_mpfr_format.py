# test_streamlit.py: Streamlitアプリ
import streamlit as st # Streamlit
import numpy as np # NumPy
import gmpy2 # GMPy2

# set context
ctx = gmpy2.get_context()

st.write('Test program for gmpy2 and Sreamlit')
#st.write('ctx = ', ctx)
user_prec = st.number_input('Prec in bit: ', value=53)
if user_prec >= 0:
    #user_prec = st.number_input('Prec in bit: ')
    ctx.precision = user_prec
    st.write('ctx prec in bit = ', ctx.precision)
    a = gmpy2.sqrt(gmpy2.mpfr('2'))
    b = gmpy2.sqrt(gmpy2.mpfr('3'))
    st.write('Pi = ', gmpy2.const_pi())
    #st.write('Pi in bit = ', gmpy2.to_binary(gmpy2.const_pi()))
    st.write('sqrt(2) + sqrt(3) = ', a + b)
