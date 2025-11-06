document.getElementById("order-button")
.addEventListener("click", validate);

grocceries = ["bread", "candy", "milk", "pepperoni"];
// I want to add the word "awesome" at the beginning
// of each item in this groccery list
// 1) for loop
for (let i = 0; i < grocceries.length; i++){
    grocceries[i] = "awesome" + grocceries[i];
}
console.log(grocceries);

function validate(){
    // return true if form is good
    // return false if form is not good
    // --> generate some alerts
    
    // 1) get all of the elements with 
    // the name "topping".
    toppings = document.getElementsByName("topping");
    let counter = 0;
    for (let i = 0; i < toppings.length; i++){
        if(toppings[i].checked){
            counter++;
        }
    }
    if (counter > 3){
        alert("You cannot select more than 3 options")
        return False
    }
}

// TASK: 
// 1) Read about: Javascript Arrays and Javascript Loops
// https://www.w3schools.com/js/js_loops.asp
// https://www.w3schools.com/js/js_loop_while.asp
// https://www.w3schools.com/js/js_arrays.asp

// 2) Programming:
// Validate the user input (when the user checks more than one box, send an alert saying "dont do that")