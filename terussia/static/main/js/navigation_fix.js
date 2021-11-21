
var navigation_2 = document.getElementById("site-navigation-750-plus");
window.addEventListener(
    "scroll", function(e) {  
        if (window.innerWidth > 750) { 
            var scrolled = document.body.scrollTop - navigation_2.offsetTop; 
            if (scrolled > 360 ) {
                navigation_2.classList.add("to-fix-2"); 
            }
            else {navigation_2.classList.remove("to-fix-2");} 
        }
    }
);