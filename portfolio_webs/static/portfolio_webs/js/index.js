// Hide cursor on click
document.addEventListener('click', function() {
    var e = document.getElementById('name-styling');
    if (e.getAttribute('style') == "animation-name: blink;") {
        e.setAttribute('style', 'animation-name: none;');
    } else {
        e.setAttribute('style', 'animation-name: blink;');
    };
});