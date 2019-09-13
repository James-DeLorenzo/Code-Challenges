#!/usr/bin/env python3

from datetime import datetime, timedelta

def calculateYear():
    currentTime = datetime.today()
    beginningOfYear = datetime(currentTime.year, 1, 1)
    difference = currentTime - beginningOfYear
    percent = (difference.total_seconds() / timedelta(days=365).total_seconds()) * 100
    print("We have completed {:.2f}% of {:d}.".format(percent, currentTime.year))


if __name__ == "__main__":
    calculateYear()
