Hashtable is gives faster read for a key defined.

Key -> hashfunction() -> Index to ArrayList.
Ther could be infinte keys possible but only finite Index so collison are
bound to happen. Chaining could be one way to resolve this problem.

HashTbale is different from HashMap in some that , HashTable are thread safe whi
le HashMap uses synchronisedMap to resolve this problem.

// Read More about collison handling
// Implement HasTbale using Balanced Binary Search Tree..to reduce the same compare to ArrayList. but this will result in O(log N) compare to O(1).


USAGE:

HashMap/HashTable/HashSet <K,V> = new HashMap<K,V>();

//More to come
