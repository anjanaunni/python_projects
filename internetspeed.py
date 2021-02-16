from speedtest import Speedtest
st= Speedtest()
print("Download Speed in bps",st.download())
print("Upload Speed bps",st.upload())
