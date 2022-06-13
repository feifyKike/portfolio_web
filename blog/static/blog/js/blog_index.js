function Select(toSelect) {
    // Remove previous messages
    document.getElementById("content-message").innerHTML = "";

    // clear previous selections
    var allCategories = document.getElementById("blog-filter").children[1].children;
    for (var i = 0; i < allCategories.length; i++) {
        document.getElementById("blog-filter").children[1].children[i].children[0].setAttribute("style", "text-decoration: none;");
    }

    // indicate activation
    document.getElementById(toSelect).style.textDecoration = "underline";
}

function Filter(selected) {
    // Remove previous messages
    var posts = document.getElementById("blogs").children[1].children;

    Select(selected);

    // Add those that meet category
    var count = 0;
    for (var i = 0; i < posts.length; i++) {
        var match = false;
        var category = posts[i].children[1].children; // array of categories

        for (var j = 0; j < category.length; j++) {
            if (category[j].innerHTML.trim() == selected) {
                match = true;
                count++;
            }
        }

        if (match) {
            posts[i].style = "display: initial;";
        } else {
            posts[i].style = "display: none;";
        }
    }
    // display message if empty
    if (count == 0) {
        document.getElementById("content-message").innerHTML = "&#8987; Coming soon. Hopefully...";
    }
}

function ShowAll() {
    // Remove previous messages
    var posts = document.getElementById("blogs").children[1].children;

    Select("show-all-posts")

    for (var i = 0; i < posts.length; i++) {
        posts[i].style = "display: initial;";
    }
}