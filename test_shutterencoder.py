# test_shutterencoder.py
"""
Tests for ShutterEncoder module.
"""

import unittest
from shutterencoder import ShutterEncoder

class TestShutterEncoder(unittest.TestCase):
    """Test cases for ShutterEncoder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShutterEncoder()
        self.assertIsInstance(instance, ShutterEncoder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShutterEncoder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
