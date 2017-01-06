from craigslist import CraigslistHousing
from slackclient import SlackClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse
from utils import find_points_of_interest, post_listing_to_slack
import settings

engine = create_engine('sqlite:///listings.db', echo=False)

Base = declarative_base()

class Listing(Base):
    """
    A table to store data on craigslist listings.
    """

    __tablename__ = 'listings'

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    created = Column(DateTime)
    geotag = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    name = Column(String)
    price = Column(Float)
    location = Column(String)
    cl_id = Column(Integer, unique=True)
    area = Column(String)
    bart_stop = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

housing = CraigslistHousing(
	site= settings.CITY,
	category = 'apa',
	filters = {
		'min_price' : settings.MIN_PRICE,
		'max_price' : settings.MAX_PRICE,
		'has_image' : True,
	})

def get_results():
	results = []
	gen = housing.get_results(sort_by = 'newest', geotagged = True, limit = 100)

	while True:
		try:
			result = next(gen)


		except StopIteration:
			break
		except Exception:
			continue

		listing = session.query(Listing).filter_by(cl_id=result["id"]).first()
		
		# Don't store the listing if it already exists.
		if listing is None:
			if result["where"] is None:
				continue

			lat = 0
			lon = 0

			if result["geotag"] is not None:
			    lat = result["geotag"][0]
			    lon = result["geotag"][1]

			    geo_data = find_points_of_interest(result["geotag"], result["where"])
			    result.update(geo_data)
			else:
			    result["area"] = ""

			price = 0
			try:
			    price = float(result["price"].replace("$", ""))
			except Exception:
			    pass
			
			# Create the listing object.
			listing = Listing(
			    link=result["url"],
			    created=parse(result["datetime"]),
			    lat=lat,
			    lon=lon,
			    name=result["name"],
			    price=price,
			    location=result["where"],
			    cl_id=result["id"],
			    area=result["area"]
			)

			# Save the listing so we don't grab it again.
			session.add(listing)
			session.commit()

			if len(result["area"]) > 0:
			    results.append(result)

	return results

def do_scrape():
	sc = SlackClient(settings.SLACK_TOKEN)

	all_results = get_results()
	
	for result in all_results:
		post_listing_to_slack(sc, result)