var slide_number = 0;
var min_slide_number=0;   

function turn_on_slide (data_type, slide_number, slideshow_id) { 
    $("#" + data_type + "-slideshow-" + slideshow_id + "-" + slide_number).css("display", "flex");
    $("#" + data_type + "-slideshow-" + slideshow_id + "-dot-" + slide_number).css("backgroundColor","#e98300");
    $("#" + data_type + "-slideshow-" + slideshow_id + "-dot-" + slide_number).css("width", 20);
    $("#" + data_type + "-slideshow-" + slideshow_id + "-dot-" + slide_number).css("height", 20);
    $("#" + data_type + "-slideshow-" + slideshow_id + "-dot-" + slide_number).addClass("checked-dot"); 

    for (var i=0;i<=max_slide_numbers[data_type + "-slideshow-" + slideshow_id];i++) { 
        if (i != slide_number) { 
            $("#" + data_type + "-slideshow-" + slideshow_id + "-" + i).css("display", "none"); 
            $("#" + data_type + "-slideshow-" + slideshow_id + "-dot-" + i).css("backgroundColor","rgba(125,125,125,0.75)");
            $("#" + data_type + "-slideshow-" + slideshow_id + "-dot-" + i).css("width", 15);
            $("#" + data_type + "-slideshow-" + slideshow_id + "-dot-" + i).css("height", 15);
            $("#" + data_type + "-slideshow-" + slideshow_id + "-dot-" + i).removeClass("checked-dot");
        } 
    }
}
turn_on_slide(data_type, 0, slideshow_id);

function clickOnDot(data_type, choosed, slideshow_id) {
    if (choosed < slide_number) { 
        document.getElementById(data_type + "-slideshow-" + slideshow_id + "-" + choosed).style.animationName = "last-slide"; 
    }
    else if (choosed> slide_number) { 
        document.getElementById(data_type + "-slideshow-" + slideshow_id + "-" + choosed).style.animationName = "next-slide"; 
    } 
    slide_number = choosed; 
    turn_on_slide(data_type, choosed, slideshow_id);  
}

function lastSlide(data_type, slideshow_id) {
    if (slide_number>0) {slide_number-=1;}
    else {slide_number=max_slide_numbers[data_type + "-slideshow-" + slideshow_id];}  
    var slide = document.getElementById(data_type + "-slideshow-" + slideshow_id + "-" + slide_number);
    slide.style.animationName = "last-slide";
    turn_on_slide(data_type, slide_number, slideshow_id);
}  

function nextSlide (data_type, slideshow_id) {
    if (slide_number<max_slide_numbers[data_type + "-slideshow-" + slideshow_id]) {slide_number+=1;}
    else {slide_number=min_slide_number;}   
    var slide = document.getElementById(data_type + "-slideshow-" + slideshow_id + "-" + slide_number); 
    slide.style.animationName = "next-slide";
    turn_on_slide(data_type, slide_number, slideshow_id);
}  
 
var interval;
function runAutoSlideshow(data_type, slideshow_id) {   
    interval= setInterval(function () {nextSlide(data_type, slideshow_id);}, delays[data_type + "-slideshow-" + slideshow_id]*1000);
} 
function stopAutoSlideshow(data_type, slideshow_id) {  
    clearInterval(interval); 
}   
   
 
function pressKey (event) {   
    switch (event.keyCode) {
        case 37:  
            lastSlide(event.data.dtype, event.data.sldshw_id);
            break; 
        case 39:  
            nextSlide(event.data.dtype, event.data.sldshw_id);
            break;  
    }
}

function addKeyControl (data_type, slideshow_id) {   
    $("body").on("keydown",{dtype:data_type, sldshw_id:slideshows[data_type + "-slideshow-" + slideshow_id] }, pressKey);
}
function removeKeyControl () {  
    $("body").unbind("keydown");
}