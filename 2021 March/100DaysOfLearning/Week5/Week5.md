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
