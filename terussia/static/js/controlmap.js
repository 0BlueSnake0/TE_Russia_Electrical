function showContacts(region) {  
    $(".contact").css("display", "none"); 
    var contact = $("#" + region);
    contact.css("display", "flex");   
 
    window.scrollTo(contact.offset().left, $(window).height() - contact.offset().top); 
}


function bindContactsWithMap(states) {  
    for (var state_slug in states) simplemaps_countrymap_mapdata['state_specific'][state_slug] = states[state_slug];
}
bindContactsWithMap(allStates); 