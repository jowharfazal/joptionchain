""" Brokerage Calculator for Zerodha & Tradeplus """

import streamlit as st
import pynse

nse = pynse.Nse()

def get_option_chain(symbol):
    oc = nse.option_chain(symbol)
    oc.drop(columns=['PE.strikePrice','PE.expiryDate','PE.underlying','PE.identifier','PE.totalTradedVolume','PE.bidQty','PE.bidprice','PE.askQty','PE.askPrice','PE.underlyingValue','CE.strikePrice','CE.expiryDate','CE.underlying','CE.identifier','CE.totalTradedVolume','CE.bidQty','CE.bidprice','CE.askQty','CE.askPrice','CE.underlyingValue'],inplace=True)
    return oc


symbol = st.sidebar.selectbox("Symbol",("NIFTY","BANKNIFTY","FINNIFTY"))

oc = get_option_chain(symbol)

st.table(oc)
