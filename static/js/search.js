function fetchSuggestions(query,url) {
    $.ajax({
        url: url,  // Update the URL to the URL of your search suggestion view
        data: {'q': query},
        dataType: 'json',
        success: function(data) {
            // Handle the suggestions received in the JSON response
            window.history.replaceState({}, document.title, window.location.origin + '/');
            var ids = data.ids;
            var names = data.names;
            var len = ids.length;
                    $("#suggestions-list").empty();
                    if(len!=0){
                        for( var i = 0; i<len; i++){
                            $('#suggestions-list').show();
                            $("#suggestions-list").append("<a class=\"text-secondary mb-2\" href=\"ProductDetails/"+ids[i]+"/\"><i class=\"fa fa-angle-right mr-2\"></i>"+names[i]+"</a> <br>");
                            //we got the response
                        }
                    }
                    else{
                        $('#suggestions-list').hide();
                    }
                    // alert('Successfully called');
                    
            // Update your UI with the suggestions, e.g., populate a dropdown with the suggestions
        },
        error: function(jqxhr, status, exception) {
            alert('Exception:', exception)}
        
    });
}

// Attach an event listener to your search box input field
$('#search-box').on('input', function() {
    var query = $(this).val();
    var url = $(this).attr('href');
    if(query==''){
        $('#suggestions-list').hide();
    } 
    else{
        fetchSuggestions(query,url);
    }
});