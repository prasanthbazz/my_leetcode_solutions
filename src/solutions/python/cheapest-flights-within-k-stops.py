'''
#787
https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/
'''
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dist = [float('inf')] * n
        
        dist[src] = 0
        
        '''
        usually bellman-ford's algorithm relaxes n-1 times.
        But since here we need results with utmost k stops,
        we are limiting it to k relaxations
        '''
        for i in range(k+1):
            '''
            making a deep copy of the dist table makes sure that
            the relaxation happens only to the immediate neighbour every time.
            i.e, one stop is considered every iteration.
            '''
            temp = dist[:]
            for f in flights:
                if dist[f[0]] + f[2] < temp[f[1]]:
                    temp[f[1]] = dist[f[0]] + f[2]
            dist = temp
        return dist[dst] if dist[dst] != float('inf') else -1