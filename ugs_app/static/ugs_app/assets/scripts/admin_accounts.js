$(document).ready(function(){

    $("form").attr('autocomplete', 'off');


  $("#user_search").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#user_tbl tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
  
    $('.addaccount').on('click',function(){

        $('#user_mdl').modal({backdrop:'static',keyboard:false, show:true})
    })
    
    load_user()

    function load_user(){
    
        $.ajax({
            method:'POST',  
            url:'getuser',
            success:function(res){
               cc=1
                $('#user_tbl').html('')
                profile='<img src="static/ugs_app/assets/user.png" data-toggle="tooltip" data-placement="top" title="" alt="Avatar" class="w35 h35 rounded" data-original-title="Avatar Name" aria-describedby="tooltip280040">'
                for(d in res.data){
                    for(w in res.wdata){
                        if(res.data[d].u_id == res.wdata[w].w_user){
    
                            // console.log(res.data[d].username +' -'+res.wdata[w] )
                            stat = res.data[d].status
                            if(stat == 'BANNED'){
                                stat='badge-danger'
                            }else if(stat == 'INACTIVE'){
                                stat='badge-warning'
                            }else{
                                stat='badge-success'
                            }
                            data='<tr><td><span>'+ cc++ +'</span></td><td>\
                            <div class="d-flex align-items-center">\
                            <div class="avtar-pic w35 bg-red" data-toggle="tooltip" data-placement="top" title="Avatar Name">'+profile+'</div>\
                            <div class="ml-3"><a href="#" class="text-warning" style="font-weight: bolder;" title>'+res.data[d].username+'</a><p>\
                            '+res.data[d].usertype+'</p></div></div></td><td>'+res.wdata[d].w_balance+'</td><td>'+res.data[d].join_date+'</td>\
                            <td><span class="badge '+stat+' ml-0 mb-0" style="padding:2px">'+res.data[d].status+'</span></td><td>\
                            <button type="button" class="btn btn-sm btn-default" title="Send Invoice" data-toggle="tooltip" data-placement="top"><i class="icon-envelope"></i></button>\
                            <button type="button" class="btn btn-sm btn-default " title="Print" data-toggle="tooltip" data-placement="top"><i class="icon-printer"></i></button>\
                            <button type="button" class="btn btn-sm btn-default" title="Delete" data-toggle="tooltip" data-placement="top"><i class="icon-trash"></i></button></td></tr>'
                            
                            $('#user_tbl').append(data)
    
    
                        }
                    }
                   
                }
    
             }
        })
    
    }
    
    
    $('#account_reg').on('submit',function(e){
        e.preventDefault()
        data=$(this).serializeArray()
        if($('.pass1').val() != $('.pass2').val()){
        $('.message').append('<div class="alert alert-danger alert-dismissible" role="alert">\
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>\
        <i class="fa fa-times-circle"></i> Password not matched!</div>')
        }else{
           
            $.ajax({
                method:'POST',
                url:'adminAccReg',
                data:data,
                success:function(res){
                    if(res.data == 'ok'){
                      $('#account_reg').trigger('reset')
                        load_user()
                        $('.message').append('<div class="alert alert-success alert-dismissible" role="alert">\
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>\
        <i class="fa fa-times-circle"></i> Account has been created successfully!</div>')
                    }
                }
            })
    
        }
    
        
    })


})