function showContacts(region) {  
    $(".contact").css("display", "none"); 
    var contact = $("#" + region);
    contact.css("display", "flex");   
 
    window.scrollTo(contact.offset().left, contact.offset().top); 
}


function bindContactsWithMap(states_info) {  
    for (var state_slug in states_info) { 
        simplemaps_countrymap_mapdata['state_specific'][state_slug] = states_info[state_slug];
    }
} 
bindContactsWithMap(allStates); 