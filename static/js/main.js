// $.ajaxSetup({
//      beforeSend: function(xhr, settings) {
//          function getCookie(name) {
//              var cookieValue = null;
//              if (document.cookie && document.cookie != '') {
//                  var cookies = document.cookie.split(';');
//                  for (var i = 0; i < cookies.length; i++) {
//                      var cookie = jQuery.trim(cookies[i]);
//                      // Does this cookie string begin with the name we want?
//                      if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                          break;
//                      }
//                  }
//              }
//              return cookieValue;
//          }
//          if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//              // Only send the token to relative URLs i.e. locally.
//              xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//          }
//      }
// });
var csrf = $('input[name=csrfmiddlewaretoken]').val()

function IncClick(id) {
    // alert('Event: ', e)
    console.log('ID: ', id)
    $.ajax({
        type: "POST",
        url: '/links/link_clicked/',
        data: {
            id: id,
            csrfmiddlewaretoken: csrf
        },
        success: function (response) {
            console.log('Success', response)
        },
    });
}


// $(document).ready(function () {
//     const left = document.querySelector(".left");
//     const right = document.querySelector(".right");
//     const container = document.querySelector(".container");
//
//     left.addEventListener("mouseenter", () => {
//         container.classList.add("hover-left");
//     });
//
//     left.addEventListener("mouseleave", () => {
//         container.classList.remove("hover-left");
//     });
//
//     right.addEventListener("mouseenter", () => {
//         container.classList.add("hover-right");
//     });
//
//     right.addEventListener("mouseleave", () => {
//         container.classList.remove("hover-right");
//     });
// });



