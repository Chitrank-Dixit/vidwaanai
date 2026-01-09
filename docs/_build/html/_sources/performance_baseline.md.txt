# Performance Baseline (Phase 1)

**Date:** 2025-11-30
**Target:** < 5 seconds per query

## Summary Metrics
- **Total Queries:** 10
- **Average Response Time:** 62.67s
- **Min Response Time:** 37.30s
- **Max Response Time:** 90.23s
- **P95 Response Time:** 90.23s

## Detailed Results

| Query | Time (s) |
|-------|----------|
| Who is Krishna? | 83.50 |
| What is Dharma? | 90.23 |
| Explain the concept of Karma Yoga. | 87.91 |
| Who are the Pandavas? | 75.26 |
| What did Krishna say to Arjuna? | 73.09 |
| Tell me about the Battle of Kurukshetra. | 49.81 |
| What is the significance of the Bhagavad Gita? | 46.43 |
| Who is Duryodhana? | 41.83 |
| What are the four varnas? | 37.30 |
| Describe the relationship between Krishna and Arjuna. | 41.31 |

## Observations
- Queries involving complex concepts ("Dharma", "Karma Yoga") take significantly longer (>80s).
- Even simple entity queries ("Who is Duryodhana?") take >40s.
- The system is currently ~12x slower than the target.
