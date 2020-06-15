function myFunction() {
  //var x = document.getElementById("search").value;
  //document.getElementById("demo").innerHTML = "You selected: " + x;
  var input_data = {
    store: $("#store").val(),
    edit: $("#edit").val(),
    phone: $("#phone").val(),
    city: $("#city").val(),
    address: $("#address").val(),
    postal_code: $("#postal_code").val(),
    opening_time: $("#opening_time").val(),
    closing_time: $("#closing_time").val(),
    square_meters: $("#square_meters").val(),
  };
  console.log(input_data);
  event.preventDefault();
  $.ajax({
    url: "search_resultS",
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
