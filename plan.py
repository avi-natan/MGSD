class Plan(object):
    object_id = 0

    def __init__(self,
                 size,
                 length,
                 intersections,
                 individual_plans):

        self.id = Plan.object_id
        self.size = size
        self.length = length
        self.intersections = intersections
        self.individual_plans = individual_plans
        Plan.object_id += 1
