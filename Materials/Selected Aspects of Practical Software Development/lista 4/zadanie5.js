var Foo = function () {
    const Qux = () => {
      console.log("Qux function is called.")
    }

    this.Bar = () => {
      console.log("Bar function is called.")
      Qux()
    }
}

var fooInstance1 = new Foo()
var fooInstance2 = new Foo()

// fooInstance1.Qux()
fooInstance1.Bar() 
fooInstance2.Bar()