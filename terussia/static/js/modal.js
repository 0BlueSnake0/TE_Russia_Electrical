
function OpenModal(id) {   
    var backgroundId = "#" + id + "-background";
    console.log("opening " + backgroundId);
    $(backgroundId).css("display", "block");
}  

function CloseModal(id) {    
    var backgroundId = "#" + id + "-background";
    $(backgroundId).css("display", "none");
}   