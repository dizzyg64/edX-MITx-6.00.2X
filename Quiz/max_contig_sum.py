def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_ending_here = max_so_far = L[0]
    for i in L[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

L = [10, 9, 8, -1]
print(max_contig_sum(L))