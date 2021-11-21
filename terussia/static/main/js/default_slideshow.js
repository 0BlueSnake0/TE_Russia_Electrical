var slide_number = 0;
var min_slide_number=0;

var last_slide_button = document.getElementById("left");
var next_slide_button = document.getElementById("right");

function turn_on_slide (slide_number, slideshow_id) { 
    $("#slideshow-" + slideshow_id + "-image-" + slide_number).css("display", "flex");
    $("#slideshow-" + slideshow_id + "-dot-" + slide_number).css("backgroundColor","#e98300");
    $("#slideshow-" + slideshow_id + "-dot-" + slide_number).css("width", 20);
    $("#slideshow-" + slideshow_id + "-dot-" + slide_number).css("height", 20);
    $("#slideshow-" + slideshow_id + "-dot-" + slide_number).addClass("checked-dot"); 
    for (var i=0;i<=max_slide_number;i++) {
        if (i != slide_number) { 
            $("#slideshow-" + slideshow_id + "-image-" + i).css("display", "none"); 
            $("#slideshow-" + slideshow_id + "-dot-" + i).css("backgroundColor","white");
            $("#slideshow-" + slideshow_id + "-dot-" + i).css("width", 15);
            $("#slideshow-" + slideshow_id + "-dot-" + i).css("height", 15);
            $("#slideshow-" + slideshow_id + "-dot-" + i).removeClass("checked-dot");
        } 
    }
}
turn_on_slide(0, slideshow_id);

function clickOnDot(choosed, slideshow_id) {
    if (choosed < slide_number) { 
        document.getElementById("slideshow-" + slideshow_id + "-image-" + choosed).style.animationName = "last-slide"; 
    }
    else if (choosed> slide_number) { 
        document.getElementById("slideshow-" + slideshow_id + "-image-" + choosed).style.animationName = "next-slide"; 
    } 
    slide_number = choosed; 
    turn_on_slide(choosed, slideshow_id);  
}

function lastSlide(slideshow_id) {
    if (slide_number>0) {slide_number-=1;}
    else {slide_number=max_slide_number;}  
    var slide = document.getElementById("slideshow-" + slideshow_id + "-image-" + slide_number);
    slide.style.animationName = "last-slide";
    turn_on_slide(slide_number, slideshow_id);
}  

function nextSlide (slideshow_id) {
    if (slide_number<max_slide_number) {slide_number+=1;}
    else {slide_number=min_slide_number;}   
    var slide = document.getElementById("slideshow-" + slideshow_id + "-image-" + slide_number); 
    slide.style.animationName = "next-slide";
    turn_on_slide(slide_number, slideshow_id);
}  

var auto_scrolling = false;

function runAutoSlideshow(slideshow_id) { 
    auto_scrolling = setInterval(function () {nextSlide(slideshow_id);}, 8000);
} 
function stopAutoSlideshow() {clearInterval(auto_scrolling);}   
   
 
function pressKey (event) {   
    switch (event.keyCode) {
        case 37: 
            lastSlide(event.data.slideshow_id);
            break; 
        case 39: 
            nextSlide(event.data.slideshow_id);
            break;  
    }
}

function addKeyControl (slideshow_id) { 
    $("body").on("keydown",{slideshow_id:slideshow_id}, pressKey);
}
function removeKeyControl (slideshow_id) { 
    $("body").unbind("keydown");
}