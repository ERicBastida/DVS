


var format_image = [ "jpg","png", "bmp", "tiff" ];
var element_pf_showing = "";
var element_in_showing = "";


function show_files_in(file1, file2 ){

	file1 = 'File1: '+ file1;
	file2 = 'File2: '+ file2;

	var table = "";


    table =	"<div class='table-responsive' style='background: white;'>" +
                "<table class='table mb-0' style='background: white;'>" +
                    "<thead>"+
                        "<tr>"+
                            "<th >"+ file1 +"</th>"+
                            "<th >"+ file2 +"</th>"+
                        "</tr>"+
                    "</thead>"+
        "</table>"+
    "</div>";



	return table;
}

function show_content_preview(name_file) {

    var style_image = "display: flex; text-align:center; position: center;  min-width: 100%; min-height: 100%;";
    var file_to_show = '<p>Incompatible format.</p>';
    var extension_file = String(name_file.split(".")[1]);

    if (format_image.includes(extension_file) ){

        file_to_show = '<img src="'+ name_file+'" class="img-responsive" style="' + style_image + '">';
    }else{
        file_to_show = '<video  id = "my-video" class ="video-js" controls preload="auto"   poster="/media/images/imagenes/datavia_logo.png"   data-setup = "{}" style="height:100%; width:100%;" >  <source src = "'+name_file+'"  type = "video/'+extension_file + '"> <p  class ="vjs-no-js"> To view this video please enable   JavaScript, and consider upgrading to a web browser that <a  href = "https://videojs.com/html5-video-support/"  target = "_blank" > supports HTML5  video </a > </p> </video>';
    }
    return file_to_show;

}

var id_pf_file_showing = "";

function preview_output_pf(element,path_file_pf,path_file_1,path_file_2) {

    var id_clicked_file_pf = element.parentElement.parentElement.getAttribute("row-id");

    // The element is showing?
    if (id_clicked_file_pf != id_pf_file_showing) {

        // Is another element showing it self?
        if (document.getElementById("preview-col-22") != null) {

            $("#preview-col-22").remove();
            $("#preview-col-111").remove();
            document.getElementById("file_list-col").className="";
        }
        document.getElementById("file_list-col").className="col-lg-6";

        path_file_pf = path_file_pf.trim(" ");
        name_file_1 = path_file_1.trim(" ").split("/").pop();
        name_file_2 = path_file_2.trim(" ").split("/").pop();
        style_element = "justify-content: center; align-items: center;";

        var row_to_span = $("#row-files-preview");

        var style_image = "display: flex; text-align:center; position: center;  min-width: 100%; min-height: 100%;";
        var str =
            "<div id='preview-col-22' style='background:black' class='col-lg-6' > " +
            "<h1 class='row justify-content-center text-primary' >Preview Processed File</h1>" +
            "<div id='preview-col'  style= " + style_element + ">" +
                show_content_preview(path_file_pf) +
                show_files_in(name_file_1, name_file_2) +
            "</div></div>";
        html = $.parseHTML(str);
        nodeNames = [];

        // Append the parsed HTML
        row_to_span.append(html);

        preview_output_in(element,path_file_1.trim(" "));
        id_pf_file_showing = id_clicked_file_pf;
    }else{
         $("#preview-col-22").remove();
         $("#preview-col-111").remove();
        id_pf_file_showing = "";
        document.getElementById("file_list-col").className="";

    }


}
var id_in_file_showing = "";

function preview_output_in(buttom, path_file){

    var id_clicked_file_1 = buttom.parentElement.parentElement.getAttribute("row-id");

    path_file = path_file.trim(" ");


    if (id_clicked_file_1 != id_pf_file_showing) {
        if (document.getElementById("preview-col-111") != null) {
            $("#preview-col-111").remove();
        }

        var row_to_span = $("#preview-col");
        style_element = "justify-content: center; align-items: center;";
        var style_image = "display: flex; text-align:center; position: center;  min-width: 100%; min-height: 100%;";
        var str =

            "<div id='preview-col-111' style='background:black'  > " +
            "<h1 class='row justify-content-center text-primary' >Preview First File</h1>" +
            "<div id='preview-col'  style= " + style_element + ">" +
            show_content_preview(path_file) +
            "</div>" +
            "</div>";
        html = $.parseHTML(str);
        nodeNames = [];

        // Append the parsed HTML
        row_to_span.append(html);

        id_in_file_showing = id_clicked_file_1;

    }else{
        $("#preview-col-111").remove();
        id_in_file_showing = "";


    }

}
var id_file_showing = "";

