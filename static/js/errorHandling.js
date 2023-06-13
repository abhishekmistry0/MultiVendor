
    $("#newsletter").click(function(event) {
      event.preventDefault(); 
      email=document.getElementById("newsletteremail").value
      $.ajax({
        url: "contactus/newsletter/"+String(email)+"/",
        type: 'GET',
        success: function(data) {
            // swal({
            //   title: "Success!",
            //   text: String(data.message),
            //   icon: "success",
            //   timer: 1000,
            //   buttons: false,
            // });
            // cart_total_amount=data.cart_total_amount.cart_total_amount
            // $('#cart_total_amount').empty();
            // $('#cart_total_amount').append('<span > '+cart_total_amount+' </span>')
            // $('#element').toast('show')
            // $('.toast').toast('show');
            $('.news').empty();
            if(data.data=="Success"){
            $(".news").append("<div class=\"alert alert-danger\" role=\"alert\">Email Subscribed</div>")}
            else{
                $(".news").append("<div class=\"alert alert-danger\" role=\"alert\">Email Already Subscribed</div>")
            }
        },
        error: function(xhr, status, error) {
          // Handle any errors
         
        }
      });
    });
  
//   $('.toast').toast(autohide)
// $('.toast').toast('hide');

// $(document).ready(function() {
//   $('.item_add').click(function(event) {
//     event.preventDefault();
//     var url = $(this).attr('href');

//     $.getJSON(url, function(response) {
//       if (response.success) {
//         swal({
//           title: "Success!",
//           text: response.message,
//           icon: "success",
//           timer: 1000,
//           buttons: false,
//         });
//       }
//     });
//   });
// });