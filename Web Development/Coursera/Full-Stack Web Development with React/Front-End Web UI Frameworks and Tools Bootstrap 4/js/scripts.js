$(document).ready(function() {
    $('#mycarousel').carousel({ interval: 2000 });
    $('#carouselButton').click(function() {
        if ($('#carouselButton').children('span').hasClass('fa-pause')) {
            $('#mycarousel').carousel('pause');
            $('#carouselButton').children('span').removeClass('fa-pause');
            $('#carouselButton').children('span').addClass('fa-play');
        }
        else if ($('#carouselButton').children('span').hasClass('fa-play')) {
            $('#mycarousel').carousel('cycle');
            $('#carouselButton').children('span').removeClass('fa-play');
            $('#carouselButton').children('span').addClass('fa-pause');
        }
        $('#mycarousel').carousel('pause');
    });
    $("#reserveTableBtn").click(function(){
        $("#reserveTable").modal('show');
    });
    $("#loginBtn").click(function(){
        $("#loginModal").modal('show');
    });       

    $("#cancelLoginBtn").click(function(){
        $("#loginModal").modal("hide");
        
    });
    $("#cancelReserveBtn").click(function(){
        $("#reserveTable").modal("hide");
        
    });
});