function preview(e,path_file) {
    path_file = path_file.trim(" ");

    var id_clicked = e.parentElement.parentElement.getAttribute("row-id");
    // Look at row has contains file_list to add preview
    var row_to_span = $( "#row-files-preview" );

    var box = document.getElementById("file_list-col");
    box.className="col-lg-6";
    if (id_clicked != id_file_showing){
        if (document.getElementById("preview-col-11") != null){
            $("#preview-col-11").remove();
        }

        var style_image = "display: flex; text-align:center; position: center;  min-width: 100%; min-height: 100%;";
        style_element = "justify-content: center; align-items: center;";

        var   str =
            "<div id='preview-col-11' style='background:black' class='col-lg-6' > " +
                "<h1 class='row justify-content-center text-primary' >Preview</h1>"+
                        "<div id='preview-col'  style= "+style_element+">"+
                                 show_content_preview(path_file) +
                         "</div></div>";

        id_file_showing = id_clicked;

        html = $.parseHTML( str );
        nodeNames = [];
        // Append the parsed HTML
        row_to_span.append( html );
    }else{
        $("#preview-col-11").remove();
        id_file_showing = "";
        document.getElementById("file_list-col").className="";

    }




}

var files_to_procces = [];
var check_boxes = [];
var chkorder = 0;


// Function that put a tracking number
function setorder(chkbx){
   if(chkbx.checked)
   {

      chkorder = parseInt(chkorder+1) ;

      if (chkorder === 3){
        alert("Please, only check two files.");
        chkbx.checked = 0;
        chkbx.parentElement.children[0].textContent = "";
        chkorder = chkorder -1;
      }else{
        // Set order to lable
        chkbx.parentElement.children[0].textContent = String(chkorder);
        // Add path files to array
        files_to_procces[chkorder-1] = chkbx.parentElement.parentElement.parentElement.getAttribute("row-id");
        // Add checkbox element to array
        check_boxes[chkorder-1]= chkbx;
        
      }
   }
   else
   {
      //Getting id
      var id = parseInt(chkbx.parentElement.children[0].textContent)-1;


      // Cleaning label
      chkbx.parentElement.children[0].textContent= "";

      if(check_boxes.length == 2  && id == 0){

      	files_to_procces=  [files_to_procces[1]];
      	check_boxes =  [check_boxes[1]];
      	check_boxes[0].parentElement.children[0].textContent = "1";

	  }else{
      	if (check_boxes.length == 2 && id == 1){
      		files_to_procces = [files_to_procces[0]];
			check_boxes=  [check_boxes[0]];
			check_boxes[0].parentElement.children[0].textContent = "1";
		}else{
      		files_to_procces = []
			check_boxes = []
		}
	  }
      chkorder = files_to_procces.length;
   }
}


// A $( document ).ready() block.
$( document ).ready(function() {
    console.log( "ready!" );
    function reset(){

    }

    $('#buttom_submit').click(function(){


        function_number = $('#buttom_submit').attr("f-id");




        if (files_to_procces.length === 2){


            $.blockUI({
              message: 'Your files are being processed by our servers.',
              css: {
                border: 'none',
                padding: '15px',
                backgroundColor: '#000',
                '-webkit-border-radius': '10px',
                '-moz-border-radius': '10px',
                opacity: '.5',
                color: '#fff',
                fontSize: '18px',
                fontFamily: 'Verdana,Arial',
                fontWeight: 200,
            } });

            setTimeout($.unblockUI, 3000);
            reset();

            var data = {'pieFact': 1};
            var csrf_token;

            $.ajax({
                 type:"GET",
                 url:"/process-file/",
                 data: {
                        'function_number' : parseInt(function_number),
                        'file1_pk': parseInt(files_to_procces[0]),
                        'file2_pk': parseInt(files_to_procces[1]),
                        },
                 dataType: 'json',
                 success: function(){
                     $('#message').html("<h2>Contact Form Submitted!</h2>")
					    alert("Data processed! You can view the output-file (It's only an example, we needed configuration file)")
                    },
                error: function(){

					    console.log("Error!");
                    }
            });

        }else{
            alert("Please, select two files to be processed.")
        }

    });








});






