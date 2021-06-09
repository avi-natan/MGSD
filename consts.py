colors = {
    0: (0, 1, 0),
    1: (0, 0, 1),
    2: (0.5, 0, 0),
    3: (0, 0.5, 0),
    4: (0, 0, 0.5),
    5: (0.1, 0.8, 0.8),
    6: (1, 0.1, 1),
    7: (1, 1, 0.1),
    8: (1, 0.7, 0),
    9: (0.6, 0, 0.6),
    10: (1, 0, 0.4),
    11: (0.3, 0.3, 0.3)
}

####################################################
#                   custom plans                   #
####################################################
intersection_custom_plan1 = [
    [(6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4)],
    [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11)],
    [(9, 4), (8, 4), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (10, 2), (10, 3), (10, 4)],
    [(2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (10, 8), (10, 9), (10, 10)],
    [(7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1)],
    [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6)]
]

traffic_circle_custom_plan1 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

####################################################
#              make or break outcomes              #
####################################################
intersection_custom_plan1_make_or_break_outcome1 = [
    [(6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5)],
    [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 11), (4, 11)],
    [(9, 4), (8, 4), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (10, 2), (10, 3), (10, 4)],
    [(2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (10, 8), (10, 9), (10, 10)],
    [(7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1)],
    [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5)]
]

traffic_circle_custom_plan1_make_or_break_outcome1 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (7, 4), (7, 4), (7, 4), (7, 4)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_custom_plan1_make_or_break_outcome2 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_custom_plan1_make_or_break_outcome3 = [
    [(6, 8), (6, 7), (7, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 4), (4, 4)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (4, 5), (4, 5), (4, 5), (4, 5)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7)],
    [(6, 9), (6, 8), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6)]
]

traffic_circle_custom_plan1_make_or_break_outcome4 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7)]
]

traffic_circle_custom_plan1_make_or_break_outcome5 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 7), (7, 7)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (7, 6), (7, 6), (7, 6), (7, 6)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5)],
    [(5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2)]
]

traffic_circle_custom_plan1_make_or_break_outcome6 = [
    [(6, 8), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9)],
    [(5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2)]
]

traffic_circle_custom_plan1_make_or_break_outcome7 = [
    [(6, 8), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7)]
]

traffic_circle_custom_plan1_make_or_break_outcome8 = [
    [(6, 8), (6, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_custom_plan1_make_or_break_outcome9 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3)]
]

traffic_circle_custom_plan1_make_or_break_outcome10 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (7, 4), (7, 4), (7, 4), (7, 4)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_custom_plan1_make_or_break_outcome11 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7)]
]

traffic_circle_custom_plan1_make_or_break_outcome12 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_custom_plan1_make_or_break_outcome13 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

####################################################
#               wait for it outcomes               #
####################################################
# TODO


####################################################
#                  packed outcomes                 #
####################################################
intersection_custom_plan1_outcomes = [
    # intersection_custom_plan1_make_or_break_outcome1
]

traffic_circle_custom_plan1_outcomes = [
    traffic_circle_custom_plan1_make_or_break_outcome1,
    traffic_circle_custom_plan1_make_or_break_outcome2,
    traffic_circle_custom_plan1_make_or_break_outcome3,
    traffic_circle_custom_plan1_make_or_break_outcome4,
    traffic_circle_custom_plan1_make_or_break_outcome5,
    traffic_circle_custom_plan1_make_or_break_outcome6,
    traffic_circle_custom_plan1_make_or_break_outcome7,
    traffic_circle_custom_plan1_make_or_break_outcome8,
    traffic_circle_custom_plan1_make_or_break_outcome9,
    traffic_circle_custom_plan1_make_or_break_outcome10,
    traffic_circle_custom_plan1_make_or_break_outcome11,
    traffic_circle_custom_plan1_make_or_break_outcome12,
    traffic_circle_custom_plan1_make_or_break_outcome13
]

