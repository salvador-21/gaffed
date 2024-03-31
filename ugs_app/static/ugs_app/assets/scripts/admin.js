

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


// /////////////// LOAD USER

'{% if page == User Account%}'
load_user()
'{% endif%}'
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

{/* <tr>
<td>
<span>01</span>
</td>
<td>
<div class="d-flex align-items-center">
<div class="avtar-pic w35 bg-red" data-toggle="tooltip" data-placement="top" title="Avatar Name"><img src="{% static 'ugs_app/assets/user.png'%}" data-toggle="tooltip" data-placement="top" title="" alt="Avatar" class="w35 h35 rounded" data-original-title="Avatar Name" aria-describedby="tooltip280040"></div>
<div class="ml-3">
<a href="#" class="text-warning" style="font-weight: bolder;" title>{{u.user|title}}</a>
<p>
    {% if w.w_status == 'BANNED'%}
    <span class="badge badge-danger ml-0 mr-0">{{ w.w_status}}</span>
    {% elif w.w_status == 'ONHOLD'%}
    <span class="badge badge-warning ml-0 mr-0">{{ w.w_status}}</span>
    {%else%}
    <span class="badge badge-success ml-0 mr-0">{{ w.w_status}}</span>
    {%endif%}
</p>
<!-- <p class="mb-0"></p> -->
</div>
</div>
</td>
<td>{{u.usertype}}</td>
<td><span class="badge badge-success ml-0 mr-0">{{u.status}}</span></td>
<td>
<button type="button" class="btn btn-sm btn-default" title="Send Invoice" data-toggle="tooltip" data-placement="top"><i class="icon-envelope"></i></button>
<button type="button" class="btn btn-sm btn-default " title="Print" data-toggle="tooltip" data-placement="top"><i class="icon-printer"></i></button>
<button type="button" class="btn btn-sm btn-default" title="Delete" data-toggle="tooltip" data-placement="top"><i class="icon-trash"></i></button>
</td>
</tr> */}

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

// //////////////////////

$('#game_frm').on('submit',function(e){
    e.preventDefault()
    $.ajax({
        url: "add_games",
        type: "POST",
        data: new FormData(this),
        contentType: false, cache: false, processData:false,
        success: function(res){
        console.log(res)
        },
        error: function(){}
        });
})



// ///////////////////////

// /////////////////////////


})