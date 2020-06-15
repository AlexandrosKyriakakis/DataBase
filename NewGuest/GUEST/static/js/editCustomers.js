function myFunction() {
  //var x = document.getElementById("search").value;
  //document.getElementById("demo").innerHTML = "You selected: " + x;
  var input_data = {
    card_id: $("#card_id").val(),
    edit: $("#edit").val(),
    first_name: $("#first_name").val(),
    last_name: $("#last_name").val(),
    total_points: $("#total_points").val(),
    rewards: $("#rewards").val(),
    birth_date: $("#birth_date").val(),
    marital_status: $("#marital_status").val(),
    social_security_number: $("#social_security_number").val(),
    phone_number: $("#phone_number").val(),
    editNumber: $("#editNumber").val(),
  };
  console.log(input_data);
  event.preventDefault();
  $.ajax({
    url: "search_resultC",
    type: "POST",
    contentType: "application/json",
    dataType: "html",
    data: JSON.stringify(input_data),
    success: function (data) {
      $("#demo").html(data);
      //console.log(data);
      //$( location ).attr("href", "/search_products");
    },
    error: function (data, status) {
      //    $( location ).attr("href", "/login");
    },
  });
}
