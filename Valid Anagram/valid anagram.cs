public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length){
            return false;
        }
        if (s==t) {
            return true;
        }
        
        Dictionary<char, int> countS = new Dictionary<char, int>();
        Dictionary<char, int> countT = new Dictionary<char, int>();

        for (int i=0; i<s.Length; i++){
            if( countS.ContainsKey(s[i])){
                countS[s[i]]++;
            }
            else{
                countS[s[i]]=1;
            }
            if( countT.ContainsKey(t[i])){
                countT[t[i]]++;
            }
            else{
                countT[t[i]]=1;
            }   
        }

        foreach(char c in countS.Keys){
           int tcount = countT.ContainsKey(c) ? countT[c]:0;
           if (countS[c] != tcount) return false;
        }
        return true;
    }
}