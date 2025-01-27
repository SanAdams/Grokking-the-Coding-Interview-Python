from heapq import heappush, heappop 
def maximum_capital(c, k, capitals, profits):
    '''
    Args:
        c (int): initial capital
        k (int): number of projects to invest in
        capitals (int[]): array on integers representing the capital requriment of each project
        profits (int[]): array of integers representing the profit possible from each project

    Returns:
        max_capital (int): the maximum capital achievable by picking k distinct projects
    '''

    # Track the max capital we've gotten so far
    max_capital = c
    capitals_min_heap, profits_max_heap = [],[]

    # Create a min_heap of (capitals, project number), sorts by capital[project] then by project
    for project_number in range(0, len(capitals)):
        heappush(capitals_min_heap, (capitals[project_number], project_number))

    
    # Find k distinct projects to invest in
    for _ in range(k):
        
        # Keep pushing to the max heap until we no longer have the capital to pay for a project
        while capitals_min_heap and capitals_min_heap[0][0] <= max_capital:
            capital, project_number = heappop(capitals_min_heap)
            heappush(profits_max_heap, -profits[project_number])
        

        if not profits_max_heap:
            break
            
        profit_from_project = -heappop(profits_max_heap)
        max_capital += profit_from_project

    
    return max_capital
    