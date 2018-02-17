import speedtest

st = speedtest.Speedtest()

st.get_best_server()

print (st.download())