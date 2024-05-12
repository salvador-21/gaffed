$(document).ready(function(){

    // ///////////////////////
    $(document).on('click','.signout',function(){
        if (confirm('Are you sure?')) {
            window.location.href = 'signout';
          }
    })

    // /////////////////////
})