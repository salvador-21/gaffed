$(document).ready(function(){
// ///////////////////////////////
$("form").attr('autocomplete', 'off');

// LOGIN SUBMIT
$('#auth').on('submit',function(e){
    e.preventDefault()
    err='<div class="alert alert-danger alert-dismissible" role="alert">\
    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>\
    <i class="fa fa-times-circle"></i> Invalid Credentials!</div>'
   
    data=$(this).serializeArray()
    
    $.ajax({
        method:'POST',
        url:'auth_user',
        data:data,
        success:function(res){
           if(res.data == 'err'){
            $('.message').html('')
            $('.message').append(err)
           }else{
            window.location.href = 'homepage';
            console.log(res.acc)
           }
        //    $('#auth').trigger('reset')
        }
    })
    
})



// //////////////////////////////////
})