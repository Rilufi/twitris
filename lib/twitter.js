import Twitter from "twitter";

const screen_name = "botoronga";

class TwitterClient {
  constructor(
    keys = {
      consumer_key: process.env.CONSUMER_KEY_COR,
      consumer_secret: process.env.CONSUMER_SECRET_COR,
      access_token_key: process.env.ACCESS_TOKEN_COR,
      access_token_secret: process.env.ACCESS_TOKEN_SECRET_COR,
    }
  ) {
    this.client = new Twitter(keys);
  }

  async tweet(status) {
    return await this.client.post("statuses/update", { status });
  }

  async getLastTweet() {
    return (
      await this.client.get("statuses/user_timeline", {
        screen_name,
        count: 1,
      })
    )[0];
  }

  filterReplies(ids, mentions) {
    let replies = mentions.filter((tweet) =>
      ids.includes(tweet.in_reply_to_status_id)
    );

    if (replies.length > 0) {
      replies = replies.concat(
        this.filterReplies(
          replies.map((tweet) => tweet.id),
          mentions
        )
      );
    }

    return replies;
  }

  async getReplies(id) {
    const mentions = await this.client.get("statuses/mentions_timeline", {
      count: 200,
      since_id: id,
      trim_user: true,
    });

    const replies = this.filterReplies([id], mentions);

    return replies;
  }
}

export default TwitterClient;
