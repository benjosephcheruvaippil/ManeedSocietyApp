function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }

function RemoveLocalStorageItems(){
  localStorage.removeItem('historyFlag');
  window.location.href="/logout";
}


$(document).ready(function(){

  $("#bond").click(function(){
    $("#total_amount").val(($("#monthly_instalment_amount").val())*($("#term").val()));
  });

  $("#setvalues").click(function(){
    $("#documentType").val("1");
    $("#person1_class_type").val("A");
    $("#person2_class_type").val("A");
    $("#person3_class_type").val("A");
    $("#person4_class_type").val("A");
    $("#person5_class_type").val("A");

    $("#person_1").val("1094");
    $("#person_2").val("1");
    $("#person_3").val("1078");
    $("#person_4").val("1063");
    $("#person_5").val("1040");

    $("#mds_no").val("MDS-001");
    $("#monthly_instalment_amount").val("4000");
    $("#term").val("5");
    //$("#total_amount").val("60000");
    $("#chittal_no").val("CGJ-45");
    $("#auction_instalment_no").val("9");
    $("#auction_date").val("12/12/2021");
    $("#less_called_amount").val("1000");
    // $("#sro").val("SQWER");
    $("#land_document_no").val("LNH-09-T");
    $("#no_of_executants").val("3");
    $("#date_of_instalment").val("11/10/2021");
    $("#property_owner_specify_no").val("OWNWER");
    // $("#district").val("");
    // $("#sub_district").val("");
    // $("#taluk").val("");
    // $("#village").val("");
     $("#kara").val("Kodumboor");
    $("#sy_no_and_sy_sub_division_no").val("qwe-1234");
    $("#re_sy_no").val("errt");
    $("#area").val("12.8");
  });

  $("#all").click(function(){
    var bondButton = document.getElementById("bond");
    bondButton.click();
  });

  window.onpageshow=function(event){
    var historyFlag=localStorage.getItem('historyFlag');
    console.log("History Flag",historyFlag);
    if(historyFlag=="1"){
      var applicationbutton = document.getElementById("applicationproperty");
      setTimeout(function(){
        applicationbutton.click();
        }, 1000);
    }
    
    if(historyFlag=="2"){
      var receiptbutton = document.getElementById("receipt");
      setTimeout(function(){
        receiptbutton.click();
        }, 1000);
    }
  
    if(historyFlag=="3"){
      var note1button = document.getElementById("promisory_note_1");
      setTimeout(function(){
        note1button.click();
        }, 1000);
    }
  
    if(historyFlag=="4"){
      var note2button = document.getElementById("promisory_note_2");
      setTimeout(function(){
        note2button.click();
        }, 1000);
    }
  
    if(historyFlag=="5"){
      var note3button = document.getElementById("promisory_note_3");
      setTimeout(function(){
        note3button.click();
        }, 1000);
    }
  
    if(historyFlag=="6"){
      var note4button = document.getElementById("promisory_note_4");
      setTimeout(function(){
        note4button.click();
        }, 1000);
    }
  
    if(historyFlag=="7"){
      var note5button = document.getElementById("promisory_note_5");
      setTimeout(function(){
        note5button.click();
        }, 1000);
    }

    // if(historyFlag=="8"){
    //   var note5button = document.getElementById("applicationproperty");
    //   setTimeout(function(){
    //     note5button.click();
    //     }, 1000);
    // }
  }
});