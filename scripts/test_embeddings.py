#!/usr/bin/env python3
"""
Test script for embeddings functionality.

This script provides basic tests to ensure embedding operations work correctly.
"""

import sys
from typing import List


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """
    Calculate cosine similarity between two vectors.
    
    Args:
        vec1: First vector
        vec2: Second vector
        
    Returns:
        Cosine similarity score between -1 and 1
    """
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same length")
    
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = sum(a * a for a in vec1) ** 0.5
    magnitude2 = sum(b * b for b in vec2) ** 0.5
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)


def test_cosine_similarity():
    """Test cosine similarity calculation."""
    print("Testing cosine similarity...")
    
    # Test 1: Identical vectors should have similarity of 1.0
    vec1 = [1.0, 2.0, 3.0]
    vec2 = [1.0, 2.0, 3.0]
    similarity = cosine_similarity(vec1, vec2)
    assert abs(similarity - 1.0) < 1e-6, f"Expected 1.0, got {similarity}"
    print("✓ Test 1 passed: Identical vectors have similarity 1.0")
    
    # Test 2: Orthogonal vectors should have similarity of 0.0
    vec1 = [1.0, 0.0, 0.0]
    vec2 = [0.0, 1.0, 0.0]
    similarity = cosine_similarity(vec1, vec2)
    assert abs(similarity - 0.0) < 1e-6, f"Expected 0.0, got {similarity}"
    print("✓ Test 2 passed: Orthogonal vectors have similarity 0.0")
    
    # Test 3: Opposite vectors should have similarity of -1.0
    vec1 = [1.0, 2.0, 3.0]
    vec2 = [-1.0, -2.0, -3.0]
    similarity = cosine_similarity(vec1, vec2)
    assert abs(similarity - (-1.0)) < 1e-6, f"Expected -1.0, got {similarity}"
    print("✓ Test 3 passed: Opposite vectors have similarity -1.0")
    
    # Test 4: Similar vectors should have high similarity
    vec1 = [1.0, 2.0, 3.0]
    vec2 = [1.1, 2.1, 2.9]
    similarity = cosine_similarity(vec1, vec2)
    assert similarity > 0.99, f"Expected >0.99, got {similarity}"
    print(f"✓ Test 4 passed: Similar vectors have high similarity ({similarity:.4f})")
    
    print("\nAll cosine similarity tests passed! ✓")


def test_vector_operations():
    """Test basic vector operations."""
    print("\nTesting vector operations...")
    
    # Test vector addition
    vec1 = [1.0, 2.0, 3.0]
    vec2 = [4.0, 5.0, 6.0]
    result = [a + b for a, b in zip(vec1, vec2)]
    expected = [5.0, 7.0, 9.0]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Vector addition works correctly")
    
    # Test vector scaling
    vec = [1.0, 2.0, 3.0]
    scale = 2.0
    result = [v * scale for v in vec]
    expected = [2.0, 4.0, 6.0]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Vector scaling works correctly")
    
    print("\nAll vector operation tests passed! ✓")


def main():
    """Run all tests."""
    print("=" * 60)
    print("Running Embeddings Tests")
    print("=" * 60)
    
    try:
        test_cosine_similarity()
        test_vector_operations()
        
        print("\n" + "=" * 60)
        print("All tests passed successfully! ✓✓✓")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
