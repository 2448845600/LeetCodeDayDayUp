from queue import Queue


class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id: int, level: int):
        min_levels = {}  # for input id, friend_id : min_level
        que = Queue()
        que.put((id, 0))
        min_levels[id] = 0

        level_friends = []
        while not que.empty():
            cur_id, cur_level = que.get()
            if cur_level == level:
                level_friends.append(cur_id)

            next_ids = friends[cur_id]
            for next_id in next_ids:
                if next_id in min_levels:
                    if min_levels[next_id] > cur_level + 1:
                        min_levels[next_id] = cur_level + 1
                        que.put((next_id, cur_level + 1))
                else:
                    min_levels[next_id] = cur_level + 1
                    que.put((next_id, cur_level + 1))

        level_friends_videos = {}
        for lf in level_friends:
            for videoname in watchedVideos[lf]:
                if videoname in level_friends_videos:
                    level_friends_videos[videoname] += 1
                else:
                    level_friends_videos[videoname] = 1

        level_friends_videos = sorted(level_friends_videos, key=lambda x: (level_friends_videos[x], x))
        res = [_ for _ in level_friends_videos]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.watchedVideosByFriends([["A", "B"], ["C"], ["B", "C"], ["D"]],
                                   [[1, 2], [0, 3], [0, 3], [1, 2]],
                                   0,
                                   1))
