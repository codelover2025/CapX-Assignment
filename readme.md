# Dynamic Multilevel Caching System

## Objective
Design a multilevel caching system that manages data across multiple cache levels with dynamic additions, eviction policies, and retrieval.

## Features
- **Multiple Cache Levels**: Support for multiple cache levels (L1, L2, ...), each with its own size.
- **Eviction Policies**: Support for LRU (Least Recently Used) and LFU (Least Frequently Used) eviction policies.
- **Data Handling**: Efficient data retrieval and insertion, with automatic promotion of frequently accessed data to higher cache levels.
- **Dynamic Cache Management**: Ability to add or remove cache levels at runtime.
- **Concurrency (Bonus)**: Thread-safe operations for concurrent access.
- **Performance**: Optimized for efficient lookups and minimized cache misses.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/dynamic-multilevel-caching-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd dynamic-multilevel-caching-system
    ```

## Usage
### Adding Cache Levels
To add a cache level with a specified size and eviction policy:
```python
cache_manager.addCacheLevel(size, eviction_policy)
