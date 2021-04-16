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

### Day 36: 13 April 2021

**Today**: Finished Chapter 6 of Practical Combine. Tested the replacement Grow HAT Mini from Pimoroni.

**Thoughts:** Pimoroni has excellent customer service.

**Key concepts:**

1. Apple introduced a setting in iOS 13+ called Low Data Mode that the user uses to indicate that apps should opt-in to use less network data.
2. To opt-in, you set the property `allowsConstrainedNetworkAccess = false` on the `URLSessionConfiguration` or on an individual `URLRequest` object.
3. Requests made while Low Data Mode is enabled while raise an URLError with the networkUnavailableReason set to .constrained.
4. Apple also introduced `allowsExpensiveNetworkAccess` (on URLSessionConfiguration and URLRequest) that will raise an URLError when the user is on an expensive network. Wonder how they determine this.

**Links:**

1. [Apple docs allowsExpensiveNetworkAccess](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/3235752-allowsexpensivenetworkaccess)

---

### Day 37: 14 April 2021

**Today**: Started on Chapter 7 of Practical Combine.

**Thoughts:** I like that Combine comes with Futures & Promises and I no longer have to use other frameworks for this.

**Key concepts:**

1. You can create custom Publishers in the form of Subject objects like CurrentValueSubject and PassthroughSubject.
2. Combine can also do `Future`s and `Promise`s.
3. A Future is a Publisher that will emit a single value and complete immediately.
4. It can never emit more than one value.
5. Recap: Swift introduced a Result generic type. `@frozen enum Result<Success, Failure> where Failure : Error`
6. Example creation of a Future

		func createFuture() -> Future<Int, Never> {
			return Future { promise in
				promise(.success(42))
			}
		}

		Output: Int
		Failure: Never
		
		Future's init takes a closure that is
		passed a Promise
		
		Future has:
		typealias Promise = (Result<Output, Failure>) -> Void
		
7. Thus a Future takes a closure param at init, which in turn will be passed a Promise closure, which will be called in the future with a Result. Where the Result's Success type must match the Future's Output type and the Result's Failure must match the Future's Failure type. <-- Did you get all that? It is a lot to unpack.
8. Recap: Publishers will not do any work unless there are Subscribers.
9. Futures on the other hand will execute the work as soon as they are created.
10. However they will emit the same result to every subscriber being added. Thus do the work once and report many.
11. You can wrap a Future in a Deferred publisher and thus the Future will behave like a "normal" publisher. I.e. Only do work when there are publishers and also do the work for each subscriber.
	
**Links:**

1. [Swift docs for @frozen etc.](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html)

---

### Day 38: 15 April 2021

**Today**: Finished Chapter 7 & 8 of Practical Combine

**Thoughts:** Paragraph or two

**Key concepts:**

1. Practical Combine Ch7 has a nice example of asking for permission to use notifications as well as an example of wrapping Core Data fetches in a Future.
2. Combine has a `receive(on:)` operator that you can use to specify on which Scheduler to receive the values on.
3. The `Scheduler` protocol is conformed by `DispatchQueue`, `OperationQueue` and `RunLoop`.
4. There is also `ImmediateScheduler` that will perform any work immediately and can't be delayed.
5. Combine expects schedulers to operate on a serial queue.
6. The default scheduler will emit values on the thread they were generated on.
7. Combine also has a `subscribe(on:)` operator that you use to specify on which Scheduler subscribers are registered with the publisher.

**Links:**

1. [Practical Combine](https://practicalcombine.com/)

---

### Day 39: 16 April 2021

**Today**: Finished Chapter 9 of Practical Combine

**Thoughts:** I am strugling tonight to download information into my brain. TGIF.

**Key concepts:**

1. It is recommended that you don't write your own custom Publishers and Subscribers unless you really need to.
2. In Combine the subscribers are in charge of how many values they want to receive.
3. A Subscriber is handed a `Subscription` object via the `receive(subscription:)` method.
4. Backpressure is managed via this subscription object.

		func receive(subscription: Subscription) {
			subscription.request(.max(1))
			...

**Links:**

n/a

---
