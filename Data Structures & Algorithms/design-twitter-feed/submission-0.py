import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        # follower -> set of followees
        self.followMap = defaultdict(set)

        # user -> list of (timestamp, tweetId)
        self.tweetMap = defaultdict(list)

        # Decreasing timestamp so Python's min heap works like a max heap
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []

        # User always follows themselves
        self.followMap[userId].add(userId)

        # Collect tweets from everyone user follows
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                for tweet in self.tweetMap[followee]:
                    heapq.heappush(heap, tweet)

        ans = []

        # Return at most 10 newest tweets
        while heap and len(ans) < 10:
            time, tweetId = heapq.heappop(heap)
            ans.append(tweetId)

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Cannot unfollow yourself
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)