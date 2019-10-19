# What is Flutter?

1. A UI Toolkit that makes it easy for developers to design beautiful interfaces for all sorts of screen sizes and devices. As Flutter draws changes/animations/interactions onto the blank screen provided by the device, so size doesn't matter.
2. It comes with lots of  pre-built widgets which can be combined (similar to Lego blocks) to create  a beautiful app which can be deployed on all sorts of devices without using any new technology for new device.

# Why Flutter?

1. ***One Codebase*** to maintain, to debug, to update.
2. Need to ***learn Dart only***. No Swift/Java/JavaScript/any other language needed for different devices.
3. ***Simple and flexible layout system*** to build beautiful UI for whatever project you want to build. Flutter gets inspiration from Web.
4. ***Hot Reload*** , i.e. , update code, hit Save and you'll see UI updates.
5. Flutter is ***Open Source*** which gives you access to source code of Flutter.

# Anatomy of Flutter App

- Scaffold (Blank screen for app)
  - AppBar (A pre-built widget to look and act like AppBar)
  - Container (A box to contain the content)
    - Column (to stack widgets vertically)
      1. Row(to position widgets horizontally)
         - Text/Image/Icon/other widgets
         - Icon/Image/Text/other widgets
      2. Image/Text/Icon/other widgets

```dart
Scaffold(
	appBar: AppBar(),
	body: Container(
		child: Column(
			children: [
				Row(
					Text(),
					Icon(),
				),
				Image(),
			]
		)
	),
)
```

# Prerequisites for Flutter Development

1. A computer(**Windows** / MAC)
2. Code Editor(**Android Studio** / VS Code / IntelliJ)
3. Testing(Android using Physical/Virtual device easily / IOS needs MAC or IOS device)
   * Because Apple has Code Signing for security purposes.
4. Toggle Platform
5. Codemagic (Build, Test, Deliver)

# Windows users Installations

### Minimum Requirements

1. Windows 7 or higher
2. ~10 GB storage for complete Setup(for Flutter only 400MB of storage)
3. git

### Installation

1. For Flutter SDK 

   ```
   flutter.dev/docs/get-started/install/windows
   ```

2. Git for Windows

   ```
   
   ```

   