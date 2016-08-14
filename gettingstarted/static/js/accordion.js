$(document).ready(function(){
  $(".image").width($("#slider").width()/3.3);

  $(window).resize(function(){
    $(".image").width($("#slider").width()/3.3);
  })

  $(".item-img-1, .item-img-2").each(function(){
    var src = $(this).attr("data-src")
    $(this).css({
      background:`url(${src}) no-repeat`,
    })
  })

  $(".image").mouseover(function(){
    $(this).find(".item-img-1").css({
      opacity:0
    })

    $(this).find(".item-img-2").css({
      opacity:1
    })

    $(".image").width($("#slider").width()/4)
    $(".image").css({"z-index":"-999px"});

    $(this).css({"z-index":"999px"})
    $(this).width($("#slider").width()/2)
  })

  $(".image").mouseout(function(){
    $(this).find(".item-img-2").css({
      opacity:0
    })

    $(this).find(".item-img-1").css({
      opacity:1
    })

    $(".image").width($("#slider").width()/3.3)
    $(this).css({"z-index":0})
  })

  $(".image:last-child").mouseover(function(event){
    $(this).find(".item-img-1").css({
      opacity:0
    })
 
    $(this).find(".item-img-2").css({
      opacity:1
    })

    $(".image").width($("#slider").width()/5)
    $(".image").css({"z-index":"-999px"});

    $(this).css({"z-index":"999px"})
    $(this).width($("#slider").width()/1.5)
  })

})
