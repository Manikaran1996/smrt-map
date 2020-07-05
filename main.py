import queue
import sys
from my_priority_queue import *


def get_adjacency_list():
    return adjacency_list


def get_num_of_links():
    return links


def add_route(station1, station2, weight=1):
    global links
    adjacency_list[station_to_index[station1]].append((station_to_index[station2], weight))
    adjacency_list[station_to_index[station2]].append((station_to_index[station1], weight))
    links = links + 1


def traversal(station_name):
    explored = [False for _ in range(len(stations))]
    visited = [False for _ in range(len(stations))]
    path_traversed = []
    q = queue.SimpleQueue()
    idx = station_to_index[station_name]
    explored[idx] = True
    q.put(idx)
    while not q.empty():
        node = q.get()
        path_traversed.append(stations[node])
        visited[node] = True
        for i, _ in adjacency_list[node]:
            if not explored[i] and not visited[i]:
                explored[i] = True
                q.put(i)
    return path_traversed


def delink(station1, station2, weight=1):
    global links
    if links == 1:
        print('De-Linking Failed!!')
    else:
        adjacency_list[station_to_index[station1]].remove((station_to_index[station2], weight))
        adjacency_list[station_to_index[station2]].remove((station_to_index[station1], weight))
        links = links - 1


def generate_paths(node):
    if len(node.parent) == 0:
        return [[stations[node.index]]]
    all_paths = []
    for parent in node.parent:
        ancestor_paths = generate_paths(parent)
        for p in ancestor_paths:
            all_paths.append(p + [stations[node.index]])
    return all_paths


def djikstra(source_station, destination_station):
    heap = PriorityQueue()
    source_index = station_to_index[source_station]
    heap.push(source_index, 0, [])
    destination_index = station_to_index[destination_station]
    visited = []
    explored = []
    shortest_path = sys.maxsize
    output = ''
    while not heap.empty():
        node = heap.pop()
        # print(node)
        visited.append(node.index)
        # print(heap.queue)
        # print()
        if node.distance > shortest_path:
            break

        if node.index == destination_index:
            shortest_path = node.distance
            output += 'Distance: {}\n\n'.format(shortest_path)
            paths = generate_paths(node)
            for p in paths:
                output += ' >>> '.join(p)
                output += '\n\n'
            continue

        for neighbor, _ in adjacency_list[node.index]:
            if neighbor in visited:
                continue
            if neighbor in explored:
                neighbor_node = heap.get_node(neighbor)
                if neighbor_node.distance == node.distance + 1 and node not in neighbor_node.parent:
                    neighbor_node.parent.append(node)
                heap.decrease_key(neighbor, node.distance + 1)
            else:
                # print(node, stations[neighbor], node.distance+1)
                heap.push(neighbor, node.distance+1, [node])
                explored.append(neighbor)
    return output


if __name__ == "__main__":
    print(adjacency_list)
    print(links)
    add_route('City Hall', 'Clarke Quay')
    print(links)
    print(djikstra('City Hall', 'Outram Park'))

