Array.from(document.getElementById("language-breakdown").children).forEach(language => {
    language.style.backgroundColor = "#" + Math.floor(Math.random()*16777215).toString(16);
});