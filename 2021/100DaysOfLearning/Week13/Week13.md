# 100 Days Of Learning

## Log book - Week X

### Day 84: 31 May 2021

**Today**: Worked through lesson 6 & 7

**Thoughts:** n/a

**Key concepts:**

1. You can have multiple modifiers like `frame`, `background` etc.

        .frame(height: 477)
        .frame(maxWidth: .infinity)
        .background(Image(uiImage: #imageLiteral(resourceName: "Card3")))
        .background(Color(#colorLiteral(red: 0.4117647059, green: 0.4705882353, blue: 0.9725490196, alpha: 1)))


2. To align background content to the bottom of it's frame.

		.background(Image(uiImage: #imageLiteral(resourceName: "Card3")), alignment: .bottom)

**Links:**

n/a

---

### Day 85: 1 June 2021

**Today**: Worked through lesson 8 to 10.

**Thoughts:** n/a

**Key concepts:**

1. SwiftUI text field

		TextField("Your Email".uppercased(), text: $email)
		    .keyboardType(.emailAddress)
		    .font(.subheadline)


2. Secure entry text field

		SecureField("Password".uppercased(), text: $password)
			.keyboardType(.default)
			.font(.subheadline)

3. To dismiss the keyboard

	    func hideKeyboard() {
	        UIApplication.shared.sendAction(#selector(UIResponder.resignFirstResponder), to: nil, from: nil, for: nil)
	    }


**Links:**

1. [LottieFiles](https://lottiefiles.com/)

---

### Day 86: 2 June 2021

**Today**: Worked through lessons 11 & 12. Login with Firebase.

**Thoughts:** n/a

**Key concepts:**

n/a

**Links:**

n/a

---

### Day 87: 3 June 2021

**Today**: Worked through lessons 13 to 15.

**Thoughts:** n/a

**Key concepts:**

1. You can bind/inject objects using `@EnvironmentObject` and provide the value to a view using `.enivornmentObject(theInstance)`
2. Y is important because of such and such

**Links:**

n/a

---

### Day 88: 4 June 2021

**Today**: Completed "Build an app with SwiftUI Parts 1 - 3".

**Thoughts:** This was a long course!

**Key concepts:**

n/a

**Links:**

n/a

---

### Day 89: 5 June 2021

**Today**: Learned how to model Steel square tubing in Fusion 360

**Thoughts:** Did a lot of sanding today.

**Key concepts:**

* Start a sketch
* Parameters: SteelWidth = 25mm, SteelHeight = 25mm, SteelThickness = 2mm, SteelOuterRadius = 1.5 * SteelThickness, SteelInnerRadius = 1.0 * SteelThickness
* Draw a rectangle: SteelWidth x SteelHeight
* Draw the inside rectangle: (SteelWidth - (SteelThickness * 2)) x (SteelHeight - (SteelThickness * 2))
* Dimension the inside rectangle to be SteelThickness away from bottom and left side
* Fillet the outside corners with SteelOuterRadius
* Filler the inside corners with SteelInnerRadius
* End sketch and Extrude to length

**Links:**

n/a

---

### Day 90: 6 June 2021

**Today**: A couple of woodworking tips and more on modeling with Fusion 360.

**Thoughts:** Spent some more time on the quick desk built today. Joined the legs. Stained all of it.

**Key concepts:**

1. Use anti-fog spray on goggles / masks etc. Motorcyclist use it.
2. Can use a digital inclometer to set a honing guide for sharpening plane blades.

**Links:**

1. [Woodworking tips](https://www.youtube.com/watch?v=z6hJgOVcHy4&t=6s)
2. [Model Diresta's workbench](https://www.youtube.com/watch?v=AH3QWscviBc)

---
