import spectrumSession
import sys
import json

stbs_status_base_url = 'https://api.spectrum.net/nrs/api/stbs'

def get_stb_mac(oauth):
  r = oauth.get(stbs_status_base_url)
  json_response = json.loads(r.text)
  for stb in json_response['setTopBoxes']:
    print("Name: {} | MAC: {}".format(stb['name'], stb['macAddressNormalized']))


# Generate the session request and change the channel
oauth = spectrumSession.get_session(sys.argv[1], sys.argv[2])
get_stb_mac(oauth)





