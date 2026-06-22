# test_hashpulse.py
"""
Tests for HashPulse module.
"""

import unittest
from hashpulse import HashPulse

class TestHashPulse(unittest.TestCase):
    """Test cases for HashPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HashPulse()
        self.assertIsInstance(instance, HashPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HashPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
