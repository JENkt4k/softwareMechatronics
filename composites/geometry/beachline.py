# beachline.py
"""
AVL-based Beach Line for Fortune's Algorithm.
This replaces the linked-list arc management with a balanced BST.
"""

from data_structures.avl_tree import AVLTree

class ArcNode:
    """
    Represents an arc on the beachline.
    """
    def __init__(self, site):
        self.site = site  # (x, y) point
        self.edge_left = None
        self.edge_right = None
        self.circle_event = None

    def __repr__(self):
        return f"ArcNode(site={self.site})"


class BeachLine:
    """
    Beachline managed by an AVL tree.
    Keys in the tree correspond to x-coordinates of breakpoints.
    Each node maps to an ArcNode.
    """
    def __init__(self):
        self.tree = AVLTree()

    def find_arc_above(self, x, sweep_y):
        """
        Find the ArcNode directly above a given x-coordinate (site.x).
        Uses binary search on the AVL tree.
        """
        if self.tree.root is None:
            return None

        node = self.tree.root
        result = None
        while node:
            breakpoint_left = self.get_breakpoint(node, sweep_y, left=True)
            breakpoint_right = self.get_breakpoint(node, sweep_y, left=False)

            if x < breakpoint_left:
                node = node.left
            elif x > breakpoint_right:
                node = node.right
            else:
                result = node
                break
        return result.value if result else None

    def insert_arc(self, site, sweep_y):
        """
        Insert a new arc for a new site event.
        This will split an existing arc into three arcs (left, new, right).
        """
        if self.tree.root is None:
            # First arc
            self.tree.insert(site[0], ArcNode(site))
            return

        arc_node = self.find_arc_above(site[0], sweep_y)
        if arc_node is None:
            return

        # Remove the existing arc and replace it with three arcs
        old_site = arc_node.site
        self.tree.delete(old_site[0])

        self.tree.insert(old_site[0] - 1e-6, ArcNode(old_site))  # left
        self.tree.insert(site[0], ArcNode(site))                # new
        self.tree.insert(old_site[0] + 1e-6, ArcNode(old_site))  # right

    def get_breakpoint(self, node, sweep_y, left=True):
        """
        Compute the x-coordinate of the breakpoint for this arc with its neighbor.
        For now, a placeholder linear approximation.
        """
        # TODO: Replace with real parabola intersection calculation
        return node.key + (-0.5 if left else 0.5)

    def __repr__(self):
        return f"BeachLine(AVL={self.tree})"
