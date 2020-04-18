
$('.fa').click(event=>{
    if($('.btn').is(":visible")){
        $(event.target).css('transform','rotate(0deg)')
        $('.btn').slideUp();
    }
    else{
        $(event.target).css('transform','rotate(45deg)')
        $('.btn').slideDown();
    }
})