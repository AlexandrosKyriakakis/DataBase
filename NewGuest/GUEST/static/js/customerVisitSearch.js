function search_customer() {
  //var x = document.getElementById("search").value;
  //document.getElementById("demo").innerHTML = "You selected: " + x;
  var input_data = {
    card_id: $("#card_id").val(),
  };
  console.log(input_data);
  event.preventDefault();
  $.ajax({
    url: "customer_result",
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
