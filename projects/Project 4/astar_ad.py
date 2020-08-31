import math
import heapq


"""
I implemented the pseudo code given by the Mentor Hemang G in the 3rd comment in this post: https://knowledge.udacity.com/questions/244266. Note: I used the pseudo code in the mentor's response, not the code in the student's question.

As suggested in the forums, I referenced this article: https://www.redblobgames.com/pathfinding/a-star/implementation.html.

I also referred to this GitHub repo for the logic retrace my steps and build the path: https://github.com/aldajo92/Udacity-Implement-Route-Planner/blob/master/01_route_planner.py
"""


def dist(start, goal):
    diff_x = start[0] - goal[0]
    diff_y = start[1] - goal[1]
    return math.sqrt(diff_x ** 2 + diff_y ** 2)


def shortest_path(M, start, goal):

    # Check that input nodes exist in the map.
    if start not in M.intersections or goal not in M.intersections:
        return 'Invalid start or goal nodes.'

    frontier_q = [(0, start)]  # Priority queue to track nodes to be explored.
    best_costs = {start: 0}  # Best cost so far to reach each node.
    prev_nodes = {start: None}  # Dictionary to track the node that led to this node's best cost.

    while len(frontier_q) > 0:  # Unexplored nodes still exist

        # Get the node with the lowest total cost f = (actual path cost so far) + (estimated distance to the goal)
        current_node = heapq.heappop(frontier_q)[1]

        # We found the goal, so retrace our steps back to the start node.
        # Since this is the first time we've reached the goal and we've been popping off the
        # min heap priority queue, this must be the shortest path to the goal.
        if current_node == goal:
            path = []
            path.append(current_node)
            while current_node != start:
                current_node = prev_nodes[current_node]
                path.append(current_node)
            return path[::-1]

        # Get the best cost we've seen so far to get to the current node.
        cost_to_current = best_costs[current_node]

        # Calculate costs for all the intersections that are adjacent to the current one.
        for adjacent_node in M.roads[current_node]:
            current_to_adj = dist(M.intersections[current_node], M.intersections[adjacent_node])
            total_to_adjacent = cost_to_current + current_to_adj

            # If we haven't visited this node, or we've just discovered a lower cost way to get this node,
            # update the best_cost dict with this cost.
            # Then calculate the estimated total cost for the node using the euclidean heuristic and
            # push it onto the priority queue.
            # Finally, update prev_nodes to show the path to follow to achieve the best cost.
            if (adjacent_node not in best_costs) or (total_to_adjacent < best_costs[adjacent_node]):
                best_costs[adjacent_node] = total_to_adjacent
                heuristic_cost = dist(M.intersections[adjacent_node], M.intersections[goal])
                estimated_total_cost = total_to_adjacent + heuristic_cost
                heapq.heappush(frontier_q, (estimated_total_cost, adjacent_node))
                prev_nodes[adjacent_node] = current_node

    # We've explored the entire frontier and haven't reached the goal. Must be a disconnected graph.
    return 'No route found.'


if __name__ == "__main__":

    from helpers import load_map
    from tests import test

    # Tests on a connected map
    map_40 = load_map('/Users/ad7073/Documents/Sharpen the saw/Udacity/DSAND/projects/Project 4/map-40.pickle')

    assert shortest_path(map_40, 5, 5) == [5]  # Single hop route
    assert shortest_path(map_40, 5, 9000) == 'Invalid start or goal nodes.'  # Invalid goal node
    assert shortest_path(map_40, 5000, 5) == 'Invalid start or goal nodes.'  # Invalid start node

    assert shortest_path(map_40, 5, 34) == [5, 16, 37, 12, 34]  # Example routes
    assert shortest_path(map_40, 19, 24) == [19, 2, 36, 28, 31, 10, 24]
    assert shortest_path(map_40, 38, 11) == [38, 29, 22, 12, 17, 15, 11]

    # Tests on a disconnected map
    map_10 = load_map('/Users/ad7073/Documents/Sharpen the saw/Udacity/DSAND/projects/Project 4/map-10.pickle')
    assert shortest_path(map_10, 6, 4) == [6, 0, 5, 3, 4]  # Works on one subgraph
    assert shortest_path(map_10, 9, 8) == [9, 8]  # Also works on the other subgraph
    assert shortest_path(map_10, 6, 9) == 'No route found.'  # Cannot route between the disconnected subgraphs

    test(shortest_path)
