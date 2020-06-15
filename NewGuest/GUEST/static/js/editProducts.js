function myFunction() {
  //var x = document.getElementById("search").value;
  //document.getElementById("demo").innerHTML = "You selected: " + x;
  var input_data = {
    action: $("#action").val(),
    barcode: $("#barcode").val(),
    product_name: $("#product_name").val(),
    producer_name: $("#producer_name").val(),
    price: $("#price").val(),
    special_note: $("#special_note").val(),
    category: $("#category").val(),
  };
  console.log(input_data);
  event.preventDefault();
  $.ajax({
    url: "search_resultP",
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
