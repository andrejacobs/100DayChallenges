# 100 Days Of Learning

## Log book - Week 12

### Day 77: 24 May 2021

**Today**: Worked through lesson 13. Also started on the introduction material for Dub Dub Grub. 

**Thoughts:** n/a

**Key concepts:**

n/a

**Links:**

1. [Sean Allen's Dub Dub Grub](https://seanallen.teachable.com/p/dub-dub-grub-swiftui-mapkit-cloudkit)

---

### Day 78: 25 May 2021

**Today**: Worked through lessons 14 and 15.

**Thoughts:** n/a

**Key concepts:**

n/a

**Links:**

1. [Random user](https://randomuser.me/)
2. [UIFaces](https://uifaces.co/)
3. [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

---

### Day 79: 26 May 2021

**Today**: Worked through lessons 16 to 18.

**Thoughts:** n/a

**Key concepts:**

1. Contentful looks like a nice easy to use CMS for APIs
2. SDWebImage is a nice image loading / caching library.
3. There is also SDWebImageSwiftUI now.
4. You can get a random element from an array with .randomElement()

**Links:**

1. [Contentful CMS](https://www.contentful.com/)
2. [SDWebImage](https://github.com/SDWebImage/SDWebImage.git)

---

### Day 80: 27 May 2021

**Today**: Finished "Build an app with SwiftUI Part 2"

**Thoughts:** n/a

**Key concepts:**

1. You use UIViewRepresentable to bridge UIKit to SwiftUI

		struct SomeView: UIViewRepresentable {
		    typealias UIViewType = UIView
		    
		    func makeUIView(context: Context) -> UIView {
		    }
		    
		    func updateUIView(_ uiView: UIView, context: Context) {
		    }
		}


2. To render the preview in dark mode

		struct SomeView_Previews: PreviewProvider {
		    static var previews: some View {
		        SomeView().environment(\.colorScheme, .dark)
		    }
		}

3. Colours and Images in an asset catalogue can both have values for Dark mode set.

4. To render with a different dynamic type setting.

		.environment(\.sizeCategory, .extraLarge)

**Links:**

n/a

---

### Day 81: 28 May 2021

**Today**: Started on Build an app with SwiftUI Part 3. Worked through the first 2 lessons.

**Thoughts:** I am feeling a bit burned out.

**Key concepts:**

n/a

**Links:**

n/a

---
