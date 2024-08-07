class PostorderTraversal {  
    // object for Node class
    Node root;  
    PostorderTraversal() { 
        root = null; 
    }  
  
    void traversePostorder(Node node){  
        if (node == null){  
            return;  
        }
        
        traversePostorder(node.left);
        traversePostorder(node.right); 
        System.out.print(node.value + " ");    
    }  
  
    void traversePostorder() {
        traversePostorder(root); 
    }  
  
    public static void main(String args[])  
    {  
        PostorderTraversal pt = new PostorderTraversal();  
        pt.root = new Node(1);  
        pt.root.left = new Node(2);  
        pt.root.right = new Node(3);  
        pt.root.left.left = new Node(4);  
        pt.root.left.right = new Node(5);  
        pt.root.right.left = new Node(6);  
        pt.root.right.right = new Node(7);    
  
        System.out.println();  
        System.out.println("Postorder traversal of given binary tree is - ");  
        pt.traversePostorder();  
        System.out.println();  
    }  
}  

class Node {  
    // Step 1: initialization
    public int value;  
    public Node left, right;  
    // step 2: constructor
    public Node(int element)  
    {  
        value = element;  
        left = right = null;  
    }  
}  
