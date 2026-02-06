# test_nodeglacier.py
"""
Tests for nodeGlacier module.
"""

import unittest
from nodeglacier import nodeGlacier

class TestnodeGlacier(unittest.TestCase):
    """Test cases for nodeGlacier class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = nodeGlacier()
        self.assertIsInstance(instance, nodeGlacier)
        
    def test_run_method(self):
        """Test the run method."""
        instance = nodeGlacier()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
