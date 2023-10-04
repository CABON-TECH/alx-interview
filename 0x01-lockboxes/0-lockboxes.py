#!/usr/bin/python3
"""Lockboxes interview qn"""


def canUnlockAll(boxes):
    """Lock box"""
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track the unlocked status of each box
    unlocked[0] = True  # The first box is initially unlocked
    keys = set(boxes[0])  # Keys available from the first box

    # Iterate through the keys and unlock boxes recursively
    while keys:
        new_keys = set()  # Store the newly discovered keys
        for key in keys:
            if not unlocked[key]:
                unlocked[key] = True
                new_keys.update(boxes[key])
        keys = new_keys - keys  # Update the keys by excluding duplicates

    return all(unlocked)
