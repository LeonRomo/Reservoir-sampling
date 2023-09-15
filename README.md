# Reservoir-sampling

**Problem**: You want to maintain a random sample of size M from a stream of data, but the full size of the stream is unknown or potentially infinite.

**Solution**: "Reservoir Sampling", introduced by Jeffrey Vitter in 1985.

Here's a breakdown of the Reservoir Sampling algorithm:

1. **Initialization**: 
   Fill the "reservoir" with the first M elements from the stream. This is your initial sample.

2. **Iteration**:
   As you proceed through the stream and encounter a new element (let's call it the n-th element, where n > M):
   - Select this n-th element with a probability of M/n.
   - If the n-th element is chosen (based on the above probability), randomly choose an existing element from the reservoir and replace it with this n-th element.

**Why does this work?**
The beauty of this algorithm is that each element in the stream has an equal probability of ending up in the final reservoir (sample). As the stream grows, the probability of newer elements being selected diminishes, but if they are selected, they have an equal opportunity to replace any element in the reservoir, ensuring randomness.

**Recommendation**:
If you're dealing with large-scale data in real-time or streaming contexts on platforms like AWS, understanding and implementing algorithms like Reservoir Sampling can be invaluable. It allows you to gather statistically valid samples from massive datasets without needing to store or process the entire dataset. This can be particularly useful for initial exploratory data analysis, anomaly detection, or other tasks where a representative sample is sufficient. Ensure that you understand the statistical implications and limitations of the samples you gather using this method.
