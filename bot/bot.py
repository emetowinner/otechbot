import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class RetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            # Ignore the tweet because is a reply or I'm its author
            return
        if not tweet.favorited:
            # Mark it as Liked
            try:
                tweet.favorite()
            except Exception as e:
                logger.error(
                    "Error occured while liking the tweet", exc_info=True)
                print(e)
        if not tweet.retweeted:
            # Retweet, if it haven't retweeted yet
            try:
                tweet.retweet()
                logger.info(f"Repling tweet id {tweet.id}")
                self.api.update_status(
                    f'@{tweet.user.screen_name} @mtechdevimo @WPowerri @owerriTechHub @OluakaInstitute @LaravelOwerri @WomenProTech1 @pyladiesimo @dscimsu @Genesysclubfuto @BleauTechOrg @oscaimo @ingressiveIMSU @dsc_futo @dotnetseNG', in_reply_to_status_id=tweet.id)
                self.api.update_status(
                    f'@{tweet.user.screen_name} @mtcowerri @gdgowerri @thaimpactcircle @losintech', in_reply_to_status_id=tweet.id)

            except Exception:
                logger.error("Error on fav and retweet", exc_info=True)

        try:
            logger.info("Retrieving and following followers")
            for follower in tweepy.Cursor(self.api.followers).items():
                if not follower.following:
                    logger.info(f"Following {follower.name}")
                    follower.follow()
        except Exception:
            logger.error("Error occured trying to follow", exc_info=True)
            pass

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api()
    tweets_listener = RetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    main(["OwerriTech", "owerritech", "Owerritech", "owerriTech",'EndSARS', 'EndSarsNow' ])
