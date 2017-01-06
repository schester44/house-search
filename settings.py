# twenty minutes
SLEEP_INTERVAL = 20 * 60

# replace with your slack token - https://api.slack.com/docs/oauth-test-tokens
SLACK_TOKEN = '<your slack token>'

# the channel to broadcast houses to
SLACK_CHANNEL = '#houses'

# the region (http://<region>.craigslist.org) where <region> is CITY
CITY = 'pittsburgh'

# minimum housing price
MIN_PRICE = 700

# maximum housing price
MAX_PRICE = 1200

# used to find listing based on these keywords in listing titles
NEIGHBORHOODS = ["mount washington", "mt. washington", "dormont", "mt washington", "greentree", "green tree", "shadyside", "shady side", "lawerenceville", "bloomfield", "friendship", "highland park", "east liberty", "west end", "south side"]

# used to find listings based on listing supplied coordinates
# http://boundingbox.klokantech.com/ for coords
BOXES = {
	"dormont" : [
		[-80.051193, 40.38029],
		[-80.00742, 40.404156]
	],
	"mt_washington" : [
		[-80.0354, 40.419704],
		[-80.005188, 40.446751]
	],
	"greentree" : [
		[-80.0354, 40.419704],
		[-80.005188, 40.446751]
	],
	"east_end" : [
		[-79.978752, 40.427872],
		[-79.896011, 40.486387]
	]
}