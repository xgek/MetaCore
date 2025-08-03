# test_metacore.py
"""
Tests for MetaCore module.
"""

import unittest
from metacore import MetaCore

class TestMetaCore(unittest.TestCase):
    """Test cases for MetaCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaCore()
        self.assertIsInstance(instance, MetaCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
