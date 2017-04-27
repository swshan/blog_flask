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
    $.getJSON(
        '/api/v1/posts/get',
        function(result) {
            console.log(result);
            $.each(result.result, function(i, item){
                $("#testing").append(
                    "<div class="PostList_title">" + item.title +"</div>"
                );
            });
        });
}
