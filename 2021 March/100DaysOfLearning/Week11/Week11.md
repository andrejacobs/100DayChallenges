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

### Day 72: 19 May 2021

**Today**: Worked through lesson 4

**Thoughts:** n/a

**Key concepts:**

1. You can create custom modifiers like this

		struct CustomModifier: ViewModifier {
		    func body(content: Content) -> some View {
		        content
		            .shadow(...)
		            .someThingElse()
		    }
		}

		...
		someView
			.modifier(CustomModifier)

2. Font modifiers can be applied to stacks and it will be applied to all Text views in the stack.
3. To add a custom font. Add the files to the bundle and add the following to the Info.plist.

	Fonts provide by application
	* This is an array so you can add the file name of each font from the bundle. I.e. Custom-Font.ttf
4. Then to use it in code.

		.font(.custom("Custom-Font", size: 28.0))

**Links:**

n/a

---

### Day 73: 20 May 2021

**Today**: Worked through lesson 5 & 6

**Thoughts:** I am feeling a lot better after the bronchitis, still the odd cought but a lot better.

**Key concepts:**

n/a

**Links:**

n/a

---

### Day 74: 21 May 2021

**Today**: Worked through lesson 7 to 10

**Thoughts:** I got my first vaccination today. They gave me the Phizer vaccine.

**Key concepts:**

1. To hide the status bar

		var body: some View {
			someView {
				...
			}
			.statusBar(hidden: true)
		}

**Links:**

n/a

---

### Day 75: 22 May 2021

**Today**: Worked through lessons 11 & 12

**Thoughts:** n/a

**Key concepts:**

n/a

**Links:**

n/a

---
