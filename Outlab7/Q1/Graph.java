package Q1;
/*
 * IMPLEMENTED BY: ASHWIN ABRAHAM
 */
import java.util.Map.Entry;
import java.util.*; 
import java.util.regex.*; 

class Pair
{
    public Integer dist;
    public Node n;
    //public Boolean marked;

    Pair(Integer a, Node b)
    {
        dist = a;
        n = b;
        //marked = bol;
    }
}


class PairComparator implements Comparator<Pair>
{
    public int compare(Pair a, Pair b)
    {
        return a.dist - b.dist;
    }
}


public class Graph {

    // Assume maximum path length to be less than INF
    private static Integer INF = 1000*1000*1000 ;
    private Map<String, Node> nodeMap = new HashMap<String, Node>() ;
    
    public void addNode(String name) {
        /*
         * TODO: Implement this method
         */
        nodeMap.put(name, new Node(name));
    }

    public void addDirectedEdge(String nameA, String nameB, Integer distance) {
        /*
         * TODO: Implement this method
         * Check if nodes with nameA and nameB exist.
         */
        if(nodeMap.containsKey(nameA) && nodeMap.containsKey(nameB))
        {
            nodeMap.get(nameA).adjacentNodes.put(nodeMap.get(nameB), distance);
            //nodeMap.get(nameB).adjacentNodes.put(nodeMap.get(nameA), distance);
        }
    }

    public Map<String, Integer> dijkstraAlgorithm(String source) {
        /*
         * TODO: Implement this method
         * Return a map of name of all the nodes
         * with the minimum distance from source node
         */
        if(!nodeMap.containsKey(source)) return new HashMap<String, Integer>();
        Node srcNode = nodeMap.get(source);
        PriorityQueue<Pair> curr_dists = new PriorityQueue<Pair>(new PairComparator());
        Map<Node, Pair> NtP = new HashMap<Node, Pair>();
        for(Node n : nodeMap.values())
        {
            Pair p = new Pair(INF, n);
            if(n == srcNode) p.dist = 0;
            curr_dists.add(p);
            NtP.put(n, p);
        }
        Map<String, Integer> ret_val = new HashMap<String, Integer>();
        while(!curr_dists.isEmpty() && curr_dists.element().dist < INF)
        {
            Pair curr_node = curr_dists.remove();
            if(NtP.get(curr_node.n) != curr_node) continue;
            for(Node adj : curr_node.n.adjacentNodes.keySet())
            {
                if(NtP.get(adj).dist > curr_node.dist + curr_node.n.adjacentNodes.get(adj))
                {
                    Pair p = new Pair(curr_node.dist + curr_node.n.adjacentNodes.get(adj), adj);
                    NtP.put(adj, p);
                    curr_dists.add(p);
                }
            }
            ret_val.put(curr_node.n.getName(), curr_node.dist);
        }
        while(!curr_dists.isEmpty())
        {
            Pair p = curr_dists.remove();
            if(NtP.get(p.n) != p) continue;
            ret_val.put(p.n.getName(), INF);
        }
        return ret_val;
    }
}