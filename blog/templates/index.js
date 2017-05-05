$(document).ready(function() {
    test();
    console.log("document ready.");
});

$(window).load(function(){
    console.log("onload");
    funcOne();
});

function funcOne() {

}

function test() {
    $.getJSON('/api/v1/posts/get', function(result) {
            $.each(result.result, function(i, item) {
                    $('#testing').append(
                        "<div class='postlist_title'>" + item.title + "</div>" + 
                        "<div class='postlist_body'>" + item.body + "</div>"
                    ); // append
                } // function item

            ); // each
        } // function result
      
    ); // getjson
} // test