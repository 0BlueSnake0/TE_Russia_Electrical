function setMobileInterface() { 
    $("#address-and-tel").css("flex-direction", "column");
    $("#address-and-tel").css("flex-wrap", "wrap");
    $("#address-and-tel").css("margin-left", "auto");
    $("#address-and-tel").css("margin-right", "auto");

    $("#logo").css("margin-left", "auto");
    $("#logo").css("margin-right", "auto"); 
    
 
    $(".gray-vl").css("display", "none");
    $(".gray-gl").css("display", "none");  

    $("#site-navigation-750-plus #sn-750-plus").css("display", "none");  

    $("#site-navigation-750-minus").css("display", "flex");
    $("#site-navigation-750-minus #sn-750-minus").css("display", "flex"); 
    $("#site-navigation-750-minus #sn-750-minus").css("top", "0");  
    $("#site-navigation-750-minus #sn-750-minus").css("position", "fixed");  
    $("#site-navigation-750-minus #sn-750-minus").css("animation-name", "opacity-occurance-1");  
    $("#site-navigation-750-minus #sn-750-minus").css("animation-duration", "1s");  
     

    $("header .search-box").css("display", "none");  

    $("#site-navigation-750-minus #sn-750-minus .search-box").css("display", "flex"); 
    $("#site-navigation-750-minus #sn-750-minus .search-box").css("margin-right", "2em"); 

    $("#site-navigation-750-minus .search-box .searcher-field").css("left", "4em"); 
} 


function isMobileDevice() {
    var isMobile = (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
    return isMobile;
}
   
if (isMobileDevice() == true || window.innerWidth < 750) { 
    setMobileInterface();
}  
else {
    var desktop_navigation = document.getElementById("site-navigation-750-plus"); 
    window.addEventListener( "scroll", function(e) {  
            var scrolled = document.body.scrollTop - desktop_navigation.offsetTop; 
            if (scrolled > 400 ) { 
                document.getElementById("page-up").style.display = "flex"; 
                    desktop_navigation.classList.add("to-fix-2");  
            }
            else {
                document.getElementById("page-up").style.display = "none";
                desktop_navigation.classList.remove("to-fix-2");
            } 
        }
    ); 
}