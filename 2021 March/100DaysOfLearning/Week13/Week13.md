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
