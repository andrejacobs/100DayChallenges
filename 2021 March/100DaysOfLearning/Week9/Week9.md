# 100 Days Of Learning

## Log book - Week X

### Day 56: 3 May 2021

**Today**: Worked through episode 15 of iOS Design Handbook.

**Thoughts:** Made some good progress on the mobile workbench today.

**Key concepts:**

1. Use SF Compact and SF Compact Rounded for watchOS.
2. Apple watchOS minimum margin is 9.5 pixels (huh?)

**Links:**

n/a

---

### Day 57: 4 May 2021

**Today**: Finished the iOS Design Handbook by Design+Code. Also learned how the Button Fix type 2 connector works.

**Thoughts:** n/a

**Key concepts:**

n/a

**Links:**

n/a

---

### Day 58: 5 May 2021

**Today**: Started the course SwiftUI for iOS 14 by Design+Code.

**Thoughts:** n/a

**Key concepts:**

1. You can visually edit the SwiftUI code using the attributes inspector.
2. `Cmd + D` will duplicate elements (a bit like Figma).
3. I need a M1 Mac!
4. Padding is the space around an element.
5. Spacing is the space between elements inside a container (like VStack).
6. `Ctrl + Option + click` inside the visual editor will bring up the attribute inspector as a pop over.
7. `Cmd + Shift + L` shows the Library from which you can choose what elements to add.

**Links:**

1. [SwiftUI for iOS 14](https://designcode.io/swiftui2-course)

---

### Day 59: 6 May 2021

**Today**: Worked through lessons 3 to 6 of SwiftUI for iOS 14. Also started reading Building Mobile Apps at Scale by Gergely Orosz

**Thoughts:** I can see what the rage is all about for SwiftUI.

**Key concepts:**

1. `Cmd + N` create new file from selecting a template.
2. Xcode can now create a group and a folder from selection. Used to be "virtual" folders in the project but not on disk.
3. Using SF Symbol icons is as easy as: `Image(systemName: "sfsymbol.icon.name")`
4. Creating a side bar:

		List {
			...
		}
		.listStyle(SidebarListStyle())

5. Creating a navigation view (legacy navigation bar + vc)
	
		NavigationView {
			...
			NavigationLink(destination: someOtherView()) {
				...
			}
		}
		.navigationTitle("Screen name")
		
6. Conditional code for iOS & iPadOS vs macOS

		#if os(iOS)
			...
		#else
			// macOS code
		#endif
		
7. On macOS you can control the window / frame sizing

		.frame(minWidth: 800, minHeight: 600)

8. Toolbar allows you to place bar button items on the top or bottom. Can be placed inside a NavigationView and can contain multiple ToolbarItems

**Links:**

n/a

---

### Day 60: 7 May 2021

**Today**: Worked through lessons 7 to 11 of SwiftUI for iOS 14.

**Thoughts:** I caught a cold earlier in the week and it is at it worst so far.

**Key concepts:**

1. In code you can get a rendered colour in the editor by specifying `Color(lit [autocomplete chose Literal])`
2. Y is important because of such and such

**Links:**

n/a

---
