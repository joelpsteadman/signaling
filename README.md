# signaling

"The handicap principle is a hypothesis proposed by the biologist Amotz Zahavi to explain how evolution may lead to "honest" or reliable signalling between animals which have an obvious motivation to bluff or deceive each other." - Wikipedia

This model is an attempt to replicate the evolutionary claim that signaling fitness and trusting signaling is a good evolutionary strategy even when Signaling actively competes with fitness.

In this first verision, it does not seem that I am replicating that at all. Average trust after 1000 generations of a 1000 member population is inconsistent and often negative, and average true / false signaling consistently goes to 3%.

Potential problems:
- Quality has an upword selection force but no downward selection, so it keeps approaching 100% (interestingly it keeps landing at 97% after 1000 generations in a 1000 member population)
    - I need to 
- "False signaling" may be superfluous and may be causing issues with my results.
- I have not set limits on the number of children that any given individual can add to the next generation

https://upload.wikimedia.org/wikipedia/en/9/9b/Handicap-signal-of-quality.png