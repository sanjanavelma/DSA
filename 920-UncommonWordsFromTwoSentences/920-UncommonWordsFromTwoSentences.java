// Last updated: 17/06/2025, 22:14:01
class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
       HashMap<String, Integer> map = new HashMap<>();
        
        for (String word : s1.split(" ")){
            map.put(word,map.getOrDefault(word, 0)+1);
        }
        for(String word : s2.split(" ")){
            map.put(word,map.getOrDefault(word, 0)+1);
        }
    ArrayList <String> list = new ArrayList<>();
    for(Map.Entry<String, Integer> entry : map.entrySet()){
        if(entry.getValue()==1){
            list.add(entry.getKey());
        }
    }
    String res[] = new String[list.size()];
    list.toArray(res);
    return res;
    }
}