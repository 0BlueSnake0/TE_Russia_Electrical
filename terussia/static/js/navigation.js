var desktop_navigation = document.getElementById("desktop-navigation");
var fix = 150;
window.addEventListener(
    "scroll", function(e) {
        var scrolled = document.body.scrollTop - desktop_navigation.offsetTop;
        if (scrolled >= fix ) {
            $("#desktop-navigation").css("position", "fixed");
            $("#desktop-navigation").css("top", "0");
            $("#desktop-navigation").css("left", "0");
            $("#desktop-navigation").css("box-shadow", "4px 4px 47px 11px rgba(0, 0, 0, 0.2)");
        }
        else {
            $("#desktop-navigation").css("position", "relative");
            $("#desktop-navigation").css("box-shadow", "0px 0px 0px 0px");
        }
    }
);
