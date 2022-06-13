function Loading_Screen() {
    var i = 0;
    var elem = document.getElementById("myBar");
    var width = 1;
    var id = setInterval(function() {
        if (width >= 100) {
            clearInterval(id);
        } else {
            width++;
            document.getElementById('progress-bar').style.width = width + "%";
            document.getElementById('counter-percent').innerHTML = width + "%";
        }
    }, 4);
    setTimeout(showPage, 1000);
};
function showPage() {
    // Display Items
    document.getElementById("loader-container").style.display = "none";
    document.getElementById("landing-page").style.display = "block";
};