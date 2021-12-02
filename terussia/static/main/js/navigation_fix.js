
var navigation_2 = document.getElementById("site-navigation-750-plus");
window.addEventListener(
    "scroll", function(e) {  
        var scrolled = document.body.scrollTop - navigation_2.offsetTop; 
        if (scrolled > 400 ) { 
            document.getElementById("page-up").style.display = "flex";
            if (window.innerWidth > 750) { 
                navigation_2.classList.add("to-fix-2"); 
            } 
        }
        else {
            document.getElementById("page-up").style.display = "none";
            navigation_2.classList.remove("to-fix-2")
        } 
    }
);