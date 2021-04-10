# 100 Days Of Learning

## Log book - Week 5

### Day 28: 5 April 2021

**Today**: Setting up the Pimoroni Grow kit with a Raspberry Pi Zero W

**Thoughts:** My Grow HAT Mini is broken :-(

**Key concepts:**

n/a

**Links:**

1. [Book about X](http://www.example.com)
2. [Pimoroni Grow kit](https://shop.pimoroni.com/products/grow?variant=32208365486163)
3. [Getting Started with Grow](https://learn.pimoroni.com/tutorial/hel/assembling-grow)
4. [Auto-Watering with Grow](https://learn.pimoroni.com/tutorial/hel/auto-watering-with-grow)
5. [Python libs for controlling the Grow HATs](https://github.com/pimoroni/grow-python)

---

### Day 29: 6 April 2021

**Today**: Started reading Practical Combine by Donny Wals and learning about Combine. Also read a very good article from Kean.blog about SwiftUI Layout System.

**Thoughts:** Things move fast in Mobile. iOS today is not what it was when I started back in 2009. Haha back then it was only Objective-C and UIKit layout was done by yourself.

Must admit, I never liked Auto Layout and never will. I did have to embrace it to be still relevant, but I can't wait for SwiftUI to become the standard.

**Key concepts:**

1. Combine is a Functional Reactive Programming (FRP) framework.
2. A Higher-order function is a function that takes another function or closure as it's parameter.
3. A Pure function is a function that operates only on the arguments it receives.
4. A Stream is an array of values delivered over time.
5. FRP reacts asynchronously to events using functional programming.
6. Everything starts with a Publisher in Combine.
7. Publisher protocol specifies the associated types Output and Failure. Thus every Publisher has an Output and Failure type.
8. Output is the type of value being produced by the Publisher.
9. A Publisher can have a Failure type of Never and thus it means the publisher can never fail while producing values successfully.
10. FRP uses Marble diagrams for communication.
11. Subscribers receive emitted values from the Publisher's stream.
12. `sink` is an extension method on Publisher that provides a Subscriber. This subscriber has two arguments `receiveCompletion` and `receiveValue`. If the Failure type is Never, then the receiveCompletion can be omitted.
13. `assign` is a subscriber that binds a property on an object to the values emitted from a publisher. `assign(to: <property key path> on: <object>`. The object has to be a Reference type (i.e. Class).

**Links:**

1. [Practical Combine](https://practicalcombine.com/)
2. [SwiftUI Layout System](https://kean.blog/post/swiftui-layout-system)
3. [SwiftUI Data Flow](https://kean.blog/post/swiftui-data-flow)

---

### Day 30: 7 April 2021

**Today**: Continuing to learn Combine from the Practical Combine book.

**Thoughts:** Today was a tough day on the "9 to 5".

**Key concepts:**

1. A Publisher will not emit any values if it does not have any Subscribers that are willing to receive values. This is known as `backpressure management`
2. `AnyCancellable` will unsubscribe the Subscriber from the Publisher on deallocation.
3. `sink` and `assign` return `AnyCancellable`.
4. You can hold on to the reference with a single property:

		var subscription: AnyCancellable?
		...
		subscription = <publisher>.sink(...)
		
5. Or by storing them in a set:

		var subscribers = Set<AnyCancellable>()
		...
		<publisher>.sink(...).store(in: &subscribers)
6. Publishers can only complete or fail once.
7. It is common to avoid processing or manipulating data in a Subscriber. Instead transform or filter the Publisher.
		
		.publisher.map({ value in
			return newTypeOrValue
		}).sink(receiveValue: { newTypeOrValue in ... })
8. Calling map on a collection results in a new collection. Calling map on a Publisher results in a new Publisher.
8. An `operator` is a function that wraps a Publisher into another Publisher.
9. Reminder: compactMap is like map except that it also filters out nil values.
10. Combine's compactMap does the same thing for Publisher values.
11. There is also replaceNil(with:<default>) that can be used to swap nil values with the specified default value.
12. flatMap is used to flatten array of arrays into a single array with the elements from the nested arrays.
13. Combine flatMap is used to flatten a Publisher that produces more Publishers.
14. setFailureType can be used to change the Failure type of a Publisher to another type.

**Links:**

1. [Practical Combine](https://practicalcombine.com/)

---

### Day 31: 8 April 2021

**Today**: Finished chapter 3 & 4 from Practical Combine.

**Thoughts:** I am liking Combine so far.

**Key concepts:**

1. Combine has a number of operators prefixed with `try` (e.g. tryMap) that allows the Publisher to throw an error.
2. Reminder: A Publisher is allowed to throw an error only once, after which it can no longer emit new values.
3. You can check for iOS version: if #available(iOS 14, *).
4. All operators are defined as an extension on Publisher.

		extension Publisher where Output == Int, Failure == Never {
			func myNewOperator(someArgs...) -> AnyPublisher<NewOutputType, NewErrorType> {
				return somePublisherOrSelf
					.eraseToAnyPublisher()
			}
		}
		
5. `eraseToAnyPublisher` is used to remove all type information from a Publisher and wrap it as AnyPublisher. Basically it removes crud while composing new operators.
6. A `subject` is a Publisher that allows you (the developer) to inject values into its stream.
7. Combine subjects have a send(_:) method to inject values and a send(completion:) to complete the Publisher.
8. `PassthroughSubject` is used to emit values from imperative code that does not hold state. Good fit for emitting events.
9. `PassthroughSubject` does not hold on to any values sent in the past.
10. `CurrentValueSubject` can be used to hold onto some state. It has a `.value` property and when this is changed all Subscribers will be notified.
11. `CurrentValueSubject` will also emit its current value to any new Subscribers.
12. `@Published` property wrapper is almost like CurrentValueSubject but makes the code cleaner. The big difference is that @Published will emits its underlying value first to its Subscribers and then update the value, whereas CurrentValueSubject will update the underlying value first and then pulish to Subscribers.

		@Published var myVar = 42
		myVar = 201
		$myVar.sink(...)
		
13. In order to subscribe to the Publisher for a @Published property, you need to access the projected value (the Publisher) using the $ syntax.
14. @Published is only available to Classes. CurrentValueSubject is available to Structs and Classes.

**Links:**

1. [Practical Combine](https://practicalcombine.com/)

---

### Day 32: 9 April 2021

**Today**: Started on Chapter 5 of Practical Combine. Received some more goodies from Pimoroni and will be testing those out.

**Thoughts:** TGIF

**Key concepts:**

1. Combine doesn't come with good built-in support for UIKit, guess the future truly is SwiftUI.
2. NSObject has a "publisher(for:)" to subscribe to KVO changes. However UIControl is not KVO compliant and thus this won't work for controls like sliders.
3. In SwiftUI binding of UI to state can be achieved with the `@State` property wrapper.

		struct MyView: View {
			@State private var sliderValue: Float = 42
			var body: some View {
				VStack {
					Text("Slider value: \(sliderValue)")
					Slider(value: $sliderValue, in: (1...100))
				}
			...


**Links:**

1. [Practical Combine](https://practicalcombine.com/)

---

### Day 33: 10 April 2021

**Today**: Today I managed to setup a test rig for pumping water with the Pimoroni Grow HAT Mini and the small water pumps.

**Thoughts:** I can't wait to get a full setup up and running and growing some plants with it.

**Key concepts:**

n/a

**Links:**

1. [Day 33 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-33-pumping-water-with-the-pimoroni-grow-hat-mini/
)
2. [Short video showing the test rig pumping water](https://youtu.be/piwJtW7JQUA)

---
