# 100 Days Of Learning

## Log book - Week 10

### Day 63: 10 May 2021

**Today**: Week 10 is off with a blast. Managed to finish the SwiftUI for iOS 14 course by Design+Code and got a certificate.

**Thoughts:** Aww yeah

**Key concepts:**

1. NavigationLink is used to make an element pop on another View on the navigation stack.
2. NavigationLink will tint the elements so you need to override the foreground colour if needed.
3. To show a modal view

		@State var showModal = false

		someThing
			.sheet(isPresented: $showModal) {
		    	viewToBeShownModally
			}

4. To dismiss a modal view

		@Environment(\.presentationMode) var presentationMode
		
		...
		presentationMode.wrappedValue.dismiss()
		
5. You can add your own Views (components) to the Library (Cmd + Shift + L)

		struct LibraryContent: LibraryContentProvider {
		    @LibraryContentBuilder
		    var views: [LibraryItem] {
		        LibraryItem(componentView(), category: .control)
		    }
		}

6. To add your own View modifiers

		extension View {
			func someModifier() -> some View {
				return self
					.otherModifiersEtc
			}
		}

**Links:**

n/a

---

### Day 64: 11 May 2021

**Today**: Started the course "Build an app with SwiftUI Part 1" by Design+Code

**Thoughts:** n/a

**Key concepts:**

n/a

**Links:**

n/a

---

### Day 65: 12 May 2021

**Today**: Worked through lesson 3 & 4.

**Thoughts:** n/a

**Key concepts:**

1. You refactor chunks of SwiftUI (containers) to its own view by `Cmd + Click` and selecting Extract Subview.
2. Some handy view modifiers
	
	    .offset(x: 0.0, y: -40.0)
	    .scaleEffect(0.9)
	    .rotationEffect(.degrees(10.0))
	    .rotation3DEffect(.degrees(10.0),
	        axis: (x: 10.0, y: 0.0, z: 0.0))
	    .blendMode(.hardLight)

3. Can change text alignment with `.multilineTextAlignment(.center)`
4. To stretch a view to the maximum available space:

		.frame(maxWidth: .infinity)

**Links:**

1. n/a

---

### Day 66: 13 May 2021

**Today**: Worked through lessons 5 & 6

**Thoughts:** n/a

**Key concepts:**

n/a

**Links:**

n/a

---

### Day 67: 14 May 2021

**Today**: Worked through lesson 7 to 10.

**Thoughts:** Still sick as a dog, but at least Covid test was negative.

**Key concepts:**

1. .background takes any view
2. Color is a view, hence you can do .background(Color.blue)
3. You can a linear gradient by using LinearGradient (as a background view)
4. You can use .overlay to place a view outside of clipping areas.

**Links:**

n/a

---

### Day 68: 15 May 2021

**Today**: Worked through lessons 11 to 16.

**Thoughts:** n/a

**Key concepts:**

1. Can create a binding to a state using @Binding

		struct someView: View {
			@Binding var showSomething: Bool
			...
		}

		// Where it is used
		@State var showSomething = false
		someView(showSomething: $showSomething)
		
2. If you don't have a state to bind to (e.g. Preview) you can use `.constant(value)`


**Links:**

n/a

---

### Day 69: 16 May 2021

**Today**: Worked through lessons 17 - 19.

**Thoughts:** n/a

**Key concepts:**

1. Most minimal code to explain "Navigation VC" + Table View + Push on VC (old skool equivalent)

        NavigationView {
          List(0 ..< 5) { item in
            NavigationLink(destination: Text("Push on")) {
                    Text("List item title")
                }
            }
            .navigationTitle(Text("Updates"))
	    }


2. **NOTE:** You put the navigation bar title on the inner view and NOT the NavigationView.
3. You can limit the lines of text using `.lineLimit(2)`
4. Navigation bar items:

		.navigationBarItems(leading: someView,
		  trailing: EditButton())
5. **NOTE:** You can have a built-in `EditButton` that just does the right thing.


**Links:**

n/a

---
