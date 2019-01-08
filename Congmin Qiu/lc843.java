/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     public int guess(String word) {}
 * }


 */
class Solution {
  public void findSecretWord(String[] wordlist, Master master) {
    for(int i = 0, x=0; i < 10 && x < 6 ; i++){
      Map<String, Integer> map = new HashMap();
      for(String w1: wordlist){
        for(String w2: wordlist){
          if(match(w1, w2) == 0){
            map.put(w1, map.getOrDefault(w1, 0) + 1);
          } // END of if
        } // END of for
      } // END of for

      
    } // END of for i
  }
}
