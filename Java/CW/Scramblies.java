import java.util.HashMap;
public class Scramblies {
    
    public static boolean scramble(String str1, String str2) {
    	str1 = str1.toLowerCase();
    	str2 = str2.toLowerCase();
    	// Convert strings into array
    	String[] array1 = str1.split("");
    	String[] array2 = str2.split("");

    	// Instantiate Hashmaps for str1 and str2
    	HashMap<String, Integer> map1 = new HashMap<String, Integer>();
    	HashMap<String, Integer> map2 = new HashMap<String, Integer>();

    	for (String c : array1) { // convert first string into a hashmap
    		if (map1.containsKey(c)) {
    			map1.put(c, map1.get(c) + 1);
    		} else {
    			map1.put(c, 1);
    		}
    	}

    	for (String c : array2) { // convert second string into a hashmap
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

    public static void main(String[] args) {
    	// Test #1
    	String str1 = "rkqodlw";
    	String str2 = "world"; 
    	boolean expected = true;
    	boolean actual = scramble(str1, str2);
    	if (actual == expected) {
    		System.out.println("Test #1 passed!");
    	} else {
    		System.out.println("Test #3 failed!");
    	}

    	// Test #2
    	str1 = "cedewaraaossoqqyt";
    	str2 = "codewars"; 
    	expected = true;
    	actual = scramble(str1, str2);
    	if (actual == expected) {
    		System.out.println("Test #2 passed!");
    	} else {
    		System.out.println("Test #3 failed!");
    	}

    	// Test #3
    	str1 = "katas";
    	str2 = "steak"; 
    	expected = false;
    	actual = scramble(str1, str2);
    	if (actual == expected) {
    		System.out.println("Test #3 passed!");
    	} else {
    		System.out.println("Test #3 failed!");
    	}

    	// Test #4
    	str1 = "dragon! BlueFireRedOnHillWind";
    	str2 = "Hello World!"; 
    	expected = true;
    	actual = scramble(str1, str2);
    	if (actual == expected) {
    		System.out.println("Test #4 passed!");
    	} else {
    		System.out.println("Test #4 failed!");
    	}
    }
}
