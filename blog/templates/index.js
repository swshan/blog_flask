$(document).ready(function() {
    test();
    funcOne();
    
    console.log("document ready.");

});

$(window).load(function(){
    console.log("onload");
});

function funcOne() {
    $('a.btn').on('click', function(evt) {
    evt.preventDefault();
    var post_id = $(this).attr('id');
    console.log(post_id);
    $.ajax({
        url: '/api/v1/post/delete/' + post_id,
        type: "POST",
        dataType: "JSON",
        success:function(resp) {
            location.reload()
        }
      })
    });
};

$('a').bind('click', function(eventa) {
    console.log("a is clicked");
});

function test() {
    $.getJSON('http://localhost/golang/test/', function(result) {
            console.log(result);
            $.each(result.result.result, function(i, item) {
                    $('#primary_content').append(
                        "<div class='postlist_title'>" + item.title + "</div>" + 
                        "<div class='postlist_body'>" + item.body + "</div>"
                    ); // append
                } // function item

            ); // each
        } // function result
      
    ); // getjson
}; // test

function funcdom() {

  div =  document.getElementById('primary_content').innerHTML;
  div = div.replace( /\n/g, "<br \>" );
  document.getElementById('primary_content').innerHTML = div;
};

setTimeout('funcdom()',1000);
