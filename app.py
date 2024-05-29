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

def merge_sort(lst):
    # Check if our list can be split in half
    if len(lst) > 1:
        # Find the midway point
        mid = len(lst) // 2
        # Split the list into a left and right
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Call merge_sort on left half
        merge_sort(left_half)
        # Call merge_sort on right half
        merge_sort(right_half)

        # Merge the left and right half lists back into the original list
        # index pointers for the three lists
        l = 0 # pointer for left half
        r = 0 # pointer for right half
        m = 0 # pointer for main list (lst)

        # While the left and right pointers are still pointing at valid indices
        while l < len(left_half) and r < len(right_half):
            # Compare the value at left pointer vs right pointer 
            if left_half[l]['title'] < right_half[r]['title']:
                # Copy the left half value into the main list
                lst[m] = left_half[l]
                # Move the left pointer right one spot
                l += 1
            else:
                # Copy the right half value into the main list
                lst[m] = right_half[r]
                # Move the right pointer right one spot
                r += 1
            # Either way, we always increse the main pointer one spot
            m += 1

        # When one half finishes (either left or right), copy the rest of the other half into the original
        while l < len(left_half):
            lst[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1
    return lst


# videos_sorted = [
#     {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
#     {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
#     {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
#     {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
#     {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
#     {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
#     {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
#     {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
#     {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
#     {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
# ]

videos_sorted = merge_sort(videos)

class vid_search(Resource):

    def get(self, video_title):
        return binary_search(videos_sorted, video_title)


class SortedVids(Resource):

    def get(self):
        return videos_sorted


api.add_resource(vid_search, '/<video_title>')
api.add_resource(SortedVids, '/')




if __name__ == "__main__":
    app.run(debug=True)