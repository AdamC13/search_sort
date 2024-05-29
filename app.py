from flask import Flask
from flask_restful import Resource, Api

app = Flask("VideoApi")
api = Api(app)




def binary_search(lst, target):
    # Set a low and high point on the list
    low = 0
    high = len(lst) - 1
    num_checks = 0
    # Keep finding the middle element as long as low is less than or equalt to high
    while low <= high:
        # Get the middle of low + high
        mid = (low + high) // 2
        num_checks += 1
        # Check if the target is the mid
        if target == lst[mid]["title"]:
            return f"{target} can be found at index {mid} and it took {num_checks} checks"
        # if the target is greater than the mid point
        elif target > lst[mid]["title"]:
            # Set the low to be one higher than mid
            low = mid + 1
        # if the target is lower than mid
        else:
            # Set the high to be one lower than mid
            high = mid - 1
    # if low ever passes high, we know the target is not there
    print('Not Found, checks:', num_checks)
    return ('Video Not Found')


# can't binary search by title if it's sorted by id
videos = [
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]

videos_sorted = [
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]


class vid_search(Resource):

    def get(self, video_title):
        return binary_search(videos_sorted, video_title)


api.add_resource(vid_search, '/<video_title>')



if __name__ == "__main__":
    app.run(debug=True)