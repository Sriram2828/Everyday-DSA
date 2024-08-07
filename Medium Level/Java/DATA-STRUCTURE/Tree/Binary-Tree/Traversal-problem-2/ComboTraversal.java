// traversing class:
public class ComboTraversal{
    void inorder(TreeNode root){
        if(root == null){
            return;
        }
        inorder(root.left);
        System.out.print(root.value+" ");
        inorder(root.right);
    }
    void preorder(TreeNode root){
        if(root == null){
            return;
        }
        System.out.print(root.value+" ");
        preorder(root.left);
        preorder(root.right);
    }
    void postorder(TreeNode root){
        if(root == null){
            return;
        }
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.value+" ");
    }

    public static void main(String[] arg){
        // [2 problem]
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(5);
        root.left.left = new TreeNode(3);
        root.left.left.right = new TreeNode(9);
        root.left.left.right.left = new TreeNode(1);
        root.right.left = new TreeNode(7);
        root.right.right = new TreeNode(6);
        root.right.right.left = new TreeNode(8);
        ComboTraversal tree = new ComboTraversal();

        System.out.println("Inorder traversal");
        tree.inorder(root);
        System.out.println();

        System.out.println("Postorder traversal");
        tree.postorder(root);
        System.out.println();

        System.out.println("Preorder traversal");
        tree.preorder(root);
        System.out.println();
    }
}

class TreeNode{
    // step 1:
    public int value;
    public TreeNode left, right;
    // step 2: constructor
    TreeNode(int value){
        this.value = value;
        left = right = null;
    }
}

