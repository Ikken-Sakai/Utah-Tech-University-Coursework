from typing import List, Tuple

def main(input_file: str) -> List[str]:
    # Open the input file and read the number of vertices and edges
    with open(input_file, 'r') as f:
        num_vertices = int(f.readline())
        num_edges = int(f.readline())

        # Create a new graph with the specified number of vertices
        graph = Graph(num_vertices)

        # Add each edge to the graph
        for i in range(num_edges):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v)

        # Read the number of test cases
        num_test_cases = int(f.readline())

        # Initialize a list to store the results of the test cases
        results = []

        # For each test case, find a path from the first vertex to the second, or 'None.'
        for i in range(num_test_cases):
            u, v = map(int, f.readline().split())
            path = graph.breadth_first_search(u, v)
            if path:
                results.append(' '.join(str(x) for x in path))
            else:
                results.append('None')

    # Return the results of the test cases
    return results

# Assume the input file is saved to the same directory as the script
input_file = 'input.txt'

# Call the main function and print the results
results = main(input_file)
print(results)
