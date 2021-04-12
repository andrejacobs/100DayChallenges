# 100 Days Of Learning

## Log book - Week 6

### Day 35: 12 April 2021

**Today**: Started on Chapter 6 of Practical Combine.

**Thoughts:** n/a

**Key concepts:**

1. Combine has a `share` operator that shares the output values from the upstream Publisher with multiple subscribers.
2. The resulting Publisher is a class instance (reference semantics)
3. This is handy for example where you want to make a single network call that multiple subscribers can subscribe to but without making a new network call for each subscriber.
4. Combine has a `decode` operator that can make short work of decoding JSON.

		// Some publisher that emits Data values
		.decode(type: T.self, decoder: JSONDecoder())
		// where T conforms to Decodable and
		// decoder conforms to TopLevelDecoder

**Links:**

1. [Apple docs about share operator](https://developer.apple.com/documentation/combine/fail/share())

---
