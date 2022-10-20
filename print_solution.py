def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    time_dimension = routing.GetDimensionOrDie('Time')
    print(f'Objective: {solution.ObjectiveValue()}')
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            time_var = time_dimension.CumulVar(index)
            # plan_output += ' {} -> '.format(manager.IndexToNode(index))
            plan_output += '{0} Time({1},{2}) -> '.format(
                manager.IndexToNode(index), solution.Min(time_var),
                solution.Max(time_var))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        time_var = time_dimension.CumulVar(index)
        # plan_output += '{}\n'.format(manager.IndexToNode(index))
        plan_output += '{0} Time({1},{2})\n'.format(manager.IndexToNode(index),
                                                    solution.Min(time_var),
                                                    solution.Max(time_var))
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        if route_distance>0:
            print(plan_output)
            total_distance += route_distance
    print('Total Distance of all routes: {}m'.format(total_distance))
