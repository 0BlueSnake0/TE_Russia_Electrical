function ActivateSlide(slideshowID, slideIndex)
{ 
    var lastIndex = activated_slides[slideshowID];
    if (slideIndex != lastIndex) {
        $("#" + slideshowID  + " .slides .slide").css("display", "none");
        var slideToActivate =  $("#" + slideshowID  + " .slides" + " #" + slideshowID + "-slide-" + slideIndex);
        var oldDot =        $("#" + slideshowID + " #" + slideshowID + "-dot-" + lastIndex);
        var dotToActivate = $("#" + slideshowID  + " #" + slideshowID + "-dot-" + slideIndex);
        if (lastIndex < slideIndex) slideToActivate.css("animation-name", "swipe-left");
        else if (lastIndex > slideIndex) slideToActivate.css("animation-name", "swipe-right");
        slideToActivate.css("display", "block");
        dotToActivate.css("width", $(":root").css("--active-dot-width"));
        oldDot.css("width", $(":root").css("--not-active-dot-width"));
        activated_slides[slideshowID] = slideIndex;
    }
}
if (slides.length > 0) ActivateSlide(currentSlideshowID, 0);


function prevSlide(slideshowID) {
    var lastIndex = activated_slides[slideshowID], slideIndex= lastIndex-1;
    if (slideIndex < 0) slideIndex = max_slide_numbers[slideshowID]-1; 

    ActivateSlide(slideshowID, slideIndex);
    activated_slides[slideshowID] = slideIndex;
}  


function nextSlide (slideshowID) {
    var lastIndex = activated_slides[slideshowID], slideIndex = lastIndex+1; 
    if (slideIndex == max_slide_numbers[slideshowID]) slideIndex = 0;  

    ActivateSlide(slideshowID, slideIndex);
    activated_slides[slideshowID] = slideIndex;
}  


var autoSlideShow; 
var delay = 8;

function runAutoSlideShow(slideshowID) {   
    autoSlideShow = setInterval(function() {nextSlide(slideshowID);}, delay*1000);
} 


function stopAutoSlideShow() {  
    clearInterval(autoSlideShow); 
}   


function pressKey(event) {  
    switch (event.keyCode) {
        case 37:  
            prevSlide(event.data.slideshowID);
            break; 
        case 39:  
            nextSlide(event.data.slideshowID);
            break;  
    }
}


function addKeyControl (slideshowID) {    
    $("body").on("keydown",{slideshowID:slideshowID }, pressKey);
}


function removeKeyControl () {   
    $("body").unbind("keydown");
}