1. One letter generics
<T>

Naming a generic with one letter

```
function head<T> (arr: T[]): T | undefined {
  return arr[0]
}

```

What it should look like

We’ve now added a type variable T to the identity function. This T allows us to capture the type the user provides (e.g. number), so that we can use that information later.

T可以是任意的type，这里的type是一个变量。例如，如果T是number的话，那么入参就是一个number[]， 我们也可以看到返回结果，是T或者undefined，这个也是正常的，也就是说，在上面这个例子中，输入的arr可以是一个空数组。


## 2Newable
Newable is just a special type of callable type annotation with the prefix new. It simply means that you need to invoke with new e.g.
interface CallMeWithNewToGetString {
  new(): string
}

// Usage
declare const Foo: CallMeWithNewToGetString;
const bar = new Foo(); // bar is inferred to be of type string


3. assertion
A common use case for type assertion is when you are porting over code from JavaScript to TypeScript. For example consider the following pattern:
var foo = {};
foo.bar = 123; // Error: property 'bar' does not exist on `{}`
foo.bas = 'hello'; // Error: property 'bas' does not exist on `{}`
Here the code errors because the inferred type of foo is {} i.e. an object with zero properties. Therefore you are not allowed to add bar or bas to it. You can fix this simply by a type assertion as Foo:
interface Foo {
    bar: number;
    bas: string;
}
var foo = {} as Foo;
foo.bar = 123;
foo.bas = 'hello';

## 4. Readonly
Difference from const
const
is for a variable reference
the variable cannot be reassigned to anything else.
readonly is
for a property
the property can be modified because of aliasing

## 5. never

The never type is used in TypeScript to denote this bottom type. Cases when it occurs naturally:
A function never returns (e.g. if the function body has while(true){})
A function always throws (e.g. in function foo(){throw new Error('Not Implemented')} the return type of foo is never)

比较一下never 和 void呢？？！

## 6. Discriminated Union


interface Square {
    kind: "square";
    size: number;
}

interface Rectangle {
    kind: "rectangle";
    width: number;
    height: number;
}
type Shape = Square | Rectangle;

# 7 type vs interface

拓展（extends）与 交叉类型（Intersection Types）
interface 可以 extends， 但 type 是不允许 extends 和 implement 的，但是 type 缺可以通过交叉类型 实现 interface 的 extend 行为，并且两者并不是相互独立的，也就是说 interface 可以 extends type, type 也可以 与 interface 类型 交叉 。

虽然效果差不多，但是两者语法不同。

interface extends interface
interface Name { 
  name: string; 
}
interface User extends Name { 
  age: number; 
}
type 与 type 交叉
type Name = { 
  name: string; 
}
type User = Name & { age: number  };
interface extends type
type Name = { 
  name: string; 
}
interface User extends Name { 
  age: number; 
}
type 与 interface 交叉
interface Name { 
  name: string; 
}
type User = Name & { 
  age: number; 
}