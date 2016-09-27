/**
 * Created by Antonio on 21/09/16.
 */

function setImg(){
    var ext = ".png";
    var fullImg = img.concat(ext);
    //alert(fullImg);
    $('#sortable').append('<li class="ui-state-default"><img src='+fullImg+' /></li>');
}

var img;

$("#FilUploader").change(function () {
    var fileExtension = ['jpeg', 'jpg', 'png', 'gif', 'bmp'];
    if ($.inArray($(this).val().split('.').pop().toLowerCase(), fileExtension) == -1) {
        alert("Only formats are allowed : "+fileExtension.join(', '));
    }
});

function checkCsv(name){
    if (name == "csv") {
        return 1;
    }
    else{
        return 0;
    }
}

function myAjax (nomefile) {
    var testo = nomefile;
    $.ajax( { type : 'POST',
        data : {testo},
        url  : 'action.php',              // <=== CALL THE PHP FUNCTION HERE.
        success: function ( data ) {
            img = testo.slice(0, -4);
            //alert( data );               // <=== VALUE RETURNED FROM FUNCTION.
        },
        error: function (xhr, status, error) {
            // executed if something went wrong during call
            if (xhr.status > 0) alert('got error: ' + status); // status 0 - when load is interrupted
        },
        complete: function (data) {
            setImg();
        }
    });
}



function setTitle(){
    var testo = document.getElementById('title').value;
    $('#sortable').append('<li class="ui-state-default"><h1>'+testo+'</h1></li>');
    $('#title').val('');
}

var x = 0; //initlal text box count
function addElements(){
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".col-md-4"); //Fields wrapper
    var add_button      = $("#addelem"); //Add button ID


    if(x < max_fields){ //max input box allowed
        x++;
        $(wrapper).append('<div class="gruppoinput"> <label class="btn btn-default btn-info" style="margin-top: 8px">Browse <input type="file" style="display: none;" class="inputfile"/> </label> <button type="button" class="btn btn-outline-danger" disabled="disabled">Ok</button> <span id="remove_field" class="glyphicon glyphicon-remove" aria-hidden="true" style="vertical-align: middle"></span> </div>');
    }


    $(wrapper).on("click","#remove_field", function(e){ //user click on remove text
        $(this).parent('div').remove(); x--;
    })
}
