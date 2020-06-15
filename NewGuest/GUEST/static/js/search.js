function myFunction() {
  //var x = document.getElementById("search").value;
  //document.getElementById("demo").innerHTML = "You selected: " + x;
  var input_data = {
    store: $("#store").val(),
    birthday: $("#birthday").val(),
    quantity: $("#quantity").val(),
    barcode: $("#barcode").val(),
    total_amount: $("#total").val(),
    payment_method: $("#card_or_cash").val(),
    category: $("#category").val(),
  };
  console.log(input_data);
  event.preventDefault();
  $.ajax({
    url: "search_result",
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
