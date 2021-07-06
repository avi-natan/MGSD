####################################################
#                   custom colors                  #
####################################################
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
#              custom boards for json              #
####################################################
board_intersection0 = {
    "board_name": "intersection0",
    "board_width": 12,
    "board_height": 12,
    "board_critical_areas": [
        [[4, 4], [8, 8]]
    ]
}

board_intersection1 = {
    "board_name": "intersection1",
    "board_width": 12,
    "board_height": 12,
    "board_critical_areas": [
        [[3, 3], [9, 9]]
    ]
}

board_traffic_circle0 = {
    "board_name": "traffic_circle0",
    "board_width": 12,
    "board_height": 12,
    "board_critical_areas": [
        [[4, 4], [8, 5]],
        [[4, 7], [8, 8]],
        [[4, 5], [5, 7]],
        [[7, 5], [8, 7]]
    ]
}

####################################################
#                   packed boards                  #
####################################################
boards = {
    'intersection0': board_intersection0,
    'intersection1': board_intersection1,
    'traffic_circle0': board_traffic_circle0
}


####################################################
#                   custom plans                   #
####################################################
intersection0_plan_pl_12_pic_19 = [
    [(6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4)],
    [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11), (3, 11)],
    [(9, 4), (8, 4), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (10, 2), (10, 3), (10, 4)],
    [(2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (10, 8), (10, 9), (10, 10)],
    [(7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1)],
    [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6)]
]

intersection1_plan_pl_12_pic_18 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9), (4, 10)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (7, 6), (8, 6), (9, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)],
]

traffic_circle0_plan_pl_12_pic_78 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

####################################################
#                   packed plans                   #
####################################################
plans = {
    'intersection0_plans': {
        "intersection0_plan_pl_12_pic_19": intersection0_plan_pl_12_pic_19
    },
    'intersection1_plans': {
        "intersection1_plan_pl_12_pic_18": intersection1_plan_pl_12_pic_18
    },
    'traffic_circle0_plans': {
        "traffic_circle0_plan_pl_12_pic_78": traffic_circle0_plan_pl_12_pic_78
    }
}

####################################################
#         intersection tables and outcomes         #
####################################################
intersection_plan_pl_12_pic_19_make_or_break_delay_table0 = [
    [False, False, False, False, False, True, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
]
intersection_plan_pl_12_pic_19_make_or_break_outcome0 = [
    [(6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5)],
    [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 11), (4, 11)],
    [(9, 4), (8, 4), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (10, 2), (10, 3), (10, 4)],
    [(2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (10, 8), (10, 9), (10, 10)],
    [(7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1)],
    [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5)]
]

