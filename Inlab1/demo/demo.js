// AUTHOR: ASHWIN ABRAHAM

var current = "cat.jpg";
function change()
{
    if(current == "cat.jpg") current = "dog.jpg";
    else current = "cat.jpg";
    document.getElementById("img").src = current;
}