function setMobileInterface() { 
    $(".contact-info a p").css("font-size", "1.5em");
    $(".under-header-content span").css("font-size", "25pt");
    $(".under-header-content .under-header-title").css("font-size", "25pt");  
    $("#footer-info #footer-copyright").css("font-size", "2em"); 
    $("#footer-info label a p").css("font-size", "2em"); 
    
    $(".dropdown-icon").css("width", "4.25vh"); 
    $(".search-icon").css("width", "4.25vh"); 
    $(".search-icon").css("height", "4.25vh"); 
    $("#address-and-tel .default-text img").css("width", "4em"); 
    $("#footer-info label img").css("width", "4em");    

    $("#huge-nums .flexbox-layer-1").css("font-size", "100px");  
    $("#huge-nums .flexbox-layer-2").css("font-size", "60px");  
    $("#huge-nums .flexbox-layer-3").css("font-size", "25px");  
     
    $("#site-navigation-750-minus .menu-item-content-1 #content").css("font-size", "28pt");  
    $(".menu-item-content-1 img").css("width", "28px");  
    $(".menu-item-content-1 img").css("height", "16px");  

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
    $("#site-navigation-750-minus #sn-750-minus .search-icon").css("margin-right", "10vw"); 

    $("#site-navigation-750-minus .search-box .searcher-field").css("left", "4em"); 
} 


function isMobileDevice() {
    var isMobile = (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
    return isMobile;
}
   
if (isMobileDevice() == true || window.innerWidth <= 750) { 
    setMobileInterface();
}  
else {
    var desktop_navigation = document.getElementById("site-navigation-750-plus"); 
    window.addEventListener( "scroll", function(e) {  
            var scrolled = document.body.scrollTop - desktop_navigation.offsetTop; 
            if (scrolled > 100 ) { 
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