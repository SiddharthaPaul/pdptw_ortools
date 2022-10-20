def create_data_model():
    """Stores the data for the problem."""
    data = {}
    ## Lets consider 8 orders which we need to batch and assign DEs. Each order has a pickup and drop point.

    ## Odd integers are pickup nodes and even integers are drop nodes
    data['pickups_deliveries'] = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10],
        [11, 12],
        [13, 14],
        [15, 16],
    ]

    ## Node to Node distance matrix
    data['distance_matrix'] = [
        [
            0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354,
            468, 776, 662
        ],
        [
            548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674,
            1016, 868, 1210
        ],
        [
            776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164,
            1130, 788, 1552, 754
        ],
        [
            696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822,
            1164, 560, 1358
        ],
        [
            582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708,
            1050, 674, 1244
        ],
        [
            274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628,
            514, 1050, 708
        ],
        [
            502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856,
            514, 1278, 480
        ],
        [
            194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320,
            662, 742, 856
        ],
        [
            308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662,
            320, 1084, 514
        ],
        [
            194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388,
            274, 810, 468
        ],
        [
            536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764,
            730, 388, 1152, 354
        ],
        [
            502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114,
            308, 650, 274, 844
        ],
        [
            388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194,
            536, 388, 730
        ],
        [
            354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0,
            342, 422, 536
        ],
        [
            468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536,
            342, 0, 764, 194
        ],
        [
            776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274,
            388, 422, 764, 0, 798
        ],
        [
            662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730,
            536, 194, 798, 0
        ],
    ]



    # Setting the vehicle speed in KMPH
    vehicle_speed = 10

    ## Travel time matrix
    time_matrix = {}
    for from_node in range(len(data['distance_matrix'])):
        time_matrix[from_node]= {}
        for to_node in range(len(data['distance_matrix'])):
            time_matrix[from_node][to_node]=data['distance_matrix'][from_node][to_node]*60/(vehicle_speed*1000)

    data['time_matrix'] = time_matrix

    data['time_windows'] = [
        (0, 150),  # depot
        (1, 12),  # 1
        (5, 15),  # 2
        (1, 11),  # 3
        (5, 13),  # 4
        (0, 15),  # 5
        (10, 20),  # 6
        (0, 10),  # 7
        (5, 20),  # 8
        (0, 8),  # 9
        (5, 16),  # 10
        (1, 5),  # 11
        (3, 15),  # 12
        (1, 10),  # 13
        (1, 18),  # 14
        (1, 15),  # 15
        (5, 25),  # 16
    ]
    data['num_vehicles'] = 4

    ## Setting vehicle capacities
    data['vehicle_capacities'] = [None] * (data['num_vehicles'])
    for vehicle_id in range(data['num_vehicles']):
        data['vehicle_capacities'][vehicle_id] = 3

    ## Denoting Depot node by index 0
    data['depot'] = 0

    # Setting the demands for each pickup and drop node as +1 and -1 respectively
    data['demands'] = [None] * (2 * len(data['pickups_deliveries']) + 1)
    data['demands'][0] = 0
    for node in (data['pickups_deliveries']):
        data['demands'][node[0]] = 1
        data['demands'][node[1]] = -1


    return data