class InorderTraversal {  
    // object for Node class
    Node root;  
    InorderTraversal() { 
        root = null; 
    }  
  
    void traverseInorder(Node node){  
        if (node == null){  
            return;  
        }
        
        traverseInorder(node.left);
        System.out.print(node.value + " ");    
        traverseInorder(node.right);  
    }  
  
    void traverseInorder() {
        traverseInorder(root); 
    }  
  
    public static void main(String args[])  
    {  
        InorderTraversal pt = new InorderTraversal();  
        pt.root = new Node(1);  
        pt.root.left = new Node(2);  
        pt.root.right = new Node(3);  
        pt.root.left.left = new Node(4);  
        pt.root.left.right = new Node(5);  
        pt.root.right.left = new Node(6);  
        pt.root.right.right = new Node(7);    
  
        System.out.println();  
        System.out.println("Inorder traversal of given binary tree is - ");  
        pt.traverseInorder();  
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
