/*
* AUTHOR: ASHWIN ABRAHAM
*/

function to_red()
{
    document.getElementById("to_change").style = "color: red;";
    document.getElementById("to_blue").style = "position: relative; left: 100px; background-color: blue; padding: 2px 4px;";
    document.getElementById("to_red").style = "position: relative; left: 100px; background-color: red; padding: 5px 10px;";
}

function to_blue()
{
    document.getElementById("to_change").style = "color: blue;";
    document.getElementById("to_red").style = "position: relative; left: 100px; background-color: red; padding: 2px 4px;";
    document.getElementById("to_blue").style = "position: relative; left: 100px; background-color: blue; padding: 5px 10px;";
}

function display()
{
    var txt = document.getElementById("textbox").value;
    if(txt != "") alert("Hello there " + document.getElementById("textbox").value + ", You're doing Well!");
}