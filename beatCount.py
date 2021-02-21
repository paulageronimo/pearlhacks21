import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Takes in a spotify url and the breathing technique desired and returns a list of how many counts for every breathing in, holding, and breathing out
def countBeats(songURL,breathTechnique):
  # Create a Spotify object using a client ID from the Spotify for Developers 
  cid = '40f47c072d6a45389707cf7dd97716d9'
  secret = '6679b67d7e4b49a594adbebaaff1a4e7'
  client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
  sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

  # Getting the audio features about the selected song
  audioFeature = sp.audio_features([songURL])
  tempo = audioFeature[0]['tempo']
  
  # Different breathing techniques return a different list [breathing in, hold, breath out]
  if breathTechnique == "4-1-4":
    newTempo = [(tempo/60)*4,1,(tempo/60)*4]
  elif breathTechnique == "4-7-8":
    newTempo = [(tempo/60)*4, (tempo/60)*7, (tempo/60)*8]
  elif breathTechnique == "5-1-5":
    newTempo = [(tempo/60)*5, 1, (tempo/60)*5]
  
  return {'breathing in':newTempo[0],'hold':newTempo[1],'breathing out':newTempo[2]}
