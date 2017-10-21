import sys
import spectrumSession

tune_channel_base_url = 'https://api.spectrum.net/ipvs/api/smarttv/epg/v0/stb/tune'
    
def change_channel(oauth, channel, mac):
	params = {'apicall': 'tune-channel', 'channel': channel, 'mac': mac}
	r = oauth.get(tune_channel_base_url, params=params)
	print(r.text)


# Generate the session request and change the channel
oauth = spectrumSession.get_session(sys.argv[1], sys.argv[2])
change_channel(oauth, sys.argv[3], sys.argv[4])





