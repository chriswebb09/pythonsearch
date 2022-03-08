function search(term) {
    window.location.assign("/search/" + term);
 }

 $(document).ready(function() {

   $("#search_button").click(function() {
     let text = $("#search_input").val()
     search(text);
   });
   
 });