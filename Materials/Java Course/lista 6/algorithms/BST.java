package algorithms;

import java.util.NoSuchElementException;

public class BST<T extends Comparable<T>> implements Dictionary<T> {

    public class Node<T extends Comparable<T>> {
        public Node<T> left, right;
        public T value;

        public Node(T value) {
            this.value = value;
        }

        public boolean search(T x) {
            if (x == null) {
                return false;
            }

            int compareResult = x.compareTo(value);
            if (compareResult == 0) {
                return true;
            } else if (compareResult < 0 && left != null) {
                return left.search(x);
            } else if (compareResult > 0 && right != null) {
                return right.search(x);
            }

            return false;
        }

        public void insert(T x) {
            if (x == null) {
                throw new IllegalArgumentException("Cannot insert null value into BST");
            }

            int compareResult = x.compareTo(value);
            if (compareResult == 0) {
            } else if (compareResult < 0) {
                if (left == null) {
                    left = new Node<>(x);
                } else {
                    left.insert(x);
                }
            } else {
                if (right == null) {
                    right = new Node<>(x);
                } else {
                    right.insert(x);
                }
            }
        }

        public void remove(T x) {
            remove(this, x);
        }
        
        private Node<T> remove(Node<T> node, T x) {
            if (node == null) {
                return node; 
            }

            int compareResult = x.compareTo(node.value);

            if (compareResult < 0) {
                node.left = remove(node.left, x);
            } else if (compareResult > 0) {
                node.right = remove(node.right, x);
            } else {
                if (node.left == null) {
                    return node.right;
                } else if (node.right == null) {
                    return node.left;
                }
        
                node.value = node.right.min();
                node.right = remove(node.right, node.value);
            }
            return node;
        }

        public T min() throws NoSuchElementException {
            if (left == null) {
                return value;
            }
            return left.min();
        }

        public T max() throws NoSuchElementException {
            if (right == null) {
                return value;
            }
            return right.max();
        }

        public int size() {
            return size(this);
        }

        private int size(Node<T> node) {
            if (node == null) {
                return 0;
            }
            return 1 + size(node.left) + size(node.right);
        }

        public void clear() {
            clear(this);
        }

        private void clear(Node<T> node) {
            if (node != null) {
                clear(node.left);
                clear(node.right);
                node.left = null;
                node.right = null;
            }
        }
    }

    public Node<T> root;

    public boolean search(T x) {
        if (root == null) {
            return false;
        }
        return root.search(x);
    }

    public void insert(T x) {
        if (root == null) {
            root = new Node<>(x);
        } else {
            root.insert(x);
        }
    }

    public void remove(T x) {
        root = remove(root, x);
    }

    private Node<T> remove(Node<T> node, T x) {
        int compareResult = x.compareTo(node.value);
        
        if (compareResult == 0 & node.value == root.value & 
           (node.left == null || node.right == null || node.left == null & node.right == null)) {
            if (node.left == null & node.right == null) {
                return null;
            } else if (node.left == null) {
                return node.right;
            } else {
                return node.left;
            }
        } else {
            if (node != null) {
                node.remove(x);
            }
            return node;
        }
    }

    public T min() throws NoSuchElementException {
        if (root == null) {
            throw new NoSuchElementException("BST is empty");
        }
        return root.min();
    }

    public T max() throws NoSuchElementException {
        if (root == null) {
            throw new NoSuchElementException("BST is empty");
        }
        return root.max();
    }

    public int size() {
        if (root == null) {
            return 0;
        }
        return root.size();
    }

    public void clear() {
        root.clear();
        root = null;
    }
}