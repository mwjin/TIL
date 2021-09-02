---
layout: default
title: Module
parent: Basics
grand_parent: Go
nav_order: 1
---
# module
Usually we want to create a module and import it from the other code. In this case, Go recommends using **Go modules** instead of ``GOPATH`` to organize your Go projects. Here is a basic usage of Go modules.

## Situation

Here is a simple Go project to print greetings such as "Hello, World!". Current directory consists of ...

```bash
.
├── greeting
│   └── greeting.go
└── main.go
```

*greeting/greeting.go* is ..

```go
package greeting

import "fmt"

func HelloWorld() {
  fmt.Println("Hello, World!")
}

func ByeWorld() {
  fmt.Println("Bye, World!")
}

```

and the *main.go* is ...

```go
package main

import "github.com/mwjjeong/go-greeting/greeting"

func main() {
  greeting.HelloWorld()
  greeting.ByeWorld()
}

```

But we cannot execute the ``main.go`` because it cannot import ``greeting``  package.

```bash
$ go run main.go
main.go:3:8: no required module provides package github.com/mwjjeong/go-greeting/greeting: go.mod file not found in current directory or any parent directory; see 'go help modules'
```

## Solution

In this case we can simply solve this problem using ``go mod init``,  which make your directory as a Go module.

```bash
# In your project root directory
$ go mod init github.com/mwjjeong/go-greeting
```

Now the directory consists of ...

```bash
.
├── go.mod
├── greeting
│   └── greeting.go
└── main.go
```

and you can run `main.go`

```bash
$ go run main.go
Hello, World!
Bye, World!
```

## Summary
* ``go mod init`` to initialize your Go project
