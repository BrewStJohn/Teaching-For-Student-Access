

// grocceries = ["bread", "candy", "milk", "pepperoni"];
// // I want to add the word "awesome" at the beginning
// // of each item in this groccery list
// // 1) for loop
// for (let i = 0; i < grocceries.length; i++){
//     grocceries[i] = "awesome" + grocceries[i];
// }
// console.log(grocceries);

document.getElementById("order-button").addEventListener("click", handleOrderClick);

function validate(){
    let toppings = document.getElementsByName("topping");
    // console.log(toppings);
    let counter = 0;
    for (let i = 0; i < toppings.length; i++){
        // console.log(i);
        if(toppings[i].checked){
            counter++;
            // console.log('Counter: ' + counter);
        }
    }
    if (counter > 3){
        alert("You cannot select more than 3 options");
        return false;
    }
    return true;
}

function buildOrder(){
    // Add up all of the info from our webpage
    // and put it into an object
    let order = {};
    order.size = document.getElementById("size-input").value;
    //console.log(order);
    order.crust = document.getElementById("crust-input").value
    //console.log(document.getElementById("crust-input").value);

    // get every sauce input
    const sauces = document.getElementsByName("sauce");
    console.log(sauces);
    // for every sauce
    for (let i = 0; i < sauces.length; i++){
        // if a sauce is checked
        if(sauces[i].checked){
            // add it to the order
            order.sauce = sauces[i].value;
            // leave the loop early
            break;
        }  
    }

    return order;
}

function handleOrderClick(){
    order = buildOrder();
    console.log(order);
    validate();
}

// TASK: 
// 1) Read about: Javascript Arrays and Javascript Loops
// https://www.w3schools.com/js/js_loops.asp
// https://www.w3schools.com/js/js_loop_while.asp
// https://www.w3schools.com/js/js_arrays.asp

// 2) Programming:
// Validate the user input (when the user checks more than one box, 
// send an alert saying "dont do that")