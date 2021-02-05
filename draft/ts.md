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

