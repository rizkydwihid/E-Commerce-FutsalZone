$(".btn_toggle").on("click", function(){
    $(".menu").toggleClass("showing");
    });

// fungsi akan dipanggil ketika menu login pada header di click
function openForm() {
    document.getElementById("myForm").style.display = "block";
}
// fungsi untuk menutup pop up form login 
function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

// login control
function validationForm(){
  var email = document.forms["Login"]["email"].value;
  var password = document.forms["Login"]["psw"].value;

  if (email == "rizky@gmail.com" && password == "admin"){
    alert("Login Berhasil!!");
  }
}
