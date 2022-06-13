function Select(toSelect) {
    // Remove previous messages
    document.getElementById("content-message").innerHTML = "";

    // clear previous selections
    var allCategories = document.getElementById("project-filter").children[0].children;
    for (var i = 0; i < allCategories.length; i++) {
        document.getElementById("project-filter").children[0].children[i].children[0].setAttribute("style", "text-decoration: none;");
    }

    // indicate activation
    document.getElementById(toSelect).style.textDecoration = "underline";
}

function Filter(selected) {
    var project_children = document.getElementById("projects").children;

    Select(selected);

    // filter those that meet category
    var count = 0;
    for (var i = 0; i < project_children.length; i++) {
        var match = false;
        var category = project_children[i].children[0].children[0].children[1]; // array of categories
        
        for (var j = 0; j < category.children.length; j++) {
            if (category.children[j].innerHTML == selected) {
                match = true;
                count++;
            }
        }
        if (match) {
            project_children[i].style = "display: initial";
        } else {
            project_children[i].style = "display: none;";
        }
    }
    // display message if empty
    if (count == 0) {
        document.getElementById("content-message").innerHTML = "&#8987; Something in works. Hold tight!";
    }
}

function ShowAll() {
    var project_children = document.getElementById("projects").children;
    
    Select("show-all-projects");

    // loop and show all
    for (var i = 0; i < project_children.length; i++) {
        document.getElementById("projects").children[i].style = "display: initial;";
    }
}