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
