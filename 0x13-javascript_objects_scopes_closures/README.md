# 0x13. Javascript - Objects, Scopes and Closures

# General
* Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
* How to create an object in Javascript
* What this means
* What undefined means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

## 0. Rectangle #0
Write an empty class Rectangle that defines a rectangle:

You must use the class notation for defining your class

    guillaume@ubuntu:~/0x13$ cat 0-main.js
    #!/usr/bin/node
    const Rectangle = require('./0-rectangle');

    const r1 = new Rectangle();
    console.log(r1);
    console.log(r1.constructor);

    guillaume@ubuntu:~/0x13$ ./0-main.js
    Rectangle {}
    [Function: Rectangle]
    guillaume@ubuntu:~/0x13$

File: `0-rectangle.js`

## 1. Rectangle #1
Write a class Rectangle that defines a rectangle:

* You must use the class notation for defining your class
* The constructor must take 2 arguments w and h
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`

Example

    guillaume@ubuntu:~/0x13$ cat 1-main.js
    #!/usr/bin/node
    const Rectangle = require('./1-rectangle');

    const r1 = new Rectangle(2, 3);
    console.log(r1);
    console.log(r1.width);
    console.log(r1.height);

    const r2 = new Rectangle(2, -3);
    console.log(r2);
    console.log(r2.width);
    console.log(r2.height);

    const r3 = new Rectangle(2);
    console.log(r3);
    console.log(r3.width);
    console.log(r3.height);

    guillaume@ubuntu:~/0x13$ ./1-main.js
    Rectangle { width: 2, height: 3 }
    2
    3
    Rectangle { width: 2, height: -3 }
    2
    -3
    Rectangle { width: 2, height: undefined }
    2
    undefined
    guillaume@ubuntu:~/0x13$

File: `1-rectangle.js`
