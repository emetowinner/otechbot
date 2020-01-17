import tweepy
import logging
import os

logger = logging.getLogger()
def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api



    """
export CONSUMER_KEY="eObu9q7cVfkJYMCwUmXtnVwXr"
export CONSUMER_SECRET="v7O3anwt4KdX7na3Iu4m1f06FuDmRJXX5ugJvaOtTPqnQuHqhm"
export ACCESS_TOKEN="1199602560472166400-N2IzWFM2qwyPx9Pn4h42ibKp6Nco5a"
export ACCESS_TOKEN_SECRET="Kxn7yES5VtNNIsQ4JWPMa2BvflR9rXgJUKGbKLfOc6fdp"


    """