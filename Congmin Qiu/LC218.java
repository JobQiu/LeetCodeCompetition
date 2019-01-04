
class Solution{
  public List<int[]> getSkyLine(int[][] buildings){
    List<int[]> res = new ArrayList();
    List<int[]> height = new ArrayList();

    for(int[] b: buildings){
      height.add(new int[]{b[0], -b[2]});
      //  up negative
      height.add(new int[]{b[1], b[2]});
      //  down, positive
    } // END of for

    Collections.sort(height, (a,b) -> {
      if(a[0] != b[0]){
        return a[0] - b[0];
      } // END of if
      return a[1] - b[1];
      // sort by the x_loc, and then by height
      // if x_loc are same, up is first, 
    });

    PriorityQueue<Integer> pq = new PriorityQueue<>((i1, i2) -> {return i2- i1;});
    // larger first?


    pq.offer(0);
    int prev = 0;

    for(int[] h: height){
      if(h[1] < 0){ // up
        pq.offer(-h[1]);
      } // END of if
      else{
        pq.remove(h[1]);
      }

      int cur = pq.peek();
      // be sure the height are not same
      if( prev != cur){
        res.add(new int[]{h[0], cur});
        prev = cur;
      } // END of if

    } // END of for

    return res;




  }


}
