#!/usr/bin/env python

"""
Greedy algorithm for minimizing the weighted sum of
all job completion times.

When put in a sequential schedule a jobs completion
time is its length + the completion time of the prior
job. For example, 3 jobs with lengths 1,2,3 and done
in that order would have completion times:

    1 -> 3 -> 6

A weighted completion time takes the completion 
time and multiplies it by a weight. For example,
jobs (1,3), (2,2),(3,1) where the tuple is (l,w)
would have the following weighted completion times:

    (1*3)->(3*2)->(6*1)
    3 -> 6 -> 6 = 15


"""

def load_data(filename):
    """ Generate edge list from text file """
    file = open(filename, 'r')
    return  map(lambda x: [int(x[0]), int(x[1])], map(lambda x: x.rstrip().split(' '), file))

def subtract_score(job):
    return (job[0] - job[1], job)

def divide_score(job):
    job = map(float, job)
    return (job[0] / job[1], job)

def generate_scores(arr):
    data = map(subtract_score, arr)
    data.sort(key=lambda x: x[1][1], reverse=True)
    data.sort(key=lambda x: x[0], reverse=True)
    data = filter_scores(data)
    data = calc_unweighted(data)
    data = weight_scores(data)
    return sum(data)

def filter_scores(arr):
    return map(lambda x: x[1], arr)

def calc_unweighted(arr):
    for i,el in enumerate(arr):
        if i > 0:
            arr[i][1] += arr[i-1][1]
    return arr

def weight_scores(arr):
    return map(lambda x: x[0]*x[1], arr)

#job_list =  [[8,50]
#            ,[74,59]
#            ,[31,73]
#            ,[45,79]
#            ,[24,10]
#            ,[41,66]
#            ,[93,43]
#            ,[88,4]
#            ,[28,30]
#            ,[41,13]
#            ,[4,70]
#            ,[10,58]
#]
job_list =  [[8,50]
            ,[74,59]
            ,[31,73]
            ,[45,79]
            ,[24,10]
            ,[41,66]
            ]
if __name__ == '__main__':
    job_list = load_data('job-scheduler-data.txt')
    print generate_scores(job_list)
