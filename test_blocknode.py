# test_blocknode.py
"""
Tests for BlockNode module.
"""

import unittest
from blocknode import BlockNode

class TestBlockNode(unittest.TestCase):
    """Test cases for BlockNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockNode()
        self.assertIsInstance(instance, BlockNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
