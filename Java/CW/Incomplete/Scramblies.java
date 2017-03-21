import java.util.HashMap;
public class Scramblies {
    
    public static boolean scramble(String str1, String str2) {
    	// Convert strings into array

    	// Instantiate Hashmaps for str1 and str2
    	HashMap<String, Integer> map1 = new HashMap<String, Integer>();
    	HashMap<String, Integer> map2 = new HashMap<String, Integer>();

    	for (String c : str1) { // convert first string into a hashmap
    		if (map1.containsKey(c)) {
    			map1.put(c, map1.get(c) + 1);
    		} else {
    			map1.put(c, 1);
    		}
    	}

    	for (String c : str2) { // convert second string into a hashmap
    		if (map2. containsKey(c)) {
    			map2.put(c, map2.get(c) + 1);
    		} else {
    			map2.put(c, 1);
    		}
    	}

    	for (String key : map2.keySet()) {
    		if (map1.containsKey(key)) {
    			if (map1.get(key) < map2.get(key)) {
    				return false;
    			}
    		} else {
    			return false;
    		}
    	}
    	return true;
    }
}
