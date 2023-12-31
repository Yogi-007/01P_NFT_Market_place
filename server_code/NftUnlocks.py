import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def get_my_nfts():
  user = anvil.users.get_user()
  if user == None:
    return []
  if not user['owned_nfts']:
    return []
  nfts = []
  for nft in user['owned_nfts']:
    nfts_info = app_tables.nfts.get(id_name=nft)
    nfts.append(nfts_info)
  return nfts
