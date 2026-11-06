class Person {
    constructor() {
        this.species = "homo sapiens";
    }
    eat(){
        console.log("eat");
    }
    
}

class Engineer  extends Person {
    constructor(branch) {
        console.log("enter child constructor");
        super(); //to invoke parent class constructor
        this.branch = this.branch;
        console.log("exit child constructor");
    }
    work(){
        console.log("solve problems,build something");
    }
}


let engObj = new Engineer("chemical engineer");