var counters = $(".animated-number");

function animateNumber(counter, start, end, duration) {
    let startTime= null;
    const step = (timestamp) => {
        if (!startTime) startTime = timestamp;
        const progress = Math.min((timestamp - startTime) / duration, 1);
        counter.innerHTML = Math.floor(progress * (end - start) + start);
        if (progress < 1) window.requestAnimationFrame(step);
    };
    window.requestAnimationFrame(step);
}

function animateAllNumbers () {  
    var dep = document.getElementById("department-info");
    var showed = document.getElementById("animated-numbers");  
    if (showed.value == "false" && dep.offsetTop -document.body.scrollTop <= 640) { 
        for (var i=0;i<counters.length;i++) {  
            var counter = counters[i]; 
            var number = counter.innerHTML; 
            animateNumber(counter, 0, number, 2000);
        }
        showed.value = "true";
        window.removeEventListener("scroll", animateAllNumbers);
    }  
}  
window.addEventListener("scroll", animateAllNumbers);