intersection_plan_pl_12_pic_19_wait_for_it_delay_table0 = [
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_19_wait_for_it_outcome0 = [
    [(6, 9), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5)],
    [(5, 2), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (4, 11)],
    [(9, 4), (8, 4), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1), (10, 2), (10, 3), (10, 4)],
    [(2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (10, 8), (10, 9), (10, 10)],
    [(7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (8, 1), (9, 1), (10, 1)],
    [(5, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6)]
]

intersection_plan_pl_12_pic_18_make_or_break_delay_table0 = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_make_or_break_outcome0 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9), (4, 10)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (7, 6), (8, 6), (9, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table0 = [
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome0 = [
    [(6, 11), (6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5)],
    [(4, 1), (4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4)],
    [(1, 3), (2, 3), (3, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (7, 6), (8, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table1 = [
    [False, False, False, False, False, False, False, False, False, False, True, False],
    [False, False, False, False, False, False, False, False, False, False, True, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome1 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (2, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9), (4, 9)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (7, 6), (8, 6), (9, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table2 = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, True, False, False, False, True, True, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome2 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (6, 5), (6, 5), (5, 5), (4, 5), (3, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 3), (4, 4), (5, 4), (5, 5), (5, 5), (5, 5), (5, 6), (5, 7), (5, 8)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 4), (6, 5), (6, 6), (7, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table3 = [
    [False, False, True, False, False, True, False, False, True, False, False, False],
    [False, False, True, False, False, True, False, False, True, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome3 = [
    [(6, 11), (6, 10), (6, 9), (6, 9), (6, 8), (6, 7), (6, 7), (6, 6), (6, 5), (6, 5), (5, 5), (4, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 3), (4, 4), (5, 4), (5, 4), (5, 5), (5, 6), (5, 6), (5, 7), (5, 8)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4)],
    [(1, 3), (2, 3), (3, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 4), (6, 4), (6, 5), (6, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table4 = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, True, True, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome4 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 3), (4, 3), (4, 4), (5, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (3, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (7, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table5 = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, True, True, False, True, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome5 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 3), (4, 3), (4, 4), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (3, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (7, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table6 = [
    [False, False, False, False, False, False, True, True, True, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome6 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (6, 5), (6, 5), (6, 5), (5, 5), (4, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9), (4, 10)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 4), (6, 4), (6, 4), (6, 5), (6, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table7 = [
    [False, False, False, False, False, False, True, True, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome7 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (6, 5), (6, 5), (5, 5), (4, 5), (3, 5)],
    [(4, 1), (4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 4), (6, 5), (6, 6), (7, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table8 = [
    [False, False, False, False, False, False, True, True, True, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome8 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (6, 5), (6, 5), (6, 5), (5, 5), (4, 5)],
    [(4, 1), (4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 4), (6, 4), (6, 5), (6, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (6, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6)],
]

intersection_plan_pl_12_pic_18_wait_for_it_delay_table9 = [
    [False, False, False, False, True, False, True, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
intersection_plan_pl_12_pic_18_wait_for_it_outcome9 = [
    [(6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 7), (6, 6), (6, 6), (6, 5), (5, 5), (4, 5), (3, 5)],
    [(4, 1), (4, 2), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9), (4, 10)],
    [(2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (9, 4)],
    [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (7, 6), (8, 6), (9, 6)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 7), (7, 7), (7, 6), (7, 5)],
    [(11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (7, 6), (7, 6), (7, 6), (7, 6), (6, 6), (5, 6), (4, 6)],
]


####################################################
#        traffic circle tables and outcomes        #
####################################################
traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table0 = [
    [False, False, False, False, False, False, True, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome0 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (7, 4), (7, 4), (7, 4), (7, 4)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table1 = [
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome1 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table2 = [
    [False, False, True, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome2 = [
    [(6, 8), (6, 7), (7, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 4), (4, 4)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (4, 5), (4, 5), (4, 5), (4, 5)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7), (5, 7)],
    [(6, 9), (6, 8), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7), (6, 7)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table3 = [
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, True, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome3 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table4 = [
    [False, False, False, False, False, True, False, False, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome4 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 7), (7, 7)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (7, 6), (7, 6), (7, 6), (7, 6)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5)],
    [(5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table5 = [
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome5 = [
    [(6, 8), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9)],
    [(5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2), (5, 2)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table6 = [
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, True, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome6 = [
    [(6, 8), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9), (6, 9)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table7 = [
    [False, True, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome7 = [
    [(6, 8), (6, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table8 = [
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, True, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome8 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3), (5, 3)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table9 = [
    [False, False, False, False, False, False, True, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome9 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 5), (7, 5), (7, 5)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (7, 4), (7, 4), (7, 4), (7, 4)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table10 = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, True, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome10 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 6), (4, 6), (4, 6)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7), (4, 7)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table11 = [
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome11 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table12 = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, True, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_make_or_break_outcome12 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table0 = [
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome0 = [
    [(6, 8), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1)],
    [(5, 2), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table1 = [
    [False, False, False, False, False, False, False, False, False, False, True, False],
    [False, False, False, False, False, False, False, False, False, False, True, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome1 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table2 = [
    [False, False, True, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, True, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome2 = [
    [(6, 8), (6, 7), (7, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table3 = [
    [False, False, True, False, False, True, False, False, True, False, False, False],
    [False, False, True, False, False, True, False, False, True, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome3 = [
    [(6, 8), (6, 7), (7, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 4), (6, 4), (6, 4), (5, 4), (4, 4)],
    [(5, 3), (5, 4), (4, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 7), (5, 7), (5, 7), (6, 7), (7, 7)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 4), (4, 5), (4, 6), (4, 6), (4, 7), (5, 7)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 4), (6, 4)],
    [(6, 9), (6, 8), (6, 7), (6, 7), (7, 7), (7, 6), (7, 6), (7, 5), (7, 4), (7, 4), (6, 4), (6, 3)],
    [(5, 2), (5, 3), (5, 4), (5, 4), (4, 4), (4, 5), (4, 5), (4, 6), (4, 7), (4, 7), (5, 7), (5, 8)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table4 = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, True, True, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome4 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (5, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table5 = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, True, True, False, True, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome5 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 4), (4, 4), (4, 5), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (6, 4), (5, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    [(5, 2), (5, 3), (5, 4), (5, 4), (5, 4), (4, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table6 = [
    [False, False, False, False, False, False, True, True, True, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome6 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 4), (6, 4), (6, 4), (5, 4), (4, 4)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 5), (7, 4), (6, 4)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (7, 4), (7, 4), (6, 4), (6, 3)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table7 = [
    [False, False, False, False, False, False, True, True, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome7 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 4), (6, 4), (5, 4), (4, 4), (4, 5)],
    [(5, 3), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 4), (6, 4), (6, 3)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(5, 2), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table8 = [
    [False, False, False, False, False, False, True, True, True, False, False, False],
    [True, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome8 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 4), (6, 4), (6, 4), (5, 4), (4, 4)],
    [(5, 3), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 5), (7, 4), (6, 4)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 4), (7, 4), (7, 4), (6, 4), (6, 3)],
    [(5, 2), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10)]
]

traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table9 = [
    [False, False, False, False, True, False, True, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]
traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome9 = [
    [(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 5), (7, 4), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5)],
    [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3)],
    [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 6), (7, 5), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]
]


####################################################
#                  packed outcomes                 #
####################################################
intersection_plan_pl_12_pic_19_outcomes = [
    # intersection_plan_pl_12_pic_19_make_or_break_outcome0,
    # intersection_plan_pl_12_pic_19_wait_for_it_outcome0
]

intersection_plan_pl_12_pic_18_outcomes = [
    # intersection_plan_pl_12_pic_18_make_or_break_outcome0,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome0,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome1,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome2,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome3,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome4,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome5,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome6,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome7,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome8,
    intersection_plan_pl_12_pic_18_wait_for_it_outcome9
]

traffic_circle_plan_pl_12_pic_78_outcomes = [
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome0,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome1,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome2,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome3,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome4,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome5,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome6,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome7,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome8,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome9,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome10,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome11,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_outcome12,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome0,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome1,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome2,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome3,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome4,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome5,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome6,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome7,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome8,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_outcome9
]


####################################################
#                packed delay tables               #
####################################################
intersection_plan_pl_12_pic_19_delay_tables = [
    # intersection_plan_pl_12_pic_19_make_or_break_delay_table0,
    # intersection_plan_pl_12_pic_19_wait_for_it_delay_table0
]

intersection_plan_pl_12_pic_18_delay_tables = [
    # intersection_plan_pl_12_pic_18_make_or_break_delay_table0,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table0,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table1,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table2,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table3,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table4,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table5,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table6,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table7,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table8,
    intersection_plan_pl_12_pic_18_wait_for_it_delay_table9
]

traffic_circle_plan_pl_12_pic_78_delay_tables = [
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table0,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table1,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table2,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table3,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table4,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table5,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table6,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table7,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table8,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table9,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table10,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table11,
    # traffic_circle_plan_pl_12_pic_78_make_or_break_delay_table12,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table0,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table1,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table2,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table3,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table4,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table5,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table6,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table7,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table8,
    # traffic_circle_plan_pl_12_pic_78_wait_for_it_delay_table9
]
