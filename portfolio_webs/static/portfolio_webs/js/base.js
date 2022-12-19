function Loading_Screen() {
    var width = 1;
    var id = setInterval(function() {
        if (width >= 100) {
            clearInterval(id);
        } else {
            width++;
            document.getElementById('progress-bar').style.width = width + "%";
            document.getElementById('counter-percent').innerHTML = width + "%";
        }
    }, 5);
    setTimeout(showPage, 1400);
};
function showPage() {
    // Display Items
    document.getElementById("loader-container").style.display = "none";
    document.getElementById("landing-page").style.display = "block";
};