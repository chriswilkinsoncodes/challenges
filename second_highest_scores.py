#!/usr/bin/env python3

'''
There's been a cheating scandal at this year's City Hacker Championship!
An investigation determined all of the first place finishers colluded
to achieve the same highest score.

As the Championship's prize coordinator, you now need to identify all
the runners up so they can share the top prize.

You have been given a list of lists (nested list) containing the
championship results. From the list of [name, score] sublists, print
alphabetically the names of all competitors that scored second-highest.

Sample Input:
results = [['Pal', 9], ['Tran', 8] ['Fox', 6], ['Carr', 9], ['Cruz', 8]]

Sample Output:
Cruz
Tran

Additional Challenges:
* Include additional placements in the output, e.g. 2nd, 3rd...
* With the additional placements output, include the competitors' scores
* Allow user or file input of results
'''
from itertools import groupby


def get_runners_up1(results):
    # Solution using lists
    # set an empty list of runners up that will be populated and
    # returned at the end of this function
    runners_up = []

    # sort results from highest to lowest
    # lambda function used to look at the score of each name, score list
    results.sort(key=lambda x: x[1], reverse=True)
    
    # from the results list set the highest score and
    # remove its first instance from the list of results
    highest = results.pop(0)[1]
    
    # remove additional results that contain the highest score
    while results[0][1] == highest:
        results.pop(0)
    
    # the second highest score is now in the first result in the list
    second_highest = results[0][1]
    
    # identify all results that include the second highest score
    while results != [] and results[0][1] == second_highest:
        # append names with second highest score to list of runners up
        runners_up.append(results.pop(0)[0])
    
    # return list of runners up, sorted alphabetically
    return sorted(runners_up)


def get_runners_up2(results):
    # Solution using a set
    runners_up = []
    scores = set()
    for i in range(len(results)):
        scores.add(results[i][1])
    second_highest = sorted(scores)[-2]
    for name, score in results:
        if score == second_highest:
            runners_up.append(name)
    return sorted(runners_up)


def get_runners_up3(results):
    # Solution using list comprehensions
    results.sort(key=lambda x: x[1], reverse=True)
    results_no_high = [i for i in results if i[1] != results[0][1]]
    scnd_high_results = [j for j in results_no_high 
        if j[1] == results_no_high[0][1]]
    scnd_high_results.sort(key=lambda x: x[1])
    return sorted([scnd_high_results[i][0] 
        for i in range(len(scnd_high_results))])


def get_runners_up4(results):
    # Solution using set and comprehensions
    scores = sorted({results[i][1] for i in range(len(results))})
    return sorted([results[i][0] for i in range(len(results)) 
        if results[i][1] == scores[-2]])


def get_runners_up5(results):
    # Solution using groupby
	list_ = sorted(results, key=lambda x: (x[1], x[0]))
	return [[names for names,_ in group]
            for key, group in groupby(list_, key=lambda x: x[1])][-2]


def get_runners_up6(results):
    # solution using dictionary
	d = dict()
	for name, scored in sorted(results, key=lambda x: (x[1], x[0])):
		d.setdefault(scores, []).append(name)
    # d.keys() is an iterable of the dict's keys (which are the scores)
    # but it's not subscriptable, so it needs to be converted to a list.
	return d[list(d.keys())[-2]]


if __name__ == '__main__':
    results = [['Terry', 94.1], ['Mason', 97.7], ['Ali', 96.9],
    ['Wise', 92], ['Rojas', 96.9], ['Jensen', 92.4], ['Bauer', 91.6],
    ['Cooper', 97.7], ['Erickson', 93.2], ['Parks', 95.3],
    ['Patel', 96.9], ['Cobb', 92.5], ['Murphy', 97.7], ['Adams', 94.5],
    ['Le', 93.7], ['Ray', 95.3], ['Scott', 96.9], ['Malone', 94.1],
    ['Booth', 94], ['Ross', 93.2]]

    # update "get_runners_up" to try alternative functions
    for runner_up in get_runners_up1(results):
        print(runner_up)
