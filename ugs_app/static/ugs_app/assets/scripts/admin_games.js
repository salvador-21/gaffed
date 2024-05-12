$(document).ready(function(){

    $('#game_img').on('change',function(){
        getImagePreview(event)
    })

    function getImagePreview(event)
    {
      var image=URL.createObjectURL(event.target.files[0]);
      var imagediv= document.getElementById('preview');
      var newimg=document.createElement('img');
      imagediv.innerHTML='';
      newimg.src=image;
      newimg.width="300";
      imagediv.append(newimg);
    }
    
    $('#game_frm').on('submit',function(e){
        e.preventDefault()
        $.ajax({
            url: "add_games",
            type: "POST",
            data: new FormData(this),
            cenctype: 'multipart/form-data',
            processData: false,
            contentType: false,   
            success: function(res){
            console.log(res)
            },
            error: function(){}
            });
    })

})