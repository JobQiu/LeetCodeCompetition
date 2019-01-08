public class Solution{
  public double minCostToHireWorkers(int[] quality, int[] wage, int k){
    double[][] ratio = new double[quality.length][2];

    for(int i = 0; i < quality.length ; i++){
      ratio[i][0] = (double)(wage[i]) / (double)(quality[i]);
      ratio[i][1] = (double)(quality[i]);


    } // END of for i

    java.util.Arrays.sort(ratio, (a,b) -> Double.compare(a[0], b[0])); //Collections.reverseOrder()

    double qSum = 0;
    double res = Double.MAX_VALUE;

    PriorityQueue<Double> pq = new PriorityQueue<>();

    for(int i = 0; i < quality.length ; i++){
      qSum += ratio[i][1];
      pq.offer(-ratio[i][1]);
      if(pq.size()>k){
        qSum += pq.poll();
      } // END of if
      if(pq.size() == k){
        res = Math.min(res, qSum * ratio[i][0]);
      } // END of if
    } // END of for i

    return  res;

  }
}
