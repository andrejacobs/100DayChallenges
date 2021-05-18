# 100 Days Of Learning

## Log book - Week 11

### Day 70: 17 May 2021

**Today**: Finished Part 1 of the Build an app with SwiftUI course by Design+Code

**Thoughts:** I am starting to feel better. Just a nagging cough is left now.

**Key concepts:**

1. To create a Tab bar, use the TabView

		TabView {
		    someView().tabItem {
		        Image(systemName: "play.circle.fill")
		        Text("Home")
		    }
		}


2. To render preview for a specific device

		static var previews: some View {
		    SomeView().previewDevice("iPhone 8")
		}

3. To render multiple previews

		static var previews: some View {
			Group {
		   		SomeView().previewDevice("iPhone 8")
		   		SomeView().previewDevice("iPhone 12")
		   	}
		}


**Links:**

n/a

---

### Day 71: 18 May 2021

**Today**: Started "Build an app with SwiftUI Part 2" from Design+Code
 
**Thoughts:** n/a

**Key concepts:**

n/a

**Links:**

1. [Design+Code](https://designcode.io/swiftui2)

---
